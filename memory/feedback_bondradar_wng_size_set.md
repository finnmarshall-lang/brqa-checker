---
name: bondradar-wng-size-set
description: "WNG (will-not-grow) with a specific size figure counts as size confirmed — combined with a set spread it makes the deal Final Terms / Launched, not Spread Set."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-07T10:53:05.236Z
---

`EUR500m (WNG)` (or any `<ccy><size> (WNG)`) is a **size lock** — the issuer has committed not to grow the deal from that number. Treat it as size set.

So if the BR body opens `Spread set at X for <issuer>'s EUR500m (WNG)...` — that is BOTH spread set AND size set. The correct stage is **Final terms** / **Launched** (interchangeable), not Spread Set. The headline may open with either stage word.

**Why:** Finn corrected a QA where the tick called Final Terms premature because "size still WNG". WNG isn't a placeholder — it's the strongest form of size confirmation the syndicate can give short of pricing.

**How to apply:** When walking the stage-detection heuristic, treat `(WNG)` / `WNG` / `no-grow` / `will not grow` next to a currency+size figure as size set. Combine that with an explicit `Spread set at X` and the deal is Final Terms — the headline stage word must be `Final terms` or `Launched`, and the tranche form's `timing` field can carry `launched` (not "today", not blank). Do not flag either as wrong.

**Exception — `capped` / `(max)` at the deal level overrides per-tranche WNG.** When the headline / deal-level size carries `capped` (source `€1.25bn capped`) or `(max)`, the deal-level total is NOT confirmed yet — it can still allocate down. In this case, EVEN IF every tranche shows WNG and every spread is set, the stage stays at **Spread set**, not Final terms. The `capped` / `(max)` cap is the deal-level signal that overrides tranche-level WNG.

**Why (Nordea Mortgage Bank dual-tranche CB, id 14650839):** both tranches had WNG at Guidance, both spreads got set to "the number", but the headline read `€1.25bn capped`. I flagged the stage word as needing to move from `Spreads set` to `Final terms` on the WNG-plus-spread-set logic. Finn: "it did say WNG for the tranches at the start earlier but it does say capped in the headline meaning its not quite set". So the deal-level `capped` overrides per-tranche WNG, and Spread set was correct.

Rule after this correction:
- Every tranche size WNG-locked AND every spread set AND no deal-level `capped`/`(max)` → **Final terms / Launched**.
- ANY of these missing (a tranche still bmk, a spread still area, or deal-level `capped`/`(max)`) → stage stays at whatever the update actually is (Spread set, Book update, etc.).

Related: [[bondradar-final-terms-casing]] (Final terms lowercase t; interchangeable with Launched).
