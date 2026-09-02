---
name: bondradar-benchmark-reference-required
description: "BR body must carry the specific benchmark reference (UKT for GBP, UST for USD, DBR/OAT for EUR, etc.) alongside the spread — flag when the reference is missing."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-02T08:10:28.409Z
---

Every BR body that quotes a Gilts/Treasuries/mid-swap spread MUST include the specific benchmark reference the spread is being quoted against. The spread alone (`G+170bp` / `T+65bp` / `MS+29bp`) is not enough — the desk needs to see WHICH underlying benchmark bond it references, spelled out.

**Required reference forms (spelled-out month + year format — see `feedback_bondradar_benchmark_date_format.md`):**

- **GBP** priced off Gilts → `UKT <coupon>% <DD Month YYYY>` (e.g. `UKT 4.25% 07 March 2033+22.8bp`, `UKT 4.125% 07 March 2033`).
- **USD** priced off Treasuries → `UST <coupon>% <DD Month YYYY>` (e.g. `UST 4.25% 15 August 2029+22.8bp`).
- **EUR** priced off Bunds/OATs → `DBR <coupon>% <Month YYYY>` (e.g. `DBR 0% August 2032+147.7bp`) or `OAT <coupon>% <DD Month YYYY>`.
- **CHF** priced off Confederation → `CH <coupon>% <Month YYYY>`.
- **JPY** priced off JGBs → `JGB <coupon>% <Month YYYY>`.

The reference typically appears next to the spread with a `/` separator: `Reoffer 99.523, spread G+107bp / UKT 4.125% 07 March 2033+22.8bp.`

**Required at every stage where a spread is stated with a benchmark:**
- Spread set / Final terms / Launched / Priced — always.
- Guidance / IPTs with a mid-swap or Gilt reference — required when source discloses it.

**Not required:**
- Pure FRN tranches priced off SOFR/SONIA/EURIBOR/SARON — the reference rate IS the benchmark; no bond needed.
- Deals priced mid-swap only (no Gilt/Treasury quoted in source).

**How to flag:**
1. Look at the source term sheet for a `Reference Benchmark` / `Reference Gilt` / `Reference Bond` / `Benchmark Bund` line — every syndicate-issued sheet with a Gilt/UST/Bund/OAT-tied deal will disclose one.
2. Check the BR body carries the same reference next to the spread, in spelled-out month form.
3. If the body is missing it, flag with:
   - `• Body spread reference — G+170bp → G+170bp / UKT 4.25% 07 March 2033+X. Source Reference Benchmark line names the Gilt; BR body must carry the UKT reference alongside the G+X spread.`

**Why:** Finn on Rothesay Life GBP bmk 10.5y T2 IPTs (id 14650085): I marked the deal clean. Finn: "this isn't correct the UKT benchmark reference is there! You should know this". The source's Reference Benchmark line named a specific Gilt that the BR body should have carried alongside `G+170/175bp`. Missing UKT reference on a GBP-off-Gilts deal is a real defect.

Related: [[bondradar-priced-spread-gilt-priority]] (Gilts have priority for GBP in the priced-form `spread` field), [[bondradar-benchmark-date-format]] (spelled-out month + year format for the reference date).
