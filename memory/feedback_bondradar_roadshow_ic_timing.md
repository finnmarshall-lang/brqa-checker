---
name: bondradar-roadshow-ic-timing
description: "When source announces a ROADSHOW / Investor Calls with specific dates (Global Investor Call #1/#2 etc.), the tranche form's `timing` field must read `i/c <date range>` — e.g. `i/c 01-02 Sep`."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-28T08:13:10.033Z
---

When a source term-sheet / mandate announcement mentions a **ROADSHOW** or **Global Investor Calls** with specific date(s), the tranche form's `timing` field encodes that as **`i/c <date range>`** — `i/c` = "investor call" — followed by the date span in the compact `DD-DD MMM` format.

**Example (Finn's illustration):**

> Source:
> ```
> ROADSHOW
> Global Investor Call #1
> Date: Tuesday, 01 September 2026
> Time: 16:00 CEST / 10:00 EDT
>
> Global Investor Call #2
> Date: Wednesday, 02 September 2026
> Time: 14:00 CEST / 08:00 EDT
> ```
>
> Tranche form `timing`: `i/c 01-02 Sep`

## How to apply

- If the source discloses one investor-call date only → `i/c <DD Mmm>` (e.g. `i/c 01 Sep`).
- If the source discloses a multi-day span → `i/c <DD-DD Mmm>` (e.g. `i/c 01-02 Sep`, `i/c 28-30 Aug`).
- The month is short-form three letters, no punctuation.
- Do not include times or timezones — they belong in the body prose, not the tranche `timing` field.
- `i/c` is lowercase with a slash — do not spell out "investor call" or capitalise.

If the tranche form's `timing` field on a mandate/roadshow-stage deal doesn't follow this format (e.g. carries `today`, `TBC`, or a longer sentence), flag it and propose the `i/c DD-DD Mmm` form derived from the source's investor-call dates.

Related: [[bondradar-timing-position]] (timing sits at the end of the LATEST live line in the body — a separate rule about body prose position, not tranche-form encoding).
