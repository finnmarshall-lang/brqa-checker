#!/usr/bin/env python3
"""
Fetch the user IDs who added a specific reaction to a Slack message.

The Slack MCP tools don't expose reactor user IDs — only counts. This helper
calls `reactions.get` directly with the SLACK_BOT_TOKEN from ~/.bondradar-env
and returns the users[] list for the named reaction.

CLI:
    python3 slack_reactors.py <channel_id> <message_ts> [reaction_name]

    reaction_name defaults to `white_check_mark`.

Library:
    from slack_reactors import reactors_of
    users = reactors_of("C09JX51GAKH", "1787..." )  # list of user IDs
    name  = display_name("U08R5SWAHGQ")             # resolves to "Finn Marshall"
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


def _call(method: str, params: dict) -> dict:
    url = f"{SLACK_API}/{method}?{urllib.parse.urlencode(params)}"
    req = request.Request(url, headers={"Authorization": f"Bearer {_token()}"})
    try:
        with request.urlopen(req, timeout=10) as resp:
            body = json.loads(resp.read().decode())
    except error.HTTPError as e:
        raise RuntimeError(f"Slack API {method} HTTP {e.code}: {e.read().decode()[:200]}")
    if not body.get("ok"):
        raise RuntimeError(f"Slack API {method} error: {body.get('error', 'unknown')}")
    return body


def reactors_of(channel_id: str, message_ts: str, reaction: str = "white_check_mark") -> list[str]:
    """Return the list of user IDs who added `reaction` to the message.

    Empty list if the reaction isn't present. The message must be readable
    by the bot (invite the bot to the channel with `/invite @BotName` first).
    """
    body = _call("reactions.get", {"channel": channel_id, "timestamp": message_ts})
    reactions = (body.get("message") or {}).get("reactions") or []
    for r in reactions:
        if r.get("name") == reaction:
            return list(r.get("users") or [])
    return []


def display_name(user_id: str) -> str:
    """Return the display name for a user ID (falls back to real name, then user_id)."""
    body = _call("users.info", {"user": user_id})
    user = body.get("user") or {}
    profile = user.get("profile") or {}
    return (
        profile.get("display_name")
        or profile.get("real_name")
        or user.get("name")
        or user_id
    )


def _cli(argv: list[str]) -> int:
    if len(argv) < 3:
        print("usage: slack_reactors.py <channel_id> <message_ts> [reaction_name]", file=sys.stderr)
        return 2
    channel, ts = argv[1], argv[2]
    reaction = argv[3] if len(argv) > 3 else "white_check_mark"
    users = reactors_of(channel, ts, reaction)
    out = [{"user_id": u, "display_name": display_name(u)} for u in users]
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(_cli(sys.argv))
