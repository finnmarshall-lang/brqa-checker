---
name: bondradar-per-tranche-denoms
description: "On multi-tranche deals where tranche denominations differ, denoms belong in the per-tranche lines, not in Common Terms. Don't cram split notation (`100k+1k (T2) / 200k+1k (RT1)`) into a single Common Terms line."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-03T07:56:57.756Z
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

## The mirror rule — shared features live in Common Terms ONLY, not both

If a feature applies identically to EVERY tranche, it lives in Common Terms **only** — do not also repeat it on each per-tranche line. Never both.

**Concrete example — MWC on 3M multi-tranche IPTs (id 14640384):** all 3 tranches have `MWC`. So MWC goes in Common Terms; the per-tranche lines drop it. Since the par-call windows differ between tranches (Tranche B `1-month par call`, Tranche C `2-month par call`), the par-call detail stays per-tranche. Correct:

```
Tranche A: EUR500m (WNG) 2-year, due 10 September 2028. IPTs MS+70bp area. ISIN XS3460877650.
Tranche B: EUR500m (WNG) 5-year, due 10 September 2031. IPTs MS+100bp area. 1-month par call. ISIN XS3460877734.
Tranche C: EUR500m (WNG) 8-year, due 10 September 2034. IPTs MS+120/125bp. 2-month par call. ISIN XS3460878203.
Common terms: … MWC. …
```

Wrong (what the tick marked clean and Finn corrected):

```
Tranche B: … MWC, 1-month par call. …
Tranche C: … MWC, 2-month par call. …
Common terms: … MWC. …
```

Rule Finn stated: "MWC can't be in common terms and in the tranches has to be one or the other but in this case it should be the common terms as all 3 tranches have MWC".

**Decision tree per feature:**
- All tranches share the feature identically → Common Terms only, drop from per-tranche lines.
- Some tranches have it, some don't (or values differ) → per-tranche lines only, drop from Common Terms.
- Same principle for MWC, CoC put, par call window, denoms, listing, law, coupon shape, format flags, tier, redemption features, etc.

Related: [[bondradar-headline-always-check]] (dual/multi-tranche headlines don't embed levels either — same principle: per-tranche detail stays per-tranche).
