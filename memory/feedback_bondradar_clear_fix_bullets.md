---
name: bondradar-clear-fix-bullets
description: "Every flagged QA finding MUST end with a clearly-formatted `Fix:` section listing each defect as an unambiguous bullet — field / current value / correct value. No burying the ask inside prose."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-01T15:35:42.991Z
---

Every flagged QA reply MUST end with a `Fix:` section that spells out each defect as its own bullet. Each bullet is unambiguous about **what to change, where, and to what**. Do not weave the fix into the walkthrough paragraphs — those are for evidence; the Fix section is for action.

**Required bullet shape:**

- `• <Field / location> — <current value> → <correct value>. <One-clause reason if not obvious.>`

**Concrete examples of good bullets:**

- `• Body book line — "Book Update: Final books over USD2.5bn (excl JLM)." → "Final books over USD2.5bn (excl JLM)." (drop the `Book Update:` prefix at Priced).`
- `• Priced-deal form 14640665 — finalBooks: null → 2500. (source disclosed Final books over USD2.5bn (excl JLM) at Launched).`
- `• Headline stage word — "Book update" → "Revised guidance MS+9bp area" (level tightened from MS+11bp to MS+9bp).`
- `• Priced-deal form 14640653 — opCo: true → false (BPCE SA is a French bank, not on the OpCo/HoldCo whitelist).`

**Format rules:**

1. Fix section always at the END of the finding, after the walkthrough sections. Never before.
2. One bullet per defect. Never combine two defects into a single bullet. Never split one defect across multiple bullets.
3. Each bullet leads with the field / location (`Body book line`, `Headline stage word`, `Priced-deal form <id>`, `Tranche form Tranche A`, `Deal-level flags`, etc.) so the desk knows exactly where to look.
4. Use the `<current> → <correct>` arrow form. State both. Do not just state the correct value — the desk needs to know what to search-and-replace.
5. Never use hedged language (`consider`, `verify`, `worth confirming`, `may need to`, `possibly`) — those are banned per the no-verify-hedges rule. If a fix is uncertain, either fetch the missing data and be certain, or don't include the bullet.

**Why:** Finn on Santander UK USD1.5bn 3y CB Priced (id 14640273): tick produced a correct finding but Finn: "be very clear on what to fix please, be very clear from now on". The fixes were embedded in paragraphs with narrative flow and diagnosis prose (⚠ FLAG lines mid-section, "Suggested rewrite:" nested inside a walk paragraph), and the desk had to hunt for the concrete asks.

**How to apply:** Complete the walkthrough sections first (Headline / Body / Tranche / Priced-form / Deal-level). Then produce a discrete `Fix:` section containing one bullet per defect, using the shape above. If the finding is clean, omit the Fix section entirely — no defects, no fix bullets.

Related: [[no-verify-hedges]] (bans hedged phrasings in every finding), [[bondradar-headline-always-check]] (walk order — Fix section always comes after the walk).
