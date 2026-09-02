---
name: bondradar-per-tranche-denoms
description: "On multi-tranche deals where tranche denominations differ, denoms belong in the per-tranche lines, not in Common Terms. Don't cram split notation (`100k+1k (T2) / 200k+1k (RT1)`) into a single Common Terms line."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-02T08:32:40.233Z
---

On multi-tranche BR bodies, per-tranche fields whose values DIFFER between tranches must live on the per-tranche lines, not in Common Terms.

**Denominations specifically:**

- **All tranches share the same denoms** → single denom string in Common Terms (`denoms 100k+1k.`).
- **Tranches have different denoms** → each per-tranche line carries its own denom, Common Terms says nothing about denoms.
  - ✓ Tranche A line ends with `... denoms 100k+1k.`; Tranche B line ends with `... denoms 200k+1k.`; Common Terms omits denoms.
  - ✗ Common Terms line reads `denoms 100k+1k (T2) / 200k+1k (RT1)` — the split-notation inside a single line is exactly the confusion Finn wants to avoid.

**Why:** Finn on The Ethniki EUR200m dual-tranche T2/RT1 IPTs (id 14640362): BR body had `denoms 100k+1k (T2) / 200k+1k (RT1)` inside the Common Terms paragraph. Finn: "this should pick up that the denoms should be in the individual tranche if its different no need to confuse the common terms".

**How to apply:**

1. When walking the Common Terms paragraph of a multi-tranche body, check each field for uniformity across tranches.
2. If any Common Terms field carries per-tranche split notation (e.g. `(T2) / (RT1)`, `(A) / (B)`, `(3y) / (7y)`, `(fixed) / (FRN)`) — flag it and move each half into the corresponding per-tranche line.
3. Applies to any field, not only denoms: coupon shape, listing, law, maturity, call schedules, ISIN, etc. Common Terms is for values that are genuinely common. Per-tranche variations go on the per-tranche line.

Related: [[bondradar-headline-always-check]] (dual/multi-tranche headlines don't embed levels either — same principle: per-tranche detail stays per-tranche).
