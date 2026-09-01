#!/usr/bin/env python3
"""Add an emoji reaction to a Slack message as the BR QA bot.

Used by the tick when a deal's QA comes back CLEAN — we react to the
original term-sheet message with `:double-tick:` so anyone scanning the
channel sees at a glance that it's been checked and passed.

Uses SLACK_BOT_TOKEN (same env/token as the other slack_*.py helpers).

CLI:
    python3 slack_react.py <channel_id> <message_ts> <emoji_name>

    emoji_name is the Slack short name WITHOUT the surrounding colons —
    e.g. `double-tick`, `white_check_mark`, `heavy_check_mark`.

    Exit 0 on success or when the reaction is already present (a no-op).
    Exit >0 on real error (bad emoji name, missing scope, network, etc.).
"""
from __future__ import annotations

import json
import os
import sys
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


def add_reaction(channel: str, message_ts: str, emoji: str) -> dict:
    payload = json.dumps({
        "channel": channel,
        "timestamp": message_ts,
        "name": emoji.strip(":"),
    }).encode("utf-8")
    req = request.Request(
        f"{SLACK_API}/reactions.add",
        data=payload,
        headers={
            "Authorization": f"Bearer {_token()}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    try:
        with request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode())
    except error.HTTPError as e:
        raise RuntimeError(f"Slack reactions.add HTTP {e.code}: {e.read().decode()[:200]}")
    # `already_reacted` is a no-op we treat as success — the ✅✅ is already there.
    if not body.get("ok") and body.get("error") != "already_reacted":
        raise RuntimeError(f"Slack reactions.add error: {body.get('error', 'unknown')}")
    return body


def _cli(argv: list[str]) -> int:
    if len(argv) < 4:
        print("usage: slack_react.py <channel_id> <message_ts> <emoji_name>", file=sys.stderr)
        return 2
    channel, ts, emoji = argv[1], argv[2], argv[3]
    body = add_reaction(channel, ts, emoji)
    print(json.dumps({
        "ok": body.get("ok", False),
        "warning": body.get("error"),
        "channel": channel,
        "ts": ts,
        "emoji": emoji.strip(":"),
    }))
    return 0


if __name__ == "__main__":
    sys.exit(_cli(sys.argv))
