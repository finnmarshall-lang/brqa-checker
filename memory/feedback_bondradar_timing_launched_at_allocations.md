---
name: bondradar-timing-launched-at-allocations
description: "Tranche form `timing: \"launched\"` at the Allocations Out stage is correct carry-forward, not a stale value. Never flag it."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-02T13:30:54.367Z
---

**When a deal is at the Allocations Out stage, the tranche form's `timing` field can legitimately still read `"launched"`.** That's expected carry-forward from the Launched stage — it describes the deal's most recent forward-progress action, not the current stage.

Do NOT flag:
- `Tranche A form timing: "launched" → reflect current Allocations Out stage`
- `Tranche B: timing=launched (should be allocations)`
- Any proposal to advance the tranche `timing` field just because the deal has moved to Allocations Out.

**Why:** Finn on a dual-tranche Allocations Out finding: I flagged both tranches' `timing: "launched"` as stale, arguing "field is stale from the Launched update at 11:51 UKT; deal has since moved to Allocations at 13:15 UKT". Finn: "having launched in timing is correct for allocations".

**How to apply:** During the tranche-form walk at Allocations Out, if the `timing` field reads `launched`, mark it clean. It's the correct prior-stage-action carry-forward. Only flag `timing` when:
- It disagrees with the source's own timing prose (e.g. source says `TOE` / `Books to close 12:00 CET` but form says something contradictory).
- It's genuinely stale relative to a stage the deal never actually reached (e.g. `launched` on a deal that never went past Guidance).
- It's a nonsense value (typo, empty, etc.).

Related: [[bondradar-timing-position]] (timing position in the BR body — separate rule about body prose, not the tranche form field).
