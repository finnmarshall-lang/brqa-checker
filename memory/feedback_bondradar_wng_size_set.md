---
name: bondradar-wng-size-set
description: "WNG (will-not-grow) with a specific size figure counts as size confirmed — combined with a set spread it makes the deal Final Terms / Launched, not Spread Set."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-24T10:01:46.910Z
---

`EUR500m (WNG)` (or any `<ccy><size> (WNG)`) is a **size lock** — the issuer has committed not to grow the deal from that number. Treat it as size set.

So if the BR body opens `Spread set at X for <issuer>'s EUR500m (WNG)...` — that is BOTH spread set AND size set. The correct stage is **Final terms** / **Launched** (interchangeable), not Spread Set. The headline may open with either stage word.

**Why:** Finn corrected a QA where the tick called Final Terms premature because "size still WNG". WNG isn't a placeholder — it's the strongest form of size confirmation the syndicate can give short of pricing.

**How to apply:** When walking the stage-detection heuristic, treat `(WNG)` / `WNG` / `no-grow` / `will not grow` next to a currency+size figure as size set. Combine that with an explicit `Spread set at X` and the deal is Final Terms — the headline stage word must be `Final terms` or `Launched`, and the tranche form's `timing` field can carry `launched` (not "today", not blank). Do not flag either as wrong.

Related: [[bondradar-final-terms-casing]] (Final terms lowercase t; interchangeable with Launched).
