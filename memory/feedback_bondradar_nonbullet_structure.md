---
name: bondradar-nonbullet-structure
description: "The priced-deal `nonBullet` field holds a structure code like `16NC6`, not a Y/N flag. Never flag it as \"holding garbage\" for containing a structure string."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-25T15:57:23.895Z
---

The `nonBullet` field on the priced-deal form is a **structure code** (e.g. `16NC6`, `10NC5`, `30NC10`), not a boolean or Y/N indicator. It describes the non-bullet call structure of the bond — the value `16NC6` for a 16-year deal callable from year 6 is correct.

**Why:** Finn cleared a QA on La Mondiale EUR500m 16NC6 T2 (deal 14631095, priced 14631286): I flagged `nonBullet: "16NC6"` as garbage, arguing it should be `Y`/`N`. Finn: "16NC6 is correct for the non-bullet."

**How to apply:** When walking the priced-deal form, treat `nonBullet` as a structure-code field. Only flag it when:
- It contradicts the tranche `structure` field (e.g. tranche says `10NC5` but nonBullet says `16NC6`).
- It's null on a deal that is clearly non-bullet (has a call schedule / NCX structure in the body).
- It carries the structure of a different tranche on a multi-tranche deal.

Do NOT propose changing it to `Y` or `N`. Do NOT propose swapping it against another priced-deal in the tick's context — different deals have different structures.

Related: [[bondradar-structure-8char-limit]] (parent-tranche `structure` field is 8-char capped; nonBullet on the priced-deal form is not).
