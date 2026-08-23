---
name: feedback-bondradar-reactor-tag
description: "BR QA findings tag the person who added the ✅ reaction on the term-sheet, not the @brqa subteam. Fetch reactor via `slack_reactors.py <channel> <ts>` and prepend `<@USERID>`."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 173ac7d1-9e30-4326-a6c3-3fdb541b1e25
  modified: 2026-08-20T17:47:01.286Z
---

BR QA Checker Slack findings tag the **reactor** — the person who added the ✅ reaction on the Slack term-sheet — instead of the `@brqa` subteam.

**HARD REQUIREMENT — never skip the reactor tag.** On 2026-08-20 Finn corrected me after I posted 5 verdicts in a batch without the `<@USERID>` mention. Verbatim: "you forgot to tag the person who did the update" → "never forget that". The reactor tag is not optional garnish — it's how the person responsible sees the finding. Every single finding, clean OR flagged, must open with `<@USERID>` on its own line before the verdict header. If the reactor fetch fails or returns an empty list, fall back to `<!subteam^S0AVADTSTFZ|@brqa>` — do NOT post without any tag.

## How to fetch the reactor

The Slack MCP tools (`slack_read_channel` / `slack_read_thread`) expose reaction counts but not user IDs. Shell out to the project's helper:

```
python3 "/Users/finn.marshall/Documents/Claude/Projects/BR QA Checker/slack_reactors.py" <channel_id> <message_ts>
```

Returns JSON `[{user_id, display_name}, …]` for everyone who added `white_check_mark` on that message. Use the first user's `user_id`.

The helper uses a bot token in `~/.bondradar-env` (`SLACK_BOT_TOKEN=xoxb-...`) that has `reactions:read` + `users:read` scopes, and the bot must be a member of `#bond-deal-alerts` (`/invite @BotName`).

## Finding template

Prepend `<@USERID>` on its own line at the top of the finding, before the `:warning: BR QA — …` header. Slack renders it as a clickable mention that fires a personal notification. The rest of the finding format is unchanged.

## Fallback

If the helper returns an empty list (unusual — the ✅ may have been removed between the poll and the fetch), fall back to the `<!subteam^S0AVADTSTFZ|@brqa>` subteam mention so the finding still routes somewhere.

## History

- 2026-08-18: Tag dropped ("annoying people") — no @-mention on findings.
- 2026-08-19 (afternoon): Reverted — tag `<!subteam^S0AVADTSTFZ|@brqa>` on all findings.
- 2026-08-20: Refined — tag the individual reactor via `<@USERID>` instead of the subteam, since that person actioned the ✅ and is the one who needs the follow-up.

See also [[br-qa-checker-project]].
