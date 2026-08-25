---
name: bondradar-headline-level-optional
description: Embedding the spread level in the BR headline is OPTIONAL specifically at Book Update. All other stages still expect it — do not overgeneralize this rule.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-25T10:54:12.034Z
---

**Book Update headlines don't need the level embedded.** `** Raiffeisenverband Salzburg EUR250m lg 5y CB: Book update` is a correct headline even though the level (`MS+29bp area`) is only in the body.

Do NOT overgeneralize this to other stages. IPTs, Guidance, Spread set, Priced, Priced tap, Launched, Final terms — those all still carry the level in the headline as normal.

**Why:** Finn cleared a QA on Raiffeisenverband Salzburg (id 14630878) where the tick flagged the Book Update headline for missing `at MS+29bp area`. Finn: "his title is fine — don't have to include the MS+29bp area." When I initially wrote this rule for all intermediate stages, Finn corrected me: "no this is just for book updates."

**How to apply:** When walking a headline whose stage word is `Book update` (single-tranche), do not flag the absence of an embedded level. For every other stage keep the existing behavior — including level required at Priced / Priced tap / Launched / Final terms, and level typically present at IPTs / Guidance / Spread set (flag only if it's contradicting the body or genuinely wrong, not if it's the standard for the stage).

Related: [[bondradar-headline-always-check]] (walk all 8 elements, but Book Update headline allows level to sit in the body), [[bondradar-no-level-embed-dual-tranche]] (dual/multi-tranche never gets an embedded joined level regardless of stage).
