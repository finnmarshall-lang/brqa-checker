---
name: feedback-bondradar-additional-info-field
description: "BR priced-deal `additionalInfo` field vocabulary — populate with EuGB / BC / Sukuk / ESN / Kangaroo / Samurai / 3-month par call / HY UOP shorthand / sale of retained bond / Books last heard over [amount], as applicable."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-03T07:51:53.397Z
---

The `additionalInfo` free-text field on the BR priced-deal form is a real signal, not a scratchpad. Populate it whenever any of the below applies, and flag if it's empty on a deal that has one of these attributes.

## Tags / phrases the field should hold

- **`EuGB`** — European Green Bond (per EU Green Bond Regulation). Set alongside `green: true`.
- **`MC`** — Mortgage Covered bond. Set alongside `covered: true` on any covered bond backed by mortgage collateral (residential or commercial).
- **`PC`** — Public Covered bond. Set alongside `covered: true` on any covered bond backed by public-sector collateral (sovereign/agency/local-government loans, Öffentliche Pfandbriefe, etc.).
- **`BC`** — Blockchain / digital bond (issued on-chain or via distributed-ledger tech).
- **`Sukuk`** — Islamic-finance structured bond (EM deals).
- **`ESN`** — European Secured Note.
- **`Kangaroo`** — Kangaroo bond (AUD, issued in Australia by a foreign issuer). Example: Alphabet AUD5.5bn Kangaroo priced-deals all had `additionalInfo: "Kangaroo"`.
- **`Samurai`** — Samurai bond (JPY-denominated, issued in Japan by a foreign issuer).
- **Par call detail** — atypical par-call windows, e.g. `"3-month par call"`, `"6-month par call"`. Standard 1-month par call often left off.
- **HY UOP shorthand — REQUIRED on every HY priced deal.** Use of proceeds in shorthand: `"UOP: GCP"` (general corporate purposes) / `"UOP: Aqui"` (acquisition) / `"UOP: Recap"` (recapitalisation) / `"UOP: Refi"` (refinancing existing debt). Multiple can be combined with `;`. Flag EVERY HY (`highYield: true` on the deal-level flags) priced deal whose `additionalInfo` doesn't carry a `UOP:` shorthand. Finn on Boels Topholding EUR400m 6NC2 Priced (id 14640452, priced-deal 14650337): tick walked additionalInfo=null on a HY deal and didn't flag it. Finn: "important rule missed, UOP im additional info for HY deals". The UOP fact appears in the body prose already; the priced-deal form's `additionalInfo` needs the shorthand mirror.
- **`sale of retained bond`** — when the deal is selling previously-retained inventory (NOT a fresh tap increasing the outstanding). Explicit call-out here so the deal isn't confused with a tap.
- **`Books last heard over [amount]`** — when the desk had book updates during the deal but never received a final book figure at pricing. Populate `additionalInfo` with the last-heard book figure (and mirror it in the pricing message body). Distinguishes from `Final books over` which requires the source to give a final figure at Priced.
  - **Mutually exclusive with `finalBooks` populated on the priced-deal form.** If `finalBooks` has a number (from Book Stats release, "Final books over" language, "Books closed" at any stage, or a book-size change between Final Terms and Allocations), leave the `Books last heard over` text OUT of `additionalInfo`. If the deal never got any final/closed/stats disclosure and `finalBooks` is null, `Books last heard over X` goes IN `additionalInfo`. Never both. Finn: "why would we need to have the books last heard when we got th final books it makes no sense".
- Legit non-taxonomy values seen: `"FA backed"` (MassMutual funding-agreement-backed), `"EMTN drawdown"`.

## How to combine

Multiple tags coexist with `;` separators, e.g. `"Kangaroo; 3-month par call"`.

## How to apply during QA

For each priced-deal record, inspect the deal for the attributes above:

1. If the outgoing message body / source term sheet says `Green` + labelled European Green Bond → `additionalInfo` should include `EuGB` AND `green: true`.
2. If the source mentions a digital/blockchain issuance → `BC`.
3. If EM Sukuk → `Sukuk`.
4. If the deal is a Kangaroo (AUD, foreign issuer in Australia) → `Kangaroo`. Same for Samurai (JPY).
5. If the par call is anything other than 1-month → note the exact window.
6. HY deal → include `UOP:` shorthand.
7. Sale of retained bonds → explicit `sale of retained bond`.
8. Book stats: if the source only gave last-heard books pre-pricing and no final at Priced → `Books last heard over EURXbn (incl EURYm JLM).` here + in message body.

Flag when: (a) the deal clearly has one of the attributes but `additionalInfo` is empty or doesn't mention it; (b) the tag is present but the corresponding boolean flag (`green`, `subordinated`, etc.) is inconsistent; (c) the deal is described as a tap in the body but `additionalInfo` says "sale of retained bond" — those are different, one is wrong.

See also [[br-qa-checker-project]].
