---
name: feedback-bondradar-no-verify-hedges
description: "Don't post soft `Note: verify this…` hedges in BR QA. Either pull the full data and post a clear FLAG or a clear CLEAN — never an ambiguous middle."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-19T12:46:31.164Z
---

**Don't hedge on BR QA calls.** Every finding must be a clear FLAG or a clear CLEAN. Never post something like "Note: source says X; verify BR body has Y" as a footer on a "clean" verdict — that's an ambiguous middle that doesn't tell the human whether to act.

**Why:** On OCBC Allocations Out (id 14620847), I marked the deal clean while noting "verify BR body's book line reads `Final books over GBP1.475bn (excl. JLM interest)` (spelled-out `over`, not `+`)" as a footer. Finn corrected: "this should be flagged as it doesn't say Final books over and has a + sign be more clear". The body actually had `Book update: Books over GBP1.475bn+ (excl. JLM interest)` — three separate bugs (wrong prefix, `Books` vs `Final books`, redundant `+`) — all of which I should have caught by fetching the full body before posting.

**How to apply:**

1. **Before posting any QA verdict**, make sure you have the FULL data you need to judge it — full BR message body (not truncated to 250 chars), full priced-deal form, full tranche.details. If the batch script truncates, either re-fetch with a longer print or fetch the message text directly.
2. **A clean verdict means every field I checked passed.** If I have a doubt about a field I didn't visibly inspect, that's not clean — either fetch the field and check it, or (if fetching isn't practical) flag the uncertainty as its own finding, not a soft "verify" note.
3. **A flag verdict means I have concrete evidence of a bug.** Quote the actual BR text that's wrong, don't paraphrase.
4. **Never mix**: don't attach "verify X" hedges to a clean verdict. It reads as noise to the human and buries a real bug behind a green checkmark.

See also [[br-qa-checker-project]].
