---
name: bondradar-headline-level-optional
description: Embedding the spread level in the BR headline is OPTIONAL at intermediate stages (IPTs / Guidance / Book update / Spread set). Never flag its absence just because other headlines in the feed happen to include it.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-25T10:52:50.267Z
---

BR headlines carry the level at final stages (Priced / Priced tap / Launched / Final terms) because the level is locked in. At intermediate stages (**IPTs, Guidance, Book update, Spread set**) the level is either still moving or the stage word already tells the reader where to look — including it is fine, omitting it is also fine.

So `** Raiffeisenverband Salzburg EUR250m lg 5y CB: Book update` is a correct headline. Do NOT flag it for "missing MS+29bp area" just because RLB Vorarlberg / Lansforsakringar / Commerzbank Book update headlines happen to include their levels. Frequency ≠ requirement.

**Why:** Finn cleared a QA on Raiffeisenverband Salzburg (id 14630878): I flagged the Book Update headline as missing `at MS+29bp area`, citing a "convention" from other headlines. Finn: "his title is fine — don't have to include the MS+29bp area."

**How to apply:** When walking the headline at IPTs / Guidance / Book update / Spread set, treat an embedded level as a nice-to-have, not a checklist item. Only flag a level problem when:
- The level shown in the headline **contradicts** the body / tranche form (wrong number, wrong reference base, wrong sign).
- The stage is **Priced / Priced tap / Launched / Final terms** and the headline has no level at all — those stages require it.

Related: [[bondradar-headline-always-check]] (walk all 8 headline elements but with the right required-vs-optional threshold per stage), [[bondradar-no-level-embed-dual-tranche]] (dual/multi-tranche never gets an embedded joined level regardless of stage).
