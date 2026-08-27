# brqa-scheduler — external cron trigger for the BR QA Checker

Cloudflare Worker that fires the GitHub Actions `qa-tick.yml` workflow every 10 minutes via GH's `workflow_dispatch` REST endpoint. GH honours `workflow_dispatch` events immediately, unlike its own scheduler which can skip cron slots for hours.

Free-tier deployment — Cloudflare's free plan includes cron triggers and 100k requests/day (we use 144/day).

## One-time setup

You'll do this once. It takes ~15 min.

### 1. Sign up for Cloudflare (free)

<https://dash.cloudflare.com/sign-up>. No card required for the free plan.

### 2. Install the wrangler CLI

```bash
npm install -g wrangler
```

You already have Node from the QA Checker setup. If `npm` complains about permissions, use `npx wrangler` in the commands below instead of `wrangler`.

### 3. Log wrangler into your Cloudflare account

```bash
cd ~/brqa-checker/scheduler-worker
wrangler login
```

Browser opens; approve the OAuth prompt. Ctrl-C wrangler once you see "You are now logged in!".

### 4. Create a fine-scoped GitHub PAT

<https://github.com/settings/personal-access-tokens/new>

- **Resource owner**: your account (`finnmarshall-lang`)
- **Repository access**: **Only select repositories** → pick `brqa-checker`
- **Repository permissions**:
  - **Actions**: **Read and write**
  - (leave everything else at "No access")
- **Expiration**: pick something reasonable (1 year is fine — Cloudflare will keep firing after that, but the worker will fail until you rotate)

Copy the token starting `github_pat_…`. You'll paste it in the next step and never see it again from GitHub.

### 5. Store the token as a Cloudflare Worker secret

```bash
cd ~/brqa-checker/scheduler-worker
wrangler secret put GH_TOKEN
```

Paste the PAT when prompted. Wrangler encrypts it inside Cloudflare; it doesn't touch this repo.

### 6. Deploy the Worker

```bash
wrangler deploy
```

Wrangler prints a URL like `https://brqa-scheduler.<your-subdomain>.workers.dev` and confirms the cron trigger is registered. You're done.

## Verifying it works

Two ways:

1. **Cloudflare dashboard** → Workers → brqa-scheduler → **Cron Triggers** tab. Shows the next run time.
2. **Tail logs live**:
   ```bash
   wrangler tail
   ```
   Wait up to 10 min. On each fire you should see `GH dispatch OK at 2026-…`. If you see `GH dispatch failed 401`, the PAT is wrong or lacks the Actions:write scope.

You can also just watch <https://github.com/finnmarshall-lang/brqa-checker/actions> — new runs should appear labelled `Manually run by finnmarshall-lang` on the 10-min mark (dispatches show as manual triggers).

## Maintenance

- **Rotating the PAT**: create a new one, `wrangler secret put GH_TOKEN` again with the new value, `wrangler deploy` is not required (secrets update in place).
- **Changing cadence**: edit `wrangler.toml`'s `crons` array, `wrangler deploy`.
- **Pausing**: Cloudflare dashboard → Workers → brqa-scheduler → **Settings** → Triggers → delete the cron entry. Or comment out the cron in `wrangler.toml` and redeploy.

## Removing the built-in GH cron

Once the Cloudflare Worker is proven reliable, you can drop the `schedule:` entries in `.github/workflows/qa-tick.yml` to avoid duplicate scheduled attempts. The `workflow_dispatch:` trigger stays — that's what the Worker uses. Do this only after seeing a few days of clean Cloudflare-triggered runs.
