---
name: bondradar-clear-fix-bullets
description: "Fix bullets must be in plain English, generously spaced (blank line between each), and readable by a human scanning the thread. Never bunch multiple items together or use jargon-heavy shorthand."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-02T13:38:27.439Z
---

Every flagged QA reply ends with a `Fix:` section. Two requirements:

## 1. Plain-English wording

Each bullet must read as clear, human directions — not a diff patch or LLM shorthand. Someone reading the thread on their phone should understand exactly what to change in one glance, without needing to decode field names.

**Rules of thumb:**

- Say what to do, not just what's wrong. `Change X to Y in the body` beats `Body: X → Y`.
- Use the desk's own vocabulary: "the headline", "the Priced body", "the tranche form's timing field", "the additionalInfo field on the priced-deal form".
- If a field name is opaque (`fpr`, `hgDetails.regionAmericas`), gloss it in the bullet: "Reoffer price (`fpr` on the priced-deal form)".
- One clear reason per bullet, in plain terms — not "per checklist rule bondradar-X".

## 2. Spacing — blank line between bullets

Bullets must be visually separated. In Slack markdown that means **a blank line between each bullet** so the thread renders with real gaps, not a bunched-up block. Do NOT run bullets together on adjacent lines.

## Fix section format

```
Fix:

• <Plain-English direction — what to change, where, and to what.> <One-line reason in the desk's own words.>

• <Second defect, same shape.>

• <Third defect.>
```

## Good examples

```
Fix:

• On the priced-deal form (id 14640665), populate the `finalBooks` field with 2500. It's currently blank, and the Launched-stage source disclosed final books over USD2.5bn (excl JLM).

• In the Priced body, drop the `Book Update:` prefix from the last line. The book-figure line at Priced doesn't take the `Book Update:` prefix — that's only for pre-pricing stages.

• On the priced-deal form (id 14640653), untick `opCo`. BPCE SA is a French bank, and OpCo/HoldCo only applies to UK / Swiss / US / Japanese-megabank issuers plus ING / Nationwide / Softbank.
```

## Bad examples (do not emit these shapes)

```
Fix:
• Body book line — "Book Update: Final books over USD2.5bn." → "Final books over USD2.5bn." (drop prefix at Priced).
• Priced-deal form 14640665 — finalBooks: null → 2500.
• opCo: true → false (BPCE SA).
```
Problems: bunched together, arrow-form is compact but not human-readable, field names not glossed, one-clause reasons too terse.

## Rules

1. Fix section always at the END of the finding. Never earlier.
2. One bullet per defect. Never combine defects. Never split one across bullets.
3. Blank line between bullets. Non-negotiable.
4. Never use hedged language — `consider`, `verify`, `worth confirming`, `may need to`, `possibly`. Banned per the no-verify-hedges rule.
5. Clean findings omit the Fix section entirely.

**Why:** Finn on Santander UK USD1.5bn 3y CB Priced (id 14640273): "be very clear on what to fix please, be very clear from now on". Then a later correction: "for the fixing bullet points it needs to be more clear use layman terms and be sperated more it is too bunched". So the first rule pass produced correct-shape bullets but they read as compact jargon and were run together — the desk wants layman phrasing with clear spacing between items.

Related: [[no-verify-hedges]] (bans hedged phrasings), [[bondradar-headline-always-check]] (walk order — Fix section always comes after the walk).
