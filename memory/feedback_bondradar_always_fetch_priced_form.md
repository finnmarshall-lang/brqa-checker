---
name: feedback-bondradar-always-fetch-priced-form
description: "For every Priced-stage QA (including Book Stats), always fetch the priced-deal form via `python3 bondradar_api.py priced <cat> <id>` and walk every field. Not optional."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-20T13:56:06.767Z
---

Every Priced-stage QA (also Priced tap, Priced increase, Book stats update) MUST fetch and walk the full priced-deal form. Not optional, not "if uncertain" — always.

**Command:**
```
python3 "/Users/finn.marshall/Documents/Claude/Projects/BR QA Checker/bondradar_api.py" priced <cat> <pricedDealId>
```

`pricedDealId` comes from the deal's `pricedDeals[].id`.

**Fields to walk every time:**

- Identity/basics: currency, nominal, cpn, perpetual, maturityDate, firstCallDate
- Pricing outputs: fpr, spread, yield, fxRate
- Identifiers: isin, figi, bloombergCode, bloombergNsnCode
- Ratings: moodysRating, snpRating, fitchRating (Fitch = NR when 3rd rating is Scope/DBRS/etc.)
- Format flags (exactly one true): dealRegsOnly, deal144aOnly, deal144aRegs, secRegistered, hgDetails.hg3a2, hgDetails.hgSecExempt
- Additional-info flags: covered, green, sustainable, sustainabilityLinked, social, seniorPreferred, seniorNonPreferred, holdCo, opCo, coc, mwc, cuc, subordinated, ggb
- tier (AT1 / RT1 / T1 / T2 / null for senior)
- leagueTable (usually true; false only per LT-eligibility rules)
- additionalInfo (vocabulary: MC, PC, BC, EuGB, Sukuk, ESN, Kangaroo, Samurai, atypical par calls, HY UOP shorthand, sale of retained bond, Books last heard over)
- dealBanks.active / .passive
- statsCategories (populated only for Book Stats updates)
- expectedPageId (should be null on Priced — cleared per rule)

**Why:** Finn corrected me on 2026-08-20 after I passed multiple Priced deals (Zibo Caijin, Swisscom, SEB, RLB Steiermark, NWM, Ocean Yield, RBI) clean without fetching the priced-deal form. The form carries fields not visible in the news JSON (fxRate, boolean flags, additionalInfo, per-agency ratings, bank tier split) — skipping it means silent-failure defects can slip through.

**How to apply:** on any finding where `type: PRICED` or the message body opens `Priced:`, run the `priced` CLI as part of the standard workflow before composing the verdict. Include the priced-deal id and a summary of the form walk in the finding (see recent Finland/CA Home Loan/KFW HKD verdicts for the pattern). Never mark a Priced deal clean without this walk.

See also [[br-qa-checker-project]], [[reference-bondradar-book-stats-workflow]].
