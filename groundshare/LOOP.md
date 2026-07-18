# groundshare/LOOP.md — The Groundshare Development Loop

## What this loop builds

**Groundshare** — the movement name (Sean Platt, MMT Nemacolin 2026) for Floyd
Marinescu's predistributive land-rent-sharing proposal — developed here until it is a
**credible and complete policy package**: quantified for Canada, mechanically specified,
morally argued, steelmanned against its best objections, narratively packaged, and
carried by a campaign site that is honest about what is proven and what is not.

This loop is **separate from the wiki loop** (`/LOOP.md`). Hard rules:

1. Everything lives in `groundshare/` — never in the wiki's category folders.
2. **Never sync any of it to Ghost.** It is not wiki content until Floyd says so.
3. Wiki pages may be *read* freely (the evidence base) and linked by URL, but not edited
   from this loop except on Floyd's instruction.
4. EDITORIAL.md's honesty rules apply in full: no fabricated sources, claim-strength
   language matched to evidence, advocacy labeled as advocacy. A campaign that claims
   to be building academic proof gets audited harder, not softer.

## Definition of done (the package)

- [ ] **Estimate** — Canada numbers on current StatCan data with a real distributional
      cut (not illustrative deciles), per-resident and per-adult designs, provincial
      splits, and a stated sensitivity range.
- [ ] **Mechanism spec** — attribution (persons vs entities), allowance design, rate
      choice and its meaning, assessment machinery, transition path, interaction with
      existing property taxes.
- [ ] **Reflexivity model** — the settlement itself lowers land *prices* (the
      speculative premium dies); model how V̄, the payments, and the schedule co-evolve
      to a stable use-value equilibrium instead of quietly assuming today's prices hold.
- [ ] **Moral case** — the "natural equity" one-pager: Locke's proviso → Paine → George
      → Steiner → Groundshare, in language a non-technical reader takes a stance on.
- [ ] **Objections file** — the strongest attacks (transition shock, asset-rich/
      cash-poor seniors, attribution gaming, "this is confiscation", capitalization
      collapse, federal/provincial jurisdiction), each steelmanned then answered or
      conceded.
- [ ] **Academic path** — the claims that need independent proof, framed as research
      questions; target collaborators/venues; a working-paper skeleton CWC could
      commission or co-author.
- [ ] **Narrative kit** — taglines, the ten-year-old explanation, the yard-sign line,
      the seminar defense; Groundshare voice guide (Sean's naming principles).
- [ ] **Site** — `groundshare/site/index.html` current with all of the above, deployed
      to groundshare.floydm.ca (blocked on Cloudflare credentials — see Deployment).

## The lanes

| Lane | File(s) | What a wave does |
|---|---|---|
| ESTIMATE | `analysis/canada-estimate.md` | Refresh StatCan 36-10-0580-01; mine SFS microdata releases for land-holdings-by-decile; provincial cuts; replace illustrative charts with real distributions. |
| MECHANISM | `proposal.md` §Design Questions → `mechanism.md` when it outgrows | Resolve one open design question per wave, with cited precedent (Detroit credit, Denmark, ACT leasehold, income-tax allowance machinery). |
| MORAL | `moral-case.md` | Draft/harden the natural-equity argument; every claim either philosophical (attributed) or empirical (cited). |
| OBJECTIONS | `objections.md` | Add/steelman one objection per wave *before* answering it; import the wiki's objection pages where they transfer. |
| ACADEMIC | `academic-path.md` | Turn one package claim into a falsifiable research question with data source and method; track outreach candidates. |
| NARRATIVE | `narrative-kit.md` | Iterate copy against Sean's principles ("people share names, not data"; "an idea, not a policy"). |
| SITE | `site/index.html` | Fold the wave's results into the site; keep the honest-limits section as prominent as the promise. |

## One wave (an iteration)

1. `git pull` on branch `claude/land-value-redistribution-8aqnw5`; read this file's
   **State** section below.
2. Pick the highest-leverage open item: an unchecked Definition-of-done box whose lane
   has the least recent progress; lint-style honesty problems in existing drafts outrank
   new drafting.
3. Do ONE lane's work well (research → draft → cite → cross-check against wiki evidence
   pages). Use web search for anything time-sensitive (StatCan releases, CWC updates).
4. Update the **State** table and the Definition-of-done checkboxes; append one line to
   the **Wave log**.
5. Rebuild the site if the wave changed anything reader-facing; republish the preview
   artifact; commit and push to the branch.
6. Surface to Floyd only decisions that are genuinely his: naming, scope, publication,
   money, outreach to real people. Everything else, decide and log.

## State

| Lane | Status | Last wave |
|---|---|---|
| ESTIMATE | First pass done from CWC 2023 figures (in `proposal.md`); needs current StatCan + real distribution | 2026-07-18 |
| MECHANISM | Design-questions section drafted; allowance model sketched | 2026-07-17 |
| MORAL | Framing section drafted in `proposal.md`; no standalone one-pager yet | 2026-07-17 |
| OBJECTIONS | Honest-limits section only; no dedicated steelman file yet | 2026-07-17 |
| ACADEMIC | Not started | — |
| NARRATIVE | Sean Platt naming brief captured in `proposal.md` §The Name | 2026-07-18 |
| SITE | v1 built (`site/index.html`); deployment blocked on credentials | 2026-07-18 |

## Wave log

- **2026-07-17/18 (w0, with Floyd live):** mechanism formulated (equal-land-share, the
  no-kink schedule, LVT+dividend equivalence); prior art surveyed (Paine, George,
  Friedman, Steiner, Barnes, CWC, Detroit); moved out of wiki namespace into this
  workspace on Floyd's ruling; Canada first-pass estimate from CWC-verified figures;
  Groundshare naming brief captured; site v1 + interactive model built; loop designed.

## Deployment (blocked — needs Floyd)

Target: **groundshare.floydm.ca** (fallback: floydm.ca/groundshare). floydm.ca is on
Cloudflare behind Cloudflare Access (team `fclaw`); `groundshare` subdomain does not
exist yet. The session vault currently provisions only the progress.org Ghost key.
Unblock options (any one):

1. Add a **Cloudflare API token** to the Emma vault (permissions: Pages:Edit +
   DNS:Edit for floydm.ca) — the loop can then create a Pages project, deploy
   `site/`, and add the DNS record. Extend `.claude/hooks/session-start.sh` to export
   it like the Ghost key.
2. Give SSH/deploy access to the origin server behind floydm.ca.
3. Floyd deploys manually: `site/index.html` is a single self-contained file — copy it
   anywhere (Cloudflare Pages drag-and-drop works) and point the subdomain at it.

Until unblocked, the site is previewable as the session's Claude artifact (private to
Floyd's account unless he shares it).
