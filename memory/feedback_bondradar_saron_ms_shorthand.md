---
name: bondradar-saron-ms-shorthand
description: "`SARON MS+X` and bare `SARON+X` are both acceptable BR house-style spread shorthands for CHF deals; never flag one against the other as a mismatch."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-24T13:19:55.510Z
---

For CHF deals priced off SARON, both spread notations are house-style:

- `SARON MS+60bp` (headline / stage lines)
- `SARON+60bp` (post-priced body / priced-deal form's `spread` field)

They are interchangeable — the headline can carry `SARON MS+` even when the priced body has already dropped the `MS`. Do NOT flag `SARON MS+X` in the headline as "stale" when the body reads `SARON+X`, and do NOT propose a rewrite that drops the `MS`. Neither is wrong.

**Why:** Finn cleared a QA finding on Nordea CHF200m 8y Grn SP (id 14630717): I flagged the headline `Priced at SARON MS+60bp` as a stale-MS mismatch against the body's `SARON+60bp` and proposed rewriting to `Priced at SARON+60bp`. Finn: "SARON MS+ is fine in title."

**How to apply:** When walking headline level ↔ body/priced-form spread on CHF (SARON) deals, treat `SARON MS+X` and `SARON+X` as the same reference. Only flag a numeric mismatch (`SARON MS+60` vs `SARON+58`) or a wrong reference base (`SARON` vs `MS` vs `Govt.`), never the presence/absence of `MS` alone. The same logic applies to any other reference-rate shorthand where `MS` is optional glue — do not invent a "canonical" form.
