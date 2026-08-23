#!/usr/bin/env python3
"""Post a threaded reply as the BR QA bot (not as the calling user).

Uses SLACK_BOT_TOKEN from ~/.bondradar-env — same token that reads reactors/files.
This is the ONLY way to make the message appear from `br_qa_reactor_reader` in
Slack instead of the human user whose OAuth backs the MCP connector.

CLI:
    python3 slack_post.py <channel_id> <thread_ts> "<message text>"

Or read message from stdin:
    python3 slack_post.py <channel_id> <thread_ts> -    <<'EOF'
    <@USERID>
    :white_check_mark: BR QA — id `X` at <stage> — Perfect! Great job
    ...
    EOF

Prints the posted message's permalink JSON on success; non-zero exit on failure.
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


def post_thread(channel: str, thread_ts: str, text: str) -> dict:
    payload = json.dumps({
        "channel": channel,
        "thread_ts": thread_ts,
        "text": text,
        "unfurl_links": False,
        "unfurl_media": False,
    }).encode("utf-8")
    req = request.Request(
        f"{SLACK_API}/chat.postMessage",
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
        raise RuntimeError(f"Slack chat.postMessage HTTP {e.code}: {e.read().decode()[:200]}")
    if not body.get("ok"):
        raise RuntimeError(f"Slack chat.postMessage error: {body.get('error', 'unknown')}")
    return body


def _cli(argv: list[str]) -> int:
    if len(argv) < 4:
        print("usage: slack_post.py <channel_id> <thread_ts> <text|->", file=sys.stderr)
        return 2
    channel, thread_ts, text_arg = argv[1], argv[2], argv[3]
    text = sys.stdin.read() if text_arg == "-" else text_arg
    body = post_thread(channel, thread_ts, text)
    print(json.dumps({
        "ts": body["ts"],
        "channel": body["channel"],
        "as_user_id": (body.get("message") or {}).get("bot_id") or (body.get("message") or {}).get("user"),
    }))
    return 0


if __name__ == "__main__":
    sys.exit(_cli(sys.argv))
