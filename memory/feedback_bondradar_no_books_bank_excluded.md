---
name: bondradar-no-books-bank-excluded
description: "A bank in the source's JLM list annotated `(no books)` is neither active nor passive — it drops OFF entirely from the BR body's bookrunner list and from both `banks.active[]` and `banks.passive[]` on the tranche form."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-03T07:44:18.625Z
---

When a source's Joint Lead Managers line names a bank with the `(no books)` annotation — e.g. `Raiffeisen Schweiz Genossenschaft (no books)` on a self-led issuer, or a broker of record listed for legal/reporting purposes only — that bank is **not active, not passive, and doesn't appear in the BR bookrunner list at all**.

## Correct handling

- **BR body JLM list**: omit the `(no books)` bank entirely. `Joint Lead Managers Deutsche Bank, DZ BANK AG, J.P. Morgan, Morgan Stanley, UBS Investment Bank (B&D).` — Raiffeisen Schweiz Genossenschaft (no books) is dropped.
- **Tranche form `banks.active[]`**: do NOT include the `(no books)` bank. Active count is only genuine bookrunners.
- **Tranche form `banks.passive[]`**: do NOT include the `(no books)` bank either. Passive is for banks that DO handle books but aren't lead pricing coordinators — a `(no books)` bank isn't handling books at all.

## What NOT to do

Do NOT flag "missing passive lead" for a `(no books)` bank. Do NOT propose adding it to the body's JLM list. Do NOT propose adding it to `banks.passive[]`.

**Why:** Finn on Raiffeisen Schweiz Genossenschaft EUR500m WNG 8NC7 IPTs (id 14650443): source's JLM line named 6 banks including `Raiffeisen Schweiz Genossenschaft (no books)`; BR body carried 5 (dropping the (no books) issuer). Tick flagged the BR body as missing a JLM AND flagged tranche form banks.passive as empty. Finn: "when its no books it means it's in active or passive- please remember" — i.e. it's in NEITHER; drop it.

## How to apply

1. When walking the JLM list, parse each source name for a `(no books)` (or `no books` / `no-books`) suffix.
2. If present, EXCLUDE the bank from every downstream check: BR body count, `banks.active` count, `banks.passive` count.
3. If the BR body body correctly omits a `(no books)` bank, mark that clean — don't flag.
4. Only flag when BR body incorrectly includes the `(no books)` bank, or when a bank without `(no books)` is genuinely missing from the JLM list.

Related: [[bondradar-book-or-rating-field]] (JT-LEADS is triggered by count of active leads only; `(no books)` banks don't count toward the >3 threshold).
