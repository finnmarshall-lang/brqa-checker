---
name: bondradar-roadshow-ic-timing
description: "When source announces a ROADSHOW / Investor Calls with specific dates (Global Investor Call #1/#2 etc.), the tranche form's `timing` field must read `i/c <date range>` — e.g. `i/c 01-02 Sep`."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-09-02T08:14:44.826Z
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

Two independent decisions: **date encoding** and **series marker**.

**Date encoding — pick one:**
- Single investor-call date → `<DD Mmm>` (e.g. `01 Sep`).
- Fixed multi-day span with fully enumerated dates (e.g. #1 on 01 Sep, #2 on 02 Sep, no open-ended language) → `<DD-DD Mmm>` (e.g. `01-02 Sep`, `28-30 Aug`).

**Series marker — append `>` when source uses "series" language, regardless of date encoding:**
- Source uses the word `series` (`a series of investor calls`, `series of fixed income investor meetings`) OR uses `commencing` / `commence` / `starting` with no explicit end → append trailing `>`.
- The `>` is orthogonal to the date form: it can attach to a single date or a multi-day range. Both are valid.

**Combined forms:**
- `i/c 01 Sep` — single date, no series wording.
- `i/c 01-02 Sep` — fixed span, no series wording.
- `i/c 31 Aug>` — single date with series wording (e.g. `arrange a series of fixed income investor meetings commencing Monday, 31 August 2026.`).
- `i/c 01-02 Sep>` — fixed span with series wording (e.g. 3M Co., id 14640384: source said `organize a series of European fixed income investor calls to be scheduled on Tuesday, September 1st and Wednesday, September 2nd`. Finn: "is right about the timing except is should have a > at the end as it's a series of investor calls as stated". Two-day fixed schedule + explicit "series" word → `i/c 01-02 Sep>`).

**Formatting details:**
- The month is short-form three letters, no punctuation.
- Do not include times or timezones — they belong in the body prose, not the tranche `timing` field.
- `i/c` is lowercase with a slash — do not spell out "investor call" or capitalise.
- The marker is always `i/c`, never `i/m`. Even when source uses "investor meetings" wording (not "investor calls"), the tranche-form marker stays `i/c`.

**When source has multiple date references — use the investor-calls/meetings date, not the "Roadshow" field.**

Source term sheets sometimes disclose two related dates: the actual investor-calls/meetings date (usually in the intro paragraph, e.g. "arrange a series of fixed income investor meetings commencing Thursday, 3rd September") AND a formal "Roadshow" line in the Timing field (e.g. "Roadshow commencing Friday, 4th September 2026"). Use the **investor-calls/meetings** date, not the "Roadshow" one. The `i/c` marker tracks the investor-call commencement, which is the first day accounts start hearing about the deal.

Finn on Tharisa USD300m 5Y Senior Secured (id 14650080): I proposed `i/c 04 Sep>` from the Timing-field "Roadshow commencing Friday, 4th September". Finn: "plz look at the source as it does say a series of investor calls 3rd september which means i/c 03 Sep>". So the intro paragraph's "series of ... investor meetings commencing Thursday, 3rd September" is the authoritative date; use 03 Sep, not 04 Sep. Same for the body's timing sentence — keep the 3rd September investor-meetings language, don't rewrite to the Roadshow-field date.

If the tranche form's `timing` field on a mandate/roadshow-stage deal doesn't follow this format (e.g. carries `today`, `TBC`, or a longer sentence), flag it and propose the `i/c DD-DD Mmm` form derived from the source's investor-call dates.

Related: [[bondradar-timing-position]] (timing sits at the end of the LATEST live line in the body — a separate rule about body prose position, not tranche-form encoding).
