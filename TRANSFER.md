# Transferring the BR QA Checker to another machine

Chat context doesn't sync between Claude Code installations — but the project is
self-contained. Follow these steps to run it on Windows (or any other Mac).

## 1. What to copy from this Mac

Copy the entire project directory to the target machine:

```
~/Documents/Claude/Projects/BR QA Checker/     (whole folder)
~/.bondradar-env                                (your Bond Radar credentials)
~/.claude/projects/-Users-finn-marshall/memory/ (feedback memories saved this session)
```

The memory files are the most important non-obvious bit — they encode all the
corrections you've made (e.g. `MWC` before `par call`, don't flag `type`, `Books
above`/`over` are equivalent, don't mention Fxd-to-Frn). Without them, the next
Claude session will repeat those mistakes.

## 2. Where they go on Windows

Windows paths mirror Mac but with `%USERPROFILE%` instead of `~`:

| Mac                                                    | Windows                                                       |
|--------------------------------------------------------|---------------------------------------------------------------|
| `~/Documents/Claude/Projects/BR QA Checker/`         | `%USERPROFILE%\Documents\Claude\Projects\BR QA Checker\`    |
| `~/.bondradar-env`                                    | `%USERPROFILE%\.bondradar-env`                               |
| `~/.claude/projects/-Users-finn-marshall/memory/`   | `%USERPROFILE%\.claude\projects\<project-slug>\memory\`     |

For the memory directory the last folder is project-slug-based — after opening
Claude Code on Windows once, look under `%USERPROFILE%\.claude\projects\` for
the slug that matches, then drop the `.md` files into its `memory/` subfolder.

## 3. Re-install on Windows

```powershell
# From an admin PowerShell in the project directory
pip install playwright
python -m playwright install chromium
# If your corporate proxy blocks the CDN, prefix with:
#   $env:NODE_TLS_REJECT_UNAUTHORIZED=0
# for the install step only.

# Re-harvest the auth cookies (the ones from Mac will still work briefly
# but re-run this to be safe):
python refresh_cookies.py

# Smoke-test:
python bondradar_api.py search "World Bank"
```

Update the hard-coded Mac path in `INSTRUCTIONS.md` if you want the scheduled
task to reference the Windows location — search for
`/Users/finn.marshall/Documents/Claude/Projects/BR QA Checker` and swap in the
Windows equivalent.

## 4. Start a fresh Claude Code session on Windows

Open Claude Code on Windows. Point Claude at the project by:

- Opening the `BR QA Checker` folder as the working directory, OR
- Pasting this into the first message:

  > Read `<project path>\INSTRUCTIONS.md`, `<project path>\checklist.md`,
  > and `<project path>\README.md` — this is the Bond Radar QA checker. State
  > lives in `state.json` in the same folder. Continue from here.

Claude will pick up the workflow immediately if the memory files transferred
correctly.

## 5. Restart the polling loop

Once Claude is oriented, ask:

> `/loop every 10 mins Poll #bond-deal-alerts and run the BR QA checker on
> any newly-✅'d messages. Follow INSTRUCTIONS.md exactly.`

Same behavior as this Mac session.

## Notes

- **Bond Radar credentials**: `refresh_cookies.py` reads `BR_USERNAME` /
  `BR_PASSWORD` from `~/.bondradar-env` on both platforms. Same values.
- **Slack MCP**: The Slack tools are authenticated via your claude.ai account,
  so they'll work automatically on Windows once you sign in with the same
  Anthropic account.
- **Cookies expire**: If a BR API call ever returns 401, `bondradar_api.py`
  auto-re-runs `refresh_cookies.py`. You shouldn't have to intervene.
- **State file** (`state.json`): keep in sync if you want to avoid re-QA'ing
  messages already checked on the other machine. Otherwise the target Mac's
  Claude will re-check anything not in its own state.
