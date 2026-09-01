---
name: feedback-bondradar-headline-always-check
description: "Every BR QA finding must walk the headline element-by-element (issuer, currency+size, tenor/structure, format flags, stage word, level, multi-tranche marker, tap/add-on). Never mark clean without checking the title."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-01T06:48:24.439Z
---

Every BR QA tick must include an explicit headline check — the title is a first-class QA target, not an afterthought. Do not mark a finding clean until you have walked all eight elements of the headline against the source term sheet AND the BR body:

1. Issuer / ticker shorthand
2. Currency + size (`EUR500m`, `USD1bn`, `CHF100m+`, `HKD bmk`)
3. Tenor / structure (`5-year`, `L-4y`, `8NC3`, `PerpNC5`, `11.5NC10`, `WNG`)
4. Format flags: `Grn`, `Soc`, `Sus`, `SLB`, `EuGB`, `CB` / `MC`, `T2`, `AT1`, `RT1`, `Sub`, `Sr Pref`, `SNP`, `HoldCo` / `OpCo`, `Sukuk`, `Kangaroo`, `Samurai`, `144A/RegS`, `SEC`, `RegS`
5. Stage word (must match body opener: `Priced:` → `Priced at [level]`; `Launched:` → `Launched at [level]`; `Guidance is` → `Guidance [level]`; `IPTs are` → `IPTs [level]`; `Spread set + size set` → `Final Terms`; `Book update` for reiterated levels)
6. Level printed after the stage word — spelled-out form matching the body, NOT the compact tranche-form shorthand:
   - ✓ `Guidance MS+11bp area`, `IPTs 3mE+55bp area`, `Priced at T+65bp`, `Spread set at SOFR MS+22bp`
   - ✗ `Guidance MS+11a` (compact) — flag; the `a` for "area" and dropped `bp` are tranche-form-only
   - The level must equal the body level, but written in the same style the body uses (`bp` / `bps` spelled out, `area` spelled out, ranges hyphenated `MS+75-80bps`, reference-base labels kept). Finn on ASFINAG EUR500m 5y WNG Guidance (id 14640112): I marked `Guidance MS+11a` clean; Finn: "this should be MS+11bp area".
7. Multi-tranche marker (`dual-tranche` for 2, `multi-tranche` for 3+)
8. Tap / increase marker (`tap` / `add-on` / `Increase Priced`)

**Why:** headlines are what the buy-side scans first; a wrong stage word, missing format flag, or stale level in the title is a house-style break that misleads readers even if the body is correct. Finn asked to make sure titles are being checked "from now on" (2026-08-20), after several clean verdicts had focused only on body + tranche form and skipped the headline walk.

**How to apply:** on every finding, include an explicit line in the QA output that names each headline element you checked (or the ones that flagged). Clean verdicts should mention "Headline stage word / level / format flags / marker all match" so the reader can see the walk happened.

See also [[br-qa-checker-project]], [[feedback-bondradar-headline-stage]].
