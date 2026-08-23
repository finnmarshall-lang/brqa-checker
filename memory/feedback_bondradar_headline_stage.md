---
# 2026-08-20 refinement: `Launched` and `Final terms` are INTERCHANGEABLE in the
# headline when the body opens `Spread set at X + size set at Y` (both set).
# Either stage word is acceptable — do not flag one in favour of the other.
# Confirmed on Thales dual-tranche (retained "Launched") and HDFC Bank USD dual-tranche
# ("launched or final terms is fine here" — Finn, 2026-08-20).
# Still flag genuinely-wrong stage words: `Spread set` when size also set,
# `Priced at [level]` when body opens `IPTs are`, etc.
---
name: feedback-bondradar-headline-stage
description: "BR headline stage word must match the body's opening. e.g. if body opens `Launched: Size set at …`, headline ends `Launched at [level]`, not `Final Terms`."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-19T12:27:39.243Z
---

Bond Radar house style: the stage word at the end of the headline must match how the body opens.

- Body opens `Launched: Size set at …` → headline ends `… : Launched at [level]` (NOT `Final Terms`).
- Body opens `Spread set at …` → the headline word depends on whether size is also set:
  - **Spread set, size still `bmk` or unset** → headline ends `Spread set MS+X` (or similar Spread Set variant).
  - **BOTH spread and size set** (body reads `Spread set at MS+X and size set at USDXbn` etc.) → headline ends `Final Terms`, NOT `Spread set`. The stage has advanced past pure Spread Set once size is confirmed. Correct form: `[Issuer] USDXbn N-year at MS+X: Final Terms`.
- Body opens `Priced: …` → headline ends `Priced at [level]`. This applies even if BR's workflow state is "Allocations" — the headline word `Allocations` is NOT an acceptable substitute for `Priced at [level]` when the body opens with `Priced:`. If the body is Priced-format, the headline must say `Priced at [level]`, full stop.
- Body opens `Guidance is …` → headline ends `Guidance [level]`.
- Body opens `Guidance remains …` / `IPTs remain …` (book update) → headline ends `Book update`.

If headline says one stage but body opens with another, flag the mismatch.

**Why:** Three corrections:
1. Kotak Mahindra Bank Launched (BR id 14620227): headline `Final Terms`, body opens `Launched:` — Finn corrected me: "Title should reflect the message this says final terms when the title should be launched at: .... which follows the format".
2. Deutsche Telekom Priced (BR id 14620737): headline `... at G+78bp: Allocations`, body opens `Priced: GBP400m, ...` — I marked it clean thinking `Allocations` was a valid BR workflow-stage headline word. Finn corrected: "the title should be priced not allocations". The headline word must match the body opener regardless of BR's underlying workflow state.
3. Macquarie Group GBP500m long 4y (BR id 14630149): headline `Macquarie Group GBP500m long 4y: Spread set at G+85bp`, body opens `Spread set at UKT+85 and size set at GBP500m` — I marked the headline stage as matching. Finn corrected: "this should be a final terms title as size and spread/yield is set". Once both spread AND size are set, the stage has advanced to Final Terms — headline should say `... at G+85bp: Final Terms`.

**How to apply:** When QA'ing any BR message with a stage keyword in its opening (Launched / Priced / Spread set / Guidance / IPTs / remains / etc.), check the headline ends with the same stage word. If not, flag the mismatch and suggest a corrected headline. See also [[br-qa-checker-project]].
