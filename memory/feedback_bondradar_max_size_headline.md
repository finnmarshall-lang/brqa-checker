---
name: bondradar-max-size-headline
description: "When source states a `max EUR X` (or `max USD X` etc.) size cap, BR headline must carry `max` after the size figure. Flag when it's dropped from the headline."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-03T07:18:39.971Z
---

When the source's Size field is a maximum cap (e.g. `max EUR 750m`, `max USD 500m`), BR headline carries the `max` qualifier after the size figure — not just in the body.

**Correct headline form:**
- Source `Size: max EUR 750m` → `** Commerzbank EUR750m max PNC7.5 AT1: IPTs 6.625% area`
- Source `Size: max USD 500m` → `** <Issuer> USD500m max <tenor>: <Stage>`

Placement: `<CCY><size> max <tenor …>` — `max` sits between the size and the tenor/format-flags.

**Why:** Finn on Commerzbank EUR750m PNC7.5 AT1 IPTs (id 14650463): source stated `Size: max EUR 750m`, BR headline read `** Commerzbank EUR750m PNC7.5 AT1: IPTs 6.625% area`. Tick marked clean; body carried `max` but headline didn't. Finn: "max should be in title too after the amount please remember".

**How to apply:**

1. On every headline walk, check whether the source's `Size:` field uses `max` (or an equivalent like `up to`, `not more than`) as a cap qualifier.
2. If yes AND the headline doesn't carry `max` after the size figure → flag with a Fix bullet proposing insertion of `max`.
3. Distinct from `WNG` — `WNG` (will-not-grow) is optional in headline (see `feedback_bondradar_headline_level_optional.md`); `max` is REQUIRED when source uses it.

Related: [[bondradar-headline-always-check]] (currency+size element — headline templates), [[bondradar-wng-size-set]] (WNG treatment on outgoing message).
