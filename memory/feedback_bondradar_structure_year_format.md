---
name: bondradar-structure-year-format
description: "Sub-2-year tranche structures use fractional-year notation (`1.5y`), not months (`18m`). Flag month-form structures on the tranche admin panel."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-27T07:34:05.283Z
---

Tranche structure codes on BR are always in years, expressed as fractional years for sub-2-year tenors:

- 18-month tenor → `1.5y` (NOT `18m`)
- 6-month tenor → `0.5y` (NOT `6m`)
- 30-month tenor → `2.5y`
- 9-month tenor → `0.75y`

The rule applies to both the outgoing BR body (`EUR benchmark 1.5y FRN`) and the tranche form's `structure` field.

**Why:** Finn flagged a defect the tick MISSED on GSK 4-tranche IPTs (deal 14631641, tranche 14631643): Tranche A's structure read `18m FRN`, but Finn: "should be 1.5y instead of 18m". The tick had walked the tranche form and marked `structure=18m FRN ✓` as clean — that was wrong. It should have been a flag.

**How to apply:** When walking a tranche's `structure` field or the body's tenor phrase, if it reads `<N>m` (e.g. `18m`, `6m`, `9m`), flag it as needing conversion to `<N/12>y` (`1.5y`, `0.5y`, `0.75y`). Same for the outgoing message body — the tenor after the currency+size should also use `y` notation. Exceptions:
- Callable structures like `10NC5`, `PerpNC5`, `16NC6` — these stay as-is; the numbers are years and `NC` marks the non-call period.
- Perpetual `Perp` / `PerpNC5` — stays.
- Whole-year figures like `3y`, `5y`, `10y`, `30y` — already correct, don't reformat.

Related: [[bondradar-structure-8char-limit]] (the parent-tranche `structure` field is 8-char capped; `1.5y FRN` fits under that limit).
