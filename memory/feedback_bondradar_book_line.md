---
# Rule refined 2026-08-20: `Final books` / `Books closed` qualifier only required when the
# SOURCE at the current stage uses `Final` / `closed` language. If BR carries a book size
# forward from an earlier stage and the current source doesn't mention books, keep
# `Book update: Books above/over Xbn` as-is — don't force `Final books`.
# Applies to Allocations Out too, not just Priced.
name: feedback-bondradar-book-line
description: "Bond Radar book-line house style — never prefix with `Book update:`, and choose between `Final books over`, `Books closed over`, or `Books last heard over` based on what the source stated."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-20T14:06:13.122Z
---

Bond Radar messages have a stage-based rule for the book-line prefix:

**Pre-pricing (any stage up to and including Launched / Final Terms / Spread Set — anything before Priced):** the `Book update:` or `Books update:` prefix IS fine. Do not flag the prefix at these stages. Do not flag `Books` vs `IOIs` word choice either — Finn's exact phrasing was "Books update: is fine in the update for book updates until pricing", i.e. the prefix is universally acceptable pre-pricing regardless of the word after it.

**Prefix rule is stage-based, wording rule is source-based — treat them separately:**

**Prefix (`Book update:` / `Books update:`):**
- **Pre-pricing including Allocations Out** — prefix is FINE. IPTs, Guidance, Book Update, Spread Set, Final Terms, Launched, Allocations Out — all can carry the `Book update:` prefix. Do NOT flag prefix at any pre-Priced stage.
- **At Priced only** — no `Book update:` / `Books update:` prefix. This is the ONLY stage where the prefix should be dropped.

**Wording (`Books over` / `Final books over` / `Books closed over` / `Books last heard over`):** is a combination of stage + source signal.

**Stage-driven rule (applies BEFORE source wording):**
- **Pre-Allocations stages (IPTs / Guidance / Book Update / Spread Set / Final Terms / Launched)** — the generic `Books over` is fine when source just says `Books >`. Upgrade to `Final books over` / `Books closed over` only when source explicitly uses those words.
- **Allocations Out** — books are implicitly final at this stage even if source doesn't say "final" or "closed" outright. Use `Final books over [amount]` or `Books closed over [amount]` — NEVER the plain `Books over` at Allocs. Default = `Final books over [amount]` (with `(incl. Ym JLM interest)` when the source discloses one); flip to `Books closed over` when the source explicitly says "closed" (or "closed at reoffer" / equivalent). Finn: "if there is a book update in the allocations and it doesn't say books closed or final books you should say that it's final books or books closed".
- **Priced** — see the Priced section below.

**Source-driven overlay (applies WITHIN the stage rule):**
- Source says "books closed" (or "orderbook closed" / "global books closed") → `Books closed over` (wins over `Final books over` even with JLM breakdown at any stage).
- Source says "final books" + JLM breakdown → `Final books over (incl. X JLM interest)`. If the Priced-stage term sheet is silent on books (as most are — the book figure was last given at Final Terms / Spread Set), the correct wording is `Books last heard over [amount].` — even if a JLM interest breakdown was disclosed at Final Terms in an earlier update. Order of precedence:
1. **If the Priced-stage source says "books closed" (or "global books closed" / "orderbook closed" / equivalent) → `Books closed over [amount].`** This wins over `Final books over` even when a JLM breakdown is also disclosed at Priced.
2. **Else, if the deal's history includes a source stating "final books" or "books closed" AND a JLM interest breakdown was disclosed somewhere in the deal's timeline (Launched / Allocations Out / any earlier stage) → `Final books over [amount] (incl. [Y] JLM interest).`** The JLM figure needs to appear in the outgoing BR message body. It does NOT need to be disclosed by the source AT the Priced-stage update specifically — an earlier stage counts. Only fall back to `Books last heard over` (case B) when the deal NEVER received "closed" or "final books" language from source at any stage. Finn on DBJ: correction applied because no source ever said closed/final. Finn on ADB: `Final books over` was fine because the Launched source said `Global books closed` with JLM breakdown, even though the Priced-stage source itself was silent. The "must be at Priced" wording in a prior version of this rule was too strict — retracted.
3. **Else (Priced-stage source silent on books / JLM breakdown)**: the body treatment depends on whether the deal *ever* received a Final Books / Books Closed figure during its life:
   - **A. Deal received a Final Books / Books Closed figure at any earlier stage** (typically Allocations Out, e.g. LHV): body book line is OPTIONAL. `finalBooks` on the priced-deal form carries the internal figure; body can be silent. Do NOT force a fallback line in.
   - **B. Deal had book updates during the deal but NEVER received a Final Books / Books Closed figure** (e.g. Chiba Bank — books were `>USD2bn / >USD2.5bn / >USD3.1bn` through the stages, but no source ever said "Final books" or "Books closed"): **body MUST carry `Books last heard over [amount].`** using the last-known figure (`USD3.1bn` for Chiba), AND the priced-deal form's `additionalInfo` field should carry the same `Books last heard over [amount].` text. This is the "no final books, but we had figures" case Finn's rule was written for.
   - **C. Deal never had any book figure at any stage** (rare — mandate went straight to priced with no book updates): body can omit the book line entirely, and `additionalInfo` doesn't need the figure either.
   
   The distinguishing question is: did the deal *ever* get a Final Books / Books Closed figure? If yes → case A, body optional. If no but there were updates → case B, `Books last heard over` required in both places. Finn: "should of noticed books last heard missing from message and additional info" (on Chiba, id 14620638).

**Example correction (World Bank Final Terms, id 14620425):** BR body ended with `Book update: Final books over USD11.25bn (incl. USD450m JLM). Global books closed.` I marked clean because the JLM breakdown was disclosed. Finn corrected: because the source said `Global books closed`, the wording should have been `Books closed over USD11.25bn (incl. USD450m JLM).` The "books closed" language beats the JLM-breakdown trigger.

**Example correction (DBJ Priced, id 14620338):** BR body ended with `Final books over USD2.05bn (incl. USD275m JLM interest).` I marked clean because a JLM breakdown was disclosed (in an earlier update). Finn corrected: "these actually look like books last heard as books were last given at FT and no mention of them being closed or final books". The rule: the JLM breakdown must be disclosed by the source AT the Priced stage — a JLM figure that came out at Final Terms and was carried into a later Priced BR message does NOT justify `Final books over`. Correct wording here was `Books last heard over USD2.05bn.`

**Example (Germany Aug 2056 tap Priced, id 14620410):** BR body ends with `Final books over EUR38bn (Incl. EUR3.35bn JLM interest).` — this is correct ONLY if the Priced-stage source itself both said "final books" and disclosed the JLM figure. If the JLM figure had been announced at Final Terms and the Priced source was silent on books, the correct wording would have been `Books last heard over EUR38bn.` instead.

`Books above` and `Books over` are equivalent.

**The word `over` (or `above`) must always be spelled out.** A trailing `+` on the amount is NOT a substitute. Correct: `Final books over EUR900m (incl. EUR50m JLM).`. Wrong: `Final books EUR900m+ (incl EUR50m JLM).`. Applies to every variant of the book line (`Books over`, `Final books over`, `Books closed over`, `Books last heard over`). Finn corrected on SpareBank 1 Sor-Norge Allocations (id 14620697) — I had let `EUR900m+` pass as equivalent to `over` and marked clean; that was wrong.

**Why:** Originally I over-generalized from the NAB Priced correction ("no `Book update:` prefix") to all stages. Finn corrected twice: first on the World Bank Guidance case (`Book update: IOIs over USD9bn` is correct), then more broadly — "Books update: is fine in the update for book updates until pricing". The rule is stage-based, not phrase-based. See NAB Priced (id 14620271) for the no-prefix example and World Bank (id 14620425) + DBJ (id 14620338) for the prefix-is-fine pre-pricing examples.

**How to apply:** When a BR message contains a book figure:
1. Determine the deal stage from the BR body.
2. Pre-pricing → prefix is fine. Don't flag prefix or the word after it. Only surface real bugs (wrong figure, missing JLM breakdown, wrong sign, etc.).
3. At Priced → no prefix. Look at what the source term sheet AT THE PRICED STAGE says about books:
   - Source says "books closed" → `Books closed over`.
   - Source says "final books" AND discloses JLM breakdown at Priced → `Final books over (incl. X JLM interest)`.
   - Source silent, or book figure carried from earlier stage → **default `Books last heard over`** (this is the common case; most Priced term sheets don't repeat book info).
See also [[br-qa-checker-project]].
