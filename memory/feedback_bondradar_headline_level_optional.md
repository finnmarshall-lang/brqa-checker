---
name: bondradar-headline-level-optional
description: Embedding the spread level in the BR headline is OPTIONAL at Book Update AND at Allocations. Do NOT flag the presence or absence of the level at those stages either way. Other stages still expect it.
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-01T14:49:25.665Z
---

**Level embedding is optional at Book Update and Allocations headlines.** Include if it fits; omit if the title is getting long. Both are valid:

- `** Raiffeisenverband Salzburg EUR250m lg 5y CB: Book update` — no level, correct.
- `** Autostrade per l'Italia EUR750m lg 7y at MS+108bp: Allocations` — level embedded, correct.
- `** Autostrade per l'Italia EUR750m lg 7y: Allocations` — no level, also correct.

Do NOT flag the presence OR absence of a level at these two stages. Other stages still expect it as normal — IPTs, Guidance, Revised guidance, Spread set, Final terms / Launched, Priced, Priced tap all carry the level in the headline. Flag missing level there; flag mismatch anywhere.

**Why:** Two Finn corrections established this rule:
- **Raiffeisenverband Salzburg (id 14630878)**: I flagged a Book Update headline for missing level. Finn: "his title is fine — don't have to include the MS+29bp area."
- **Autostrade per l'Italia EUR750m lg 7y Allocations (id 14640328)**: I proposed dropping `at MS+108bp` from the Allocations headline, arguing "Allocations-stage headlines never embed a level". Finn: "no need to say this as the title isn't too long." So embedded level at Allocations is fine — decision is a length judgement, not a strict house-style rule, and either way is not a defect to flag.

**How to apply:** When walking a headline whose stage word is `Book update` or `Allocations`:
- Level embedded → no flag.
- Level absent → no flag.
- Level embedded AND contradicts body/tranche → flag (that's a real number mismatch).
For every other stage keep the existing behaviour — including level required at Priced / Priced tap / Launched / Final terms, and level typically present at IPTs / Guidance / Revised guidance / Spread set (flag only if it's contradicting the body or genuinely wrong, not if it's the standard for the stage).

Related: [[bondradar-headline-always-check]] (walk all 8 elements; Book Update AND Allocations headlines allow level to sit in the body only), [[bondradar-no-level-embed-dual-tranche]] (dual/multi-tranche never gets an embedded joined level regardless of stage).
