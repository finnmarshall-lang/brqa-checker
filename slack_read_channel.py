#!/usr/bin/env python3
"""
Read recent messages from a Slack channel using the bot token.

Replaces the Slack MCP `slack_read_channel` tool for environments (e.g. GitHub
Actions) that don't have an MCP connector wired up. Calls conversations.history
directly with the SLACK_BOT_TOKEN from ~/.bondradar-env or the env.

CLI:
    python3 slack_read_channel.py <channel_id> [--oldest <unix_ts>] [--limit N]

    Prints a JSON array of messages, newest first. Each entry:
      {ts, user, text, reactions:[{name, users, count}], files:[{id,name}], thread_ts}

Library:
    from slack_read_channel import fetch_history
    msgs = fetch_history("C09JX51GAKH", oldest=1735000000, limit=200)
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.parse
from pathlib import Path
from urllib import request, error

ENV_FILE = Path.home() / ".bondradar-env"
SLACK_API = "https://slack.com/api"


def _token() -> str:
    tok = os.environ.get("SLACK_BOT_TOKEN")
    if tok:
        return tok
    if not ENV_FILE.exists():
        raise RuntimeError(f"{ENV_FILE} not found and SLACK_BOT_TOKEN not in env")
    for line in ENV_FILE.read_text().splitlines():
        line = line.strip()
        if line.startswith("SLACK_BOT_TOKEN="):
            return line.split("=", 1)[1].strip()
    raise RuntimeError(f"SLACK_BOT_TOKEN not found in {ENV_FILE}")


def _call(method: str, params: dict) -> dict:
    url = f"{SLACK_API}/{method}?{urllib.parse.urlencode(params)}"
    req = request.Request(url, headers={"Authorization": f"Bearer {_token()}"})
    try:
        with request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode())
    except error.HTTPError as e:
        raise RuntimeError(f"Slack API {method} HTTP {e.code}: {e.read().decode()[:200]}")
    if not body.get("ok"):
        raise RuntimeError(f"Slack API {method} error: {body.get('error', 'unknown')}")
    return body


def fetch_history(channel_id: str, oldest: float | None = None, limit: int = 100) -> list[dict]:
    params: dict = {"channel": channel_id, "limit": min(max(1, limit), 200)}
    if oldest is not None:
        params["oldest"] = f"{oldest:.6f}"
    body = _call("conversations.history", params)
    out: list[dict] = []
    for m in body.get("messages") or []:
        out.append({
            "ts": m.get("ts"),
            "user": m.get("user") or m.get("bot_id"),
            "text": m.get("text") or "",
            "thread_ts": m.get("thread_ts"),
            "reactions": [
                {"name": r.get("name"), "count": r.get("count"), "users": r.get("users") or []}
                for r in (m.get("reactions") or [])
            ],
            "files": [
                {"id": f.get("id"), "name": f.get("name"), "mimetype": f.get("mimetype")}
                for f in (m.get("files") or [])
            ],
            "subtype": m.get("subtype"),
        })
    return out


def _cli(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("channel_id")
    ap.add_argument("--oldest", type=float, default=None,
                    help="Unix seconds; default: now - 5400 (90 min window)")
    ap.add_argument("--limit", type=int, default=100)
    args = ap.parse_args(argv[1:])
    oldest = args.oldest if args.oldest is not None else (time.time() - 5400)
    msgs = fetch_history(args.channel_id, oldest=oldest, limit=args.limit)
    print(json.dumps(msgs, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(_cli(sys.argv))
