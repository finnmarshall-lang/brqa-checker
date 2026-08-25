#!/usr/bin/env python3
"""
Pre-tick step: fetch the channel, filter to ✅'d term-sheet messages that
aren't already in state.json, cap at MAX_MSGS, split into N_SHARDS files.

Writes shard_0.json ... shard_{N-1}.json (each an array of message dicts,
oldest-first) plus queue_meta.json with the total.

Doing this once in Python is much cheaper than four Claude sessions each
independently re-polling the channel, and it guarantees the shards don't
overlap.

CLI:
    python3 prepare_batches.py [N_SHARDS] [MAX_MSGS]

Env:
    SLACK_BOT_TOKEN — required.
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.parse
from pathlib import Path
from urllib import request, error

CHANNEL = "C09JX51GAKH"
WINDOW_SECONDS = 21600  # 6h — matches the tick's own window
BBG_MARKERS = ("***", "€€€", "£££", "$$$", "★★★", "###")
SLACK_API = "https://slack.com/api"


def _token() -> str:
    tok = os.environ.get("SLACK_BOT_TOKEN")
    if tok:
        return tok
    envf = Path.home() / ".bondradar-env"
    if envf.exists():
        for line in envf.read_text().splitlines():
            if line.startswith("SLACK_BOT_TOKEN="):
                return line.split("=", 1)[1].strip()
    raise RuntimeError("SLACK_BOT_TOKEN not set")


def _get(method: str, params: dict) -> dict:
    url = f"{SLACK_API}/{method}?" + urllib.parse.urlencode(params)
    req = request.Request(url, headers={"Authorization": f"Bearer {_token()}"})
    with request.urlopen(req, timeout=15) as resp:
        body = json.loads(resp.read().decode())
    if not body.get("ok"):
        raise RuntimeError(f"Slack API {method}: {body.get('error')}")
    return body


def is_qa_candidate(m: dict, state: dict) -> bool:
    ts = m.get("ts")
    if not ts or ts in state:
        return False
    if not any(r.get("name") == "white_check_mark" for r in (m.get("reactions") or [])):
        return False
    text = m.get("text") or ""
    has_bbg_marker = any(mk in text for mk in BBG_MARKERS)
    has_file = bool(m.get("files"))
    return has_bbg_marker or has_file


def main(argv: list[str]) -> int:
    n_shards = int(argv[1]) if len(argv) > 1 else 4
    max_msgs = int(argv[2]) if len(argv) > 2 else 40

    state_path = Path("state.json")
    state = json.loads(state_path.read_text()) if state_path.exists() else {}

    resp = _get("conversations.history", {
        "channel": CHANNEL,
        "oldest": f"{time.time() - WINDOW_SECONDS:.6f}",
        "limit": 200,
    })
    msgs = resp.get("messages") or []

    candidates = sorted(
        [m for m in msgs if is_qa_candidate(m, state)],
        key=lambda m: float(m["ts"]),
    )[:max_msgs]

    shards: list[list[dict]] = [[] for _ in range(n_shards)]
    for i, m in enumerate(candidates):
        shards[i % n_shards].append(m)

    for i, s in enumerate(shards):
        Path(f"shard_{i}.json").write_text(json.dumps(s, indent=2))

    Path("queue_meta.json").write_text(json.dumps({
        "total": len(candidates),
        "shards": n_shards,
        "per_shard": [len(s) for s in shards],
    }, indent=2))

    print(f"prepared {len(candidates)} messages across {n_shards} shards")
    print(f"per-shard counts: {[len(s) for s in shards]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
