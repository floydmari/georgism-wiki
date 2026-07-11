#!/usr/bin/env python3
"""
sync_tag_descriptions.py — Set the description on each wiki category tag in Ghost.

The /wiki/category/<name>/ pages are Ghost tag archives: the theme renders the tag's
`description` under the category title, and Ghost uses it as the page's meta description.
Ghost caps tag descriptions at 500 characters.

DESCRIPTIONS below is the canonical copy, keyed by repo folder (same keys as
CATEGORY_TAG in sync_to_ghost.py). Edit here, then re-run — idempotent upsert.

Usage:
    python3 scripts/sync_tag_descriptions.py            # apply all
    python3 scripts/sync_tag_descriptions.py --dry-run  # show what would change

Requires the same credentials as sync_to_ghost.py (GHOST_ADMIN_KEY env or 1Password
via OP_SERVICE_ACCOUNT_TOKEN).
"""
import os, sys, time

import jwt
import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sync_to_ghost import TAG_IDS, CATEGORY_TAG, GHOST_URL, KEY_ID, SECRET

# Canonical category descriptions, keyed by repo folder. Keep each under ~300 chars
# (Ghost caps at 500): the theme shows this under the category title and search
# engines use it as the page's meta description.
DESCRIPTIONS = {
    "concepts": (
        "The building blocks of Geoism — economic rent, land value, and the mechanics of "
        "capturing publicly created value. Start here to get the vocabulary the rest of the "
        "wiki relies on."
    ),
    "people": (
        "Economists, reformers, and critics who shaped — or fought — the idea of capturing "
        "economic rent for the public, from the Physiocrats and Henry George to modern "
        "researchers on both sides."
    ),
    "places": (
        "Where land value capture has actually been tried: cities, regions, and countries, "
        "with honest accounts of what worked, what didn't, and what remains disputed."
    ),
    "events": (
        "Land booms, busts, panics, reform campaigns, and turning points — the historical "
        "episodes that test the theory against the record."
    ),
    "problems": (
        "Claims about what goes wrong when economic rent is privately captured — unaffordable "
        "housing, speculation, inequality, distorted investment — each stated precisely and "
        "graded by the strength of its evidence."
    ),
    "benefits": (
        "Claims about what improves when rent is captured for the public — more construction, "
        "better affordability, less speculation — each stated precisely and graded by the "
        "strength of its evidence, including where it is confounded."
    ),
    "research": (
        "The evidence base: academic papers, reports, and empirical studies on land, rent, and "
        "taxation, summarized with their findings, methods, and limits."
    ),
    "organizations": (
        "Institutes, campaigns, schools, and advocacy groups working on land value taxation "
        "and rent capture, past and present."
    ),
    "objections": (
        "The strongest arguments against land value taxation and Geoism — steelmanned first, "
        "then answered, with an honest net assessment of where each objection stands."
    ),
    "narratives": (
        "Recurring stories and framings in the land debate — from \"this time is different\" to "
        "\"landowners deserve the gains\" — examined against the evidence."
    ),
    "books": (
        "Book-length treatments of land, rent, and the Georgist tradition, summarized with "
        "what each contributes to the evidence base and where each is contested."
    ),
    "texts": (
        "Primary sources: the historical texts of the land question, from Paine and George "
        "onward, presented with context on what they argue and how they were received."
    ),
}


def headers():
    iat = int(time.time())
    token = jwt.encode({"iat": iat, "exp": iat + 300, "aud": "/admin/"},
                       bytes.fromhex(SECRET), algorithm="HS256",
                       headers={"alg": "HS256", "typ": "JWT", "kid": KEY_ID})
    return {"Authorization": f"Ghost {token}", "Content-Type": "application/json"}


def main():
    dry = "--dry-run" in sys.argv
    changed, same, failed = [], [], []
    for folder, desc in DESCRIPTIONS.items():
        tag_slug = CATEGORY_TAG.get(folder)
        tag_id = TAG_IDS.get(tag_slug)
        if not tag_id:
            failed.append((folder, f"no tag id for {tag_slug}")); continue
        if len(desc) > 500:
            failed.append((folder, f"description too long ({len(desc)} > 500)")); continue
        url = f"{GHOST_URL}/ghost/api/admin/tags/{tag_id}/"
        r = requests.get(url, headers=headers(), timeout=30)
        if r.status_code != 200:
            failed.append((folder, f"GET {r.status_code}: {r.text[:120]}")); continue
        tag = r.json()["tags"][0]
        if (tag.get("description") or "").strip() == desc.strip():
            same.append(folder); continue
        if dry:
            changed.append(folder)
            print(f"[dry-run] {folder} ({tag_slug}):\n  old: {tag.get('description')!r}\n  new: {desc!r}")
            continue
        payload = {"tags": [{"description": desc, "updated_at": tag["updated_at"]}]}
        r = requests.put(url, json=payload, headers=headers(), timeout=30)
        if r.status_code == 200:
            changed.append(folder)
        else:
            failed.append((folder, f"PUT {r.status_code}: {r.text[:120]}"))
    print(f"UPDATED ({len(changed)}): {', '.join(changed)}")
    print(f"UNCHANGED ({len(same)}): {', '.join(same)}")
    if failed:
        print(f"FAILED ({len(failed)}):")
        for f, why in failed:
            print(f"  {f}: {why}")
        sys.exit(1)


if __name__ == "__main__":
    main()
