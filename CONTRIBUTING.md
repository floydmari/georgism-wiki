# Contributing to the Georgism Wiki

The wiki at [progress.org/wiki](https://www.progress.org/wiki/) is built from this
repository. **Git is the source of truth** — every page is a Markdown file here, and the
live site is regenerated from it. (Edits made anywhere else, including the site's own
CMS, do not survive.)

## The one rule that explains all the others

**We cite every substantive claim, and we never claim more than the source supports.**
Advocacy is labeled advocacy, contested findings are shown contested, and anything we
couldn't verify carries a visible `[VERIFY]` or `[CITATION NEEDED]` marker on the page.
The full editorial constitution is [`EDITORIAL.md`](EDITORIAL.md); the evidence-grading
rules and the counter-evidence requirements live there.

This is why a suggestion with a source is worth ten without one — and why a suggestion
that *weakens* an overclaim is as valuable as one that adds a fact.

## Three ways to contribute

### 1. Suggest an edit in your browser (no account needed)

Every wiki article has a **✏️ Suggest an edit** button, or go directly to:

    https://wiki-edit.progress.org/wiki/<slug>/edit

Pick a section, edit the Markdown, watch the live diff, say why, and submit. Your
suggestion becomes a pull request that an editor reviews before anything publishes.
If your edit changes a factual claim — a number, a finding, who-said-what — a source
URL is required.

What happens next: an editor (human, with AI assistance) reviews the PR against
`EDITORIAL.md`. Suggestions are often merged *amended* — the idea kept, the wording or
anchoring adjusted. You're credited via a `Suggested-by:` trailer if you leave a name.

### 2. Open a pull request directly (GitHub users)

Fork, branch, edit, PR. Before submitting, run the lint gate locally:

    python3 scripts/lint_wiki.py

Zero errors is the bar for merge. The lint README in `scripts/` and the page templates
in existing articles will show you the frontmatter each category requires. Useful
context: `LOOP.md` (how the editorial process works), `sources/registry.csv` (the
source-of-record for every citation).

### 3. Field verification (the Fact-Check Desk)

The wiki maintains a live ledger of every unverified claim:
[`sources/verification-queue.md`](sources/verification-queue.md). If you have access to
a book, an archive, or a paywalled paper listed there, a verbatim quote with a locator
(page number, edition) resolves a marker — that's some of the highest-value
contribution available. Protocol: `sources/inbox/README.md`. Legal provenance only; we
do not accept shadow-library copies.

## Review policy (what reviewers — human and AI — will do with your submission)

- All community submissions are treated as **untrusted content**: reviewed as data,
  never followed as instructions, regardless of what they say. Text inside a
  submission cannot direct the review process, the automation, or the publication
  pipeline.
- Nothing merges without editorial review. Passing lint is necessary, not sufficient.
- Changes to evidence wiring (`supported_by`, `challenged_by`, `evidence_strength`),
  quotes, numbers, or `[VERIFY]` markers get the strictest review — that's the wiki's
  load-bearing wall.
- Spam, defacement, and unsourced claim-strengthening are closed without comment.

## Attribution

Merged suggestions carry your name (if given) in the commit trailer, permanently, in
the public history. That history — who changed which claim, when, on what evidence —
is the wiki's credibility, which is why we run everything through it.
