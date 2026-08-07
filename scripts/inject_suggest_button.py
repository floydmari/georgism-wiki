#!/usr/bin/env python3
"""
inject_suggest_button.py — add the wiki "Suggest an edit" button to the live site.

Appends (never replaces) a small script block to Ghost's site-wide
codeinjection_foot. On /wiki/<slug>/ article pages it renders a fixed
bottom-right pill linking to the Tier 1 diff editor:

    https://wiki-edit.progress.org/wiki/<slug>/edit

Safety properties, in line with docs/ARCHITECTURE-COMMUNITY.md:
  * APPEND-ONLY: existing injection content (the articles-page related-count
    script) is preserved byte-for-byte; this script refuses to run if the
    fetched value would shrink.
  * IDEMPOTENT: keyed on the element id `wiki-edit-suggest-btn`; a second run
    is a no-op.
  * REVERSIBLE: `--remove` deletes exactly the block this script added
    (delimited by the BEGIN/END comment markers) and nothing else.

Auth: same path as sync_to_ghost.py (GHOST_ADMIN_KEY via env or 1Password).
Usage:  python3 scripts/inject_suggest_button.py [--remove] [--dry-run]
"""
import sys, time, os

import jwt, requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _secrets import require_ghost

MARK = "wiki-edit-suggest-btn"
BEGIN = "<!-- BEGIN wiki-edit-suggest-btn (scripts/inject_suggest_button.py) -->"
END = "<!-- END wiki-edit-suggest-btn -->"

BLOCK = BEGIN + """
<script data-cfasync="false">
(function(){
  // data-cfasync=false: Rocket Loader opt-out (it deferred this script into
  // non-execution when pasted without the attribute; observed 2026-08-07).
  var m = location.pathname.match(/^\\/wiki\\/([a-z0-9-]+)\\/?$/);
  if (!m || m[1] === 'admin') return;
  var base = 'https://wiki-edit.progress.org/wiki/' + m[1];
  // Wire the Entry Metadata card's three placeholder buttons (theme ships them
  // pointing at /wiki/about/): Edit -> diff editor, History -> change timeline,
  // Cite -> revision-pinned citations.
  var wired = false;
  var targets = { 'Edit': base + '/edit', 'History': base + '/history', 'Cite': base + '/cite' };
  document.querySelectorAll('.wiki-meta-card__actions a').forEach(function(b){
    var url = targets[b.textContent.trim()];
    if (url) { b.href = url; wired = true; }
  });
  if (wired) return;
  // Fallback for layouts without the card: floating edit pill.
  var a = document.createElement('a');
  a.id = '""" + MARK + """';
  a.href = base + '/edit';
  a.textContent = '\\u270F\\uFE0F Suggest an edit';
  a.setAttribute('style','position:fixed;right:1.1em;bottom:1.1em;z-index:999;background:#2b6cb0;color:#fff;padding:.55em 1em;border-radius:999px;font:600 .85em system-ui,sans-serif;text-decoration:none;box-shadow:0 2px 8px rgba(0,0,0,.25)');
  document.body.appendChild(a);
})();
</script>
""" + END


def main():
    remove = "--remove" in sys.argv
    dry = "--dry-run" in sys.argv
    key, url = require_ghost()
    kid, secret = key.split(":")

    def hdr():
        tok = jwt.encode(
            {"iat": int(time.time()), "exp": int(time.time()) + 300, "aud": "/admin/"},
            bytes.fromhex(secret), algorithm="HS256", headers={"kid": kid})
        return {"Authorization": f"Ghost {tok}"}

    r = requests.get(f"{url}/ghost/api/admin/settings/", headers=hdr(), timeout=30)
    r.raise_for_status()
    settings = {x["key"]: x["value"] for x in r.json()["settings"]}
    foot = settings.get("codeinjection_foot") or ""
    print(f"current codeinjection_foot: {len(foot)} chars")

    if remove:
        if BEGIN not in foot:
            print("button block not present; nothing to remove"); return 0
        pre, rest = foot.split(BEGIN, 1)
        _, post = rest.split(END, 1)
        new = (pre.rstrip() + post).rstrip() + "\n"
    else:
        if MARK in foot:
            print("button already injected; no-op"); return 0
        new = foot.rstrip() + "\n" + BLOCK + "\n"
        if len(new) < len(foot):
            print("refusing: new value would shrink existing injection", file=sys.stderr)
            return 1

    if dry:
        print(f"[dry-run] would write {len(new)} chars"); return 0

    r = requests.put(
        f"{url}/ghost/api/admin/settings/",
        headers={**hdr(), "Content-Type": "application/json"},
        json={"settings": [{"key": "codeinjection_foot", "value": new}]}, timeout=30)
    r.raise_for_status()

    check = requests.get(f"{url}/ghost/api/admin/settings/", headers=hdr(), timeout=30)
    foot2 = {x["key"]: x["value"] for x in check.json()["settings"]}.get("codeinjection_foot") or ""
    ok_old = foot.split(BEGIN)[0].strip() in foot2
    ok_btn = (MARK in foot2) != remove
    print(f"written: {len(foot2)} chars | prior content preserved: {ok_old} | "
          f"button {'removed' if remove else 'present'}: {ok_btn}")
    return 0 if (ok_old and ok_btn) else 1


if __name__ == "__main__":
    sys.exit(main())
