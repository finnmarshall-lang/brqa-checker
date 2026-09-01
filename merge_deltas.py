#!/usr/bin/env python3
"""
Post-tick step: merge state_delta_*.json files (written by each parallel
shard) into state.json, then remove the deltas.

Each delta is a JSON dict of {message_ts: {checked_at, verdict}}. On
conflict (unlikely — prepare_batches.py assigns disjoint TSs to shards)
the newer checked_at wins.

ALSO applies the term-sheet-message emoji reaction based on verdict —
this used to be a shard-prompt step but the LLM would silently skip
it maybe 30% of the time. Doing it here makes reactions deterministic:
clean → :double-tick:, flagged → :exclamation:, skipped → no react.
Idempotent — reactions.add returns already_reacted as a no-op success,
so re-running is safe. Uses SLACK_BOT_TOKEN.
"""
from __future__ import annotations

import glob
import json
import os
import sys
import urllib.parse
from pathlib import Path
from urllib import request, error

CHANNEL = "C09JX51GAKH"
VERDICT_EMOJI = {
    "clean": "double-tick",
    "flagged": "exclamation",
    # "skipped" deliberately absent — we don't react on skipped verdicts.
}
SLACK_API = "https://slack.com/api"


def _slack_token() -> str | None:
    tok = os.environ.get("SLACK_BOT_TOKEN")
    if tok:
        return tok
    envf = Path.home() / ".bondradar-env"
    if envf.exists():
        for line in envf.read_text().splitlines():
            if line.startswith("SLACK_BOT_TOKEN="):
                return line.split("=", 1)[1].strip()
    return None


def _add_reaction(channel: str, ts: str, emoji: str, tok: str) -> str:
    """Return 'ok', 'already', or an error string. Never raises."""
    payload = json.dumps({"channel": channel, "timestamp": ts, "name": emoji}).encode()
    req = request.Request(
        f"{SLACK_API}/reactions.add",
        data=payload,
        headers={
            "Authorization": f"Bearer {tok}",
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


def main() -> int:
    state_path = Path("state.json")
    state: dict = json.loads(state_path.read_text()) if state_path.exists() else {}

    delta_files = sorted(glob.glob("state_delta_*.json"))

    # Collect every new/updated entry from all shard deltas BEFORE we
    # merge, so we can apply reactions per-entry after the merge succeeds.
    to_react: list[tuple[str, str]] = []  # (message_ts, verdict)
    merged = 0
    for f in delta_files:
        try:
            delta = json.loads(Path(f).read_text())
        except (json.JSONDecodeError, OSError) as e:
            print(f"skipping malformed delta {f}: {e}", file=sys.stderr)
            continue
        if not isinstance(delta, dict):
            print(f"skipping non-dict delta {f}", file=sys.stderr)
            continue
        for ts, v in delta.items():
            if not isinstance(v, dict):
                continue
            is_new = ts not in state or (v.get("checked_at", "") > state[ts].get("checked_at", ""))
            if is_new:
                state[ts] = v
                merged += 1
                verdict = v.get("verdict")
                if verdict in VERDICT_EMOJI:
                    to_react.append((ts, verdict))
        os.remove(f)

    state_path.write_text(json.dumps(state, indent=2))
    print(f"merged {merged} state updates from {len(delta_files)} shard delta(s)")

    # Reactions pass — deterministic, doesn't depend on the LLM.
    tok = _slack_token()
    if not tok:
        print("SLACK_BOT_TOKEN not available; skipping reactions pass", file=sys.stderr)
        return 0

    ok = already = failed = 0
    for ts, verdict in to_react:
        emoji = VERDICT_EMOJI[verdict]
        result = _add_reaction(CHANNEL, ts, emoji, tok)
        if result == "ok":
            ok += 1
        elif result == "already":
            already += 1
        else:
            failed += 1
            print(f"react failed on {ts} ({emoji}): {result}", file=sys.stderr)
    print(f"reactions: {ok} added, {already} already-present (idempotent), {failed} failed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
