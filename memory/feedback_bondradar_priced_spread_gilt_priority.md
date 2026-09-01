---
name: bondradar-priced-spread-gilt-priority
description: "The priced-deal form's `spread` field carries the primary pricing spread (Gilts for GBP, Treasuries for USD, etc.), NOT any secondary post-reset margin (SONIA/SOFR-MS) even if the source discloses both."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-01T13:47:28.044Z
---

For callable / resettable / hybrid notes, source term sheets often disclose two spreads:

1. **The primary pricing spread** — the level at which the deal actually printed against the underlying benchmark (e.g. `UKT+160bp`, `T+65bp`, `MS+110bp`).
2. **A post-reset margin** — the reset spread that applies after the first call date if the issuer chooses not to redeem (e.g. `SONIA Mid-Swap + 184.5bp`, `SOFR MS + 220bp`).

**Only #1 belongs in the priced-deal form's `spread` field.** The post-reset margin is a secondary/future detail — it doesn't describe the pricing today.

**Correct on the priced-deal form:**
- GBP deal priced off Gilts → `spread=G+160`
- USD deal priced off Treasuries → `spread=T+65`
- EUR corporate priced off mid-swaps → `spread=MS+110`

**Wrong:**
- `spread=SMS+184.5` on a GBP T2 priced at Gilts+160 — that's the post-reset SONIA margin, not the deal's pricing spread.
- `spread=SOFR MS+220` on a USD resettable priced off Treasuries — same class of error.

Priority order when source shows multiple spreads:
1. Gilts (`G+X` / `UKT+X`) — for GBP deals, always priority.
2. Treasuries (`T+X` / `UST+X`) — for USD deals.
3. Mid-swaps (`MS+X`) — for EUR/other fixed-rate deals when there's no sovereign benchmark.
4. Reference-rate FRN (`SOFR+X`, `SONIA+X`, `3mE+X`, `SARON+X`) — for pure FRN tranches only.

Reset margins (SONIA MS+, SOFR MS+, EURIBOR MS+ etc. after call date) go INTO the body's prose describing the coupon reset — they NEVER become the priced-deal form's `spread` value.

**Why:** Finn on BPCE GBP400m lg 11NC6 T2 Priced (id 14640297, priced-deal 14640637): tick marked `spread=SMS+184.5` as clean, sourcing it from the term sheet's `Margin (184.5bps)` for the post-reset SONIA leg. Finn: "why are we accepting SMS+184.5 in the priced deal form spread it should be G+160 please read the term sheet G will always be the priority spread". Correct value was `G+160` — the actual pricing spread from the source's `Reoffer: UKT+160bps` line.

**How to apply:** When walking the priced-deal form's `spread` field, cross-check against the source's `Reoffer` line specifically — that's the deal's pricing spread. If the field carries a reset margin (usually recognisable by `SMS+`, `SONIA MS+`, `SOFR MS+`, `EURIBOR MS+` with a spread wider than the pricing spread), flag it and propose the Gilts/Treasuries/MS+ value from the Reoffer line.

Related: [[bondradar-saron-ms-shorthand]] (SARON scope note reinforces reference-rate hierarchy), [[bondradar-headline-always-check]] (headline level and priced-deal `spread` must match the outgoing body's primary spread).
