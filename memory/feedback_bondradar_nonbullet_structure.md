---
name: bondradar-nonbullet-structure
description: "The priced-deal `nonBullet` field tracks CALL structures only. Callable bonds carry a structure code (`16NC6`, `10NC5`, `PNC5.5`). Non-callable amortising / sinking-fund bonds stay `N`. Never propose `Y` on an amortiser without a call date."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-01T15:11:15.523Z
---

The `nonBullet` field on the priced-deal form specifically tracks **call structures**, not any deviation from bullet. Two cases:

- **Callable bond (has a first call date, `NCX` structure)** → field holds a **structure code** like `16NC6`, `10NC5`, `PNC5.5`, `30NC10`. The code is the correct value.
- **Non-callable amortiser / sinking fund / any other non-bullet structure without a call** → field stays `N` (not `Y`, not a code). The amortisation schedule doesn't live here — that's a separate covenant detail.
- **Plain bullet** → `N`.

**How to apply:** When walking the priced-deal form, only flag `nonBullet` when:
- The bond has a call date (source's `First Call Date` / `Optional Redemption Date`) and the field is null / `N` / holds the wrong code → flag; propose the correct `NCX` structure.
- The bond is a plain bullet with no call and the field carries `Y` or a structure code → flag; propose `N`.
- The field's code contradicts the tranche `structure` (`10NC5` vs `16NC6` on the same tranche) → flag with the correct value.
- Different priced deals in the same batch — do NOT copy one deal's `nonBullet` onto another.

Do NOT propose `Y` on an amortising bond just because it has an unusual repayment schedule. `Y` is not a valid value in general — the field is either a call-structure code or `N`.

**Why (two Finn corrections that established this rule):**
- **La Mondiale EUR500m 16NC6 T2 (id 14631095, priced 14631286):** I flagged `nonBullet: "16NC6"` as garbage, arguing it should be `Y`/`N`. Finn: "16NC6 is correct for the non-bullet." → the field IS a structure code for callable bonds.
- **[Amortiser deal] priced 14640656:** I proposed setting `nonBullet=Y` because the source disclosed a 3-instalment amortisation schedule (33.33% each on 9 Jun / 9 Sep / 9 Dec 2029). Finn: "NB is a no as its not a call date" → the field only marks call structures; a sinking fund without a call stays `N`.

Related: [[bondradar-structure-8char-limit]] (parent-tranche `structure` field is 9-char capped; nonBullet on the priced-deal form isn't).
