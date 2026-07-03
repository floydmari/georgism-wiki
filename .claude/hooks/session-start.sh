#!/bin/bash
# SessionStart hook — prepare a Claude Code session to work on and publish the wiki.
#   1. Install the Python deps the wiki tooling needs.
#   2. Install the 1Password CLI (`op`) if a service-account token is present.
#   3. Resolve the Ghost Admin key from 1Password (Emma vault) into the session env so
#      scripts/sync_to_ghost.py and scripts/pull_from_ghost.py work without manual export.
#
# Idempotent and non-interactive. Never prints secret values. Safe if the token is absent —
# the session still starts; publishing simply stays unavailable until the token is added.
#
# Root of trust (must be set once, by a human, in the environment's settings — it CANNOT be
# bootstrapped from the vault it unlocks):
#   OP_SERVICE_ACCOUNT_TOKEN = ops_...   (persists across all sessions you create)
set -uo pipefail

log() { echo "[session-start] $*"; }

# --- 1. Python dependencies (cached after first run) ---
if command -v pip >/dev/null 2>&1; then
  pip install --quiet --disable-pip-version-check \
    markdown pyyaml python-frontmatter PyJWT cffi requests html2text 2>/dev/null \
    && log "python deps ready" || log "python dep install skipped/failed (non-fatal)"
fi

# --- 2. Install the 1Password CLI if we have a token and op is missing ---
if [ -n "${OP_SERVICE_ACCOUNT_TOKEN:-}" ] && ! command -v op >/dev/null 2>&1; then
  OP_VERSION="v2.31.1"
  ARCH="amd64"; case "$(uname -m)" in aarch64|arm64) ARCH="arm64";; esac
  URL="https://cache.agilebits.com/dist/1P/op2/pkg/${OP_VERSION}/op_linux_${ARCH}_${OP_VERSION}.zip"
  TMP="$(mktemp -d)"
  if curl -fsSL "$URL" -o "$TMP/op.zip" 2>/dev/null && unzip -oq "$TMP/op.zip" op -d "$TMP" 2>/dev/null; then
    install -m 0755 "$TMP/op" /usr/local/bin/op 2>/dev/null \
      || { mkdir -p "$HOME/.local/bin"; install -m 0755 "$TMP/op" "$HOME/.local/bin/op"; \
           echo 'export PATH="$HOME/.local/bin:$PATH"' >> "${CLAUDE_ENV_FILE:-/dev/null}"; }
    export PATH="$HOME/.local/bin:$PATH"
    log "installed op CLI ${OP_VERSION}"
  else
    log "could not download op CLI (network policy?) — publishing stays unavailable"
  fi
fi

# --- 3. Resolve Ghost credentials into the session environment ---
if [ -n "${OP_SERVICE_ACCOUNT_TOKEN:-}" ] && command -v op >/dev/null 2>&1; then
  VAULT="${OP_VAULT:-Emma}"
  ITEM="${OP_GHOST_ITEM:-Ghost Admin API Key — progress.org wiki}"
  KEY=""
  for f in credential password "api key" notesPlain; do
    KEY="$(op read "op://${VAULT}/${ITEM}/${f}" 2>/dev/null || true)"
    case "$KEY" in *:*) break;; *) KEY="";; esac
  done
  if [ -n "$KEY" ] && [ -n "${CLAUDE_ENV_FILE:-}" ]; then
    { echo "export GHOST_ADMIN_KEY='${KEY}'"
      echo "export GHOST_URL='${GHOST_URL:-https://progress-org.ghost.io}'"
    } >> "$CLAUDE_ENV_FILE"
    log "Ghost credentials loaded from 1Password (${VAULT}) into session env"
  else
    log "op present but Ghost key not resolved — check item name/fields in vault '${VAULT}'"
  fi
elif [ -z "${OP_SERVICE_ACCOUNT_TOKEN:-}" ]; then
  log "OP_SERVICE_ACCOUNT_TOKEN not set — add it in env settings to enable Ghost publishing"
fi

exit 0
