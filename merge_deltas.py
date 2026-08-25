#!/usr/bin/env python3
"""
Post-tick step: merge state_delta_*.json files (written by each parallel
shard) into state.json, then remove the deltas.

Each delta is a JSON dict of {message_ts: {checked_at, verdict}}. On
conflict (unlikely — prepare_batches.py assigns disjoint TSs to shards)
the newer checked_at wins.
"""
from __future__ import annotations

import glob
import json
import os
import sys
from pathlib import Path


def main() -> int:
    state_path = Path("state.json")
    state: dict = json.loads(state_path.read_text()) if state_path.exists() else {}

    merged = 0
    delta_files = sorted(glob.glob("state_delta_*.json"))
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
            if ts not in state or (v.get("checked_at", "") > state[ts].get("checked_at", "")):
                state[ts] = v
                merged += 1
        os.remove(f)

    state_path.write_text(json.dumps(state, indent=2))
    print(f"merged {merged} state updates from {len(delta_files)} shard delta(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
