---
name: bondradar-tap-use-original-isin
description: "On taps / reopenings, the BR body and priced-deal form's `isin` field must carry the ORIGINAL bond's ISIN, not the temporary \"reopening ISIN\" that will later consolidate."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-03T11:32:11.711Z
---

Taps / reopenings frequently come with two ISINs in the source term sheet:

- **`Original ISIN`** (or `Original ISIN / Valor`) — the pre-existing bond line the tap will consolidate into.
- **A temporary reopening ISIN** (labelled `ISIN / Valor` alone, or `Temporary ISIN`) — a separate identifier used only until the accrued-interest window closes and the tap folds into the original line.

**BR always uses the ORIGINAL ISIN.** The temporary reopening ISIN never appears in the outgoing body or on the priced-deal form.

**Correct on a tap:**
- Body: `... ISIN <ORIGINAL>.`
- Priced-deal form `isin`: `<ORIGINAL>`
- Priced-deal form `figi` / `bloombergCode`: also inherited from the original line.

**Wrong (flag):**
- Body / priced-deal form carrying the temporary reopening ISIN → flag; propose the original ISIN from the source's `Original ISIN` field.

**Why:** Finn on a CHF tap: source term sheet listed `CH1605365068` as `ISIN / Valor` (reopening, 108 days accrued interest) and `CH1415780126` as `Original ISIN / Valor`. Tick proposed the reopening ISIN. Finn: "on BR we shoud always use original isin".

**How to apply:**

1. On any tap / reopening / increase update, scan the source for both a plain `ISIN` line AND an `Original ISIN` line.
2. If both are present:
   - Body's `ISIN <X>` should be the `Original ISIN` value.
   - Priced-deal form `isin` should be the `Original ISIN` value.
   - Priced-deal form `figi` / `bloombergCode` typically also inherit from the original bond's record — these are usually carried across automatically via `parentPricedDeal`.
3. If only one ISIN is disclosed → use that; no flag.

Related: [[bondradar-additional-info-field]] (taps trigger `sale of retained bond` on additionalInfo in the specific retained-bond case, unrelated to the ISIN rule but same "tap treatment" cluster).
