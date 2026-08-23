---
name: feedback-bondradar-dont-nit-shorthand
description: "Don't flag punctuation-only or word-omission nits on established BR shorthand — `excl JLM` / `incl JLM` / `T+X` / etc. Only flag things that materially misinform."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-19T14:17:51.740Z
---

BR house style uses compressed shorthand for common phrases. Don't flag missing periods, dropped filler words, or minor case variations on established forms — those are stylistic latitude, not bugs.

## Accepted shorthand (do NOT flag)

- **`(excl JLM)`** or `(excl. JLM)` or `(excl. JLM interest)` — all acceptable variants for "excluding JLM interest".
- **`(incl EUR175m JLM)`** or `(incl. EUR175m JLM interest)` — all acceptable variants for "including EUR175m JLM interest". A missing period after `incl` is not a flag on its own.
- **`T+X`** / **`SMS+X`** / **`MS+X`** — established BR spread shorthand for Treasury+X, SOFR MS+X, mid-swaps+X. Never expand.
- **`bp` vs `bps`** — both fine. `48bp` and `48bps` are equivalent.
- **`Aug 2029`** / **`26 August 2029`** — either date form is fine.
- **`Book update:` vs `Books update:`** — both fine at pre-Priced stages.

## What IS worth flagging

- **Wrong or missing content** — a wrong figure (`USD1.125bn` instead of `USD11.25bn`), wrong tenor (`4NC5` vs source `4NC3`), missing coupon or spread that materially changes what the deal is.
- **House-style contract violations** — `Books over EUR3bn+` (the `+` sign is spelled-out `over`; can't stack both), `Book update:` prefix at Priced stage, `Books over` at Allocations (should be `Final books over`).
- **Field-level bugs** — `cpn: null` on a priced deal, wrong currency in tranche form, `regionAmericas: false` on a USD deal, `expectedPageCount` mismatch with tranche count.

## Why

On CPPIB Allocations Out (id 14620830), I flagged `(excl JLM)` as needing to be `(excl. JLM interest)` — a punctuation + missing-word nit. Finn corrected: "that is too harsh". The two forms carry the same meaning and both are seen in the wild — flagging them wastes reviewer attention on non-issues.

## How to apply

Before posting a nit-flag: does this change what the deal *means* or what the reader takes away? If no — hold it. Only flag issues that materially misinform, break house-style contracts, or diverge in field data.

See also [[br-qa-checker-project]] and [[feedback-bondradar-no-verify-hedges]].
