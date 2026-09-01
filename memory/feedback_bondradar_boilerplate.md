---
name: feedback-bondradar-boilerplate
description: Never flag Fxd-to-Frn coupon structure or other regulatory/prospectus boilerplate as missing from Bond Radar messages — that stuff intentionally does not belong in the BR message.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-01T15:19:06.475Z
---

Bond Radar messages intentionally OMIT a bunch of things that appear in the term sheet. Do NOT flag any of these as "missing":

- **Fixed-to-Floating (Fxd-to-FRN) coupon structure** on SNP / callable MREL notes. The switch from fixed coupon to 3mEURIBOR+X after the first call is intentionally left out. `coupon 3.875%` with `callable from [date]` is a complete BR message; the fxd-to-frn nature is understood from context and doesn't belong in the message body.
- **CUSIP**. Bond Radar uses ISIN as the primary identifier and CUSIP is not required — do not flag as missing even for SEC-registered US corp deals that only carry a CUSIP in the term sheet. (Finn: "cusip doesn't matter stop pointing it out.") If the ISIN is genuinely missing at Priced / Final Terms, flag the ISIN, never the CUSIP.
- Interest payment schedule details (payment dates, first-coupon short/long, day-count basis)
- Business-day conventions
- Statutory loss-absorption / MREL disqualification / waiver-of-set-off verbiage
- MiFID II / UK MiFIR product-governance / PRIIPs KID language
- Events-of-default / negative-pledge boilerplate
- **`Sale into Canada`** language — "Sale into Canada Yes" or "Sale into Canada Yes, via exemption" should NOT appear in the BR message. If present, flag as something to remove. If absent from BR but present in the term sheet, do NOT flag as missing — it's intentional omission. (Finn: "this is unneeded in message".)
- **Clearing** language ("Clearing: Euroclear/Clearstream", "CMU with linkage to…", "Fedwire, Euroclear, Clearstream", etc.) — NOT required in BR messages. Do not flag as missing at any stage, and do not flag Common terms of multi-tranche messages for lacking a Clearing line. (Finn: "clearing doesn't need to be in common terms".)
- **Tax-changes call / tax-event redemption** ("Tax Event", "Withholding Tax Event", "Gross-Up Event", "Tax Deductibility Event", "Additional Amounts Event", "Change of Tax Law call") — NOT required in the BR message body AND NOT required on the priced-deal form's `additionalInfo`. If present in BR, flag as something to remove; if absent, do NOT flag as missing. Regulatory-event calls are standard in every prospectus and don't belong in either the outgoing message or the admin panel. (Finn: "Tax changes call this should not be in message or additional info".)

**Why:** In the Credit Agricole 6.5NC5.5 SNP Priced QA (BR id 14620276), I flagged the message for not capturing the Fxd-to-Frn coupon structure. Finn corrected: it's irrelevant to mention, it shouldn't be in the message. See [[br-qa-checker-project]].

**How to apply:** When walking `checklist.md` for a stage, ignore any item that would surface term-sheet regulatory/prospectus boilerplate. Only flag things that belong in the BR message per house style. When in doubt about whether something belongs, prefer NOT flagging over false-positive noise.
