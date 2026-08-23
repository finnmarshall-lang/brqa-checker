---
name: feedback-bondradar-check-deal-history
description: "Before flagging a missing field in a BR body, check `dealHistoryEntries[]` — fields disclosed in prior stage updates carry forward and don't need to repeat in every update."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-19T14:43:06.241Z
---

BR update bodies are cumulative in context, not standalone: information disclosed in an earlier stage update (Mandated / IPO / Investor Call / IPTs / etc.) carries forward and doesn't need to be repeated in the current update. Before flagging a field as missing from the current body, walk `dealHistoryEntries[]` (the array of prior BR message versions on the same deal) and check whether the field was already stated.

## Fields that commonly carry from earlier updates

- **Ratings** (`Baa2/BBB-` etc.) — usually disclosed at Mandate / IPTs; may not be re-stated at every later update.
- **Bookrunner list** — often disclosed at Mandate; later stages may abbreviate.
- **Format** (RegS/144A) — same.
- **Guarantors** — same.
- **UoP** — same.
- **Settle date** — sometimes at Mandate/IPTs; sometimes at Priced. Check both.
- **Denominations, listing, law** — sometimes carried forward.

## Fields that MUST be in the current update's body

These are stage-specific and must appear in the update's own body:

- **Current stage level** (IPTs / Guidance / Spread / Reoffer / Yield for the stage in question).
- **Priced-stage line at Priced**: coupon, reoffer price, spread, yield, ISIN, settle date.
- **Book line** when applicable (see the book-line memory for stage-specific wording).
- **Timing** in the current update's language (`today's business`, `TOE`, `Books close at …`).

## Why

On Wealthspire USD300m 8NC3 HY Price Talk (id 14620210), I flagged "body missing Exp. Ratings Caa1/CCC" because the current Price Talk update didn't include ratings. Finn corrected: "there is rating info from the previous update we did". The ratings had been disclosed in an earlier Investor Call / Mandate update on the same deal, so the Price Talk didn't need to repeat them.

## How to apply during QA

1. Before posting a "body missing X" flag, pull the deal's `dealHistoryEntries[]` (via the news JSON — it's already in the same fetch).
2. Search prior entries for the field you're about to flag. If it's there in any prior stage, don't flag it as missing.
3. Only flag when: (a) the field is genuinely absent across the deal's full history, AND (b) house style requires it at the current stage.

See also [[br-qa-checker-project]] and [[feedback-bondradar-no-verify-hedges]].
