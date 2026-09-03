---
name: bondradar-tap-use-original-isin
description: "On taps/reopenings, the priced-deal form's `isin` field always uses the ORIGINAL bond's ISIN. The BR body may carry both the Original and Temporary reopening ISIN when source discloses both — don't flag that."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-03T13:14:40.741Z
---

Taps / reopenings frequently come with two ISINs in the source term sheet:

- **`Original ISIN`** (or `Original ISIN / Valor`) — the pre-existing bond line the tap will consolidate into.
- **`Temporary Tap ISIN`** (or `ISIN / Valor` alone, or `Temporary ISIN`) — a separate identifier used only until the accrued-interest window closes.

## Priced-deal form `isin` field — always ORIGINAL

The priced-deal form's `isin` field always carries the **Original ISIN**, never the temporary reopening one. Same for `figi` / `bloombergCode`, which inherit from the original line via `parentPricedDeal`.

- Flag `isin=<temp reopening ISIN>` on the form → propose the Original ISIN value.

## BR body ISIN clause — either is acceptable

The BR body can:
- Carry ONLY the Original ISIN: `... ISIN XS3232968985.` — clean.
- Carry BOTH the Original and Temporary Tap ISINs: `... Temporary Tap ISIN XS3490003855, original ISIN XS3232968985.` — also clean (do NOT flag).

Finn: "we can have both in message if it's there" — when source discloses both, BR can mirror both in the body verbatim; the tick should not propose dropping the temporary one.

**Do NOT flag:**
- Body carrying both ISINs when source provided both.
- Body carrying only the original ISIN when source provided both.

**Do flag:**
- Body carrying only the temporary reopening ISIN and omitting the original.
- Priced-deal form's `isin` field holding the temporary reopening ISIN (see Priced-deal section above).

**Why (two Finn corrections):**
- On a CHF tap: I marked clean on a priced-deal form that carried the reopening `CH1605365068`. Finn: "on BR we shoud always use original isin". Established: form's isin field must be Original.
- On Compass Group EUR250m Jan 2035 tap Allocations (id 14650513): I flagged the body's `Temporary Tap ISIN XS3490003855, original ISIN XS3232968985` as needing to drop the temporary part. Finn: "we can have both in message if it's there". Established: body can carry both.

Combined rule: **strict on the form field, permissive in the body**.

**How to apply:**

1. On any tap / reopening / increase update, scan source for both an `Original ISIN` and a plain `ISIN` / `Temporary Tap ISIN`.
2. **Priced-deal form isin/figi/bloombergCode:** must inherit from the ORIGINAL bond via parentPricedDeal. Flag temporary values.
3. **BR body ISIN clause:** either the original alone OR both ISINs is fine. Only flag when the body carries the temporary alone without the original.

Related: [[bondradar-additional-info-field]] (taps trigger `sale of retained bond` on additionalInfo in the specific retained-bond case).
