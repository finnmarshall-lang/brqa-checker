---
name: reference-bondradar-book-stats-workflow
description: "How book stats (Geography + Investor Type distributions) are added to a BR priced deal: input stats on priced-deal form, update IGRD headline to `** [issuer + size + level]: Book stats`, then Send to Bloomberg."
metadata:
  node_type: memory
  type: reference
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-20T09:18:25.467Z
---

Book stats are a post-pricing update announcing distribution breakdown by geography + investor type on a deal that has already priced.

## The BR workflow (from Finn, 2026-08-20)

**1. Add stats to the priced deal**

- Priced Deals tab → search for the deal
- Scroll down → *Add stats categories* → *Add new item* for each category
- Input percentages for:
  - **Geography** (must sum to 100%)
  - **Investor type** (must sum to 100%)
- Save

**2. Update the headline on IGRD (Latest Updates tab)**

- Rewrite headline to:
  - Prefix: `** ` (two stars)
  - Suffix: `: Book stats`
  - Example rewrite: `MuniFin EUR1bn long 7y: Priced at MS+21bp` → `** MuniFin EUR1bn long 7y at MS+21bp: Book stats`
- Note the level moves INTO the middle of the headline (`at MS+21bp`) — the stage word replaces `Priced at [level]`

**3. Send to Bloomberg**

- Return to the priced-deal form → *Send to Bloomberg*
- Confirm the headline appears on NEWBON

## QA checks for book stats updates

- **Headline** — `** [issuer] [size] [tenor] at [level]: Book stats` — check the `at [level]` is embedded and the stage word is `Book stats` (not `Book Stats`, not `Book update` — this is a distinct post-pricing stage)
- **Priced deal form** — `stats` field on the priced-deal record should now be populated (previously null). Both Geography and Investor type breakdowns present, each summing to 100%.
- **Percentages** — cross-check the percentages against the Bloomberg source (both categories, each row).
- **Total = 100%** — flag if either sum is off.
- **Source book size in body** — the body may append the finalised book stat (e.g. `Books above GBP1.475bn (excl. JLM interest)`).

## Related

- The `stats` field lives on the priced-deal form (id from `pricedDeals[].id`). Fetch via `python3 bondradar_api.py priced <cat> <id>`.
- See also [[br-qa-checker-project]], [[feedback-bondradar-book-line]].
