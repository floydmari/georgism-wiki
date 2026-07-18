#!/usr/bin/env python3
"""
apply_intext_links.py — Option 2 APPLY step (writes to Ghost; run only after Floyd approves
the manifest rendered by render_intext_manifest.py).

Method = the proven 2026-07-12 top-100 technique (BACKLOG "Phase 2 status"): lexical
link-node surgery. Never uses ?source=html (card-corruption risk); posts whose lexical is
null (pre-2021 HTML-only imports) are SKIPPED and reported — the theme's "From the Georgism
Wiki" box covers those.

Per post:
  1. GET  formats=lexical; skip if lexical null; snapshot original to cache/apply-backups/.
  2. For each approved (phrase -> target): find the FIRST plain text node inside a
     paragraph (never headings/quotes/links) containing the exact matched string, split it
     into [before][link][after], mirroring the link-node schema of real posts
     (rel=noopener, absolute https://www.progress.org/wiki/<slug>/ URL — matches the
     top-100 wave).
  3. Skip any target the live post already links (re-checked at apply time, not just at
     manifest time).
  4. PUT lexical (no source param) with the fetched updated_at (conflict guard).
  5. VERIFY: re-GET html; plain text (tags stripped) must be byte-identical to the
     original's plain text, and every applied target must appear as a href. On any
     mismatch: restore the snapshot lexical immediately and log the drift.
  6. Append applied links to sources/interlink-ledger.jsonl (the long-term record).

Usage:
  python3 scripts/apply_intext_links.py --pilot 5          # first N articles only
  python3 scripts/apply_intext_links.py --slugs a b c      # specific articles
  python3 scripts/apply_intext_links.py --all              # full approved set
"""
import argparse, copy, html as htmllib, json, os, re, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jwt, requests
from _secrets import require_ghost

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "scratchpad", "cache")
MERGED = os.path.join(CACHE, "intext_pruned_merged.json")
BACKUPS = os.path.join(CACHE, "apply-backups")
LEDGER = os.path.join(ROOT, "sources", "interlink-ledger.jsonl")

TEXT_TYPES = {"text", "extended-text"}
SKIP_PARENTS = {"link", "extended-quote", "quote", "extended-heading", "heading"}


def headers():
    key, _ = require_ghost()
    kid, sec = key.split(":")
    iat = int(time.time())
    tok = jwt.encode({"iat": iat, "exp": iat + 300, "aud": "/admin/"},
                     bytes.fromhex(sec), algorithm="HS256",
                     headers={"alg": "HS256", "typ": "JWT", "kid": kid})
    return {"Authorization": f"Ghost {tok}"}


def plain_text(html_body):
    t = re.sub(r"<[^>]+>", "", html_body or "")
    return re.sub(r"\s+", " ", htmllib.unescape(t)).strip()


def make_link_node(text, fmt, slug):
    return {
        "children": [{"detail": 0, "format": fmt, "mode": "normal", "style": "",
                      "text": text, "type": "extended-text", "version": 1}],
        "direction": None, "format": "", "indent": 0, "type": "link", "version": 1,
        "rel": "noopener", "target": None, "title": None,
        "url": f"https://www.progress.org/wiki/{slug}/",
    }


def try_link_phrase(node, phrase, slug, parent_type="root"):
    """DFS; splice the first eligible text node containing phrase. True if spliced."""
    if not isinstance(node, dict):
        return False
    ntype = node.get("type")
    if ntype in SKIP_PARENTS:
        return False
    kids = node.get("children")
    if not isinstance(kids, list):
        return False
    for i, ch in enumerate(kids):
        if (isinstance(ch, dict) and ch.get("type") in TEXT_TYPES
                and ch.get("mode", "normal") == "normal"
                and ntype in ("paragraph", "listitem")):
            text = ch.get("text") or ""
            j = text.find(phrase)
            if j >= 0:
                fmt = ch.get("format", 0)
                pieces = []
                if j > 0:
                    pre = copy.deepcopy(ch); pre["text"] = text[:j]; pieces.append(pre)
                pieces.append(make_link_node(phrase, fmt, slug))
                if j + len(phrase) < len(text):
                    post = copy.deepcopy(ch); post["text"] = text[j + len(phrase):]
                    pieces.append(post)
                kids[i:i + 1] = pieces
                return True
        if try_link_phrase(ch, phrase, slug, ntype):
            return True
    return False


def existing_slugs(html_body):
    return set(re.findall(r'href="[^"]*?/wiki/([a-z0-9-]+)/?["#?]', html_body or ""))


def try_link_phrase_mobiledoc(doc, phrase, slug):
    """Mobiledoc path for pre-2021 posts (lexical null). Sections are
    [1, "p"|..., [markers]]; markers are [type, openMarkupIdxs, closes, text].
    We only splice PLAIN text markers (type 0, no open markups) inside "p"
    sections, and never touch cards/atoms — the closes count moves to the last
    piece so any enclosing markup still closes in the right place."""
    markups = doc.setdefault("markups", [])
    marker_lists = []
    for sec in doc.get("sections", []):
        if isinstance(sec, list) and len(sec) >= 3 and sec[0] == 1 and sec[1] == "p":
            marker_lists.append(sec[2])
        elif isinstance(sec, list) and len(sec) >= 3 and sec[0] == 3:   # ul/ol lists
            marker_lists.extend(m for m in sec[2] if isinstance(m, list))
    for markers in marker_lists:
        for i, mk in enumerate(markers):
            if not (isinstance(mk, list) and len(mk) == 4 and mk[0] == 0):
                continue
            opens, closes, text = mk[1], mk[2], mk[3] or ""
            # Case A: plain run. Case B: self-contained formatting (marker opens N
            # markups and closes all N itself, none of them links) — split re-wraps
            # each piece in the same markups so styling survives. Anything else
            # (markups spanning multiple markers, existing links) stays untouched.
            self_contained = (opens and closes == len(opens)
                              and all(markups[x][0] != "a" for x in opens))
            if opens and not self_contained:
                continue
            j = text.find(phrase)
            if j < 0:
                continue
            markups.append(["a", ["href", f"https://www.progress.org/wiki/{slug}/",
                                  "rel", "noopener"]])
            midx = len(markups) - 1
            pieces = []
            if j > 0:
                pieces.append([0, list(opens), len(opens) if opens else 0, text[:j]])
            pieces.append([0, list(opens) + [midx], (len(opens) + 1) if opens else 1,
                           phrase])
            tail = text[j + len(phrase):]
            if tail:
                pieces.append([0, list(opens), closes if opens else 0, tail])
            elif not opens:
                pieces[-1][2] += closes          # keep enclosing closes intact
            markers[i:i + 1] = pieces
            return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pilot", type=int)
    ap.add_argument("--slugs", nargs="*")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()

    merged = json.load(open(MERGED))
    work = [(s, c) for s, c in merged.items() if c]
    if args.slugs:
        work = [(s, c) for s, c in work if s in set(args.slugs)]
    elif args.pilot:
        work = work[: args.pilot]
    elif not args.all:
        sys.exit("choose --pilot N, --slugs ..., or --all")

    _, gurl = require_ghost(); gurl = gurl.rstrip("/")
    os.makedirs(BACKUPS, exist_ok=True)
    stats = {"applied": 0, "posts": 0, "skipped_html_only": [], "drift_restored": [],
             "already_linked": 0, "phrase_not_found": 0, "errors": []}

    for slug, cands in work:
        try:
            r = requests.get(f"{gurl}/ghost/api/admin/posts/slug/{slug}/",
                             params={"formats": "lexical,mobiledoc,html"},
                             headers=headers(), timeout=60)
            if r.status_code != 200:
                stats["errors"].append(f"{slug}: GET {r.status_code}"); continue
            post = r.json()["posts"][0]
            mode = "lexical" if post.get("lexical") else (
                "mobiledoc" if post.get("mobiledoc") else None)
            if mode is None:
                stats["skipped_html_only"].append(slug); continue

            orig_doc = post[mode]
            orig_plain = plain_text(post.get("html"))
            live = existing_slugs(post.get("html"))
            doc = json.loads(orig_doc)

            applied_here = []
            for c in cands:
                tslug = c["target"].split("/", 1)[1]
                if tslug in live:
                    stats["already_linked"] += 1; continue
                hit = (try_link_phrase(doc["root"], c["matched"], tslug, "root")
                       if mode == "lexical"
                       else try_link_phrase_mobiledoc(doc, c["matched"], tslug))
                if hit:
                    applied_here.append((c["matched"], tslug)); live.add(tslug)
                else:
                    stats["phrase_not_found"] += 1
            if not applied_here:
                continue

            open(os.path.join(BACKUPS, f"{slug}.json"), "w").write(orig_doc)
            pr = requests.put(f"{gurl}/ghost/api/admin/posts/{post['id']}/",
                              json={"posts": [{mode: json.dumps(doc),
                                               "updated_at": post["updated_at"]}]},
                              headers=headers(), timeout=60)
            if pr.status_code != 200:
                stats["errors"].append(f"{slug}: PUT {pr.status_code} {pr.text[:100]}"); continue

            vr = requests.get(f"{gurl}/ghost/api/admin/posts/{post['id']}/",
                              params={"formats": "html"}, headers=headers(), timeout=60)
            vpost = vr.json()["posts"][0]
            new_plain = plain_text(vpost.get("html"))
            new_slugs = existing_slugs(vpost.get("html"))
            ok = (new_plain == orig_plain and
                  all(t in new_slugs for _, t in applied_here))
            if not ok:
                requests.put(f"{gurl}/ghost/api/admin/posts/{post['id']}/",
                             json={"posts": [{mode: orig_doc,
                                              "updated_at": vpost["updated_at"]}]},
                             headers=headers(), timeout=60)
                stats["drift_restored"].append(slug)
                print(f"  ❌ DRIFT {slug} — restored original")
                continue

            stats["posts"] += 1; stats["applied"] += len(applied_here)
            with open(LEDGER, "a") as lf:
                for phrase, tslug in applied_here:
                    lf.write(json.dumps({"date": time.strftime("%Y-%m-%d"), "article": slug,
                                         "phrase": phrase, "wiki": tslug,
                                         "method": f"{mode}-surgery"}) + "\n")
            print(f"  ✅ {slug}: +{len(applied_here)} links "
                  f"({', '.join(t for _, t in applied_here)})")
            time.sleep(0.4)
        except Exception as e:
            stats["errors"].append(f"{slug}: {e}")

    print(json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in stats.items()},
                     indent=1))
    if stats["skipped_html_only"]:
        print("HTML-only (skipped):", " ".join(stats["skipped_html_only"][:20]),
              "..." if len(stats["skipped_html_only"]) > 20 else "")
    for e in stats["errors"][:10]:
        print("ERR:", e)
    for d in stats["drift_restored"]:
        print("DRIFT:", d)


if __name__ == "__main__":
    main()
