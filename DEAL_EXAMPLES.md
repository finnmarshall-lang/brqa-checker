# BR Deal Examples — 2026-08-20

Real deals from today's QA log, one per stage, showing the actual headline + body + tranche form values that were published (or should have been). Use these as reference patterns when generating new updates from source term-sheets.

Each block is labelled with the BR deal ID (fetch via `python3 bondradar_api.py list <cat>` or `news <cat> <id>`).

---

## Mandated

### Arkéa Public Sector SCF EUR500m 8y Covered Bond (id 14630386)

```
** Arkea Public Sector SCF EUR500m 8-year CB: Mandated

"Arkéa Public Sector SCF has mandated Crédit Agricole CIB, Crédit Mutuel Arkea, Dekabank, DZ BANK, LBBW and Santander as joint bookrunners for its upcoming 8-year EUR 500m (WNG) fixed-rate Public Sector Covered Bond (Obligations Foncières). The issue is expected to be rated Aaa by Moody's. The transaction will be launched in the near future, subject to market conditions.
This new issue will be ECBC Covered Bond Premium Label / CRD 4 Compliant."

Tranche A
  currency: EUR
  volume: 500m
  structure: 8y CB
  priceEvolution: (null — no level at mandate)
  bookOrRating: JT-LEADS
  timing: this week

Flags: coveredBonds=true, regionAmericas=false, expectedPageId=IGRB18, expectedPageCount=1
```

### HKSAR working group (id 14630442) — Sovereign working-group mandate

```
** Gov of Hong Kong USD/EUR/HKD/CNH up to 5-year Grn: Mandated

"The Government of the Hong Kong Special Administrative Region [...] has appointed HSBC, Bank of China (Hong Kong), Bank of Communications, Barclays, BNP PARIBAS, Citigroup, Crédit Agricole CIB, Deutsche Bank, ICBC (Asia), J.P. Morgan, Societe Generale, Standard Chartered Bank and UBS to form a working group to explore the possibility of a USD and/or EUR and/or HKD and/or CNH, multi-series, fixed rate, up to 5-year, digitally native green/social/infrastructure bond issuance. [...]"

Tranche A
  currency: USD
  volume: TBA
  structure: 5y Grn
  priceEvolution: null
  bookOrRating: Aa3/AA+/AA-  # EM issuer rating triplet (not NR/NR/NR — HKSAR is rated)
  timing: this week

Flags: emDetails.regionAsia=true, expectedPageId=EMRH45, expectedPageCount=1
```

---

## IPTs

### Crédit Agricole HL SFH CHF100m+ 8y Green Covered (id 14630381)

```
* Credit Agricole HL SFH CHF100m+ 8-year Grn CB: IPTs SARON+45bp area

IPTs are SARON+45bp area for Credit Agricole Home Loan SFH's minimum CHF100m 8-year Green Public Covered Bonds, due 4 September 2034. Settle 4 September 2026. Issuer Credit Agricole Home Loan SFH. Direct, unconditional, unsubordinated and privileged obligations. RegS. List SIX, denoms 5k. French law. UOP The net proceeds will be used in accordance with the Credit Agricole Group Green Bond Framework dated November 2023 to finance or refinance in whole or in part new or existing Eligible Green residential real estate assets in France included or to be included in the cover pool of Credit Agricole Home Loan SFH. Expected issue ratings Aaa/AAA/AAA. Lead Managers UBS, Commerzbank. Credit Agricole CIB. Books can close at short notice.

Tranche A
  currency: CHF
  volume: 100m+
  structure: 8y Grn CB
  priceEvolution: SARON+45a
  bookOrRating: JT-LEADS
  timing: today

Note: "Lead Managers UBS, Commerzbank. Credit Agricole CIB." — period-separated
      no-books lead is house style.
Flags: coveredBonds=true, regionAmericas=false, expectedPageId=IGRB17
```

### RBI EUR bmk 10.5NC5.5 Green Tier 2 (id 14630400)

```
** RBI EUR bmk 10.5NC5.5 Grn T2: IPTs MS+165/170bp

IPTs are MS+165/170bp for Raiffeisen Bank International AG's EUR benchmark 10.5NC5.5 Green Tier 2 Notes, due 31 March 2037 (callable from 31 March 2032). Settle 27 August 2026 (T+5). Issuer Raiffeisen Bank International AG. Subordinated Notes, intended to qualify as Tier 2 capital. Green. RegS Bearer, Classical Global Note. CUC 75. List Luxembourg Stock Exchange, denoms 100k. German law (subordination provisions governed by Austrian law). UOP [...]. Issuer ratings A1/A- (M/S). Expected issue rating Baa2. Joint Lead Managers Barclays, Citi, Natixis, Raiffeisen Bank International, UBS Investment Bank, UniCredit (B&D). ISIN XS3480675597. Books open, today's business.

Tranche A
  currency: EUR
  volume: bmk
  structure: 10.5NC5.5
  priceEvolution: MS+165/170
  bookOrRating: JT-LEADS
  timing: today

Flags: coveredBonds=false, regionAmericas=false, expectedPageId=IGRB28
```

---

## Guidance

### RLB Steiermark EUR500m 5y Mortgage Covered (id 14630174)

```
** RLB Steiermark EUR500m 5-year MC: Guidance MS+27bp area

Guidance is MS+27bp area for Raiffeisen-Landesbank Steiermark AG's EUR500m (WNG) 5-year Mortgage Covered Bond, due 27 August 2031 (soft bullet). Settle 27 August 2026 (T+5). Issuer Raiffeisen-Landesbank Steiermark AG. Mortgage Covered Bond (Hypothekenpfandbrief), European Covered Bond (Premium). RegS Bearer. List Vienna Stock Exchange Regulated Market, denoms 100k+100k. Austrian law. Expected issue rating Aaa. Joint Bookrunners ABN AMRO, Erste Group, Helaba, LBBW, Raiffeisen Bank International (B&D). Co-Lead CMTA AG. ISIN AT0000A3WQC0. Books open, today's business.

Tranche A
  currency: EUR
  volume: 500m
  structure: 5y CB
  priceEvolution: MS+27a
  bookOrRating: JT-LEADS
  timing: today

Flags: coveredBonds=true, regionAmericas=false, expectedPageId=IGRB23
```

### Swisscom Debut Hybrid PNC5.5 (id 14630409)

```
** Swisscom Finance EUR500m PNC5.5 Hybrid: Guidance 4.375% area

Guidance is 4.375% area (+/-12.5bps) WPIR for Swisscom Finance's EUR500m (WNG) PNC5.5 Hybrid, perpetual (callable from 27 November 2031). Settle 27 August 2026 (T+5). Issuer Swisscom Finance B.V. Guarantor Swisscom Ltd. Direct, unsecured and subordinated obligations. RegS Bearer, TEFRA D. MWC. List Luxembourg Stock Exchange, denoms 100k+1k. Law English except status and subordination of the Securities and Coupons governed by Dutch law and status, subordination of the Guarantee and set-off governed by Swiss law. UOP general corporate purposes including to refinance existing indebtedness of the Group. Guarantor ratings A2/A-. Expected issue ratings Baa2/BBB-. Bookrunners BBVA, BNP PARIBAS, BofA Securities, Deutsche Bank (B&D), UBS Investment Bank. ISIN XS3460850616.
Book update: Books over EUR4.7bn (pre rec). Books subject at 12.00 UKT.

Tranche A
  currency: EUR
  volume: 500m
  structure: PNC5.5
  priceEvolution: 4.375%a
  bookOrRating: JT-LEADS
  timing: today

Flags: coveredBonds=false, regionAmericas=false, expectedPageId=IGRB30
```

---

## Book Update (level unchanged, new book size)

### RLB Steiermark (id 14630174 — earlier state)

```
** RLB Steiermark EUR500m 5-year CB at MS+27bp area: Book update

Guidance remains MS+27bp area for Raiffeisen-Landesbank Steiermark AG's EUR500m (WNG) 5-year Mortgage Covered Bond, due 27 August 2031 (soft bullet). [standing terms carried forward]. ISIN AT0000A3WQC0.
Book update: Books over 2bn (Incl. 280m JLMs). Today's business.

Note: Level embedded (`at MS+27bp area`) between descriptor and stage word.
      Timing "Today's business" sits at the end of the Book update line, not
      the guidance paragraph.
```

---

## Spread Set (size not yet firm)

### BNG USD bmk 2y Social (id 14630231)

```
** BNG USD benchmark 2y Soc: Spread set at SMS+20bp

Spread is set at SOFR MS+20bp for BNG Bank N.V.'s USD benchmark 2-year Social bond, due 1 September 2028. Settle 27 August 2026 (T+5). Issuer BNG Bank N.V. Senior unsecured. 144A/RegS, registered. List Luxembourg Stock Exchange, denoms 200k+2k. Law Dutch. UOP The proceeds of the bond will be utilised for lending to Dutch Social Housing Associations to finance their social expenditures as defined in BNG Bank's Sustainable Finance Framework. Issuer Rating/Expected issue rating Aaa/AAA/AAA. Bookrunners Citi, Daiwa, GSBE SE, NBC Paris. ISIN XS3481696618 (Reg S) / US05591F3G36 (144A).
Book update: Books above USD1.95bn (excl. JLM). Global books close at 08:00 NY / 13:00 LDN.

Tranche A
  currency: USD
  volume: bmk
  structure: 2y Soc
  priceEvolution: SMS+20   # no `a` — spread SET
  bookOrRating: JT-LEADS
  timing: today

Flags: coveredBonds=false, regionAmericas=true (144A/RegS US targeting)
```

---

## Final Terms (both spread + size set)

### KFW HKD4bn 5y (id 14630367)

```
** KFW HKD4bn 5-year at HIBOR MS-3bp: Final terms

Size set at HKD4bn and spread set at HIBOR MS-3bp for Kreditanstalt für Wiederaufbau (KfW)'s planned 5-year Senior Unsecured Unsubordinated Notes, due 1 September 2031. Settle 1 September 2026 T+8. Issuer KfW. Guarantor Federal Republic of Germany. Reg S, Bearer, drawdown off the Issuer's EMTN Programme. Fixed, annual coupon, Act/365 (Fixed). List Luxembourg Stock Exchange. Denoms 1,000,000. German law. Clearing CMU with links to Euroclear/Clearstream. Issuer/Expected issue ratings Aaa/AAA/AAA, Moody's/S&P/Scope. Lead Managers BofA Securities (B&D) and HSBC.
Book update: Books over HKD6.4bn (Incl. HKD3.85bn JLM). Global books subject 15:00 HKT. Today's business during Asia hours.

Tranche A
  currency: HKD
  volume: 4bn
  structure: 5y
  priceEvolution: HIBOR MS-3
  bookOrRating: BOA/HSBC   # ≤3 leads → ticker shorthand
  timing: launched

Note: Stage word is `Final terms` (lowercase `t`) — house style.
      Body opens "Size set at X and spread set at Y" — both set → Final terms.
Flags: coveredBonds=false, regionAmericas=false, expectedPageId=IGRB15
```

### SEB EUR1.5bn dual-tranche Covered (id 14630414)

```
** SEB EUR1.5bn dual-tranche CB: Final terms

Tranche A: EUR1bn 3-year covered bond, due 27 August 2029. Spread set at MS+8bp. ISIN XS3482637496.
Tranche B: EUR500m 3-year covered FRN, due 27 August 2029. Spread set at 3mE+18bp. ISIN XS3484200541.
Common terms: Settle 27 August 2026 (T+5). Issuer Skandinaviska Enskilda Banken AB (publ). Swedish Covered Bond, soft bullet, extended maturity 27 August 2030. RegS, NGN, Bearer form, TEFRA D. List Euronext Dublin, denoms 100kx1k. Law English and Swedish. Issuer ratings Aa3/AA-/AA+. Expected issue rating Aaa. Joint Bookrunners Barclays, Commerzbank, Deutsche Bank, Natixis, Nomura (B&D), SEB.
Book update: Combined books above EUR4.3bn pre-rec (incl EUR850m JLMs). EUR2.8bn (incl EUR450m JLMs) and EUR1.5bn (incl EUR400m JLMs), respectively. Books subject 12:30 CEST / 11:30 UKT.

Tranche A: EUR / 1bn / 3y CB / MS+8 / JT-LEADS / launched
Tranche B: EUR / 500m / 3y CB FRN / E+18 / JT-LEADS / launched

Note: Aggregate size (EUR1.5bn) in headline, per-tranche split in body book line.
      No embedded level in dual-tranche headline.
Flags: coveredBonds=true, expectedPageCount=2 (one page per tranche)
```

---

## Allocations Out

### RLB Steiermark (id 14630174 — Allocations state)

```
** RLB Steiermark EUR500m 5-year CB at MS+19bp: Allocations

Spread set at MS+19bp for Raiffeisen-Landesbank Steiermark AG's EUR500m 5-year Mortgage Covered Bond, due 27 August 2031 (soft bullet). [standing terms]. ISIN AT0000A3WQC0.
Book update: Final books at reoffer over 2.1bn (Incl. 305m JLMs). Hedge deadline 12:55 UK/ 13:55 CET.  Allocations out, pricing later on today.
```

### Thales EUR1bn dual-tranche (id 14630427)

```
** Thales EUR1bn dual-tranche: Allocations

Tranche A: EUR500m. 4-year, due 27 August 2030. Spread set at MS+45bp. WPIR. 2-month par call. ISIN FR001401AM07.
Tranche B: EUR500m. 8-year, due 27 August 2034. Spread set at MS+65bp. WPIR. 3-month par call. ISIN FR001401AM15.
Common terms: [carried forward from FT]
Book update: Final books over EUR1.45bn and EUR1.1bn respectively. Allocations out, hedges by 15:55 UKT. Pricing to follow.
```

---

## Launched (single-tranche when both size + yield set)

### Zibo Caijin CNY580m 3y (id 14630357)

```
** Zibo Caijin CNY580m 3-year: Launched at 2.70%

Launched: Size is set at CNY580m and yield is set at 2.70% for Zibo Caijin Holding Group Co., Ltd. CNY580m 3-year Fixed Rate Senior Unsecured Bonds. Settle 27 August 2026 (T+5). Issuer Zibo Caijin Holding Group Co., Ltd. Reg S only, Category 1, Registered form. COC put 101%. List HKSE. Denoms 1mx10k. English law. UOP: For refinancing of its existing indebtedness in accordance with the NDRC Certificate. Issuer/Expected issue Unrated. JGCs, JBRs and JLMs Guotai Junan International (B&D), China Securities International, CITIC Securities and SunRiver International Securities Group Limited. JBRs and JLMs [10 banks]. Allocation and pricing shortly.

Note: Body opens `Launched: Size is set...` → headline `Launched at [level]`.
      Only single-tranche uses this form. Dual/multi go `dual-tranche: Final terms`.
```

---

## Priced

### RLB Steiermark Priced (id 14630174)

```
** RLB Steiermark EUR500m 5-year CB: Priced at MS+19bp

Priced: EUR500m, coupon 3.25%, due 27 August 2031. Reoffer 99.646, spread MS+19bp / DBR 0% 15 August 2031+35.3bp. Yield 3.328%. Settle 27 August 2026 (T+5). Issuer Raiffeisen-Landesbank Steiermark AG. Mortgage Covered Bond (Hypothekenpfandbrief), European Covered Bond (Premium). RegS Bearer. List Vienna Stock Exchange Regulated Market, denoms 100k+100k. Austrian law. Expected issue rating Aaa. Joint Bookrunners ABN AMRO, Erste Group, Helaba, LBBW, Raiffeisen Bank International (B&D). Co-Lead CMTA AG. ISIN AT0000A3WQC0. Final books at reoffer over 2.1bn (Incl. 305m JLMs).

Priced-deal form (id 14630506):
  currency=EUR, nominal=500, cpn=3.25, fpr=99.646, spread=MS+19, yield=3.328%, fxRate=1.16945
  isin=AT0000A3WQC0, figi=BBG024GT9B86, bloombergCode=DO7452497
  tier=null (senior covered), covered=true, dealRegsOnly=true
  moodys=AAA, snp=NR, fitch=NR (Aaa Moody's-only expected)
  additionalInfo="MC" (Mortgage Covered)
  leagueTable=true

Note: Benchmark date spelled out `15 August 2031` per rule.
      Book line at Priced: no `Book update:` prefix; `Final books at reoffer over`
      is Case A/B variant carried from Allocations.
```

### Swisscom Priced (fixed-yield hybrid) (id 14630409)

```
** Swisscom Finance EUR500m PNC5.5 Hybrid: Priced at 4.25%

Priced: EUR500m, coupon 4.125%, perpetual (callable from 27 November 2031). Reoffer 99.419, spread MS+111.4bp / DBR 0% 15 February 2032+126.3bp. Yield 4.250%. Settle 27 August 2026 (T+5). Issuer Swisscom Finance B.V. Guarantor Swisscom Ltd. Direct, unsecured and subordinated obligations. RegS Bearer, TEFRA D. MWC. List Luxembourg Stock Exchange, denoms 100k+1k. Law English except [...] Dutch law [...] Swiss law. UOP general corporate purposes including to refinance existing indebtedness of the Group. Guarantor ratings A2/A-. Expected issue ratings Baa2/BBB-. Bookrunners BBVA, BNP PARIBAS, BofA Securities, Deutsche Bank (B&D), UBS Investment Bank. ISIN XS3460850616.

Priced-deal form (id 14630537):
  cpn=4.125, fpr=99.419, spread=MS+111.4, yield=4.250%, fxRate=1.1679
  isin=XS3460850616, figi=BBG024L609R3, bloombergCode=DO7838844
  tier=null, subordinated=true, coc=true (CoC step-up), mwc=true (MWC Bund+20)
  covered=false, green=false, dealRegsOnly=true
  moodys=BAA2, snp=BBB_MINUS, fitch=NR

Note: For fixed-yield hybrids, body opener is `Yield set at X%` at pre-Priced
      stages (not "Spread set"). At Priced the "spread MS+111.4bp" is a computed
      spread to benchmark, distinct from a benchmark-referenced pricing spread.
```

### Ocean Yield PerpNC5 Hybrid FRN (Priced) (id 14620730) — HY

```
** Ocean Yield USD100m PNC5 Hybrid: Priced at SOFR+350bp

Priced: USD100m, coupon SOFR+350bp, perpetual (callable from 3 September 2031). Reoffer 100.00, spread SOFR+350bp. Settle 3 September 2026. Issuer Ocean Yield AS. Subordinated Hybrid notes. COC 101. RegS. denoms 200k x 200k. UOP Refinancing of OCY10 and for general corporate purposes. Bookrunners Arctic, Danske, DNB Carnegie (B&D). List Oslo Stock Exchange. Norwegian law. ISIN NO0013759829.

Priced-deal form:
  currency=USD, nominal=100, cpn=SOFR+350, perpetual=true, subordinated=true
  coc=true (CoC 101), fxRate=1.0
Flags: HY dual-feed (highYield=true, feedIgrd=true), hyExpectedPageId=HYRE7,
       regionAmericas=false (Norwegian issuer, Reg S only, non-US targeting)
```

### KFW HKD4bn 5y Priced (id 14630367)

```
** KFW HKD4bn 5-year: Priced at HIBOR MS-3bp

Priced: HKD4bn, coupon 3.617%, due 1 September 2031. Reoffer 100.00, spread HIBOR MS-3bp. Yield 3.617%. Settle 1 September 2026 T+8. Issuer KfW. Guarantor Federal Republic of Germany. Reg S, Bearer, drawdown off the Issuer's EMTN Programme. Fixed, annual coupon, Act/365 (Fixed). List Luxembourg Stock Exchange. Denoms 1,000,000. German law. Clearing CMU with links to Euroclear/Clearstream. Issuer/Expected issue ratings Aaa/AAA/AAA, Moody's/S&P/Scope. Lead Managers BofA Securities (B&D) and HSBC. ISIN HK0001326518. Books last heard over HKD6.4bn (Incl. HKD3.85bn JLM).

Note: 3-agency rating with Scope in the Fitch-slot — body labels `Moody's/S&P/Scope`
      while the priced-deal form marks Fitch=NR (schema limitation).
      Book line `Books last heard over` = Case B (source silent at Priced, earlier
      had book updates without "closed"/"final" language). Also mirrored in
      priced-deal `additionalInfo`.
```

---

## Book Stats (post-pricing distribution update)

### Finland EUR4bn 7y (id 14620791)

```
** Finland EUR4bn 7-year at MS+15bp: Book stats

Priced: EUR4bn, coupon 3.30%, due 15 April 2033. Reoffer 99.953, spread MS+15bp / DBR 2.30% 15 February 2033+25.0bp. Yield 3.310%. [...] Bookrunners BNP Paribas, BofA Securities, Danske Bank, Deutsche Bank, J.P. Morgan (DM/B&D). ISIN FI4000609516. Final books over EUR11.25bn (incl. EUR700m JLM interest).

Priced-deal form.statsCategories (each sums to 100%):
  GEOGRAPHY:
    Middle East + Asia:                            23%
    France + Netherlands + Belgium + Luxembourg:   20%
    Nordics:                                       20%
    UK:                                            20%
    Austria + Germany + Switzerland:               10%
    Italy + Spain + Portugal:                       4%
    Other Eurozone:                                 2%
    Americas:                                       1%
  INVESTOR:
    Central Banks + Official Institutions:         43%
    Banks + Bank Treasuries:                       24%
    Insurers + Pension Funds:                      14%
    Asset Managers:                                12%
    Hedge Funds:                                    5%
    Others:                                         2%

Note: Book stats update ONLY changes the headline (Priced → Book stats,
      level embedded) and populates statsCategories. Body carries the
      original Priced content unchanged.
```

### SpareBank 1 Boligkreditt EUR1bn 7y EuGB Covered (id 14630099)

```
** SpareBank 1 Boligkreditt EUR1bn 7y EuGB CB at MS+23bp: Book stats

[Priced body unchanged, statsCategories added:]

  GEOGRAPHY: DACH 49, Benelux 20, UK+Ireland 9, Southern Europe 8, Nordics 6, France 6, Others 2
  INVESTOR:  Banks 59, Asset Managers 16, Insurers+Pension 10, Central Banks+OI 10, Hedge Funds 4, Others 1

Priced-deal additionalInfo: "MC, EuGB"  # Mortgage Covered + EU Green Bond
covered=true, green=true, dealRegsOnly=true
```

---

## IMA (Investor Meeting Announcement — EM)

### KEB Hana Bank plans investor calls (id 14630423)

```
** KEB Hana Bank plans investor calls

"KEB Hana Bank, rated Aa3 (Stable) by Moody's, A+ (Stable) by S&P and A (Stable) by Fitch, has mandated BNP PARIBAS, Citigroup, MUFG, Standard Chartered Bank and Wells Fargo Securities to arrange a series of fixed income investor update meetings and conference calls in Asia, commencing on September 7, 2026.
KEB Hana Bank Representatives:
- Mr. Beomjun Cho, Head of Group, Financial Markets Group
[...]
Singapore Logistics: Wells Fargo Securities · Shanghai Logistics: MUFG · Beijing Logistics: BNP Paribas, MUFG
Meeting slots Sep 7 (Singapore group), Sep 8 (Singapore group), Sep 9–10 (Shanghai 1x1), Sep 11 (Beijing 1x1)."

type: UPDATE, typeCustom: "Investor calls"
Flags: emDetails.regionAsia=true, notifyMobile=false (IMA, not live deal)
       expectedPageId=null (acceptable for IMA), expectedPageCount=1
```

---

## Multi-tranche (3+ tranches)

### People's Republic of China CNH6bn 2y/3y/5y/10y (id 14630085) — 4 tranches

```
** People's Republic of China CNH6bn multi-tranche: Final terms

Tranche A: CNH3bn 2-year Senior Unsecured Fixed Rate Bonds. Yield set at 1.30% (the number).
Tranche B: CNH1bn 3-year Senior Unsecured Fixed Rate Bonds. Yield set at 1.33% (the number).
Tranche C: CNH1bn 5-year Senior Unsecured Fixed Rate Bonds. Yield set at 1.46% (the number).
Tranche D: CNH1bn 10-year Senior Unsecured Fixed Rate Bonds. Yield set at 1.76% (the number).
Common terms: Issuer The Ministry of Finance of the People's Republic of China. Reg S (Category 1), Bearer Form. Settle 27 August 2026 T+5. UOP: The net proceeds will be used by the Ministry of Finance for general governmental purposes. List Chongwa (Macao) Financial Asset Exchange Co., Ltd. Denoms 1,000,000 / 10,000. Law Macau law. Clearing Macao Central Securities Depository and Clearing Limited with linkage to Central Moneymarkets Unit Service. JGCs, JLMs and JBRs Bank of China Macau Branch, Bank of Communications Macau Branch and ICBC (Macau). JLMs and JBRs [13 banks]. Fiscal Agent Bank of Communications Macau Branch.
Book update: Combined books over CNH 69.96bn (Incl. CNH 33.5bn JLM + CNH 2.76bn PROP). Allocations and pricing shortly.

Note: 4 tranches → `multi-tranche` (never dual-tranche).
      expectedPageCount = number of tranches (4 here).
```

### Vylor USD dual-tranche 5y+10y IPTs (id 14630517) — spin-off deal

```
** Vylor USD benchmark dual-tranche: IPTs

Tranche A: USD benchmark 5-year fixed, due 15 August 2031. IPTs are T+110bp area. 1-month par call.
Tranche B: USD benchmark 10-year fixed, due 15 August 2036. IPTs are T+135bp area. 3-month par call.
Common terms: Settle 31 August 2026 (T+7). Issuer Vylor Inc. Guarantor EIDP, Inc. until consummation of the Separation. Senior unsecured notes. 144A/RegS with reg rights. COC 101. MWC. Denoms 2k x 1k. UOP To make a cash distribution to EIDP [...]. Exp. Ratings Baa1/BBB+/BBB+. Bookrunners BofA, JPM, MS. Today's business.

Note: Guarantor clause with limitation "until consummation of the Separation"
      preserved. Special Mandatory Redemption clause from source is NOT
      included (house style omits SMR).
Flags: regionAmericas=true (US issuer 144A), expectedPageCount=2
```

---

## Reference

See `CHAT_GENERATOR.md` for the full generation workflow and `checklist.md` for stage-by-stage required items and BR house-style ordering rules.
