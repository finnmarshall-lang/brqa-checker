---
name: feedback-bondradar-quote-body-in-thread
description: "Every BR QA finding (clean AND flagged) must include the full BR headline + message body verbatim in a Slack blockquote in the thread — so readers see exactly what was published without leaving the channel."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-20T06:58:02.129Z
---

Every BR QA finding posted to Slack must quote the BR message back into the thread. The finding is not complete without the body — readers need to see exactly what was published, side-by-side with the verdict.

**Format** (append to every finding, clean or flagged):

```
Published to BR:
> <full BR headline on its own blockquote line>
>
> <BR message body verbatim, one blockquote line per paragraph>
```

For multi-tranche messages: include every tranche line plus the `Common terms:` paragraph, all inside the same blockquote.

**Why:** without the quoted body, the reader has to open BR to compare — defeats the point of the automated verdict. Finn asked to bring this back after two clean ticks on 2026-08-20 skipped it. The template in `INSTRUCTIONS.md` already specifies the blockquote — this memory is the enforcement note.

**How to apply:** compose the finding as verdict header → walk-of-checks summary → `Published to BR:` blockquote of headline + body → `_(automated · BR QA Checker)_` footer. Never omit the blockquote, even on clean verdicts.

See also [[br-qa-checker-project]], [[feedback-bondradar-perfect-verdict-phrasing]].
