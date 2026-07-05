#!/usr/bin/env python3
"""
llm_worker.py — run a T2/T3 drafting task on an external model (e.g. ollama-cloud GLM-5.2).

The loop's tiers are roles, not models. Claude subagents can self-lint and web-search; a bare
chat-completions model cannot. This driver adapts for that: it packs the editorial rules + the
task + any reference material into one prompt, forbids invented URLs (the model may only cite
sources given to it in the task context, and must use [CITATION NEEDED] otherwise), writes the
draft to the target file, and leaves lint + web verification + review to the T1 orchestrator.
External-model drafts therefore get a STRICTER T1 review than Claude-subagent drafts.

Config (env):
    LLM_API_KEY     required — bearer token for the endpoint
    LLM_BASE_URL    default https://ollama.com     (ollama-cloud)
    LLM_MODEL       default glm-5.2
    LLM_API_STYLE   ollama (default) → POST {base}/api/chat
                    openai           → POST {base}/v1/chat/completions

Usage:
    python3 scripts/llm_worker.py --task taskfile.md --out narratives/foo.md [--context file ...]
    python3 scripts/llm_worker.py --selftest        # connectivity check, no file writes

Zero non-stdlib dependencies.
"""
import json
import os
import re
import sys
import urllib.request

BASE = os.environ.get("LLM_BASE_URL", "https://ollama.com").rstrip("/")
MODEL = os.environ.get("LLM_MODEL", "glm-5.2")
STYLE = os.environ.get("LLM_API_STYLE", "ollama")
KEY = os.environ.get("LLM_API_KEY")

SYSTEM = """You are a staff writer on the research desk building the definitive, honest
reference on Georgism and land value taxation (progress.org/wiki). Your page will be read by
skeptics as well as supporters — it persuades ONLY by being accurate, well-sourced, and
intellectually fair. Your job on this task: read what you are given about the land question,
mine it fully, and write ONE page that makes the wiki's coverage stronger — the evidence at
its true strength, the counterarguments at theirs. Follow the editorial rules included in
the task. Hard rules:
- NEVER invent a source, quotation, author, year, page number, or URL. You have NO web access:
  you may cite ONLY sources explicitly provided in the task context. For anything else write
  [CITATION NEEDED: <what is needed>]. Overusing [CITATION NEEDED] is fine; fabricating is not.
- Match claim language to evidence strength; avoid 'proves/always/clearly/the only' unless the
  provided source justifies it. Quote at most 50 words from any source.
- Neutral encyclopedic tone; steelman opposing views.
- Output ONLY the complete markdown file content (YAML frontmatter first), no commentary."""


def call(messages):
    if not KEY:
        sys.exit("LLM_API_KEY not set. Add it to the environment (or Emma vault via op).")
    if STYLE == "openai":
        url, payload = f"{BASE}/v1/chat/completions", {"model": MODEL, "messages": messages}
        pick = lambda d: d["choices"][0]["message"]["content"]
    else:
        url, payload = f"{BASE}/api/chat", {"model": MODEL, "messages": messages, "stream": False}
        pick = lambda d: d["message"]["content"]
    req = urllib.request.Request(url, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {KEY}"})
    with urllib.request.urlopen(req, timeout=600) as resp:
        return pick(json.loads(resp.read()))


def main():
    args = sys.argv[1:]
    if "--selftest" in args:
        out = call([{"role": "user", "content": "Reply with exactly: WORKER-OK"}])
        print(f"model={MODEL} base={BASE} style={STYLE} → {out.strip()[:80]}")
        return

    def arg(flag):
        return args[args.index(flag) + 1] if flag in args else None

    task_path, out_path = arg("--task"), arg("--out")
    if not (task_path and out_path):
        sys.exit(__doc__)
    task = open(task_path, encoding="utf-8").read()
    context = ""
    i = 0
    while "--context" in args[i:]:
        i = args.index("--context", i) + 1
        context += f"\n\n--- REFERENCE: {args[i]} ---\n" + open(args[i], encoding="utf-8").read()

    draft = call([{"role": "system", "content": SYSTEM},
                  {"role": "user", "content": task + context}])
    # strip a ```markdown fence if the model added one
    m = re.match(r"^```(?:markdown|md)?\n(.*)\n```\s*$", draft.strip(), re.S)
    if m:
        draft = m.group(1)
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    open(out_path, "w", encoding="utf-8").write(draft.strip() + "\n")
    cn = len(re.findall(r"\[CITATION NEEDED", draft))
    print(f"llm_worker: wrote {out_path} ({len(draft.splitlines())} lines, "
          f"{cn} [CITATION NEEDED]) — requires T1 review + lint before commit")


if __name__ == "__main__":
    main()
