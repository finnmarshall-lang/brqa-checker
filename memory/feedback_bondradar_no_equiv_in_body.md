---
name: bondradar-no-equiv-in-body
description: "Never carry \"equivalent\" / \"equiv\" / \"equiv.\" from a source term sheet into the BR body. Flag when it appears — the desk wants concrete levels or an omitted line, never \"equivalent\" prose."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-02T09:20:47.341Z
---

**BR body must NOT contain the word "equivalent" / `equiv` / `equiv.` in any form.** Two common places it leaks in — both are defects to flag:

**Case A — FRN placeholder (pre-set FRN levels):** source describes an FRN tranche's level as `SOFR equivalent`, `EURIBOR equivalent`, `Compounded SONIA equivalent`, etc. — meaning the FRN spread will match whatever converts from the sibling fixed-rate tranche's spread. Drop the level clause or replace with the concrete SOFR+X / E+X once source publishes one.

**Case B — MS-conversion parentheticals on fixed-rate deals (e.g. OAT-interp levels):** source's spread references a specific govie or two, and BR body then appends `(equiv. MS+X)` as a parenthetical mid-swap conversion. `(equiv. MS+11)` — drop entirely. The primary reference (`OAT+15bp` / interpolated `FRTR X% May 2028 & FRTR Y% Sept 2028+15bp`) stands on its own; the mid-swap conversion is trader-desk noise that doesn't belong in the outgoing message. Finn on ACOSS EUR bmk 2-year Soc Spread set (id 14640357, marked CLEAN by the tick): body reads `Spread set at FRTR 0.75% May 2028 & FRTR 2.40% September 2028+15bp (equiv. MS+11) for...` — Finn: "can we please check the body more closely this shouldn't have the equiv". So the `(equiv. MS+11)` clause is a real defect I missed.

**Wrong (source-copied without cleanup):**
- `Tranche B: USD benchmark 4NC3 FRN, due 4 Sep 2030. IPTs are SOFR equivalent.`
- `Tranche B: EUR bmk 3y FRN. Guidance is 3mE equiv.`

**Right (pre-set):**
- `Tranche B: USD benchmark 4NC3 FRN, due 4 Sep 2030. IPTs are SOFR MS+50bp area.` — if source has an actual FRN IPT level, use it.
- If source only says "equivalent" and no concrete level, drop the FRN IPT line and leave the tranche description without a level for now. Source will publish a concrete SOFR+X once the fixed-leg spread is set.

**Why:** Finn corrected me on a body-walk that carried `IPTs are SOFR equivalent`: "can we please check the body more closely this shouldn't have the equiv". The `equivalent` phrasing is source shorthand for "no explicit level yet, will match the fixed leg" — BR doesn't publish that placeholder wording.

**How to apply:**

1. When walking any body line that quotes a level (`IPTs`, `Guidance`, `Spread set`, `Priced`), grep for `equiv` / `equivalent`. If present, flag.
2. Fix bullet form:
   - `• Body Tranche B level — "IPTs are SOFR equivalent." → drop the level clause until the concrete spread is set; body should read "Tranche B: USD benchmark 4NC3 FRN, due 4 Sep 2030."` OR
   - `• Body Tranche B level — "IPTs are SOFR equivalent." → "IPTs are SOFR MS+50bp area." (if source discloses a concrete FRN IPT elsewhere).`
3. Same rule applies at every stage — Mandated / IPTs / Guidance / Book Update / Spread Set / Priced. `equivalent` never belongs.

Related: [[bondradar-boilerplate]] (other regulatory / prospectus wording that shouldn't leak into the BR body).
