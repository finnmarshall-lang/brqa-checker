---
name: feedback-bondradar-dont-flag-missing-smr-list-law
description: "Never flag missing Special Mandatory Redemption (SMR) — BR bodies don't carry it. Never flag missing List/Law fields — only include when the source explicitly names them."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-20T13:06:00.896Z
---

Two BR body items to STOP suggesting as missing:

1. **Special Mandatory Redemption (SMR)** — do not flag when omitted from Common terms, even for spin-off / M&A / Acquisition-Event-Call deals. BR bodies don't include the SMR clause as a house-style rule, regardless of what the source term-sheet says. Similar Acquisition Event Call details are the exception — those DO belong in the body (like Thales earlier). But SMR specifically stays out.

2. **List + Law** — do not flag when omitted. Only quote a listing venue or governing law when the source explicitly names it. If the source term-sheet doesn't provide List/Law, BR omits them and that's correct; don't propose SGX/Lux/NY defaults.

**Why:** Finn corrected me on 2026-08-20 after I flagged Vylor USD dual-tranche IPTs for missing SMR + List + Law. Verbatim: "is not required we weren't sent it plus we don't include Special Mandatory Redemption". SMR omission is house-style; List/Law omission is source-driven.

**How to apply:** on the body walk, treat SMR as never-flag. For List/Law, only flag if the SOURCE has them and BR dropped them — never when both source and BR are silent.

See also [[br-qa-checker-project]], [[feedback-bondradar-boilerplate]].
