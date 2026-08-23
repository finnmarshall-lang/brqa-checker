---
name: feedback-bondradar-issuer-name-shortening
description: "Issuer-name variations in the headline (dropped SCF, AG, N.V., trimmed to a ticker, etc.) are intentional to fit Bloomberg's headline character limit. Do NOT flag issuer-name shortening in headlines."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-20T09:13:51.838Z
---

Do not flag issuer-name shortening or variation in BR headlines. The desk trims to fit the Bloomberg headline character limit — the body carries the full legal name.

**Common trims that are fine, not flags:**

- Drop legal suffix: `SCF`, `AG`, `N.V.`, `SA`, `Ltd`, `plc`, `Corp.`, `Inc.`, `Co., Ltd.`, `Bank` (when redundant)
- Drop parent qualifier: `Home Loan SFH`, `Global Funding`, `Finance B.V.`
- Ticker/short forms: `KFW`, `RBI`, `NAB`, `CBA`, `BNG`, `SEB`, `ACA` (for Crédit Agricole)
- Casing normalisation: `Zibo` vs `ZIBO` (allow either; only flag if it looks like a real typo e.g. `ZIbo` — capital I mid-word)

**Still flag:**

- Wrong issuer entirely (different entity)
- Typographical errors in the shortened form (`ZIbo` capital-I typo)
- Inconsistency WITH the body (headline says one issuer, body says another entity)

**Why:** Finn corrected me on 2026-08-20 after I flagged Arkéa Public Sector for dropping `SCF` from the headline on a book update — trimming was intentional to fit Bloomberg's headline width, and both mandate/guidance and book update BR headlines are self-consistent for their stage.

**How to apply:** during the headline walk, accept issuer-name variations that are shorter versions of the same entity. Only flag when the change looks like a typo or points to a different issuer.

See also [[br-qa-checker-project]], [[feedback-bondradar-headline-always-check]].
