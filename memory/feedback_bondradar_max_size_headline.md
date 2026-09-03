---
name: bondradar-max-size-headline
description: When source states a `max EUR X` size cap, BR headline carries a parenthesised `(max)` qualifier after the size figure. Flag when it's dropped OR when it's bare (unparenthesised).
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-03T10:17:15.583Z
---

When the source's Size field is a maximum cap (e.g. `max EUR 750m`, `max USD 500m`), BR headline carries `(max)` — **parenthesised** — after the size figure.

**Correct headline form:**
- Source `Size: max EUR 750m` → `** Commerzbank EUR750m (max) PNC7.5 AT1: IPTs 6.625% area`
- Source `Size: max USD 500m` → `** <Issuer> USD500m (max) <tenor>: <Stage>`

Placement: `<CCY><size> (max) <tenor …>` — `(max)` sits between the size figure and the tenor/format-flags, in parentheses.

**Wrong forms (both flag):**
- `EUR750m PNC7.5 AT1: IPTs …` — no `(max)` at all.
- `EUR750m max PNC7.5 AT1: IPTs …` — bare `max` without parentheses. Finn: "(max) in brackets is better than just max". Parenthesised is the correct house form.

**Why:** Two Finn corrections on Commerzbank EUR750m PNC7.5 AT1:
- At IPTs (id 14650463): I marked clean, headline had no `max` at all. Finn: "max should be in title too after the amount please remember". Established `max` is required.
- At Guidance: I proposed `EUR750m (max)` → `EUR750m max`. Finn: "(max) in brackets is better than just max". Established the parenthesised form is preferred.

Reconciled rule: `(max)` in parentheses is the correct form.

**How to apply:**

1. On every headline walk, check whether the source's `Size:` field uses `max` (or an equivalent like `up to`, `not more than`) as a cap qualifier.
2. If yes:
   - Headline missing the marker entirely → flag; propose `(max)` insertion.
   - Headline has bare `max` (no parentheses) → flag; propose `(max)` with brackets.
   - Headline has `(max)` in parens → clean.
3. Distinct from `WNG` — `WNG` (will-not-grow) is optional in headline (see `feedback_bondradar_headline_level_optional.md`); `(max)` is REQUIRED when source uses `max` language.

Related: [[bondradar-headline-always-check]] (currency+size element — headline templates), [[bondradar-wng-size-set]] (WNG treatment on outgoing message).
