---
name: bondradar-spread-range-preservation
description: "When the source term-sheet gives a spread as a range (e.g. `+[55-57]bps`, `MS+75-80`), BR must carry the full range in body/headline/tranche — not just one endpoint."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-01T08:19:31.037Z
---

Source term-sheets sometimes express the set spread as a range rather than a single number — e.g. `Reoffer: 3-month EURIBOR +[55-57]bps`, `Spread: MS+75-80bps`, `Reoffer +55/57`. In these cases the deal is being priced across a small band (typically 2-5bp wide), and both endpoints matter — BR must render the range, not just one side.

**Correct renderings:**

- Body / headline: `Spread set at 3mE+55/57bp` (or `+55-57bps`) — matching source form.
- Tranche form `priceEvolution`: `3mE+55/57` — range preserved, `a` / `area` suffix dropped once set.

**Wrong renderings:**

- Body: `Spread set at 3mE+55bp` — dropped the upper endpoint (looks like a single set value).
- Body: `Spread set at 3mE+57bp` — dropped the lower endpoint.
- Tranche form: `3mE+55` — dropped upper.

**Why:** Finn on TD EUR bmk 3y FRN bail-inable Spread set (id 14640347): tick marked level `3mE+55bp` as clean against source. Finn: "this didn't see the term sheet Reoffer: 3-month EURIBOR +[55-57]bps this meant it was 55/57bp not just 55bp". The source's `+[55-57]bps` is a set-price range; the BR body only carried `3mE+55bp` (low end), missing the upper 57.

**How to apply:**

1. Read the source term sheet's `Reoffer` / `Spread` / `Pricing` field literally — do not silently drop range brackets or the upper endpoint.
2. When the field contains `[X-Y]bps` / `X-Y` / `X/Y` / `+X-Ybps`, that's a range. Preserve it verbatim into body, headline level (where the level appears), and the tranche form's `priceEvolution` field.
3. If BR body currently shows only one endpoint, flag it and propose the corrected range form.
4. The `area` suffix drops once spread is SET regardless of whether the value is a single number or a range — a set range is still set.

Same principle applies to yield ranges, coupon ranges, and reoffer-price ranges on taps — carry the range if source gave one.

Related: [[bondradar-headline-always-check]] (level format), [[bondradar-frn-priceevolution]] (compact form on tranche field, but range preservation applies inside that compact form too).
