---
# 2026-08-20 reinforced: NEVER pass a Priced deal clean without flagging `opCo: true`
# on an ineligible issuer — even if the desk has been ticking it consistently across
# similar deals. Finn's earlier KB Securities `OpCo: TRUE` example was demonstrating
# FIELD ORDER on the admin form, not endorsing the value. Apply the eligibility rule
# strictly: opCo/HoldCo true only for UK/Swiss/US/Japanese banks + ING/Nationwide/Softbank.
# Any other issuer with opCo=true or holdCo=true is a flag, every time.
# Correction thread: Finn "why didn't you flag opco being ticked" → "never forget that"
# earlier in the same day.
---
name: feedback-bondradar-opco-holdco
description: "BR `opCo` / `holdCo` flags apply only to bank issuers that actually use the OpCo/HoldCo debt structure — UK / Swiss / US / Japanese banks + ING + Nationwide. Not for Australian banks, Canadian banks, or non-bank corporates."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-19T14:14:02.234Z
---

The `opCo` and `holdCo` booleans on the BR priced-deal form are NOT general operating-company / holding-company labels. They're **only ticked when the issuer is actually using the OpCo/HoldCo debt-structure design** (which is a bank-capital thing, done for NSFR purposes).

## Which issuers use OpCo/HoldCo

- **UK banks** — HSBC, NatWest, Barclays, StanChart, Lloyds, Nationwide (Nationwide despite being a building society)
- **Swiss banks** — UBS, Credit Suisse
- **US banks** — JPMorgan, BofA, Citi, Wells Fargo, Goldman Sachs, Morgan Stanley
- **Japanese banks** — **megabanks only: MUFG, SMBC, Mizuho.** Regional Japanese banks (Chiba Bank, Shizuoka, Bank of Kyoto, Iyo, Concordia, etc.) do NOT use OpCo/HoldCo — they sell senior unsecured directly, so both flags stay `false`.
- **Continental European exception**: **ING** (Dutch) uses OpCo/HoldCo
- **Non-bank exceptions**: **Softbank** (Japanese multinational holding); sometimes bank-adjacent finance subsidiaries like Credit Agricole Auto Bank

## How to tell HoldCo from OpCo when both flags are candidates

- **OpCo** = higher rated, shares parent's ratings, bullet or no-call structure. Issued by the operating bank entity (e.g. `NatWest Markets Plc`, `HSBC Bank Plc`, `MUFG Bank Sydney Branch`).
- **HoldCo** = one notch or more lower rated. Issued by the parent holding company (e.g. `NatWest Group Plc`, `HSBC Holdings Plc`, `Mitsubishi UFJ Financial Group`).
- **HoldCo structural signal**: HoldCo notes typically carry a **1-year call prior to maturity** — `5NC4`, `9NC8`, `11NC10`, etc. Done to maintain NSFR eligibility (the deal can be called before it ceases counting for NSFR; investors get 5-year spread on effectively a 4-year deal).

## When neither flag is ticked

- **Most Continental European banks** (French, German, Italian, Spanish) — issue **senior preferred** or **senior non-preferred** instead; neither `opCo` nor `holdCo` gets ticked (`seniorPreferred` / `seniorNonPreferred` do the ranking work).
- **Smaller banks** selling plain senior or subordinated debt — neither.
- **Australian banks** (CBA, Westpac, NAB, ANZ) — do NOT use OpCo/HoldCo. Their T2 / senior deals should have both flags `false`.
- **Canadian banks** — typically not OpCo/HoldCo.
- **Non-bank corporates** — never OpCo/HoldCo, regardless of whether the issuing entity is technically an operating subsidiary or parent.

## Concrete example (NatWest, Sept-2026)

- Tranche A: `NatWest Markets Plc`, 5-year bullet MS+70, ratings `A1/A/AA-` → **`opCo: true`, `holdCo: false`**
- Tranche B: `NatWest Group Plc`, 9NC8 MS+110, ratings `A3/BBB+/A+` → **`holdCo: true`, `opCo: false`**

Different legal entity, 1-year call structure (9NC8), lower ratings — all three signals converge on HoldCo.

## Why (context)

Finn's 2016 note: "For the issuer the prime objective of selling HoldCo is to maintain its Net Stable Funding Ratio (NSFR). The structure means that the issuer can call the deal a year prior to maturity before it ceases to count as eligible for NSFR purposes and investors get the equivalent of a 5-year spread on a 4-year deal in the event of the deal being called."

## Corrections that produced this rule

- **CBA SGD 10NC5 T2 Priced (BR id 14630063):** priced-deal form had `opCo: true`. I incorrectly assessed this as correct, reasoning "CBA issues directly, not via HoldCo → therefore OpCo". Wrong — CBA is Australian, and Australian banks don't use the OpCo/HoldCo structure at all. Both flags should have been `false`. Finn corrected: "this should not be ticked".
- **Chiba Bank USD300m 5y Priced (BR id 14620638):** priced-deal form had `opCo: true`. I marked it as correct, reasoning "Japan is on the OpCo/HoldCo list". Wrong — only the Japanese *megabanks* (MUFG, SMBC, Mizuho) use OpCo/HoldCo. Chiba is a regional bank (source: "a leading regional bank in Japan"), which sells senior unsecured directly. Both flags should have been `false`. Finn corrected: "opco shouldn't of been ticked — i gave you the rules".

## How to apply during QA

1. Is the issuer in the OpCo/HoldCo list above (UK/Swiss/US/JP bank, ING, Nationwide, Softbank)? If NO → both flags must be `false`. Flag if either is ticked.
2. If YES → look at the legal issuer entity, ratings vs parent, and call structure (1-year call = HoldCo signal). One flag should be `true`, the other `false`. Flag if the wrong one is ticked or both are.

See also [[br-qa-checker-project]].
