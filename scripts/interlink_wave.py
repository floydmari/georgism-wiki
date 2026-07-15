#!/usr/bin/env python3
"""
interlink_wave.py — standing maintenance orchestrator for legacy-article interlinking.
Run this whenever new articles have been published (or let the monthly Routine run it).
It PREPARES a review manifest for articles not yet processed; it never writes to Ghost.

Pipeline per wave:
  1. Fresh read-only fetch of all non-wiki posts (fetch_legacy_articles.py).
  2. Select NEW articles: not in sources/interlink-scanned.txt (the processed ledger).
  3. Option-2 candidates: build_intext_manifest.py (deterministic dictionary scan,
     restricted to the new slugs), then GLM keep/drop pruning on Ollama Cloud (same
     rules the 2026-07-14 Haiku pass used).
  4. Option-3 candidates: build_concept_manifest.py --slugs (GLM conceptual mappings).
  5. Render ONE combined review manifest: scratchpad/interlink-wave-<date>.md.
  6. Append the new slugs to sources/interlink-scanned.txt (so the next wave skips them).

APPLY (after Floyd approves the manifest — never before):
  python3 scripts/apply_intext_links.py --slugs <approved slugs>   # option-2 links
  (option-3 conceptual links: apply with the same script once the anchor phrases are
   approved — they use the identical lexical-surgery path via the merged JSON.)

Requires: GHOST_ADMIN_KEY (or op fallback), OLLAMA_API_KEY.
Usage: python3 scripts/interlink_wave.py [--dry-run]
"""
import json, os, re, subprocess, sys, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "scratchpad", "cache")
SCANNED = os.path.join(ROOT, "sources", "interlink-scanned.txt")
MODEL = os.environ.get("CONCEPT_MODEL", "glm-4.7")
KEY = os.environ.get("OLLAMA_API_KEY")

PRUNE_PROMPT = """You are pruning candidate hyperlinks for a progress.org article (Georgist economics site).
Candidates (phrase | wiki target | context sentence):
{cands}

KEEP only genuine, editorially valuable links where the phrase is used in the same sense as
the wiki page topic. DROP: wrong sense; byline/credit/footnote/citation/navigation text;
quoted matter; incidental place mentions (keep places only when the article substantively
discusses that place's land/tax/economic policy); generic uses. Keep at most 6.
Reply ONLY JSON: {{"keep": [{{"phrase": "...", "target": "..."}}]}}"""


def sh(cmd):
    print("+", " ".join(cmd)); subprocess.run(cmd, check=True)


def glm(prompt):
    body = json.dumps({"model": MODEL, "stream": False, "think": False,
                       "messages": [{"role": "user", "content": prompt}],
                       "options": {"temperature": 0.1}}).encode()
    req = urllib.request.Request("https://ollama.com/api/chat", data=body, headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {KEY}"})
    content = json.loads(urllib.request.urlopen(req, timeout=600).read())["message"]["content"]
    m = re.search(r"\{.*\}", content, re.S)
    return json.loads(m.group(0)) if m else {"keep": []}


def main():
    dry = "--dry-run" in sys.argv
    if not KEY:
        sys.exit("OLLAMA_API_KEY not set (op read the 'ollama cloud' item)")

    sh([sys.executable, os.path.join(ROOT, "scripts", "fetch_legacy_articles.py")])
    scanned = set()
    if os.path.exists(SCANNED):
        scanned = {l.strip() for l in open(SCANNED) if l.strip()}
    arts = [json.loads(l) for l in open(os.path.join(CACHE, "legacy-articles.jsonl"))]
    new = [a for a in arts if a["slug"] not in scanned]
    print(f"wave: {len(new)} new articles (of {len(arts)} total; {len(scanned)} already processed)")
    if not new:
        print("nothing to do"); return

    sh([sys.executable, os.path.join(ROOT, "scripts", "build_intext_manifest.py")])
    raw = {a["slug"]: a for a in json.load(open(os.path.join(CACHE, "intext_manifest.json")))}

    date = time.strftime("%Y-%m-%d")
    out_md = os.path.join(ROOT, "scratchpad", f"interlink-wave-{date}.md")
    merged_path = os.path.join(CACHE, f"wave-{date}-merged.json")
    merged, L = {}, [f"# Interlink wave {date} — REVIEW COPY (nothing applied)", ""]

    for a in new:
        entry = raw.get(a["slug"])
        L.append(f"### [{a['title']}]({a['url']})")
        kept = []
        if entry and entry["candidates"]:
            cands = "\n".join(f"{c['matched']} | {c['target']} | {c['sentence'][:180]}"
                              for c in entry["candidates"])
            try:
                keep = glm(PRUNE_PROMPT.format(cands=cands)).get("keep", [])
                keyed = {(k.get("phrase", "").lower()) for k in keep if isinstance(k, dict)}
                kept = [c for c in entry["candidates"] if c["matched"].lower() in keyed]
            except Exception as e:
                L.append(f"- (prune failed: {e}; showing raw candidates)")
                kept = entry["candidates"]
        merged[a["slug"]] = kept
        if kept:
            L.append("**In-text links (option 2):**")
            for c in kept:
                s = c["target"].split("/", 1)[1]
                L.append(f"- “{c['matched']}” → /wiki/{s}/ — {c['sentence'][:160]}")
        else:
            L.append("- no in-text candidates")
        L.append("")

    json.dump(merged, open(merged_path, "w"), indent=1)
    L += ["", f"*Apply after approval:* `python3 scripts/apply_intext_links.py --slugs "
          f"{' '.join(s for s, v in merged.items() if v)}`",
          f"*(point apply at {os.path.basename(merged_path)} via MERGED env or copy it over "
          "intext_pruned_merged.json)*", "",
          "**Conceptual mappings (option 3):** run scripts/build_concept_manifest.py for "
          "these slugs and scripts/render_concept_manifest.py, review the same way."]
    open(out_md, "w").write("\n".join(L) + "\n")

    if not dry:
        with open(SCANNED, "a") as f:
            for a in new:
                f.write(a["slug"] + "\n")
    print(f"review manifest -> {out_md}  ({'dry-run: scanned list untouched' if dry else 'scanned list updated'})")


if __name__ == "__main__":
    main()
