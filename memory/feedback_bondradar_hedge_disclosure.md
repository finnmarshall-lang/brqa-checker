---
name: bondradar-hedge-disclosure
description: "Hedge reference bond + hedge ratio disclosures (`Hedges for T2 vs OBL 2.9% August 2031, HR 97%.` / `No Hedges for RT1.`) are source-only content — never flag as missing from the BR body."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-02T13:30:42.089Z
---

Source term sheets sometimes disclose hedge-related fields for capital-instrument tranches — the specific hedge reference bond and hedge ratio (e.g. `Hedges for T2 vs OBL 2.9% August 2031, HR 97%.` or `No Hedges for RT1.`). **BR body does NOT carry these disclosures**, and their absence is not a defect.

Do NOT:
- Flag the BR body for missing `Hedges for <tranche> vs <bond>` language.
- Propose adding a hedge-reference-bond line.
- Propose adding a `HR <n>%` hedge-ratio value.
- Flag `No Hedges for <tranche>` as needing to appear in the outgoing message.

**Why:** Finn on a T2/RT1 dual-tranche finding: I proposed adding "Hedges for T2 vs OBL 2.9% August 2031, HR 97%." before "No Hedges for RT1." based on source disclosure. Finn: "this doesn't need to be in message please remember".

**How to apply:** In the housekeeping / body-walk sweep, do NOT look for hedge disclosures in the source and compare against the BR body. Skip that check entirely. Same class of source-only content as: interest schedule, MiFID, MREL disqualification, day-count, TEFRA, business-day convention, Sale-into-Canada, Clearing, tax-changes call. See `feedback_bondradar_boilerplate.md` for the complete boilerplate-exclusion list.

Related: [[bondradar-boilerplate]] (main boilerplate-exclusion index).
