---
name: feedback-bondradar-headline-always-check
description: "Every BR QA finding must walk the headline element-by-element (issuer, currency+size, tenor/structure, format flags, stage word, level, multi-tranche marker, tap/add-on). Never mark clean without checking the title."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-02T10:48:26.379Z
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

## Real templates observed in the BR API (updated 2026-09-01 from a live `list hg 200` sample)

Concrete patterns to match — anything else on a QA is a candidate flag.

**Overall skeleton (single tranche):**
```
** <Issuer> <CCY><size> <tenor>[ <flags>][ at <level>]: <Stage>[ at <level>]
```
- `**` prefix always. Issuer is short-form (ticker or shortened name, no `Ltd`/`plc`/`AG`).
- Currency + size: `EUR500m`, `USD1bn`, `CHF150m`, `EUR bmk`, `EUR Benchmark`, `AUD400m` — no space between number and unit.
- Tenor: `5y`, `5-year`, `5.5-year`, `Long 3-year` / `long 6-year` / `lg 5y` / `L-4y` are all valid variants (do NOT flag between them).
- Structure alt for non-callables: `3NC2`, `10NC5`, `16NC6`, `PNC10.25`, `PNC5`.
- WNG in the headline is **OPTIONAL** — its absence is not a defect. Both `EUR500m 5y WNG` (with WNG) and `EUR500m 5y` (without) are valid headlines; the WNG fact lives in the body via `EUR500m (WNG)`. Do NOT flag a missing WNG marker in the headline. Finn on Banca MPS EUR500m 10.5NC5.5 Grn T2 IPTs (id 14650075): "Don't worry about WNG".

**Stage placement of level** — this is the rule the tick got wrong on ASFINAG and needs to memorise:
- **Book stats** stage: level goes BEFORE the colon — `... 10-year at MS+24bp: Book stats`, `... 5-year Grn CB at MS+16bp: Book stats`.
- **Every other stage**: level goes AFTER the stage word — `: Priced at T+65bp`, `: Guidance MS+11bp area`, `: IPTs 7.25% area`, `: Spread set at SOFR MS+22bp`.
- **Dual/multi-tranche**: NO level embedded anywhere in the headline regardless of stage — level lives per-tranche in the body only. Templates: `EUR bmk dual-tranche SP`, `EUR2.6bn dual-tranche Hybrid EuGB`, `USD bmk multi-tranche`.

**Level format** — always the spelled-out body form:
- `MS+11bp area` / `MS+29bp` / `MS+75-80bps` / `MS+120bp area`
- `T+65bp` / `T+115bp` (Treasuries)
- `G+85bp` / `G+105bp` (Gilts)
- `OAT+10bp` / `OAT+12bp` (French OAT)
- `ASW+130bp` (Aussie asset swap)
- `SONIA MS+36bp` (GBP FRN)
- `BBSW+130bp area` (Aussie FRN)
- `SOFR MS+32bp` (USD FRN — full form) OR `SMS+22bp` (compact form both seen in the live sample — do NOT flag either)
- `SARON MS+20bp` on the outgoing message (see the SARON memory rule)
- `E+52bp` / `3mE+47bp` (EUR FRN)
- Fixed coupon on some taps: `Priced at 4.99%`, `Priced at 100.00`

**Stage word templates:**
- `Mandated` (no level).
- `IPTs [level]` — e.g. `IPTs`, `IPTs 7.25% area`, `IPTs BBSW+130bp area`.
- `Guidance [level]` — e.g. `Guidance MS+11bp area`, `Guidance MS+60bp area`.
- `Book Update` — level optional (see `feedback_bondradar_headline_level_optional.md`).
- `Spread set at [level]`.
- `Final terms` / `Launched at [level]` (interchangeable when body opens Spread set + size set).
- `Allocations` — no level in headline.
- `Priced [at level]` — level required unless dual/multi-tranche.
- `Priced at [level]: Book stats` — the ONLY case where level sits between title and stage word.
- `Priced` for `Priced tap` / dual-tranche without level.

**Format flags (order matters — appear right after tenor):**
- ESG: `Grn` / `Green` / `Soc` / `Sus` / `SLB` / `EuGB` / `SDB` — `Grn` and `Green` are interchangeable in the headline; do NOT flag one against the other. Finn on MuniFin EUR bmk 5-year Green Mandated (id 14650171): "Grn and green mean the same thing!" — I had proposed rewriting `Green` to `Grn`; that's not a defect.
- Covered: `CB` (`Grn CB` / `Green CB` = Green Covered Bond, both flags can chain)
- Ranking: `SP` (Senior Preferred), `SNP`, `Sub`
- Capital tier: `T2`, `AT1`, `RT1`, `Hybrid`, `Hybrid EuGB`
- Structure descriptors: `FRN`, `FA backed`
- **Docs-format flags DO NOT belong in the headline.** `144A/RegS`, `SEC`, `RegS`, `TEFRA D`, `NGN`, `Reg S Cat 2` and similar selling-restriction / doc-format markers live in the BODY only. Do NOT propose adding any of these to a headline (single, dual, or multi-tranche). Finn on Pakistan USD benchmark dual-tranche IPTs (2026-09-02): I proposed adding `144A/RegS` to the dual-tranche headline. Finn: "this isn't right I have given you a headline format". The real templates in the BR API confirm — none of the ~80 headlines sampled carried `144A/RegS`, `SEC`, or `RegS` as a headline flag.
- Docs / origin markets: `Sukuk`, `Samurai`, `Kangaroo`
- Canadian bail-inable: `bail-inable` (see canadian-bail-inable memory rule) — NOT `SNP`

**Tap format:** `<CCY><size> <MonthName Year> tap: <Stage>[at level]` — e.g. `Rentenbank CHF65m Mar 2036 tap: Priced at SARON MS+20bp`, `Rentenbank AUD100m 2031 tap: Priced at 4.99%`.

See also [[br-qa-checker-project]], [[feedback-bondradar-headline-stage]], [[bondradar-headline-stage-by-update]], [[bondradar-headline-level-optional]], [[bondradar-no-level-embed-dual-tranche]], [[bondradar-saron-ms-shorthand]], [[bondradar-canadian-bail-inable-snp]].
