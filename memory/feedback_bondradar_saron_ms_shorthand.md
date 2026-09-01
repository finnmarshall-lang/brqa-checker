---
name: bondradar-saron-ms-shorthand
description: "In BR headlines and message bodies, CHF/SARON spreads use `SARON MS+X` (with MS). Bare `SARON+X` in body/headline is a defect. Tranche/priced-deal form fields use the compact `SARON+X` / `SMS+X` — that's system-generated and correct."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-01T11:56:39.590Z
---

## Scope — CHF/SARON only

**This rule applies to SARON (CHF) deals only.** Do NOT extrapolate to other reference rates:

- **USD / SOFR**: tranche form's `priceEvolution` uses `SMS+X` (compact form, MS baked in — the `S` in `SMS` stands for SOFR). Keep `SMS+X` as-is. Do NOT rewrite to `SOFR+X` on a USD tranche.
- **GBP / SONIA**: `SONIA MS+X` in outgoing message, compact `SMS+X`-style on the tranche form. Not this rule.
- **EUR / Euribor**: see `feedback_bondradar_frn_priceevolution.md` for the `E+X` convention.

Finn on Dexia USD1bn 3y IPTs (id 14640551): I proposed rewriting Tranche A's `priceEvolution=SMS+50a` to `SOFR+50a` "per the same shorthand convention used for SARON MS". Finn: "what are you doing this rule is for CHF deals only". Do NOT apply the drop-MS rewrite to USD/SOFR tranche fields.

## Two-tier rule for SARON spreads on CHF deals:

## Outgoing BR message (headline + body)

Correct form: `SARON MS+X` (with `MS`). This is house style.

- ✓ `** Rentenbank CHF50m+ Mar 2036 tap at SARON MS+20bp: Timing update`
- ✓ `Spread is set at SARON MS+20bp for Landwirtschaftliche Rentenbank's ...`
- ✗ `... at SARON+20bp: Timing update` — missing MS, flag
- ✗ `Spread is set at SARON+20bp for ...` — missing MS, flag

Flag bare `SARON+X` in the headline or the body. Suggest adding `MS`.

## Tranche form / priced-deal form fields

Both fields use bare `SARON+X` — no `MS`, no `SMS` compression:

- ✓ `priceEvolution=SARON+20` (tranche form)
- ✓ `spread=SARON+20` (priced-deal form)
- ✗ `priceEvolution=SMS+20` on the tranche form — flag; should be `SARON+20`
- ✗ `spread=SARON MS+20` on the priced-deal form — flag; should be `SARON+20`

Finn: "Tranche form (priceEvolution): SARON+x no ms at all too". So both admin-panel fields carry the bare `SARON+X` form. Any `MS` on either of those fields is a defect.

**Why:** Two Finn corrections established the two-tier rule.
- **Nordea CHF200m 8y Grn SP Priced (id 14630717)** — headline said `SARON MS+60bp`, body said `SARON+60bp`. I flagged the headline as stale-MS and proposed dropping MS. Finn: "SARON MS+ is fine in title". So MS in headline is correct.
- **Rentenbank CHF50m+ tap Timing update (id 14631697)** — headline AND body both said bare `SARON+20bp`. I marked clean. Finn: "should be SARON MS in title and body". So bare `SARON+` in the outgoing message (headline or body) is the defect — MS must be added.

Combined: MS belongs in the outgoing BR message. The Nordea case had the correct MS-in-headline; its bare-SARON-in-body was actually also a defect that Finn didn't call out at the time, but the Rentenbank correction makes the rule clear.

**How to apply:** When walking the outgoing BR headline or body on a CHF/SARON deal, check that the spread reads `SARON MS+X` — if it reads bare `SARON+X`, flag it. When walking the tranche form's `priceEvolution` or priced-deal form's `spread`, the compact `SMS+X` / `SARON+X` is canonical — don't flag.

Related: [[bondradar-frn-priceevolution]] (compact form on tranche fields — same principle, different field).
