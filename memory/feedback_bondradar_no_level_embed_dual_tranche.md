---
name: feedback-bondradar-no-level-embed-dual-tranche
description: "Do NOT suggest embedding levels between issuer and stage word for dual/multi-tranche headlines (e.g. `at MS+45/65bp`). Only single-tranche headlines carry the level in-line."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-20T12:42:08.019Z
---

Do NOT suggest inserting a joined level (e.g. `at MS+45/65bp`) between the issuer/tenor and the stage word for **dual-tranche or multi-tranche** headlines.

**Correct dual-tranche patterns:**
- `** Thales EUR1bn dual-tranche: Final terms` ✓
- `** SEB EUR1.5bn dual-tranche CB: Allocations` ✓
- `** Thales EUR1bn (exp.) dual-tranche: Guidance` ✓

**WRONG suggestions to never make:**
- `** Thales EUR1bn dual-tranche at MS+45/65bp: Final terms` ✗
- `** SEB EUR1.5bn dual-tranche at MS+8/E+18bp: Final terms` ✗

Only **single-tranche** headlines embed the level between the descriptor and the stage word (`at MS+19bp: Final terms`, `at HIBOR MS-3bp: Priced`). Dual/multi-tranche headlines have two-plus levels which can't cleanly compose, so BR keeps the stage word without an embedded level and each tranche line in the body carries its own level.

**Why:** Finn corrected me on 2026-08-20 after I posted a Thales dual-tranche flag suggesting `** Thales EUR1bn dual-tranche at MS+45/65bp: Final terms` — that composed pattern isn't house style. The main Thales flag (`Launched` → `Final terms` since body opens `Spread set`) still stood; only the level-embedding suggestion was wrong.

**How to apply:** during the headline walk on any 2+ tranche deal, if the level isn't in the headline, don't flag it or suggest adding one — that's correct house style. Level lives per-tranche in the body.

See also [[br-qa-checker-project]], [[feedback-bondradar-headline-stage]].
