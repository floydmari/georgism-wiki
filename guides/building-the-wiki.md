---
title: "How This Wiki Was Built"
category: guides
tags: [guides, meta, methodology, ai, process, transparency]
stub: false
excerpt: "This wiki was written by AI agents running in loops under human editorial direction — a research desk staffed by models, governed by a written constitution, and gated by one person's judgment. Here is exactly how it works: the loop, the roles, the rules that keep it honest, and where the human sits."
last_reviewed: 2026-07-15
---

## What you're looking at

The progress.org wiki is a verified evidence reference on Geoism — land value taxation and the broader capture of economic rent. As of this writing it is **836 pages**: 313 research summaries, 133 people, 118 concepts, 51 historical events, 40 places, 37 steelmanned objections, and the problem/benefit claim pages the evidence is wired into.

It was **written by AI agents running in loops, under the editorial direction of one person.** Not generated in a single pass — grown, over hundreds of iterations, the way a research desk grows a beat. This page explains the machinery honestly, because a reference that asks you to trust its method should show you the method.

The short version: a **written constitution** defines what a good page is; **loops** of AI agents find sources, read them, write pages, and cross-check each other against that constitution; a **human editor** sets the priorities, makes the judgment calls, and is the sole gate to the published site. The result is checked by scripts on every change and published through an automated pipeline.

## The loop

The wiki grows the way a newsroom works a story, in five repeating moves:

1. **Find** the literature — the papers, books, and people that bear on the land question. What's been found is tracked in a reading list (**1,106 sources** logged so far).
2. **Read and mine** each source — write its research page, and pull out *every* finding, figure, person, and counter-argument it contains. A source isn't done when it's summarized; it's done when everything it teaches has a home on the wiki.
3. **Synthesize** what the sources collectively show into the argument pages — the problems, the benefits, and the objections.
4. **Verify** relentlessly — every claim the wiki couldn't confirm carries a visible unverified-claim flag until someone works it down.
5. **Expand** — reading keeps surfacing new topics worth covering; the best-connected ones become pages.

Each pass through the loop is a **wave**. There have been **167 loop-wave commits** across **649 commits** total. A wave picks a lane — reinforce the problem claims, answer the objections, sweep the dead links, deepen the thin pages — does the work, checks it, and records what it changed and what it left undone.

## The roles: a desk staffed by models

Work is tiered, the way an editorial desk is — and the tiers are *editorial roles*, not just model sizes:

- **T1 — the editor** (a frontier model). Judgment calls: what the evidence collectively justifies, whether a page's wording matches its source's strength, review of everyone else's drafts. **T1 is the sole gate to the published site.**
- **T2 — the staff writers** (mid-tier models). Research and draft pages against vetted sources and templates.
- **T3 — the copy desk** (fast, cheap models). Scan sources, wire cross-links, keep the checks green.

For big jobs the desk **fans out**: a dozen agents run in parallel, each owning an exclusive set of files so they never collide, each returning its proposed changes to a coordinator that harvests them centrally, re-checks, and commits once. A single enrichment wave might launch three agents over the 37 objection pages, or twelve over a batch of articles — then one editor pass reconciles the lot. When the work is mechanical, it goes to the cheapest capable model; when it needs judgment, it waits for T1.

## The constitution that keeps it honest

None of this would be trustworthy without a rule the loop can't talk itself out of. So the repository carries an **editorial constitution** — a single file every agent must read before it writes. Its load-bearing rules:

- **Persuade by being accurate, never by asserting the conclusion.** A reader who disagrees should be able to see that their strongest objection was understood, sourced, and answered. This is why every objection page *steelmans* the criticism from its best source before replying, and concedes — out loud — wherever the criticism has real force.
- **Classify every substantive sentence** by what kind of claim it is (measured finding, historical fact, theoretical prediction, interpretation, advocacy) and **match the language to the strength of the evidence.** "Proven" and "suggests" are not interchangeable.
- **Never fabricate.** An unverified fact gets a visible in-text flag reading *verify* — not a confident guess. Quotes are transcribed word-for-word against the primary source or they don't get quotation marks.
- **One finding, one home, many links.** A result lives on one page and is linked from everywhere it's relevant, rather than being restated (and subtly drifting) across a dozen pages.
- **The rent gradient — the honesty rule that matters most here.** Land is the *clean* case: fixed supply, no incentive to damage, a century of evidence. Every step away from land — resource, monopoly, innovation, platform rents — is more contested. The airtight land case is *not allowed* to lend its certainty to the contested frontier. Pages carry that gradient explicitly.

Two automated checks enforce the mechanical half of this on every change: a **linter** that fails the build if a page misrepresents itself (an evidence slug with no backing link, a claim page with no counter-evidence, an unresolved flag), and a **census** that tracks every page's backlinks and flags orphans. A page that breaks the rules doesn't ship.

## Where the human sits

This is the part people get wrong about AI-built work. The models did the writing; a **human did the governing**, and the governing is what makes it a reference rather than a pile of plausible text. The editor's job, in practice:

- **Setting the priorities.** The ruling that the wiki serves the *advocate needing ammunition* first and the *policymaker's staffer* second is a human decision that shaped every guide and page-design choice. So was the ruling that each wave's first duty is to enrich the evidence behind the claims, not to tidy formatting.
- **Making the judgment calls the models defer.** When to split a category, whether a contested frontier claim can be made at all, which of two framings is honest — these come back to the editor, by design.
- **Guarding the gates.** Nothing merges to the main record, and nothing publishes to the live site, without an explicit human go-ahead. The loop can run all night; it cannot publish itself.
- **Catching the contradictions.** When a mid-stream instruction conflicts with an established rule, the agents are told to *surface it in the moment* rather than silently comply — and the editor rules on it. That standing tension between "do what I just said" and "protect the corpus's integrity" is resolved by a person, not a model.

The cadence that produced this was blunt and effective: *"keep looping,"* the editor would say, and the desk would run waves through the night — enriching claims, answering objections, fixing link-rot — and report each morning what it had done, what it had verified, and what it had honestly failed to verify. Then a human decided what to merge and publish.

## The pipeline

Every page is a Markdown file with structured front-matter, in one Git repository. On each change: the linter and census run; the evidence dashboard regenerates itself from the claim pages; and — on a human's word — a publish script upserts the changed pages to the live site through its content API, matched exactly so the public wiki contains precisely what the repository holds and nothing it doesn't. The site's look is a **separate** repository that deploys itself on merge. It is boring, reproducible plumbing, which is the point.

## The honest limits

Because the method is the argument, the method's limits belong on the page too:

- **Some sources remain unverified,** and say so — where a primary text is paywalled or a copy couldn't be obtained, the page states that it relied on a secondary account rather than pretending otherwise. A running backlog tracks what's still owed.
- **The frontier is contested,** and the wiki marks it. The land case is strong; the extensions to monopoly, innovation, and platform rents are where honest people disagree, and the pages say which is which.
- **AI wrote it, so it was checked like AI wrote it** — verbatim-quote discipline, a linter that fails on self-misrepresentation, and a human editor who reads the judgment-heavy pages. The claim isn't that the models were trustworthy; it's that the *system around them* was built not to trust them.

## Could you build one?

Yes — and the ingredients are all here. A written constitution that defines a good page and can't be argued with. A loop that finds, mines, synthesizes, and verifies. Tiered agents that fan out for scale and defer to judgment. Mechanical checks that fail the build on dishonesty. An automated publish pipeline. And — the non-negotiable part — a human who sets the priorities, makes the calls the models can't, and holds the sole key to the front door.

The models are the labour. The constitution and the editor are why you can cite it.

---

**Guides:** [Start Here](/wiki/start-here/) · [How We Verify](/wiki/how-we-verify/) · [Evidence Dashboard](/wiki/evidence-dashboard/) · [The Advocate's Arsenal](/wiki/advocates-arsenal/)
