#!/usr/bin/env python3
"""
pull_from_ghost.py — reverse of sync_to_ghost.py. Fetch a published wiki post from Ghost by slug
and write it back to the repo as a Markdown source file. Use this to RECONCILE drift — pages that
exist live on Ghost but are missing from git — so GitHub remains the complete master record.

Requires the same credentials as sync_to_ghost.py:
    export GHOST_ADMIN_KEY="<key-id>:<hex-secret>"
    export GHOST_URL="https://progress-org.ghost.io"
    pip install PyJWT requests html2text

Usage:
    python3 scripts/pull_from_ghost.py <folder> <slug> [<slug> ...]
    # e.g. reconcile the Common Wealth Canada cluster:
    python3 scripts/pull_from_ghost.py organizations common-wealth-canada
    python3 scripts/pull_from_ghost.py research natural-common-wealth-economic-rent-canada \\
            cwc-distributional-impacts-lvt cwc-lvt-price-reaction-model common-wealth-fund
    python3 scripts/pull_from_ghost.py places british-columbia

It writes <folder>/<slug>.md with reconstructed frontmatter (title, category, tags from Ghost
tags minus wiki/category tags, excerpt, stub:false). REVIEW the result and complete the
frontmatter per EDITORIAL.md before committing — Ghost stores rendered HTML, so the Markdown is a
best-effort round-trip, not a byte-perfect source.
"""
import os, sys, time, re

def _need(mod):
    try:
        return __import__(mod)
    except ImportError:
        sys.exit(f"missing dependency '{mod}'. Run: pip install PyJWT requests html2text")

jwt = _need("jwt"); requests = _need("requests"); html2text = _need("html2text")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def headers():
    GHOST_ADMIN_KEY = os.environ["GHOST_ADMIN_KEY"]
    KEY_ID, SECRET = GHOST_ADMIN_KEY.split(":")
    iat = int(time.time())
    token = jwt.encode({"iat": iat, "exp": iat + 300, "aud": "/admin/"},
                       bytes.fromhex(SECRET), algorithm="HS256",
                       headers={"alg": "HS256", "typ": "JWT", "kid": KEY_ID})
    return {"Authorization": f"Ghost {token}"}


def pull(folder, slug):
    GHOST_URL = os.environ["GHOST_URL"].rstrip("/")
    url = f"{GHOST_URL}/ghost/api/admin/posts/slug/{slug}/?formats=html&include=tags"
    r = requests.get(url, headers=headers())
    if r.status_code != 200:
        print(f"  ❌ {slug}: {r.status_code} {r.text[:120]}")
        return
    post = r.json()["posts"][0]
    body_md = html2text.html2text(post.get("html") or "")
    tags = [t["slug"] for t in post.get("tags", [])
            if t["slug"] not in ("wiki",) and not t["slug"].startswith("wiki-")]
    excerpt = (post.get("custom_excerpt") or "").replace('"', "'")
    title = post["title"].replace('"', "'")
    fm = (f"---\ntitle: \"{title}\"\ncategory: {folder}\n"
          f"tags: [{', '.join(tags) if tags else folder}]\nstub: false\n"
          f"excerpt: \"{excerpt}\"\n---\n\n")
    out_dir = os.path.join(ROOT, folder)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"{slug}.md")
    open(path, "w", encoding="utf-8").write(fm + body_md.strip() + "\n")
    print(f"  ✅ wrote {os.path.relpath(path, ROOT)} — REVIEW frontmatter/citations before commit")


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    folder, slugs = sys.argv[1], sys.argv[2:]
    for slug in slugs:
        pull(folder, slug)


if __name__ == "__main__":
    main()
