---
name: feedback-bondradar-benchmark-date-format
description: "BR body benchmark refs spell out month + full year — `OBL 2.1% April 2029`, not `04/29`. MM/YY shorthand is a flag; expand to `Month YYYY` (with day if source has it)."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-19T15:12:09.823Z
---

BR house style spells out **month + full year** in benchmark-note references inside the spread field of a Priced (or Spread-Set / Final-Terms / Launched) body. `MM/YY` shorthand is not used.

**Correct forms:**

- `OBL 2.1% 04/29+35bp` → `OBL 2.1% April 2029+35bp`
- `DBR 3% 08/36+54.5bp` → `DBR 3% August 2036+54.5bp`
- `T 4.25 08/15/29+22.1bp` → `UST 4.25% 15 August 2029+22.1bp` (with day when source gives it)
- `UKT 0.375 10/28/30+85bp` → `UKT 0.375% October 2030+85bp`
- Precedents in the wild: Land NRW `DBR 2.60% 15 August 2033+24.8bp`; Macquarie `UKT 0.375% October 2030+85bp`; Chiba `UST 4.375% 31 July 2031+53bp`; Finland `DBR 2.30% 15 February 2033+25.0bp`.

**When to flag:** any BR body where the benchmark note reference uses `MM/YY` (e.g. `04/29`, `08/36`) or `MM/DD/YY` shorthand instead of full `Month YYYY` (or `DD Month YYYY` when the source provides the day).

**Why:** CA Home Loan SFH Priced (id 14630118) — body had `OBL 2.1% 04/29+35bp` (Tranche A) and `DBR 3% 08/36+54.5bp` (Tranche C). Finn corrected: "date should be written out in the spread i.e OBL 2.1% 04/29+35bp should be OBL 2.1% April 2029+35bp".

**How to apply:**

1. Parse the spread field of each tranche's Priced/Spread-Set line — look for the benchmark-note reference.
2. If the year is written as 2-digit `04/29` (or dates as `04/29/29`), flag it and give the spelled-out equivalent.
3. Preserve the day when the source has it (Land NRW `15 August 2033`, Chiba `31 July 2031`); omit the day only when source itself omitted it.

See also [[br-qa-checker-project]].
