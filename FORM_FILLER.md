# BR Admin Form Filler — Field Order

Fill the priced-deal admin form in the exact order shown below. One line per field, labels verbatim.

## Field order

```
Nominal:         <size in mm, plain number — 300 for USD300m, 4000 for HKD4bn>
Moody's Rating:  <e.g. A3, Aa1, Baa2, NR>
Coupon:          <fixed decimal e.g. 4.875, or FRN e.g. SOFR+350, or hybrid initial rate>
Maturity:        <DD Month YYYY — e.g. 26 August 2029; Perpetual if no maturity>
FPR:             <reoffer price — e.g. 99.297, 100.00>
Spread:          <e.g. T+85, MS+140, HIBOR MS-3 (no `a` — spread SET)>
Yield:           <decimal % — e.g. 5.131; blank for FRN>
LT:              <TRUE / FALSE — league-table eligibility>
ISIN:            <e.g. XS3464389678>
RegS:            <TRUE if Reg S only; FALSE otherwise>
Active:          <TRUE unless deal killed>
OpCo:            <TRUE for UK/Swiss/US/Japanese banks + ING + Nationwide + Softbank>
Tier:            <AT1 / RT1 / T1 / T2 / No Tier>
```

## Worked example — KB Securities USD300m 3-year Priced

```
Nominal:         300
Moody's Rating:  A3
Coupon:          4.875
Maturity:        26 August 2029
FPR:             99.297
Spread:          T+85
Yield:           5.131
LT:              TRUE
ISIN:            XS3464389678
RegS:            TRUE
Active:          TRUE
OpCo:            TRUE
Tier:            No Tier
```

## Notes

- **Nominal**: size in millions, no currency prefix, no `m`/`bn` suffix, no commas.
- **Coupon**: decimal for fixed (`4.875`, not `4.875%`); base+spread for FRN (`SOFR+350`).
- **Maturity**: full month name spelled out (`26 August 2029`), or `Perpetual`.
- **FPR**: 2–3 decimal places, whatever the source states (`100.00`, `99.297`).
- **Spread**: drop the `a` (area) suffix at Priced — spread is SET.
- **Yield**: decimal % without the `%` sign.
- **LT**: `TRUE` unless sub-18m HG, sub-365d EM, sub-USD100m HG, ABS/CDO (except EM covered), or missing disclosures.
- **RegS**: `TRUE` for pure Reg S only. `FALSE` for 144A/RegS dual, 144A only, SEC registered — those tick a different format flag elsewhere on the form.
- **OpCo**: only tick for UK/Swiss/US/Japanese banks + ING + Nationwide + Softbank. `FALSE` for HoldCo debt, non-bank corps, sovereigns, supras, insurers, Australian/Canadian/Nordic/Austrian/French banks.
- **Tier**: `No Tier` for senior corp/sovereign/supra/covered/senior unsec bank. `AT1`/`RT1`/`T1`/`T2` for bank subordinated capital.

## Reference

See `CHAT_GENERATOR.md` for the headline + body + deal-level flag workflow. This document is scoped to the priced-deal admin form fill only.
