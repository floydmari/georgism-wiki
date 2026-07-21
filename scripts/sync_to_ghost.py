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

 4. tag identity    — ALWAYS reference tags by Ghost `id`, never by {name, slug}. Ghost
                     matches tags by NAME on create/update. If the stored tag has a
                     different display name than what you send, Ghost silently creates a NEW
                     tag with a de-duped slug (e.g. `wiki-outcomes-14`) and the category
                     listing drops to 1 entry. TAG_IDS in this file holds the canonical IDs;
                     update it if you add new tags via the Ghost admin UI.

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

# ─── GOTCHA 4: always reference tags by Ghost ID, never by name+slug ───────────
# Ghost matches tags by NAME when you POST {name, slug}. If the stored tag has a
# different display name (e.g. was created as name="wiki-outcomes" but we send
# name="Outcomes"), Ghost creates a NEW tag with a de-duped slug like
# "wiki-outcomes-14" instead of reusing the existing one. Referencing by `id`
# bypasses name-matching entirely and is guaranteed idempotent.
#
# To find the current IDs:  GET /ghost/api/admin/tags/slug/<slug>/
# Last verified: 2026-07-04 against https://progress-org.ghost.io
TAG_IDS = {
    "wiki":               "6a232c3e819cc700017226b2",
    "wiki-concepts":      "6a232c3f819cc700017226b4",
    "wiki-people":        "6a232c40819cc700017226b6",
    "wiki-places":        "6a232c40819cc700017226b8",
    "wiki-events":        "6a23a953819cc700017227a7",
    "wiki-outcomes":      "6a23a94f819cc70001722791",
    "wiki-problems":      "6a525e658f5d6d0001cfd591",
    "wiki-benefits":      "6a525e658f5d6d0001cfd593",
    "wiki-research":      "6a23a175819cc70001722769",
    "wiki-organizations": "6a23a952819cc7000172279f",
    "wiki-objections":    "6a23a955819cc700017227af",
    "wiki-narratives":    "6a495ad76c64fd00014ca8d1",
    "wiki-most-cited":    "6a232c42819cc700017226bc",
    "wiki-theories":      "6a232c41819cc700017226ba",
    "stub":               "6a232c42819cc700017226be",
    "wiki-books":         "6a4affad6c64fd00014cae89",
    "wiki-texts":         "6a4b01d76c64fd00014cb22a",
    "wiki-guides":        "6a53d2f28f5d6d0001cffc54",
    # ─── wiki-research sub-categories (added 2026-07-12) ───────────────
    "wiki-research-lvt":        "6a53badc8f5d6d0001cff916",
    "wiki-research-housing":    "6a53badc8f5d6d0001cff918",
    "wiki-research-georgism":   "6a53badd8f5d6d0001cff91a",
    "wiki-research-inequality": "6a53badd8f5d6d0001cff91c",
    "wiki-research-finance":    "6a53badd8f5d6d0001cff91e",
    "wiki-research-urban":      "6a53bade8f5d6d0001cff920",
    "wiki-research-resources":  "6a53bade8f5d6d0001cff922",
}

CATEGORY_TAG = {            # folder -> category tag slug (ID looked up from TAG_IDS)
    "concepts":      "wiki-concepts",
    "people":        "wiki-people",
    "places":        "wiki-places",
    "events":        "wiki-events",
    "problems":      "wiki-problems",
    "benefits":      "wiki-benefits",
    "research":      "wiki-research",
    "organizations": "wiki-organizations",
    "objections":    "wiki-objections",
    "narratives":    "wiki-narratives",
    # books: create a 'wiki-books' tag in Ghost admin, then add its ID to TAG_IDS
    # above — _tag() raises loudly until then, so books pages can't half-publish.
    "books":         "wiki-books",
    "guides":        "wiki-guides",
    # texts: create a 'wiki-texts' tag in Ghost admin, then add its ID to TAG_IDS.
    "texts":         "wiki-texts",
}

def headers():
    """Fresh JWT per call (5-min expiry)."""
    iat = int(time.time())
    token = jwt.encode({"iat": iat, "exp": iat + 300, "aud": "/admin/"},
                       bytes.fromhex(SECRET), algorithm="HS256",
                       headers={"alg": "HS256", "typ": "JWT", "kid": KEY_ID})
    return {"Authorization": f"Ghost {token}", "Content-Type": "application/json"}

def _tag(slug):
    """Return a Ghost tag reference by ID (never by name) to avoid de-duped slug creation."""
    tag_id = TAG_IDS.get(slug)
    if not tag_id:
        raise ValueError(f"Unknown tag slug '{slug}' — add it to TAG_IDS with its Ghost ID first")
    return {"id": tag_id}

def build_tags(post, folder):
    cat_slug = CATEGORY_TAG[folder]
    # GOTCHA 3: primary tag must be 'wiki' first
    # GOTCHA 4: use {id} only — never {name, slug} — prevents Ghost creating duplicate tags
    tags = [_tag("wiki"), _tag(cat_slug)]
    extra = post.get("tags", []) or []
    if "most-cited" in extra or post.get("most_cited"):
        tags.append(_tag("wiki-most-cited"))
    if post.get("stub"):
        tags.append(_tag("stub"))
    # ─── sub-category tags (e.g. wiki-research-lvt) ───────────────────
    # If the frontmatter has a `subcategory` field (e.g. "wiki-research-lvt"),
    # add that tag. This enables filter chips on the category page.
    subcat = post.get("subcategory")
    if subcat:
        if isinstance(subcat, list):
            for sc in subcat:
                if sc in TAG_IDS:
                    tags.append(_tag(sc))
                else:
                    print(f"  WARNING: unknown subcategory tag '{sc}' — add to TAG_IDS")
        elif subcat in TAG_IDS:
            tags.append(_tag(subcat))
        else:
            print(f"  WARNING: unknown subcategory tag '{subcat}' — add to TAG_IDS")
    return tags

def fit_excerpt(text, limit=300):
    """Ghost hard-caps custom_excerpt at 300 chars. Always cut at a sentence
    boundary (no ellipsis). If no sentence boundary in window, cut at word
    boundary and add a period. Excerpts within the cap pass through."""
    text = (text or "").strip()
    if len(text) <= limit:
        return text
    window = text[:limit]
    best_sentence = max(window.rfind(". "), window.rfind("! "), window.rfind("? "))
    if best_sentence >= 100:
        return window[: best_sentence + 1]
    cut = window.rfind(" ")
    if cut < 1:
        cut = limit
    result = window[:cut].rstrip(" ,;:—-")
    if result and result[-1] not in ".!?":
        result += "."
    return result


def upsert(path):
    folder = os.path.basename(os.path.dirname(path))
    fm = frontmatter.load(path)
    slug = os.path.splitext(os.path.basename(path))[0]
    html = md.markdown(fm.content, extensions=["extra", "toc"])

    payload_post = {
        "title": fm["title"],
        "slug": slug,
        "html": html,
        "custom_excerpt": fit_excerpt(fm.get("excerpt")),
        "status": "published",
        "visibility": "public",
        # NOTE: `featured` is intentionally NOT set here. The curated homepage
        # picks ("A cross-section worth your time") are managed OUT of band by
        # the theme repo's set-wiki-featured workflow, not by markdown
        # frontmatter. Forcing featured=false on every upsert wiped all picks
        # on each full sync (2026-07-13). On update we preserve Ghost's current
        # value (set below); on create Ghost defaults to false.
        "custom_template": "custom-wiki-entry",            # GOTCHA 2: or it renders as an article
        "authors": [{"slug": "progress-llm"}],             # all wiki entries attributed to Progress LLM
        "tags": build_tags(fm, folder),
    }

    # Does it already exist?
    r = requests.get(f"{GHOST_URL}/ghost/api/admin/posts/slug/{slug}/", headers=headers())
    if r.status_code == 200:
        existing = r.json()["posts"][0]
        payload_post["updated_at"] = existing["updated_at"]   # required for PUT collision check
        payload_post["featured"] = existing.get("featured", False)  # preserve curated homepage picks
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
    # Filter out any paths outside known wiki content folders (e.g. sources/, scripts/)
    targets = [t for t in targets if t.split("/")[0] in CATEGORY_TAG]
    print(f"Syncing {len(targets)} entr{'y' if len(targets)==1 else 'ies'} to {GHOST_URL}")
    for path in targets:
        upsert(path)

if __name__ == "__main__":
    main()
