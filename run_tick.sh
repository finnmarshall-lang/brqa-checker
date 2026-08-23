#!/bin/bash
# BR QA Checker — one tick.
# Invoked by ~/Library/LaunchAgents/com.finn.brqa-checker.plist every 10 minutes.

set -euo pipefail

PROJECT_DIR="/Users/finn.marshall/brqa-checker"
LOG_DIR="$PROJECT_DIR/logs"
LOG_FILE="$LOG_DIR/tick.log"
PROMPT_FILE="$PROJECT_DIR/tick_prompt.txt"

mkdir -p "$LOG_DIR"

# Rotate log if it's over 5MB
if [ -f "$LOG_FILE" ]; then
  SIZE=$(stat -f%z "$LOG_FILE" 2>/dev/null || stat -c%s "$LOG_FILE" 2>/dev/null || echo 0)
  if [ "$SIZE" -gt 5242880 ]; then
    mv "$LOG_FILE" "$LOG_FILE.$(date +%Y%m%d-%H%M%S)"
  fi
fi

cd "$PROJECT_DIR"

# Corp TLS interception — Node needs the Mac's trust store
export NODE_EXTRA_CA_CERTS="$HOME/corp-ca-bundle.pem"
export NODE_OPTIONS=--use-system-ca

# Load nvm so we can use the CLI installed under it
export NVM_DIR="$HOME/.nvm"
if [ -s "$NVM_DIR/nvm.sh" ]; then
  . "$NVM_DIR/nvm.sh"
fi

# Source env vars (BR_USERNAME, BR_PASSWORD, SLACK_BOT_TOKEN)
if [ -f "$HOME/.bondradar-env" ]; then
  set -a
  source "$HOME/.bondradar-env"
  set +a
fi

CLAUDE_BIN="$HOME/.nvm/versions/node/v24.19.0/bin/claude"

echo "=== tick $(date -u +%Y-%m-%dT%H:%M:%SZ) ===" >> "$LOG_FILE"
"$CLAUDE_BIN" -p "$(cat "$PROMPT_FILE")" \
  --dangerously-skip-permissions \
  >> "$LOG_FILE" 2>&1 || echo "tick failed with exit $?" >> "$LOG_FILE"

echo "=== done $(date -u +%Y-%m-%dT%H:%M:%SZ) ===" >> "$LOG_FILE"
