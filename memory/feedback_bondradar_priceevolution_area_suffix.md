---
name: bondradar-priceevolution-area-suffix
description: "When the source/body's level is quoted as area / +/- WPIR / range (i.e. NOT yet set), the tranche form's `priceEvolution` field must carry a trailing `a` suffix — `MS+110a`, `T+65a`, `3mE+55a`, etc. Only drop the `a` once spread is SET."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-03T10:56:14.309Z
---

The tranche form's `priceEvolution` field takes an `a` suffix (short for "area") while the level is still being marketed — i.e. **any pre-Spread-Set stage** where source quotes the level as an area or range: IPTs, Guidance, Revised guidance, Book Update. The `a` drops only once spread is definitively SET (Spread Set / Final Terms / Priced).

**Correct forms by stage:**

- IPTs / Guidance / Revised guidance / Book Update (level still area) → `MS+110a`, `T+65a`, `3mE+55a`, `G+170/175a`, `SOFR+50a`, `SONIA+70a`
- Spread Set / Final Terms / Launched / Priced (level locked) → `MS+110`, `T+65`, `3mE+55`, `SOFR+50` (no `a`)

**Wrong (flag):**
- Source at Guidance says `MS+110 area` / `MS+110a` / `MS+110bp area (+/- 5, WPIR)` → tranche form `priceEvolution=MS+110` (missing `a`) → flag; propose `MS+110a`.
- Source at Priced says `Spread MS+110bp` → tranche form `priceEvolution=MS+110a` (stale `a`) → flag; propose `MS+110`.

**Why:** Finn on Sage Group EUR500m 5.5-year Guidance/Book Update (id 14640340): source at Guidance stage carried `MS+110a (+/- 5, WPIR)`; the tranche form's `priceEvolution` field held `MS+110` (no `a`). I marked clean. Finn: "when the update is area the tranche should have a 'a' at the end of it so MS+110a — save to logic".

**How to apply:**

1. Determine the deal's current stage from the body opener.
2. If stage is pre-Spread-Set (IPTs / Guidance / Revised guidance / Book Update) AND the level is quoted as area / range / `+/-` / WPIR:
   - Tranche form `priceEvolution` must end with `a` → flag if missing.
3. If stage is Spread Set or later (Spread Set / FT / Launched / Priced):
   - Tranche form `priceEvolution` must NOT end with `a` → flag if stale.
4. Ranges keep the `a` too — `MS+120/125a`, `G+170/175a` — until spread is set to a single number.

Related: [[bondradar-frn-priceevolution]] (compact form on tranche `priceEvolution` — same field, different rule about the reference-rate prefix), [[bondradar-headline-always-check]] (headline level uses spelled-out forms — headline says `Guidance MS+110bp area`, tranche form says `MS+110a`, both correct for their contexts).
