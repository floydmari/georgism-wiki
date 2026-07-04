#!/usr/bin/env python3
"""
sync_to_ghost.py — Publish Georgism wiki Markdown files to the progress.org Ghost site.

Reads Markdown entries from concepts/ people/ places/ theories/, converts each to a
Ghost wiki post, and upserts it (create or update by slug). Idempotent — safe to re-run.

═══════════════════════════════════════════════════════════════════════════════════════
 THREE GHOST GOTCHAS — every one of these will silently break wiki entries if omitted.
═══════════════════════════════════════════════════════════════════════════════════════

 1. ?source=html   — Ghost stores content as Lexical, NOT html. When you send an `html`
                     field, you MUST append `?source=html` to the create/update URL or
                     Ghost silently DROPS the body (post saves with title+excerpt, empty
                     body). This is the #1 cause of "the page looks empty".

 2. custom_template — Ghost does NOT auto-pick a template by primary tag. `post-{slug}.hbs`
                     matches the POST's own slug, not its tag. To get the wiki layout you
                     MUST set  custom_template = "custom-wiki-entry"  on every wiki post,
                     or it renders with the plain article template (post.hbs).

 3. tags            — primary tag MUST be `wiki` (first in the list), plus a category tag
                     (`wiki-concepts` | `wiki-people` | `wiki-places` | `wiki-theories` |
                     `wiki-events` | `wiki-inventions`). The `wiki` primary tag is what
                     routes the post to /wiki/{slug}/ and excludes it from the essays
                     homepage. Optional: `wiki-most-cited`, `stub`.

═══════════════════════════════════════════════════════════════════════════════════════

Usage:
    export GHOST_ADMIN_KEY="<key-id>:<hex-secret>"     # from 1Password: "Ghost Admin API Key — progress.org wiki"
    export GHOST_URL="https://progress-org.ghost.io"
    python3 scripts/sync_to_ghost.py            # sync all
    python3 scripts/sync_to_ghost.py concepts/land-value-tax.md   # sync one

Requires: pip install PyJWT requests markdown python-frontmatter
"""
import os, sys, glob, time, jwt, requests
import frontmatter
import markdown as md

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _secrets import require_ghost   # resolves from env or 1Password (op)

_KEY, GHOST_URL = require_ghost()
GHOST_URL = GHOST_URL.rstrip("/")
KEY_ID, SECRET = _KEY.split(":")

CATEGORY_TAG = {            # folder -> (category tag slug, display name)
    "concepts":      ("wiki-concepts",      "Concepts"),
    "people":        ("wiki-people",        "People"),
    "places":        ("wiki-places",        "Places"),
    "events":        ("wiki-events",        "Events & Campaigns"),
    "outcomes":      ("wiki-outcomes",      "Outcomes"),
    "research":      ("wiki-research",       "Research"),
    "organizations": ("wiki-organizations", "Organizations"),
    "objections":    ("wiki-objections",    "Objections"),
    "narratives":    ("wiki-narratives",    "Narratives"),
}

def headers():
    """Fresh JWT per call (5-min expiry)."""
    iat = int(time.time())
    token = jwt.encode({"iat": iat, "exp": iat + 300, "aud": "/admin/"},
                       bytes.fromhex(SECRET), algorithm="HS256",
                       headers={"alg": "HS256", "typ": "JWT", "kid": KEY_ID})
    return {"Authorization": f"Ghost {token}", "Content-Type": "application/json"}

def build_tags(post, folder):
    cat_slug, cat_name = CATEGORY_TAG[folder]
    tags = [{"name": "Wiki", "slug": "wiki"},                # GOTCHA 3: primary tag first
            {"name": cat_name, "slug": cat_slug}]
    extra = post.get("tags", []) or []
    if "most-cited" in extra or post.get("most_cited"):
        tags.append({"name": "Most Cited", "slug": "wiki-most-cited"})
    if post.get("stub"):
        tags.append({"name": "Stub", "slug": "stub"})
    return tags

def upsert(path):
    folder = os.path.basename(os.path.dirname(path))
    fm = frontmatter.load(path)
    slug = os.path.splitext(os.path.basename(path))[0]
    html = md.markdown(fm.content, extensions=["extra", "toc"])

    payload_post = {
        "title": fm["title"],
        "slug": slug,
        "html": html,
        "custom_excerpt": (fm.get("excerpt") or "")[:300],
        "status": "published",
        "visibility": "public",
        "featured": bool(fm.get("featured", False)),
        "custom_template": "custom-wiki-entry",            # GOTCHA 2: or it renders as an article
        "authors": [{"slug": "progress-llm"}],             # all wiki entries attributed to Progress LLM
        "tags": build_tags(fm, folder),
    }

    # Does it already exist?
    r = requests.get(f"{GHOST_URL}/ghost/api/admin/posts/slug/{slug}/", headers=headers())
    if r.status_code == 200:
        existing = r.json()["posts"][0]
        payload_post["updated_at"] = existing["updated_at"]   # required for PUT collision check
        # GOTCHA 1: ?source=html  — without it the body is dropped
        u = f"{GHOST_URL}/ghost/api/admin/posts/{existing['id']}/?source=html"
        resp = requests.put(u, headers=headers(), json={"posts": [payload_post]})
        action = "updated"
    else:
        # GOTCHA 1: ?source=html  — without it the body is dropped
        u = f"{GHOST_URL}/ghost/api/admin/posts/?source=html"
        resp = requests.post(u, headers=headers(), json={"posts": [payload_post]})
        action = "created"

    if resp.status_code in (200, 201):
        print(f"  ✅ {action}: {slug}")
    else:
        print(f"  ❌ {slug}: {resp.status_code} {resp.text[:200]}")

def main():
    targets = sys.argv[1:] or [
        p for folder in CATEGORY_TAG for p in glob.glob(f"{folder}/*.md")
        if not os.path.basename(p).startswith("_")   # _-prefixed = internal, never published
    ]
    print(f"Syncing {len(targets)} entr{'y' if len(targets)==1 else 'ies'} to {GHOST_URL}")
    for path in targets:
        upsert(path)

if __name__ == "__main__":
    main()
