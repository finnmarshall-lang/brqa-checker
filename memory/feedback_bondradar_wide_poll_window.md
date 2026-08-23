---
name: feedback-bondradar-wide-poll-window
description: "On every BR QA tick, widen the Slack poll window to catch messages that were 👀-only earlier and have since been ✅'d. Never use `oldest=<last_new_ts>` — always poll at least a 90-minute window back."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-20T15:07:18.293Z
---

Never restrict the poll window to only messages POSTED after the last-seen ts. Messages that were 👀-only at an earlier tick can pick up a ✅ later, and using `oldest=<last_new_ts>` on `slack_read_channel` will silently skip them — the harness returns nothing new, and the QA never runs.

**Rule:** on every tick, poll with `oldest = now - 90 minutes` (or wider if the day is busy — PRC was ✅'d ~50 minutes after posting). This costs almost nothing but guarantees we catch late-fired reactions.

**Why:** Finn flagged on 2026-08-20 that I missed the PRC (People's Republic of China) CNH multi-tranche Priced update — the message was posted at 15:37 with 👀, and I QA'd only what looked new on subsequent ticks. It was ✅'d some time later and my narrow poll window missed it. The BR QA is worthless if a real ✅ is silently skipped — "can't miss this stuff".

**How to apply:**
- `slack_read_channel(oldest = now - 5400)` (90 min) or `oldest = now - 7200` (2h) on every tick, instead of `oldest = last-new-ts`.
- Then dedupe against a running set of "already QA'd message TSs" (stored in `state.json`) so we don't repost on threads we already handled.
- The dedupe gate is the state file (already implemented), not the poll window.

See also [[br-qa-checker-project]], [[feedback-bondradar-retry-when-stale]].
