---
name: bondradar-hy-nc-structure
description: "HY deals with a non-call period must carry the NCX structure code in BOTH the headline and the tranche form's structure field — not just the bare tenor."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-07T08:25:48.414Z
---

On HY deals with a non-call period / call schedule (which is nearly every HY deal), the headline tenor slot AND the tranche form's `structure` field must use the **`<tenor>NC<call>` format** — not the bare tenor / not `long <N>-year` on its own.

**Correct forms:**

- HY deal with `NC2` step-down call schedule → headline `... EUR500m long 5NC2: Mandated`, tranche `structure=5NC2` (or `long 5NC2` if it fits under the 9-char cap; `5NC2` if not).
- HY deal `NC3` → `long 7NC3` / `7NC3`.
- HY deal `NC2.5` (mid-year fractional) → `5NC2.5`.
- HY perpetual with call → `PNC5`, `PNC7.5`, `PNC10.25` (see also [[bondradar-structure-year-format]] for fractional-year rules).

**Wrong (flag):**

- Headline `... EUR500m long 5-year: Mandated` when source discloses NC2 → flag; propose `long 5NC2`.
- Tranche form `structure=long 5y` when source discloses NC2 → flag; propose `long 5NC2` or `5NC2`.

**Why:** Two Finn corrections:
- Tharisa USD300m 5Y Senior Secured (id 14650080): I proposed `5-year` in headline; tranche form already carried `5NC2.5`. Finn corrected the headline to `5NC2.5`.
- Clariane EUR500m long 5-year Mandated (id 14650939): source disclosed `CALL PROTECTION | NC2 (50%, 25%, PAR)`. My headline said `long 5-year`, my tranche form said `long 5y`. Finn: "title should include the NC2 so should be long 5NC2 and the tranche should be 5NC2 please save to memory to not make the same mistake again".

**How to apply:**

1. On every HY deal (highYield: true) at any stage, source-check for a `CALL PROTECTION` / `Call option` / `NCX (…)` field or the standard HY step-down schedule (`50% / 40% / 30% / 20% / 10% of the coupon after X / Y / Z months`).
2. If NCX / call schedule is disclosed:
   - Headline tenor slot uses `<tenor>NC<call>` — e.g. `long 5NC2`, `7NC3`, `10NC5`, `PNC5.5`, `16NC6`.
   - Tranche form `structure` uses the same, subject to the 9-char cap ([[bondradar-structure-8char-limit]]).
3. Flag both places if either uses the bare tenor.

Related: [[bondradar-structure-year-format]] (fractional years for sub-2y tenors), [[bondradar-structure-8char-limit]] (9-char cap on the tranche form's structure field).
