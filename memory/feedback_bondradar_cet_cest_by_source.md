---
name: bondradar-cet-cest-by-source
description: "Do NOT auto-correct CET↔CEST based on the calendar — carry the source's own timezone label into BR verbatim, even if it disagrees with DST."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-26T11:56:13.509Z
---

BR body times should match what the source (Bloomberg forward / syndicate email) actually wrote. If the source says `12:15 CET` in August, BR carries `12:15 CET` — do NOT rewrite to CEST just because August is daylight-saving time.

**Why:** Finn cleared a QA on Deutsche Bank CHF150m 10NC5 T2 (id 14631371): I flagged the body's `Books to close at 12:15 CET` as needing to be CEST for a 26 August deal. Finn: "go by source this should of been correct" — the source Slack used CET, and BR was right to carry that verbatim regardless of what the calendar says.

**How to apply:** When walking BR body timing lines, compare the timezone label against what the source term-sheet / forward literally printed. Match → clean. Mismatch → flag. Do not use the deal date to derive whether CET or CEST is technically correct; that is a source-editorial call, not a house-style rule. Same treatment for UKT/BST, EST/EDT, JST, HKT — carry the source label.

This overrides the earlier stub "CET vs CEST (August = CEST)" line in tick_prompt.txt / checklist — that guidance is retired.

Related: [[bondradar-benchmark-date-format]] (spell out month + year, unrelated to timezones).
