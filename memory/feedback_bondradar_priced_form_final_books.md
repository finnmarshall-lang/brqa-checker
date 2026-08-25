---
name: bondradar-priced-form-final-books
description: "Every Priced-stage QA must walk each tranche's `finalBooks` field on its priced-deal form; a null finalBooks when the source gave a final book size is a flag."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-25T15:54:32.131Z
---

On Priced / Priced tap / Book stats forms, `finalBooks` holds the deal's final book size in millions of the tranche currency (e.g. `2500.0` = EUR2.5bn). The QA walk must check this field explicitly on EVERY tranche — not just the deal-level fields (currency/spread/isin/etc.). A tranche whose `finalBooks` is `null` while the source (or another tranche of the same deal) had a final book figure is a defect — Books ops missed a step in the priced-deal admin.

**Why:** Finn flagged TenneT Germany EUR2.6bn dual-tranche Hybrid EuGB (deal 14630593, tranches 14631296 / 14631297): Tranche A had `finalBooks: 2500`, Tranche B had `finalBooks: null` — despite both being priced off the same source with the same book coverage. The tick walked every other priced-deal field on both tranches but silently skipped `finalBooks`, so the missing figure on Tranche B slipped through.

**How to apply:** In the Priced-deal form walk, on EVERY tranche, print `finalBooks=<value>` inline alongside the other fields. When the deal is dual/multi-tranche, sanity-check finalBooks against the other tranches — a single tranche with `null` when its siblings have a figure is almost always a miss, not intentional (deals rarely have partial book disclosure across tranches). Also compare against the outgoing BR message's book line — if the source ever printed a final book figure, it should live in finalBooks. Do NOT walk `finalAccounts` — it's populated inconsistently and not part of the standard checklist.

Related: [[bondradar-always-fetch-priced-form]] (always fetch priced form on Priced stages — this rule specifies what fields to walk), [[bondradar-book-line]] (source book-line phrasing rules).
