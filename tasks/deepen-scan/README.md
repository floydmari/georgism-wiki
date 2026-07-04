# Deepen-scan task prompts

One file per `[DEEPEN-SCAN]` item in `BACKLOG.md`. These are **self-contained T2 task prompts**
written to run on a no-web external model (e.g. ollama-cloud GLM) via:

    python3 scripts/llm_worker.py --task tasks/deepen-scan/<task>.md \
        --out <target file> --context <source text file> [--context ...]

Rules baked into every task (per `EDITORIAL.md` + `LOOP.md` external-model section):
- The model may cite ONLY the supplied `--context` material; everything else is
  `[CITATION NEEDED: …]`. Quotes ≤ 50 words. Claim language matched to evidence.
- The orchestrator (T1) supplies the source text as context (fetched or pasted), then reviews:
  verify citations, run `scripts/lint_wiki.py`, wire bidirectional + inbound links, update
  `sources/registry.csv` (Scan Depth Light→Medium/Heavy) and the Google Sheet mirror, commit.

A Claude subagent (Sonnet) can run the same task file directly — it may additionally web-search,
but the same T1 review applies.
