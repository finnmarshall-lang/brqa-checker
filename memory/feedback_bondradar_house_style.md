---
name: feedback-bondradar-house-style
description: "When QA'ing Bond Radar messages, apply house-style ordering rules — never carry over the source term sheet's ordering. Key rule: MWC comes before par call."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-17T15:02:04.780Z
---

Bond Radar house style has its own canonical field order that OVERRIDES whatever order the source term sheet uses. When flagging or suggesting fixes, always suggest the house-style ordering — do not tell the writer to keep the term sheet's ordering.

Concrete rules I've been corrected on:
- **`MWC` precedes `par call`**, always. Correct: `MWC, 1-month par call.` — NOT `1-month par call, MWC`. Even when the source term sheet writes `1-month par call, MWC`, the BR message must be reordered.
- **`Books above [amount]` and `Books over [amount]` are equivalent** — either is acceptable in the book-update line; don't flag as a style issue. (Finn: "they are the same thing".)

**Why:** In the BNY dry run of the BR QA Checker ([[br-qa-checker-project]]), I flagged that Tranche B was missing MWC but suggested the fix as `1-month par call, MWC` — Finn corrected: the house-style order is `MWC, 1-month par call`. The bond-radar-deal-messages skill has the full ruleset.

**How to apply:** For any QA of a BR message, load the `anthropic-skills:bond-radar-deal-messages` skill to see the canonical ordering rules, and phrase every suggested fix in house style — not in term-sheet style.
