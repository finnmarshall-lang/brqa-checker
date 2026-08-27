---
name: feedback-bondradar-check-deal-history
description: "Before flagging a missing field in a BR body, check `dealHistoryEntries[]` — fields disclosed in prior stage updates carry forward and don't need to repeat in every update."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-27T07:00:46.812Z
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

## Also applies to book-line wording decisions

The same "walk every dealHistoryEntry" rule applies when deciding between `Final books over`, `Books closed over`, and `Books last heard over` at Priced. Before proposing a `Books last heard over` rewrite on the grounds that "no earlier stage used final/closed wording", literally grep every `dealHistoryEntries[i].message` for the substrings `Final books`, `final books`, `Books closed`, `books closed`, `orderbook closed`, `global books closed`. Do NOT rely on a summary of prior stages — a rendered list of stage names like `IPTs → Guidance → Final terms → Allocations` tells you nothing about whether any of those updates' bodies contained the closed/final wording.

**Why:** On NIB USD1bn 3-year Priced (id 14631253) I flagged the Priced body's `Final Books over USD1.75bn (incl USD200m JLM).` and proposed rewriting to `Books last heard over`, claiming "none of this deal's earlier stages ever used final books or books closed wording". Finn corrected: "this is wrong FYI they received final books at allocation" — the Allocations-stage body did carry `Final books over` language that I missed by inspecting the history at too high a level. `Final books over` at Priced was correct because a prior stage established the "final" wording; `Books last heard over` is only correct when NO earlier stage carried it.

## How to apply for book-line calls at Priced

1. Fetch the deal via `bondradar_api.py news <cat> <id>`.
2. For every entry in `dealHistoryEntries[]`, print or scan its `message` field text — not a stage-name summary.
3. If ANY prior message contains `final books`/`closed` language → `Final books over` (or `Books closed over` — see the book-line memory) is correct at Priced.
4. **Only propose `Books last heard over` when ALL of these are true**:
   - No prior message contains `final books` / `closed` language anywhere in its body text (per step 2 above).
   - The **Allocations** stage message doesn't mention books at all (or mentions them without any `final`/`closed` qualifier).
   - The **Final terms** (or Launched / Spread set) stage message doesn't say `books closed` or `final books`.
   If any one of those three is false, `Final books over` / `Books closed over` is correct — not `Books last heard over`.
5. Same logic for `additionalInfo` on the priced-deal form: only populate with `Books last heard over` when the same three conditions all hold.

See also [[br-qa-checker-project]], [[bondradar-book-line]], and [[feedback-bondradar-no-verify-hedges]].
