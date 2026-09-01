---
name: bondradar-canadian-bail-inable-snp
description: "Canadian bail-inable senior notes count as Senior Non-Preferred (SNP). Set `seniorNonPreferred=true` on the priced-deal form and include SNP in the format flags on the outgoing message."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-01T00:37:05.896Z
---

Canadian banks issue senior notes under the **bail-in regime** — under Canadian regulation, these bail-inable senior notes rank as Senior Non-Preferred (SNP) internally, but the outgoing house-style vocabulary is `bail-inable`, NOT `SNP` / `Senior Non-Preferred`:

- **Priced-deal form**: `seniorNonPreferred=true`, `seniorPreferred=false`. This is the internal SNP categorisation.
- **Outgoing BR body**: use `bail-inable` (e.g. `Senior unsecured bail-inable notes` / `Bail-inable Notes`). Do NOT rewrite to `Senior Non-Preferred`.
- **Headline format flag**: use `bail-inable` — NOT `SNP` (e.g. `** NBC USD1.25bn 3NC2 bail-inable: Priced at T+65bp`).

**Why:** Finn on National Bank of Canada USD1.25bn 3NC2 Priced (id 14640158, priced-deal 14640180): tick marked `seniorPreferred=false / seniorNonPreferred=false ✓ (plain Senior Unsecured, not SP/SNP ranking)` as clean. Finn: "need to remember canadian bail-inable notes are senior non preferred". So the correct value was `seniorNonPreferred=true`, and the body / headline should have been treated as SNP.

**How to apply:** When walking a priced-deal on a Canadian bank issuer (BNS, BMO, RBC, TD, CIBC, National Bank of Canada, Desjardins, etc.), check the source for "bail-in" / "bail-inable" language. If present:

- Flag the priced-deal form's `seniorNonPreferred=false` as needing to be `true`.
- Body wording is `bail-inable` (`Senior unsecured bail-inable notes` or similar). Do NOT propose rewriting to `Senior Non-Preferred`.
- Headline format flag is `bail-inable`. Do NOT propose adding `SNP`.

Finn: "can just say bail-inable in headline and body for these just needs ticked in priced deal form". So the SNP categorisation only surfaces internally on the admin form; the outgoing message just says bail-inable.

Do NOT apply this to Canadian corporate issuers (Enbridge, TC Energy, etc.) — bail-in regime is bank-specific. Do NOT apply to Canadian bank covered bonds or subordinated deals — those are their own categories.

Related: [[bondradar-opco-holdco]] (Canadian banks don't tick OpCo/HoldCo either — same jurisdictional cluster as this rule).
