---
name: br-qa-checker-project
description: "Automated Bond Radar QA checker project — Slack-triggered on ✅ reactions in #bond-deal-alerts, replaces the old @brqa human-QA ping."
metadata: 
  node_type: memory
  type: project
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-17T13:44:05.818Z
---

Project directory: `/Users/finn.marshall/Documents/Claude/Projects/BR QA Checker/`

**What it does:** On a ✅ reaction in Slack channel `#bond-deal-alerts` (`C09JX51GAKH`), extracts the issuer from the term-sheet message, fetches the corresponding Bond Radar deal, runs four checks (missing fields, stuck stage, house-style, duplicates), and posts findings as a threaded reply in a rolling parent thread.

**Auth strategy:** Two-layer.
1. nginx Basic auth at the edge: `REDACTED_NGINX_USER:REDACTED_NGINX_PASS` (baked into Playwright via `http_credentials`).
2. User-level login form on the SPA → JSESSIONID cookie. `refresh_cookies.py` handles both, saves to `cookies.json`. On any 401 from the API, `bondradar_api.py` re-invokes the harvester automatically.

**API base:** `https://www.bondradar.com/admin/api`. Valid MarketType slugs are ONLY `hg` (68k deals) and `em` (18k deals). HY / SSA / FIG live as flags inside items (`hgDetails.highYield` etc.), NOT as separate endpoints.

**Cloudflare gotcha:** the site 403s Python's default User-Agent — must send a real browser UA.

**Related:** Replaces the existing `bond-deal-qa-monitor` scheduled task (which just pings `@brqa` humans on 👀). The old task should be disabled once this checker is scheduled.

**How to apply:** When Finn asks about Bond Radar deal checking, the QA workflow, or the checker itself, refer to the project files. See also [[feedback-bondradar-type-field]] for the key correction on `type` semantics.
