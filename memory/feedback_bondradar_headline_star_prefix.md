---
name: feedback-bondradar-headline-star-prefix
description: "Every BR headline opens with `** ` (double asterisk + trailing space). No priority tiers, no exceptions — single `*` or missing prefix is always a defect."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-20T08:20:50.224Z
---

Every Bond Radar headline must open with `** ` (double asterisk + trailing space). Fixed prefix — there is no priority-tier variation.

**How to apply:** on every finding, the first element of the headline walk is the `** ` prefix check.
- No leading `*` → flag.
- Single `*` → flag (must be `**`).
- `**` → correct.
- `***` or more → flag.

If wrong, quote the corrected form (`** <rest of headline>`) as the first fix. Applies to every feed (HG, HY, EM, covered, IMA/investor calls) and every stage (Mandated, IPTs, Guidance, Book update, Spread set, Final terms, Launched, Priced, tap).

**Why:** Finn confirmed on 2026-08-20 that only `**` is used — no priority-tier interpretation. I mis-heard an earlier Slack comment ("credit agricole has one star") as endorsing single `*` when the commenter was actually pointing out the same defect. Reverting to strict rule.

Known-good examples this session:
- `** RLB Steiermark EUR500m 5-year MC: Guidance MS+27bp area` ✓
- `** RBI EUR bmk 10.5NC5.5 Grn T2: IPTs MS+165/170bp` ✓
- `** Thales EUR1bn (exp.) dual-tranche: IPTs` ✓
- `** KFW HKD4bn 5-year at HIBOR MS-3bp: Final terms` ✓

Defects this session:
- `Ocean Yield USD100m PNC5 Hybrid: IPTs SOFR+375/400bp` — no prefix (missing `**`)
- `* Credit Agricole HL SFH CHF115m+ 8-year Grn CB: Spread set SARON+45bp` — single `*`, should be `**`

See also [[br-qa-checker-project]], [[feedback-bondradar-headline-always-check]].
