---
name: bondradar-cet-cest-by-source
description: NEVER flag CET vs CEST (or UKT vs BST, EST vs EDT, JST, HKT) in any direction. Timezone-label differences between source and BR do not matter, do not propose changes.
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-02T10:02:57.223Z
---

**Timezone-label differences are not defects and never appear in any QA finding.** This includes:

- `CET` vs `CEST` (Central European Time vs Central European Summer Time)
- `UKT` vs `BST` (UK time — same label used year-round in market usage)
- `EST` vs `EDT`
- `JST`, `HKT`, `AEST`, etc.

Regardless of direction:
- Source says CEST, BR says CET → do NOT flag.
- Source says CET, BR says CEST → do NOT flag.
- BR carries a timezone that disagrees with the calendar → do NOT flag.
- BR carries a timezone that disagrees with source → do NOT flag.

Just leave the timezone alone. The desk doesn't care about this and repeatedly-flagged timezone corrections waste their time.

**Why:** Two Finn corrections established this rule, but the tick kept flagging it after each.

- Deutsche Bank CHF150m 10NC5 T2 (id 14631371): I flagged CET→CEST based on the DST calendar. Finn: "go by source this should of been correct".
- Later on another deal: I flagged CET→CEST based on source saying CEST (applying the "carry source verbatim" rule from the earlier correction). Finn: "IVE SAID TO YOU THIS DOESN'T MATTER PLZ REMEMBER".

The correct rule is stronger than "match source" — it's **never flag timezone labels at all, in any direction, for any reason**. Full stop. Don't compare source to BR on timezone. Don't propose CET/CEST/UKT/BST/EST/EDT changes. Skip that check entirely.

**How to apply:** In the housekeeping/typos sweep (check f), do NOT compare timezone labels between source and BR body. If your finding contains a bullet about a timezone label — CET, CEST, UKT, BST, EST, EDT, JST, HKT — delete that bullet before posting. Even if you think it's "helpful" or "for consistency", it isn't; drop it.

Related: [[bondradar-benchmark-date-format]] (date format is a real house-style rule, unrelated).
