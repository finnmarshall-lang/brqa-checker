---
name: feedback-bondradar-final-terms-casing
description: "House-style capitalisation for the Final Terms stage in BR headlines is `Final terms` (lowercase `t`), NOT `Final Terms`. Never flag lowercase `terms` as a casing error."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-20T07:33:34.965Z
---

Bond Radar's house-style casing for the Final Terms stage in headlines is `Final terms` — capital `F`, lowercase `t`. Do NOT flag lowercase `terms` and do NOT suggest `Final Terms`.

**Why:** Finn corrected me after I flagged the KFW HKD 5-year Final-terms headline (`** KFW HKD4bn 5-year at HIBOR MS-3bp: Final terms`) as a casing error on 2026-08-20. Reply verbatim: "his style is correct!" — meaning `Final terms` lowercase is the intended house style.

**How to apply:** when QA'ing a headline that ends with the Final Terms stage word, accept `Final terms` (lowercase t) as correct. Only flag if the whole word is wrong (e.g. `Spread set` when both size and spread are set) or if the case is `FINAL TERMS` all-caps / `final terms` all-lowercase.

Applies to headlines only. In prose the phrase can appear either way depending on context.

See also [[br-qa-checker-project]], [[feedback-bondradar-headline-stage]].
