---
name: reference-bondradar-league-table-rules
description: "BR league-table (`leagueTable` flag) eligibility rules for HG and EM — minimums, region coverage, structural exclusions, when to flag false."
metadata:
  node_type: memory
  type: reference
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-19T12:35:06.614Z
---

The `leagueTable` boolean on BR's priced-deal form is **almost always `true`** — most deals qualify. Set `false` only when a specific rule below fails. The full rules live in `/Users/finn.marshall/Documents/Claude/Projects/BR QA Checker/checklist.md` under "League-table eligibility rules"; this memory is the pocket summary for QA.

## HG (High Grade) — league-table `true` iff ALL of:

- Borrower originates from Japan / Australia / New Zealand / Western Europe / North America. SSA has its own table.
- Coupon, size, currency, maturity, issue price, and lead managers ALL disclosed.
- International bond market + international documentation (RegS, SEC Global, etc.). Domestic-only is out.
- Maturity ≥ 18 months. Hard calls/puts before 18 months exclude the deal (Make-Whole calls are fine).
- Size ≥ USD100m equivalent. For taps, the original deal must have been ≥ USD100m.
- Multi-tranche: each tranche is a separate LT record.

## EM (Emerging Markets) — league-table `true` iff ALL of:

- Borrower originates from non-Japan Asia / CEEMEA / Latam (per the region definitions in the checklist).
- International bond market + international documentation.
- Maturity ≥ 365 days. Hard calls/puts before 365 days exclude the deal (MWCs fine).
- Not an ABS / CDO / securitisation. **Exception: covered bonds from EM regions are included.**
- Coupon / size / currency / maturity / reoffer / leads disclosed.
- Sub-IG table requires ≥1 senior unsubordinated rating below IG at launch.

## When to flag

- Priced deal is HG with maturity < 18 months → `leagueTable` must be `false`. Flag if true.
- Priced deal is EM with maturity < 365 days → `leagueTable` must be `false`. Flag if true.
- Priced deal < USD100m HG → `leagueTable` must be `false`. Flag if true.
- ABS / CDO / non-covered securitisation → `leagueTable` must be `false`. Flag if true.
- Hard call/put before threshold (excl MWC) → `leagueTable` must be `false`. Flag if true.
- Otherwise → `leagueTable` must be `true`. Flag if false.

See also [[br-qa-checker-project]].
