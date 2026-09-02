---
name: bondradar-ggb-never-ticked
description: "The priced-deal form's `ggb` (Government-Guaranteed Bond) flag should never be ticked. Never propose setting `ggb=true` on any deal, regardless of what the source's guarantee structure looks like."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-02T12:07:36.399Z
---

**Do not tick `ggb` on the priced-deal form.** Per desk practice, this flag stays `false` on every deal. Even when the notes are explicitly and unconditionally guaranteed by a sovereign (e.g. BGK guaranteed by the State Treasury of Poland, KfW guaranteed by the Federal Republic of Germany, ESM/EU sovereign-backed issuers, agency-guaranteed deals) — do not propose `ggb=true`.

**How to apply:**

1. Walk the priced-deal form's additional-info booleans and check `ggb` is `false`.
2. If it's `true` → flag it and propose `ggb=false`.
3. If it's `false` → clean; do NOT propose `ggb=true` even if the deal has an obvious sovereign guarantee.

**Why:** Finn on BGK USD2.5bn dual-tranche Priced (id 14640427, priced deals 14640717/14640718): tick proposed setting `ggb=true` because the notes are "irrevocably and unconditionally guaranteed by the State Treasury of the Republic of Poland". Finn: "GGB should not be ticked, should realistically never be ticked". The field is not the right place to record sovereign guarantees — that fact lives in the body's Guarantor line and in the ratings.

Related: [[bondradar-additional-info-field]] (other additionalInfo booleans and when they apply — GGB is the odd one out that should never apply).
