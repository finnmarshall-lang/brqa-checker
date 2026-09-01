---
name: feedback-bondradar-structure-8char-limit
description: "BR tranche form `structure` field has an 9-character limit. Long tenor descriptors like `11.5NC10.5` (10 chars) get truncated to `11.5NC10` (9 chars). This is by design, not a bug — don't flag."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-01T16:36:09.412Z
---

The BR admin's tranche `structure` field (visible on the tranche form as `Structure` in the details table) is **capped at 9 characters**. Any longer tenor descriptor is truncated on save.

**How truncation shows up:**

- `11.5NC10.5` (10 chars) → doesn't fit; stored as `11.5NC10.` or `11.5NC10` (9 chars).
- `10.5NC5.5` (9 chars) → fits exactly.
- `30NC5.75` (8 chars) → fits fine.
- `3y FRN CB` (9 chars incl. space) → fits exactly, no truncation. Confirmed on CA Home Loan Tranche B.
- `PNC5.5 RT1` (10 chars incl. space) → doesn't fit; stored as `PNC5.5` (tenor only) with the `RT1` flag dropped. Tenor takes priority over trailing flag when the field is full.
- Body message ALWAYS renders the full descriptor (`11.5NC10.5 fixed-to-FRN`, `PNC5.5 RT1`, etc.) — the truncation is only inside the compressed form field.

**Why:** I flagged Mizuho FG Tranche B `structure: '11.5NC10'` as a `.5`-missing typo four separate times today (id 14630107). Finn corrected: "There is only [9] characters in the tranche so the .5 can't fit". The apparent typo is actually the correct on-form representation given the field width.

**How to apply during QA:**

1. When the tranche `structure` field shows a truncated-looking value like `11.5NC10`, `10.5NC5`, `9.5NC8.`, cross-check against the body text — if the body has the full descriptor with `.5`, the form's shorter value is the field-length truncation, not a bug.
2. Same for missing FLAG suffixes: when a body says `PNC5.5 RT1` / `10NC5 SNP` / etc. but the form's `structure` only carries the tenor part (e.g. `PNC5.5`, `10NC5`), that's the 9-char limit dropping the trailing flag — tenor takes priority. Do NOT propose adding the flag back to the `structure` field. The flag lives on the priced-deal form's own tier / seniorNonPreferred / etc. booleans and in the body/headline text — those are the fields to check for correctness.
3. **Do NOT propose adding `FXD` or any other rate-type suffix to the `structure` field.** BR has never put `FXD` on the tranche structure. `4NC3` is complete as-is for a fixed-rate tranche; only FRN tranches carry the `FRN` suffix to distinguish the floating leg. Finn on BMO USD bmk 4NC3 Bail-inable Guidance (id 14640595, tranche 14640597): I flagged Tranche A `structure=4NC3` as needing to be `4NC3 FXD` because Tranche B carried `4NC3 FRN`. Finn: "don't make up rules we have never put FXD in the tranche". Do not extrapolate a rule from one tranche's presence to another's absence.
4. Only flag `structure` field values when they meaningfully disagree with the body (e.g. `4NC5` on a body-says-`4NC3` deal — that's a real typo, different digit not truncation).
5. Same limit likely applies to other short form fields; when unsure whether a truncation is by design or a bug, check the body/outgoing text before flagging.

## General principle — don't invent house-style rules

If a flagged item isn't backed by a memory rule, a checklist entry, or an observed pattern in the live BR API, do NOT flag it. Better to miss a subtle defect than to propose changes based on inferred consistency ("well tranche B has it so tranche A should"). Speculative flags waste the desk's time and erode trust in the QA. When in doubt, don't flag.

See also [[br-qa-checker-project]].
