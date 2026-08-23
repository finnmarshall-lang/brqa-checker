# BR QA Checker

Automated QA for deals published to Bond Radar. Watches `#bond-deal-alerts` for
term-sheet messages that get a ✅ reaction, pulls the corresponding deal from
Bond Radar, runs four checks (missing fields, stuck at stage, house-style,
duplicates), and posts findings as a threaded reply on the original term-sheet
message. Replaces the existing `@brqa` human-QA ping.

## Files

- `refresh_cookies.py` — Playwright login → `cookies.json`
- `bondradar_api.py` — Bond Radar admin API client + CLI
- `INSTRUCTIONS.md` — prompt for the scheduled Claude task
- `checklist.md` — per-stage required-fields spec (IPTs, Guidance, Priced, …)
- `cookies.json` — cached session cookies (auto, chmod 600, gitignore)
- `state.json` — dedup state (which Slack messages already checked)

## One-time setup

1. **Create the credentials file** — put your Bond Radar login into `~/.bondradar-env`:
   ```
   BR_USERNAME=you@9fin.com
   BR_PASSWORD=your-password
   ```
   Then lock it down:
   ```bash
   chmod 600 ~/.bondradar-env
   ```

2. **Install Playwright**:
   ```bash
   pip3 install playwright
   python3 -m playwright install chromium
   ```

3. **Do the first login manually** (verifies the form selectors work):
   ```bash
   cd "/Users/finn.marshall/Documents/Claude/Projects/BR QA Checker"
   python3 refresh_cookies.py
   ```
   Expected output: `Saved N cookies to .../cookies.json`.
   If it fails, it will dump `_login_page_debug.png` — open it, check the
   username/password field selectors, and adjust the constants at the top of
   `refresh_cookies.py`.

4. **Smoke-test the API client**:
   ```bash
   python3 bondradar_api.py search "World Bank"
   ```

5. **Disable the old `@brqa` scheduled task** (it's superseded by this one). Ask
   Claude to list scheduled tasks, then delete `bond-deal-qa-monitor` — or gate
   its logic behind a flag.

6. **Schedule this checker**: ask Claude to run `INSTRUCTIONS.md` every ~2
   minutes as a routine (uses the `schedule` skill / cron scheduler).

## Refresh behavior

`bondradar_api.py` calls `refresh_cookies.py` automatically on any 401. So a
short outage after a JSESSIONID expires will self-heal on the next run.
