---
name: feedback-bondradar-mandate-quotes
description: "Quotation marks wrapping a BR mandate message body are correct — do not flag them as extra punctuation. They indicate we're quoting a mandate received direct from a bank."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-18T07:52:38.555Z
---

Bond Radar mandate messages sometimes have the entire body wrapped in `"..."` quotation marks. This is INTENTIONAL: the quotes indicate that the body is a verbatim quotation of a mandate received directly from a bank, rather than a reformatted term sheet. Do not flag the quotes as extra/wrong punctuation.

**Why:** In the AUSCAP mandated tap QA (BR id 14620686), I flagged `Extra "" quotes wrapping the message body`. Finn corrected: "Quotes should be there if we received mandate from bank."

**How to apply:** When you see a BR message wrapped in `"..."`:
- Default: assume the quotes are correct (mandate from a bank).
- Only flag if you have clear evidence the source was NOT a direct mandate quotation (e.g. the BR body is a reformatted term sheet with distinct structure, not a bank's mandate text).

See also [[br-qa-checker-project]].
