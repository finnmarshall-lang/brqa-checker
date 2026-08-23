---
name: feedback-bondradar-timing-position
description: "The timing statement (`Books open, today's business`, `As early as today's business`, etc.) always goes at the end of the LATEST live line — after the Book update line at book-update stages, not attached to the carried-forward guidance/IPT paragraph."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-20T08:14:13.782Z
---

The timing statement in a Bond Radar body always sits at the end of the **latest live line** — never appended to a carried-forward earlier paragraph.

**Placement by stage:**

- **IPTs / Guidance / Spread set (no book line yet)** — timing at the end of the main paragraph. `[...] ISIN XYZ. Books open, today's business.`
- **Book update (has a `Book update:` line)** — timing at the end of the `Book update:` line, NOT after the guidance section. Example:
  ```
  Guidance remains MS+27bp area for [...]. ISIN XYZ.
  Book update: Books over 2bn (Incl. 280m JLMs). Books open, today's business.
  ```
- **Allocations Out** — timing at the end of the Allocations line.
- **Final Terms / Launched** — timing at the end of the update line, often `Allocation and pricing shortly.` in place of book timing.
- **Priced** — no forward-looking timing; the deal is done.

**Why:** the timing is a live signal about what's happening now, so it belongs with the freshest content. Attaching it to a stale (carried-forward) paragraph misleads readers about which state the timing applies to. Finn corrected me on 2026-08-20 after I passed the RLB Steiermark Book Update body clean while `Books open, today's business.` still sat at the end of the guidance section — should have been moved to the end of the `Book update:` line.

**How to apply:** on every finding at a stage that has a book line, verify the timing sits at the end of the book line. If it's still attached to the guidance/IPT paragraph, flag it and quote the corrected ordering.

See also [[br-qa-checker-project]], [[feedback-bondradar-book-line]].
