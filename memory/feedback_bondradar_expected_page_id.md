---
name: feedback-bondradar-expected-page-id
description: "BR `expectedPageId` clears automatically once a deal moves to `type: PRICED`. Do NOT flag `null` on a Priced deal — that's the normal post-pricing state."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-19T15:05:01.795Z
---

The BR admin's `expectedPageId` field (Expected Bloomberg page dropdown) **AND** the `expectedPageCount` field (Bloomberg total number of pages) are both **pre-Priced-only** checks. Once the deal moves to `type: PRICED`, `expectedPageId` gets cleared automatically and `expectedPageCount` is no longer a meaningful QA target — the BBG page reservation isn't needed post-pricing.

**Rule for flagging:**

- **Pre-Priced deals** (Mandated / IPTs / Guidance / Book Update / Final Terms / Launched / Allocations Out — anything with `type != PRICED`) → `expectedPageId` MUST be populated when `activeBloomberg: true`, AND `expectedPageCount` MUST equal `len(tranches)`. Flag either if wrong.
- **PRICED deals** (`type: PRICED`) → do NOT flag `expectedPageId` or `expectedPageCount`. Both are pre-pricing routing fields; they don't need to match anything post-pricing.

**Why:** I incorrectly flagged `expectedPageId: null` on three Priced deals in a row — MassMutual (id 14620753), HSBC Holdings CNH dual-tranche (id 14620643), and CBA T2 (id 14630063). Finn corrected on the HSBC one: "the bbg page disappears once it has priced". Same rule applies to the CBA T2 and MassMutual flags.

**How to apply:**

1. Check `deal.type` before applying the `expectedPageId` rule.
2. If `type == "PRICED"` → skip the `expectedPageId` check entirely (it's expected to be null).
3. If `type` is any other value AND `activeBloomberg: true` AND `expectedPageId` is null/empty → flag.

See also [[br-qa-checker-project]].
