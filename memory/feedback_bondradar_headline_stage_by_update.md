---
name: bondradar-headline-stage-by-update
description: "The headline stage word reflects what THIS update brings, not the deal's current status. A Book Update that carries a prior Spread-set line forward is still a Book Update headline — do not rewrite to Spread set."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-26T14:22:27.155Z
---

BR updates ratchet through stages: IPTs → Guidance → Spread set → Book update → Final terms → Launched → Priced. Each update's headline stage word must reflect **what the current update is delivering as new information** — not what stage the deal has previously reached.

**Post-Spread-set book updates are still Book Updates.** Once the spread is set, subsequent updates that carry the standing "Spread is set at X for [issuer]'s ..." line forward AND add a new book size are Book Updates in headline terms, not Spread Sets. Same principle for Guidance-remains updates after Guidance, Book Update after Final Terms, etc. — the standing line at the top of the body is not the update's identity; the newly-added information at the bottom is.

**Why:** Two corrections established this rule:
- **World Bank GBP bmk 6y SDB (id 14631451):** tick flagged `** World Bank GBP bmk 6y SDB at SONIA MS+36bp: Book Update` as needing `Spread set` because the body opened `Spread is set at SONIA MS+36bp for World Bank's GBP benchmark 6-year SDB…`. Finn: "this seems correct as the spread was set in the previous update, this new update is just a book update". The Spread-set line was carried from the prior update; the new information was the book size.
- **OKB USD1bn 5-year (id 14631206):** tick flagged `** OKB USD1bn 5-year at SOFR MS+32bp: Allocations` as needing `Final terms` because the body opened `Spread set at SOFR MS+32bp for … USD1bn 5-year Global` (spread AND size both set → the pre-existing "Final terms / Launched interchangeable when body opens Spread set + size set" rule triggered). Finn: "this is at allocations". The Final-terms-style opener was carried forward; the NEW content in this update was the `Book update: … Hedge Deadline … Pricing to follow` block — that's Allocations. Headline `Allocations` is correct.

**How to apply:** When walking a headline stage word, do not match it against the body's OPENING line alone (which is the carried-forward standing paragraph). Instead:
1. Identify what part of the body is NEW in this update — usually the last paragraph or the appended line starting `Book update:` / `Guidance remains` / etc. Look for `Hedge Deadline` / `Pricing to follow` / `Allocation and pricing later today` — those markers pin the update at Allocations even if the standing paragraph reads like Final terms.
2. Match the headline stage word to that new content:
   - Body appends `Book update: Books over/above X` → headline `Book Update` ✓
   - Body appends `Book update: … Hedge Deadline … Pricing to follow` or `Allocations out. Pricing soon after` → headline `Allocations` ✓ (even when standing line has Spread set + size set)
   - Body opens `Spread set/Set at X for …` for the FIRST time → headline `Spread set` ✓
   - Body opens `Spread set at X for …` with size confirmed for the FIRST time and no Allocations markers → headline `Final terms` / `Launched` ✓
   - Body opens `Priced: <currency><size>, coupon X, due …` for the FIRST time → headline `Priced` ✓
3. Do NOT propose rewriting a headline `Book Update` to `Spread set`, or `Allocations` to `Final terms`, just because a standing Spread-set / Final-terms line is still at the top of the body.
4. This rule OVERRIDES the earlier "Final terms / Launched interchangeable when body opens Spread set + size set" heuristic when the update carries Allocations markers (Hedge Deadline / Pricing to follow). Only apply Final terms / Launched to updates that DON'T carry Allocations markers.

Related: [[bondradar-headline-stage]] (headline stage must match body — refined: matches the update's NEW body content, not the standing paragraph), [[bondradar-timing-position]] (timing sits at the end of the LATEST live line — same logic: identify the "new line" of this update).
