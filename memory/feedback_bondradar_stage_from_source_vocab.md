---
name: bondradar-stage-from-source-vocab
description: "Detect the BR stage from the SOURCE term sheet's own stage-word vocabulary, not by defaulting to IPTs. Source labels the stage explicitly — `IPTs`, `Initial Guidance`, `Guidance`, `Revised guidance`, `Spread set`, `Final terms`, etc."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-07T06:51:00.435Z
---

Determine the BR update's stage from the source term sheet's own stage vocabulary. Do NOT default to `IPTs` on any first-marketing update.

## Source stage words → BR stage

| Source label(s) | BR stage |
| --- | --- |
| `IPTs`, `Initial Price Thoughts`, `IPT` | `IPTs` |
| `Initial Guidance`, `Price Guidance`, `Guidance` (when first-appearing) | `Guidance` |
| `Revised Guidance`, `Guidance revised at`, `Revised Price Guidance` | `Revised guidance` |
| `Spread set at`, `Spread fixed`, `Price fixed at` | `Spread set` |
| `Size set` + `Spread set` (both together) | `Final terms` / `Launched` (interchangeable) |
| `Priced`, `Reoffer` line with final coupon/spread | `Priced` |
| Post-Priced stats block | `Book stats` |

If source explicitly says `Initial Guidance` and the BR body opens `IPTs are …`, that's a stage-mismatch defect — flag it. Same in reverse.

**Why:** Finn on Nordea Mortgage Bank EUR1.25bn dual-tranche CB (id 14650839): source term sheet's marketing-level field was labelled `Initial Guidance 3mE+23bps area / MS+27bps area`. BR body opened `IPTs are 3mE+23bp area for …` and headline read `IPTs`. Tick took the BR body's own wording as authoritative and marked stage clean. Finn: "this should have noticed that it's guidsncd rather than IPTs please make sure to check the stage for the message and title- please save to memory".

**How to apply:**

1. Fetch the source term sheet / Slack forward. Find its stage-word — the field label that quotes the marketing level (`IPTs`, `Initial Guidance`, `Guidance`, `Revised Guidance`, `Spread set at`, etc.).
2. Compare against BR body's opener AND the headline stage word.
3. If the source's stage-word disagrees with what BR published:
   - Body → flag body opener rewrite (e.g. `IPTs are X` → `Guidance is X`).
   - Headline → flag headline stage word (e.g. `: IPTs` → `: Guidance <level>`).
   - Both should end up in agreement with the source.
4. When source has NO explicit stage word (a bare mandate announcement or a Bloomberg wire without a marketing-level field), fall back to the previous-stage-in-history + stage-detection heuristic in `checklist.md`.

Related: [[bondradar-headline-stage]] (headline stage must match body opener — this rule extends it: body opener must also match source vocabulary), [[bondradar-revised-guidance-stage]] (specific rule for the Revised guidance transition when level moves).
