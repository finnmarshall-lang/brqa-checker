---
name: feedback-bondradar-type-field
description: "Bond Radar's `type` field (EXPECTED, PRICED, etc.) is BR's own workflow state, not the current deal stage — never flag it as a stage mismatch. Judge stage from headline/message text."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-17T13:43:48.290Z
---

When QA'ing Bond Radar deals against Slack term sheets, do NOT flag the deal's `type` field (values like `EXPECTED`, `PRICED`, `IPTS`) as a stage mismatch against the Slack term-sheet stage.

An IPTs-stage update legitimately sits under `type: EXPECTED` in Bond Radar. That's how their workflow works — the `type` reflects BR's internal state, not the update stage in the message body.

**Why:** In the first dry run of the BR QA Checker (see [[br-qa-checker-project]]), I flagged a World Bank IPTs term sheet as having a "stage mismatch" because BR's `type` was `EXPECTED` while the message body described IPTs. Finn corrected: this is normal, `EXPECTED` is expected at that phase.

**How to apply:** For any Bond Radar deal QA:
- Determine the deal's current stage from the `headline` and `message` body (e.g. "IPTs are MS+40bp area..." → IPTs stage).
- Ignore `type` for stage-comparison purposes.
- The "stuck at stage" check can still use `type` combined with `changedAt` timestamp, but do NOT create standalone flags about `type` value alone.
