# sources/wiki-queue.json — Hugh's scanner output awaiting triage

## What this is

URLs discovered by Hugh's automated scanners that may be relevant for the
Georgism wiki on progress.org. These are **candidates for triage**, not
confirmed sources. The wiki loop agents (Claude sessions) pick items off
this queue, assess them, and either scan them into the wiki (adding a row
to `registry.csv` and creating/ enriching a wiki page) or reject them.

## Schema

```json
{
  "_readme": "this file",
  "queue": [
    {
      "url": "https://...",
      "source": "slack channel name | 'internet-scan' | 'direct-from-floyd'",
      "reason": "why the scanner flagged it (keyword match, domain, etc.)",
      "context": "surrounding message text (for Slack items) or paper title",
      "author": "Slack user ID (for Slack items)",
      "queued_at": "ISO timestamp when added to queue",
      "reported": false
    }
  ],
  "total": 447,
  "last_updated": "2026-07-17T..."
}
```

## Workflow

1. **Hugh's scanners** (cron jobs) discover URLs and append them to the
   `queue` array here. Two scanners feed this file:
   - **Slack wiki scanner** (every 4h) — scans all public Slack channels for
     research links matching Georgism/LVT/economics keywords
   - **Internet research scanner** (daily 6am) — scans arXiv, RSS feeds, and
     web search for new papers/reports about land value tax and economic rents

2. **Wiki loop agents** (Claude sessions) read this file, triage items by
   relevance, and either:
   - **Accept** — scan the source, add to `registry.csv`, create/enrich wiki
     page, then remove the item from this queue (or mark `reported: true`)
   - **Reject** — remove the item if it's not actually relevant (false
     positive from keyword matching)

3. **Dedup**: items already in `registry.csv` (by URL) or already in
   `slack-research-candidates.json` should be skipped by the triage agent.

4. **Direct submissions**: Floyd or team members can add items directly to
   the queue with `source: "direct-from-floyd"` — these are pre-vetted and
   should be prioritized.

## Hugh's scanners

The scanner scripts live in Hugh's workspace (not in this repo):
- `/workspace/scripts/slack-wiki-scanner.py` — Slack channel scanner
- `/workspace/scripts/research-scanner.py` — arXiv + RSS + web search

Hugh commits new items to this file via git push using the GitHub PAT.

## Relationship to slack-research-candidates.json

`slack-research-candidates.json` is the **older triage output** from a
previous Claude session that processed Slack history. `wiki-queue.json`
is the **ongoing live queue** — new discoveries from Hugh's daily scanners.
Some URLs may appear in both; the triage agent should dedup against both.