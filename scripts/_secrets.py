#!/usr/bin/env python3
"""
_secrets.py — resolve the Ghost Admin API credentials from the environment, falling back to
1Password (`op read`) when a service-account token is available.

Resolution order for each secret:
  1. The plain environment variable (GHOST_ADMIN_KEY / GHOST_URL) — set by the SessionStart hook
     (.claude/hooks/session-start.sh writes it to $CLAUDE_ENV_FILE) or by hand.
  2. `op read` from 1Password, if `op` is installed and OP_SERVICE_ACCOUNT_TOKEN is set.

This keeps the token as the single root of trust: it must be injected into the environment as
OP_SERVICE_ACCOUNT_TOKEN (env settings persist across sessions). Nothing secret is committed.

Overridable via env:
  OP_VAULT       (default: ID of the "Emma / Floyd Agent" vault — the name contains " / ",
                  which op:// path parsing can't handle, so refs must use IDs)
  OP_GHOST_ITEM  (default: ID of "Ghost Admin API Key — progress.org wiki")
  GHOST_URL      (default "https://progress-org.ghost.io")
"""
import os
import shutil
import subprocess

OP_VAULT = os.environ.get("OP_VAULT", "cupqdml5deh2x6povtmqsxdzyu")
OP_GHOST_ITEM = os.environ.get("OP_GHOST_ITEM", "dvu2rmbugwj3lhtacwoddb2cja")
DEFAULT_GHOST_URL = "https://progress-org.ghost.io"


def _op_available():
    return shutil.which("op") and os.environ.get("OP_SERVICE_ACCOUNT_TOKEN")


def _op_read(ref):
    try:
        out = subprocess.run(["op", "read", ref], capture_output=True, text=True, timeout=30)
        if out.returncode == 0:
            return out.stdout.strip()
    except Exception:
        pass
    return None


def ghost_admin_key():
    """Return the Ghost Admin key '<id>:<hex>' or None. Tries env, then 1Password fields."""
    if os.environ.get("GHOST_ADMIN_KEY"):
        return os.environ["GHOST_ADMIN_KEY"]
    if _op_available():
        for field in ("credential", "password", "api key", "notesPlain"):
            ref = f"op://{OP_VAULT}/{OP_GHOST_ITEM}/{field}"
            val = _op_read(ref)
            if val and ":" in val:
                return val
    return None


def ghost_url():
    if os.environ.get("GHOST_URL"):
        return os.environ["GHOST_URL"]
    if _op_available():
        for field in ("url", "website", "server"):
            val = _op_read(f"op://{OP_VAULT}/{OP_GHOST_ITEM}/{field}")
            if val:
                return val.rstrip("/")
    return DEFAULT_GHOST_URL


def require_ghost():
    """Return (key, url) or exit with a clear, actionable message."""
    key = ghost_admin_key()
    if not key:
        import sys
        sys.exit(
            "No Ghost Admin key found.\n"
            "  Set GHOST_ADMIN_KEY directly, or make 1Password reachable:\n"
            "  1. Add OP_SERVICE_ACCOUNT_TOKEN to this environment's settings (env vars).\n"
            "  2. Ensure the `op` CLI is installed (the SessionStart hook does this).\n"
            f"  3. The key is read from op://{OP_VAULT}/{OP_GHOST_ITEM}/credential\n"
        )
    return key, ghost_url()


if __name__ == "__main__":
    # Diagnostic only — prints presence, never the secret value.
    k = ghost_admin_key()
    print(f"op available: {bool(_op_available())}")
    print(f"GHOST_ADMIN_KEY resolved: {'yes' if k else 'no'}")
    print(f"GHOST_URL: {ghost_url()}")
