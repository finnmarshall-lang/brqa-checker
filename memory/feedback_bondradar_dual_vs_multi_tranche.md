---
name: feedback-bondradar-dual-vs-multi-tranche
description: "Bond Radar naming rule — 2 tranches is `dual-tranche`, 3+ is `multi-tranche`. Never call a 2-tranche deal multi-tranche."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-18T12:37:24.946Z
---

Bond Radar tranche naming:

- **2 tranches → `dual-tranche`** (in the headline and body).
- **3 or more tranches → `multi-tranche`**.
- Never call a 2-tranche deal `multi-tranche`.

**Why:** In the Santander USD dual-tranche SNP IPTs QA (BR id 14620853), the BR headline read `** Santander USD bmk multi-tranche SNP: IPTs` for a 2-tranche deal (4NC3 + 8NC7). I marked it clean. Finn corrected: "this is wrong as it's a dual-tranche a multi-tranche is more than two please remember this."

**How to apply:** When QA'ing a tranched deal, count the tranches in the BR body. If it's 2 and the headline/body uses `multi-tranche`, flag it with the fix `dual-tranche`. If it's 3+, `multi-tranche` is correct. See also [[br-qa-checker-project]].
