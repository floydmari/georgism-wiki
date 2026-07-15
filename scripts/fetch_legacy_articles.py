#!/usr/bin/env python3
"""
fetch_legacy_articles.py — READ-ONLY. Pull every published NON-wiki post from Ghost into a
local JSONL cache for the legacy-article interlinking project (Phase 2).

Each line of the output file is one post:
    {"slug", "id", "url", "title", "tags": [tag slugs], "html", "updated_at", "published_at"}

The cache feeds two consumers:
  * Option 1 (tag audit)  — which articles carry a topic tag usable by the theme's
    "Related on the wiki" box.
  * Option 2 (in-text links) — raw text scan for wiki-term candidates, plus each
    article's EXISTING /wiki/ hrefs so we never propose a duplicate link.

Never writes to Ghost. Output goes to scratchpad/cache/ (gitignored — bulky, reproducible).

Usage:  python3 scripts/fetch_legacy_articles.py [outfile]
"""
import json, os, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jwt, requests
from _secrets import require_ghost

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "scratchpad", "cache", "legacy-articles.jsonl")


def headers():
    key, _ = require_ghost()
    kid, secret = key.split(":")
    iat = int(time.time())
    tok = jwt.encode({"iat": iat, "exp": iat + 300, "aud": "/admin/"},
                     bytes.fromhex(secret), algorithm="HS256",
                     headers={"alg": "HS256", "typ": "JWT", "kid": kid})
    return {"Authorization": f"Ghost {tok}"}


def main():
    _, ghost_url = require_ghost()
    ghost_url = ghost_url.rstrip("/")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    page, kept, skipped_wiki = 1, 0, 0
    with open(OUT, "w") as fh:
        while True:
            r = requests.get(
                f"{ghost_url}/ghost/api/admin/posts/",
                params={"limit": 50, "page": page, "formats": "html",
                        "include": "tags", "filter": "status:published"},
                headers=headers(), timeout=60)
            r.raise_for_status()
            data = r.json()
            for p in data["posts"]:
                tag_slugs = [t["slug"] for t in p.get("tags") or []]
                if "wiki" in tag_slugs:          # wiki entries are not legacy articles
                    skipped_wiki += 1
                    continue
                fh.write(json.dumps({
                    "slug": p["slug"], "id": p["id"], "url": p.get("url"),
                    "title": p.get("title"), "tags": tag_slugs,
                    "html": p.get("html") or "",
                    "updated_at": p.get("updated_at"),
                    "published_at": p.get("published_at"),
                }) + "\n")
                kept += 1
            pg = data["meta"]["pagination"]
            if pg["page"] >= pg["pages"]:
                break
            page += 1
    print(f"kept {kept} legacy articles ({skipped_wiki} wiki posts skipped) -> {OUT}")


if __name__ == "__main__":
    main()
