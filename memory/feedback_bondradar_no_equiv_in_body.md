---
name: bondradar-no-equiv-in-body
description: "`equivalent` / `equiv.` in a BR body is OPTIONAL — carry it verbatim when source discloses one (e.g. `(equiv. MS+11)`), drop it when source doesn't. Do NOT flag either way."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-02T09:22:00.775Z
---

**`equivalent` / `equiv.` is OPTIONAL in BR body.** Do NOT flag its presence and do NOT flag its absence — either is fine.

- **Source has an equivalent conversion disclosed** (e.g. `Reoffer: OAT interp.+15bps (equiv. MS+11)`, `IPTs are SOFR equivalent`) → BR body may carry it verbatim (`Spread set at FRTR 0.75% May 2028 & FRTR 2.40% September 2028+15bp (equiv. MS+11) for …`) OR drop it. Both are correct.
- **Source doesn't disclose an equivalent** → BR body doesn't invent one. Not a defect either way.

**Why:** I initially wrote a rule that treated `(equiv. MS+X)` as a defect after Finn said "can we please check the body more closely this shouldn't have the equiv" on ACOSS EUR bmk 2-year Soc (id 14640357). Finn then corrected the correction: "having the equiv in is fine if we are given it". So the rule is: source-given equivs are fine to carry; the tick shouldn't propose adding OR removing them.

Only flag when the numerical figure or the reference base of the equivalent is genuinely wrong (e.g. `(equiv. MS+50)` on a deal whose MS-conversion is actually MS+11 — that's a real number defect).

Related: [[bondradar-book-line]] (JLM qualifier — similar asymmetric-optional pattern).
