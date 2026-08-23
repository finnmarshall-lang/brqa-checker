---
name: feedback-bondradar-book-or-rating-field
description: "BR admin `bookOrRating` field is market-dependent — labelled `Books` on IG (value `JT-LEADS` when >3 bookrunners), labelled `Ratings` on EM (value like `Aa1/AA+/AA` M/S/F). Never flag `JT-LEADS` on an IG deal."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-19T13:21:16.231Z
---

The `bookOrRating` field on `tranches[i].details[]` in the BR admin API is confusingly named — it's dual-purpose, but the switch is **market-dependent, not stage-dependent**. Check `hgDetails` vs `emDetails` on the deal object to decide which:

- **IG / HG deals (`hgDetails` populated)**: the admin UI labels this field **"Books"**. Value depends on bookrunner count:
  - **> 3 bookrunners → `JT-LEADS`** (standard shorthand for "books are collectively with the joint leads; the desk isn't itemising per-bank IOIs").
  - **≤ 3 bookrunners → any of**: the bank-ticker summary slash-separated (e.g. `WF/BOA` for 2-book, `BOFA/TD/WFC` for 3-book), OR the expected issue ratings triple (e.g. `A2/A-/A` for CBA T2 with 2 books). Both are valid — the desk picks depending on habit. **Don't flag either form.**
  - Do NOT flag `JT-LEADS` OR bank-ticker summaries OR ratings triples on IG deals — all three are legitimate values for the field.
- **EM deals (`emDetails` populated)**: the admin UI labels this field **"Ratings"**. Value is the expected issue ratings in slash-separated `Moody's/S&P/Fitch` order (empty slot allowed with double slash, e.g. `Aaa//AAA` = Moody's/no S&P/Fitch; `A1/A-/A` = all three; `Aaa//` = Moody's only).

**Why:** In the Jyske Realkredit Final Terms QA (id 14630129) and the Republic of Finland Spread Set QA (id 14620791), I flagged `bookOrRating: JT-LEADS` as stale, thinking the field rotated from `JT-LEADS` (pre-guidance) to ratings (guidance onwards) universally. Finn corrected: "This is correct it's only EM deals that mention the ratings as its labeled Ratings while this is Labelled books, as this has more than 3 bookrunners we label it as JT-LEADS." Both deals were IG (`hgDetails` populated) so `JT-LEADS` was correct.

**How to apply:** When walking `tranches[i].details[-1].bookOrRating`:

1. Check `deal.hgDetails` vs `deal.emDetails` on the parent deal to determine the market.
2. **IG deals**: `bookOrRating` is a book descriptor. `JT-LEADS` on a tranche with >3 bookrunners is normal — never flag it as stale. Only surface real anomalies (e.g. `JT-LEADS` on a tranche where `banks.active` count is 1 or 2, or a value that doesn't fit any known book-status marker).
3. **EM deals**: `bookOrRating` is expected issue ratings. Verify M/S/F order and that agencies the source disclosed are present. Empty double-slash slots are fine (missing rating agencies).

See also [[br-qa-checker-project]].
