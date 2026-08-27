---
name: bondradar-casing-and-synonyms
description: Stage words and book-line phrasing are case-insensitive and several pairs are house-style synonyms. Do NOT flag cosmetic capitalisation differences or interchangeable wording as defects.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-27T11:49:05.237Z
---

BR house style is looser on casing and phrasing than the tick has been treating it. Do not flag these:

## Stage-word casing is flexible

Any stage word can appear title-cased or lowercase — both are correct:

- `Allocations` ↔ `allocations`
- `Final Terms` ↔ `final terms`
- `Book Update` ↔ `book update` (also `Books update` — see the book-line memory)
- `Guidance` ↔ `guidance`
- `Spread set` ↔ `Spread Set`
- `Priced` ↔ `priced`
- `Launched` ↔ `launched`

Do NOT rewrite `Final Terms` to `final terms` (or vice versa) on grounds that "house style is lowercase". Do NOT rewrite `Allocations` to `allocations`. If the substance is right, casing stands.

## Interchangeable pairs

Treat these as the same thing — never flag one as needing to be the other:

- **`Final books over` ↔ `Books closed over`** — both are valid house-style wording for a finalised book (already codified in `feedback_bondradar_book_line.md`; reiterated here as a casing/synonym rule).
- **`CET` ↔ `CEST`** — timezone label carried from source, never auto-corrected by the calendar. Already codified in `feedback_bondradar_cet_cest_by_source.md`; reiterated here because it's part of the same general "don't nit-flag cosmetic differences" theme.
- **`Books above` ↔ `Books over`** — equivalent (already in the book-line memory).
- **`Books update:` ↔ `Book update:`** — equivalent prefix (already in the book-line memory).

## Only flag substantive differences

The rule underneath all of this: flag on **meaning changes**, not **cosmetic changes**. A wrong number, wrong ISIN, wrong tranche assignment, wrong bookrunner list, wrong stage of the deal — flag. A different capital letter, a synonym, a source-preserved timezone label — do not flag.

**Why:** Finn's consolidated feedback batch: "Bot tells us Allocations is incorrect should be allocations (needs recognised as same thing) / Bot tells us Final books should be books closed (need recognised as same thing) / Final Terms and final terms- same thing- says the capital T is wrong- same for Book Update (update) / CET and CEST same thing (basically)."

**How to apply:** When walking the headline stage word, the body opener, the book line, or any timezone label, compare on substance not surface. Normalise for case before comparison. When two phrasings are on the interchangeable list above, treat them as equal — do not include either in the finding.

Related: [[bondradar-book-line]] (source-driven book-line rules), [[bondradar-cet-cest-by-source]] (timezone verbatim), [[bondradar-final-terms-casing]] (retired: this rule was the earlier "Final terms lowercase t" one — superseded, casing is flexible either way).
