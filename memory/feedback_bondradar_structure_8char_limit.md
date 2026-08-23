---
name: feedback-bondradar-structure-8char-limit
description: "BR tranche form `structure` field has an 9-character limit. Long tenor descriptors like `11.5NC10.5` (10 chars) get truncated to `11.5NC10` (9 chars). This is by design, not a bug — don't flag."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-19T14:00:47.302Z
---

The BR admin's tranche `structure` field (visible on the tranche form as `Structure` in the details table) is **capped at 9 characters**. Any longer tenor descriptor is truncated on save.

**How truncation shows up:**

- `11.5NC10.5` (10 chars) → doesn't fit; stored as `11.5NC10.` or `11.5NC10` (9 chars).
- `10.5NC5.5` (9 chars) → fits exactly.
- `30NC5.75` (8 chars) → fits fine.
- `3y FRN CB` (9 chars incl. space) → fits exactly, no truncation. Confirmed on CA Home Loan Tranche B.
- Body message ALWAYS renders the full descriptor (`11.5NC10.5 fixed-to-FRN` etc.) — the truncation is only inside the compressed form field.

**Why:** I flagged Mizuho FG Tranche B `structure: '11.5NC10'` as a `.5`-missing typo four separate times today (id 14630107). Finn corrected: "There is only [9] characters in the tranche so the .5 can't fit". The apparent typo is actually the correct on-form representation given the field width.

**How to apply during QA:**

1. When the tranche `structure` field shows a truncated-looking value like `11.5NC10`, `10.5NC5`, `9.5NC8.`, cross-check against the body text — if the body has the full descriptor with `.5`, the form's shorter value is the field-length truncation, not a bug.
2. Only flag `structure` field values when they meaningfully disagree with the body (e.g. `4NC5` on a body-says-`4NC3` deal — that's a real typo, different digit not truncation).
3. Same limit likely applies to other short form fields; when unsure whether a truncation is by design or a bug, check the body/outgoing text before flagging.

See also [[br-qa-checker-project]].
