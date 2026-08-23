---
name: feedback-bondradar-perfect-verdict-phrasing
description: "For BR QA passing verdicts, use `Perfect! Great job` — not `clean`. Encouraging phrasing replaces the technical `clean` label in Slack findings."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-19T14:29:06.431Z
---

When a BR QA verdict passes with no flags, phrase the Slack finding using `Perfect! Great job` instead of `clean`.

**Old header (deprecated):**
`*BR QA — id <X> — <Issuer> <deal descriptor> ✅ clean*`

**New header (use this):**
`*BR QA — id <X> — <Issuer> <deal descriptor> ✅ Perfect! Great job*`

Same structure otherwise — quote the BR headline + body in a Slack blockquote, then note the checks that passed. Encouraging tone throughout the write-up.

The `flagged` verdict phrasing stays the same (`⚠️ flagged (<what area>)`) — only the passing verdict changes.

**Why:** Finn: "instead of saying 'clean' lets say Perfect! Great job".

**How to apply:**

1. All future passing QA findings in Slack use `Perfect! Great job` in the header line, not `clean`.
2. Internal state file (`state.json`) can keep `verdict: "clean"` as the value — that's structured data, not human-facing. Only the Slack post text changes.
3. When reviewing verified fields, lean into positive framing (e.g. "great to see …") but keep the report factual.

See also [[br-qa-checker-project]].
