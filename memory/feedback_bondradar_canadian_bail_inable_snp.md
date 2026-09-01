---
name: bondradar-canadian-bail-inable-snp
description: "Canadian bail-inable senior notes count as Senior Non-Preferred (SNP). Set `seniorNonPreferred=true` on the priced-deal form and include SNP in the format flags on the outgoing message."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-01T00:33:54.111Z
---

Canadian banks issue senior notes under the **bail-in regime** — under Canadian regulation, these bail-inable senior notes rank as Senior Non-Preferred (SNP) in the creditor hierarchy. Treat them as SNP throughout the QA:

- **Priced-deal form**: `seniorNonPreferred=true`, `seniorPreferred=false`.
- **Outgoing BR body**: describe as `Senior Non-Preferred` (not plain "Senior Unsecured").
- **Headline format flag**: include `SNP` (e.g. `** RBC USD1bn 3NC2 SNP: Priced at T+65bp`).

**Why:** Finn on National Bank of Canada USD1.25bn 3NC2 Priced (id 14640158, priced-deal 14640180): tick marked `seniorPreferred=false / seniorNonPreferred=false ✓ (plain Senior Unsecured, not SP/SNP ranking)` as clean. Finn: "need to remember canadian bail-inable notes are senior non preferred". So the correct value was `seniorNonPreferred=true`, and the body / headline should have been treated as SNP.

**How to apply:** When walking a priced-deal on a Canadian bank issuer (BNS, BMO, RBC, TD, CIBC, National Bank of Canada, Desjardins, etc.), check the source for "bail-in" / "bail-inable" language. If present:

- Flag the priced-deal form's `seniorNonPreferred=false` as needing to be `true`.
- Flag the outgoing body's "Senior Unsecured" as needing to be `Senior Non-Preferred, Bail-inable Notes`.
- Flag a headline missing the `SNP` format flag on a Canadian-bank bail-inable deal.

Do NOT apply this to Canadian corporate issuers (Enbridge, TC Energy, etc.) — bail-in regime is bank-specific. Do NOT apply to Canadian bank covered bonds or subordinated deals — those are their own categories.

Related: [[bondradar-opco-holdco]] (Canadian banks don't tick OpCo/HoldCo either — same jurisdictional cluster as this rule).
