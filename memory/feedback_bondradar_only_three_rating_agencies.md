---
name: bondradar-only-three-rating-agencies
description: "BR body/headline Ratings lines only carry Moody's, S&P, and Fitch. Never flag a missing Scope / DBRS / KBRA / other secondary-agency rating as a defect."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-01T06:45:25.778Z
---

Only the three main rating agencies count in BR house style:

- **Moody's**
- **S&P**
- **Fitch**

Secondary or regional agencies — **Scope**, **DBRS**, **KBRA**, **JCR**, **R&I**, **ARC Ratings**, etc. — are NOT included in the BR body's Ratings line or on the priced-deal form's `moodys` / `snp` / `fitch` fields (obviously). Do NOT flag their absence, do NOT propose adding them.

**Why:** Finn on CFF EUR Benchmark 10y CB Guidance (id 14640259): source and mandate history gave a three-agency rating triplet Aaa/AAA/AAA (Moody's/S&P/Scope). Outgoing BR body carried Aaa/AAA (Moody's/S&P). Tick flagged the Scope rating as dropped and proposed rewriting to `Aaa/AAA/AAA (Moody's/S&P/Scope)`. Finn: "you should know that it's only the 3 rating agencies Moody's, S&P and Fitch".

Note the source had Scope specifically here (a common secondary on covered bonds); the tick over-eagerly treated any 3-agency source triplet as authoritative. The rule is the OPPOSITE — BR only publishes M/S/F.

**How to apply:** When walking the Ratings line:

- Confirm the M/S/F values against the source (each is `NR` / `NA` if not disclosed).
- Ignore any Scope / DBRS / KBRA / other agency values in the source, even if the source presents them alongside the main three.
- If Moody's or S&P or Fitch is genuinely missing from BR when source disclosed it, that's a real flag.
- Do NOT propose adding secondary-agency ratings to bring the BR line into alignment with a source that carried extras.

Related: [[bondradar-book-or-rating-field]] (EM tranche form's `bookOrRating` uses M/S/F triplet, same three-agency vocabulary).
