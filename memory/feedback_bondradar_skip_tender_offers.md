---
name: bondradar-skip-tender-offers
description: "Skip tender-offer / liability-management ✅'d messages silently — no Slack post, just mark verdict:\"skipped\" in the state delta."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-01T09:16:01.289Z
---

**Tender offers and other liability-management announcements are not primary bond issues** and are not tracked in Bond Radar's deal feed. When a ✅ lands on one, the tick should skip it silently — do NOT post a `:question:` explainer to the thread, do NOT try to search for a BR record, do NOT propose a manual entry.

**Identifying signals in the source text** (any one is enough):
- `tender offer`, `invitation to tender`, `invite holders to tender`
- `tender for cash consideration`, `cash tender offer`
- `any and all tender offer`, `partial tender`
- `exchange offer`, `invitation to exchange`
- `consent solicitation`
- Body describes retiring / buying back existing notes rather than issuing new ones — usually references an existing ISIN of an outstanding bond with a specific coupon and maturity.

**How to apply:**
1. Read the message text (and any attached file). If it matches the tender-offer signals above, skip immediately.
2. Write a state-delta entry: `{"<message_ts>": {"checked_at": "<ISO UTC>", "verdict": "skipped"}}`. Do not post to Slack.
3. Do not call `bondradar_api.py search` on tender-offer issuers — you'll get either no match or a stale primary-issuance record that doesn't correspond to the tender.

**Why:** Finn on Rentokil Initial plc tender-offer (id 14640xxx-ish, no BR deal found): the tick posted a `:question:` explainer saying "no Bond Radar deal found — tender-only". Finn: "just ignore tender offers like this as they are separate from the deal updates". No Slack post at all is the right output.

Related: the same skip-silently pattern is already used for non-deal ✅'d messages that aren't deal-related at all (chatter, off-topic). This just adds tender/exchange/consent-solicitation to that skip list explicitly.
