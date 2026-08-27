---
name: bondradar-frn-priceevolution
description: "FRN `priceEvolution` on the tranche form drops the reference-tenor prefix (`E+55a`, not `3mE+55a`); do not flag its absence."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-27T07:33:52.392Z
---

For floating-rate tranches, the `priceEvolution` field on the tranche form omits the reference-rate tenor prefix by convention:

- Source and BR body write the full form: `3mE+55bp area`, `6mE+40`, `SOFR+65a`, `SONIA+70a` — with the tenor for Euribor variants (`3m` / `6m`) or the plain reference for others.
- Tranche form's `priceEvolution` writes the compact form: `E+55a`, `E+40`, `SOFR+65a`, `SONIA+70a` — no `3m` / `6m` prefix in front of `E`.

Both are correct in their contexts. Do NOT flag `priceEvolution=E+55a` on a `3mE+55` FRN as "dropping the reference tenor" — the compact form is standard.

**Why:** Finn cleared a QA on GSK 4-tranche IPTs (deal 14631641, tranche 14631643): I flagged Tranche A's `priceEvolution=E+55a` as missing the `3m` prefix that the source/body carried. Finn: "no need for 3me in price evolution".

**How to apply:** In the tranche-form walk on an FRN tranche, treat `E+X` / `SOFR+X` / `SONIA+X` / `SARON+X` as the canonical `priceEvolution` value even when source and body carry a longer reference-tenor phrase. Only flag when:
- The numeric spread differs (`E+55a` vs body `3mE+60a` → real mismatch, flag).
- The reference index is wrong (`E+X` on a SOFR-based FRN → real mismatch, flag).
- The area/set suffix is wrong for the current stage (see [[bondradar-book-line]] and the standing "area suffix drops once spread SET" rule).

Related: [[bondradar-saron-ms-shorthand]] (similar MS-vs-bare interchangeability on CHF/SARON), [[bondradar-check-deal-history]].
