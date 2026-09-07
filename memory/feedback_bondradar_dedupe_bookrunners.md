---
name: bondradar-dedupe-bookrunners
description: "Source term sheets sometimes list the same bank twice in the bookrunner list (typo or copy-paste error). When comparing `banks.active[]` count to the source JLM count, dedupe first — BR carries unique banks only."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-07T12:57:58.562Z
---

Source term sheets — especially on Asian / EM deals with long JLM lists — occasionally list the same bookrunner twice. That's a source typo, not a BR defect. When validating the tranche form's `banks.active[]` count against the source JLM list, **deduplicate the source list first** before comparing counts.

**Correct behaviour:**
- Source JLM list has 28 entries but 2 are duplicates (e.g. `China CITIC Bank International` appears twice, `Haitong Bank` appears twice) → deduped count is 26.
- Tranche form `banks.active[]=26` → **clean**, matches the deduped count.
- BR body's JLM list should also show each bank once (deduplicated) — the outgoing message doesn't repeat a bank.

**Wrong:**
- Flagging the tranche form's 26 entries as needing to be 28 — that would just re-introduce the source's duplicate.
- Missing the source's duplicate in the first place — worth flagging back to the desk that source has a JLM listed twice.

**Why:** Finn on Jinan City Construction CNY bmk 5-year FPG (id 14650817): I flagged `banks.active[]` count 26 as needing to match source's 28 (4 JGC/JBR/JLMs + 24 JBR/JLMs). Finn: "another flag is China CITIC Bank International and Haitong Bank are twice in bookrunners so it had the correct entries". So 26 was already the correct deduped count and 28 was the raw-source count with dupes.

**How to apply:**

1. Before comparing `banks.active[]` count to source JLM count, run a case-insensitive dedupe on the source list (normalise whitespace, drop suffixes in parentheses like `(Hong Kong Branch)` when the base name is identical elsewhere).
2. If the deduped source count matches `banks.active[]` count → clean.
3. If source count without dedupe matches AND with dedupe doesn't match `banks.active[]` → the source has duplicates. Flag that fact as a secondary observation ("source lists X and Y twice; deduped count matches BR's 26"), don't propose adding back the duplicates to BR.
4. If both counts genuinely differ from `banks.active[]` even after dedupe → real count mismatch, flag with the correct value.

Related: [[bondradar-no-books-bank-excluded]] (`(no books)` banks drop off entirely — same "count is deduped" cluster of rules).
