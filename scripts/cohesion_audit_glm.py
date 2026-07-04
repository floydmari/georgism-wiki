#!/usr/bin/env python3
"""Whole-corpus cohesion audit on GLM (Ollama Cloud) — the 1M-context-window play.

Loads the ENTIRE wiki (every page, full text, ~1.5M chars ≈ 350k tokens) into a single GLM
call and asks for a structured cohesion report: contradictions between pages, duplicated
content that should be merged/cross-linked, missing cross-links between pages that discuss
each other's topics, terminology drift, and stub/coverage gaps visible only at whole-corpus
scale. Zero Claude session quota; output is a CANDIDATE report for T1 review (external-model
rule) — this script never edits the wiki.

Usage: python3 scripts/cohesion_audit_glm.py
Output: preview/cohesion_audit.json (+ a readable .md next to it)
"""
import glob, json, os, re, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL = os.environ.get("SWEEP_MODEL", "glm-5.2:cloud")
OLLAMA = os.environ.get("OLLAMA_LOCAL", "http://localhost:11434")
NUM_CTX = int(os.environ.get("AUDIT_NUM_CTX", "1000000"))
CATS = ["concepts", "people", "places", "organizations", "objections", "events", "outcomes",
        "narratives", "research"]

SYSTEM = """You are a whole-corpus cohesion auditor for a Georgism wiki. You receive EVERY page
of the wiki, full text, delimited by '===== PAGE: <path> ====='. Audit the corpus AS A WHOLE and
return STRICT JSON only:
{"contradictions":[{"pages":["path","path"],"issue":"what factually conflicts, quoting the
conflicting phrases briefly","severity":"high|medium|low"}],
 "duplications":[{"pages":["..."],"issue":"substantially same content; merge or cross-link"}],
 "missing_crosslinks":[{"from":"path","to":"path","why":"from-page discusses to-page's exact
topic without linking"}],
 "terminology_drift":[{"term":"...","variants":["..."],"pages":["..."],"fix":"canonical form"}],
 "stale_or_inconsistent_facts":[{"pages":["..."],"issue":"figures/dates that disagree"}],
 "corpus_scale_gaps":[{"gap":"topic multiple pages point at that has no page","evidence":["paths"]}]}
Rules: cite only what is actually in the supplied text (quote short fragments as evidence);
rank each list by importance; max 15 items per list; empty lists are fine. No prose outside JSON."""


def main() -> None:
    parts = []
    for c in CATS:
        for p in sorted(glob.glob(os.path.join(ROOT, c, "*.md"))):
            rel = os.path.relpath(p, ROOT)
            parts.append(f"===== PAGE: {rel} =====\n{open(p).read()}")
    corpus = "\n\n".join(parts)
    print(f"corpus: {len(parts)} pages, {len(corpus):,} chars")
    body = json.dumps({
        "model": MODEL,
        "messages": [{"role": "system", "content": SYSTEM},
                     {"role": "user", "content": corpus + "\n\nProduce the cohesion audit JSON now."}],
        "stream": False,
        "options": {"temperature": 0.2, "num_ctx": NUM_CTX},
    }).encode()
    t0 = time.time()
    req = urllib.request.Request(OLLAMA + "/api/chat", data=body,
                                 headers={"Content-Type": "application/json"})
    r = urllib.request.urlopen(req, timeout=1800)
    d = json.load(r)
    content = d["message"]["content"]
    print(f"elapsed {time.time()-t0:.0f}s · prompt_eval={d.get('prompt_eval_count')} eval={d.get('eval_count')}")
    try:
        report = json.loads(content)
    except Exception:
        m = re.search(r"\{.*\}", content, re.S)
        report = json.loads(m.group(0)) if m else {"raw": content}
    out = os.path.join(ROOT, "preview/cohesion_audit.json")
    json.dump(report, open(out, "w"), indent=1)
    md = [f"# Cohesion audit ({time.strftime('%Y-%m-%d')}) — GLM whole-corpus pass, T1 review required\n"]
    for k, items in report.items():
        md.append(f"\n## {k} ({len(items) if isinstance(items, list) else '?'})\n")
        if isinstance(items, list):
            for it in items:
                md.append(f"- {json.dumps(it, ensure_ascii=False)}")
    open(os.path.join(ROOT, "preview/cohesion_audit.md"), "w").write("\n".join(md))
    print("wrote preview/cohesion_audit.json + .md")
    for k, v in report.items():
        if isinstance(v, list):
            print(f"  {k}: {len(v)}")


if __name__ == "__main__":
    main()
