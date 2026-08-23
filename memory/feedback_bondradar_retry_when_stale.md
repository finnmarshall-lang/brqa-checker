---
name: feedback-bondradar-retry-when-stale
description: "When the BR record's `changedAt` is older than the ✅'d Slack message's timestamp, the desk hasn't published the update yet — re-fetch a minute later before flagging BR as stale."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-20T09:10:11.777Z
---

There's a natural lag between a Slack term-sheet post getting ✅'d and the desk publishing the corresponding BR update. Before flagging a BR record as stale, check the timing.

**When BR looks behind the Slack post:**

1. Compare BR `changedAt` (UTC) — or `changed` (UK local) — against the Slack message timestamp.
2. If BR's timestamp is EARLIER than the Slack message, the update likely hasn't been published yet — the ✅ ticker was faster than the publisher.
3. Wait one cron tick (5 min) and re-fetch. Nine times out of ten BR will have caught up.
4. Only flag "BR is stale — needs to be updated to [stage]" if BR is still behind after the retry.

**Why:** on 2026-08-20 I flagged RLB Steiermark as stale (BR still at Book Update, source at Final Terms) — within one minute Finn told me "read RLB Steiermark it is at FT", and re-fetching showed BR had been published in the interim. Would have avoided the noise by pacing the check.

**How to apply:** if the initial fetch shows BR is a stage behind the Slack source, post the finding with a caveat like "waiting one tick before flagging as stale" OR just skip the ✅ this tick and let the next tick catch it. Better to be a few minutes late than to flag a real update in progress.

See also [[br-qa-checker-project]].
