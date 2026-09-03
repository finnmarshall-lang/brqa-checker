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
SLACK_API = "https://slack.com/api"

# Reaction map for the pre-tick self-heal sweep — mirrors merge_deltas.py.
# Any state.json entry within the last 6h with one of these verdicts should
# already have the corresponding emoji reaction on its parent Slack message.
# If it doesn't, this sweep adds it (idempotent — already_reacted is a no-op).
VERDICT_EMOJI = {
    "clean": "double-tick",
    "flagged": "exclamation",
}


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
    """A message qualifies iff it has a ✅ reaction and isn't already in state.

    The desk uses ✅ to mark a term-sheet post as ready-for-QA — so ✅ is
    itself the authoritative signal. No content filter: if a ✅ ever lands
    on a message that ISN'T a deal (e.g. accidental react on chatter), the
    tick's per-message logic will fail to find a BR match and mark it
    'skipped' in the state delta. That's cheap and keeps the pipeline from
    silently missing real deals because of an unfamiliar format.
    """
    ts = m.get("ts")
    if not ts or ts in state:
        return False
    return any(r.get("name") == "white_check_mark" for r in (m.get("reactions") or []))


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

    # Pre-tick reaction self-heal — mirror of the sweep in merge_deltas.py.
    # Runs at the START of every tick so any reaction the previous tick's
    # merge missed (crash, transient reactions.add failure, delta file that
    # never landed) gets caught within one tick cycle instead of two.
    # Idempotent — reactions.add returns already_reacted as success.
    cutoff = time.time() - WINDOW_SECONDS
    heal = [(ts, v.get("verdict")) for ts, v in state.items()
            if isinstance(v, dict)
            and v.get("verdict") in VERDICT_EMOJI]
    heal = [(ts, verdict) for ts, verdict in heal
            if _safe_float(ts) is not None and _safe_float(ts) >= cutoff]
    if heal:
        ok = already = failed = 0
        for ts, verdict in heal:
            emoji = VERDICT_EMOJI[verdict]
            result = _react(CHANNEL, ts, emoji)
            if result == "ok": ok += 1
            elif result == "already": already += 1
            else:
                failed += 1
                print(f"  pre-tick react failed on {ts} ({emoji}): {result}", file=sys.stderr)
        print(f"pre-tick reaction sweep: {ok} added, {already} already-present, {failed} failed")
    return 0


def _safe_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def _react(channel: str, ts: str, emoji: str) -> str:
    """Non-raising reaction add. Returns 'ok', 'already', or an error string."""
    payload = json.dumps({"channel": channel, "timestamp": ts, "name": emoji}).encode()
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
        return f"http_{e.code}"
    except Exception as e:
        return f"err_{type(e).__name__}"
    if body.get("ok"):
        return "ok"
    err = body.get("error", "unknown")
    return "already" if err == "already_reacted" else err


if __name__ == "__main__":
    sys.exit(main(sys.argv))
