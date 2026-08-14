# Publish Notification Protocol

## Problem

The loop agent publishes wiki pages to progress.org (Ghost CMS) as part of its
shift. Hugh (the Hermes agent) runs a cron job that reports new and updated
wiki pages to the team's Slack channel — but Hugh detects changes by polling
the Ghost Content API on a schedule (every 48h). This creates a lag of up to
two days between publication and team notification.

## Solution: Signal file in the repo

When the loop agent publishes pages to Ghost (via `scripts/sync_to_ghost.py`
or equivalent), it appends an entry to a signal file in the repo. Hugh's cron
reads this file on each run, reports any unpublished notifications, marks them
as notified, and commits the file back.

This requires no new infrastructure — both agents already share the git repo.

## Signal file

**Path:** `sources/.publish-notify.json`

**Schema:**

```json
{
  "notifications": [
    {
      "slug": "tourek-drc-progressive-property-tax",
      "title": "Does Progressivity Raise Tax Capacity? Experimental Evidence from the D.R. Congo",
      "url": "https://www.progress.org/wiki/tourek-drc-progressive-property-tax/",
      "category": "research",
      "tags": ["Research", "LVT Studies"],
      "action": "published",
      "published_at": "2026-08-14T12:00:00.000Z",
      "notified": false
    },
    {
      "slug": "split-rate-taxation",
      "title": "Split-Rate Taxation",
      "url": "https://www.progress.org/wiki/split-rate-taxation/",
      "category": "concepts",
      "tags": ["Concepts"],
      "action": "updated",
      "published_at": "2026-08-14T12:30:00.000Z",
      "notified": false
    }
  ]
}
```

### Field reference

| Field | Type | Description |
|-------|------|-------------|
| `slug` | string | Ghost post slug (matches the markdown filename) |
| `title` | string | Full page title |
| `url` | string | Full URL on progress.org |
| `category` | string | Repo directory: `research`, `concepts`, `people`, `places`, etc. |
| `tags` | string[] | Ghost tags (excluding the `wiki` primary tag) |
| `action` | `"published"` \| `"updated"` | New page vs. existing page updated |
| `published_at` | string (ISO 8601) | Ghost `published_at` or `updated_at` timestamp |
| `notified` | boolean | `false` when the loop agent adds it; Hugh flips to `true` after reporting |

## Loop agent responsibilities

At the end of any shift that runs `scripts/sync_to_ghost.py` (or otherwise
publishes or updates pages on Ghost):

1. **Append to `sources/.publish-notify.json`** — one notification object per
   page, with `notified: false`. If the file doesn't exist, create it with the
   schema above. If it exists, append to the `notifications` array.
2. **Commit and push** the signal file in the same commit as the publish action
   (or the immediately following commit). The file path starts with a `.` so it
   won't clutter the directory listing.
3. **Dedup check** — before appending, check if a notification for the same
   slug with `notified: false` already exists. If so, update its `published_at`
   rather than adding a duplicate.

### Example loop agent code

```python
import json
from pathlib import Path

NOTIFY_FILE = Path("sources/.publish-notify.json")

def notify_publish(pages):
    """Call after sync_to_ghost.py publishes pages.
    
    pages: list of dicts with keys: slug, title, url, category, tags, action, published_at
    """
    if NOTIFY_FILE.exists():
        data = json.loads(NOTIFY_FILE.read_text())
    else:
        data = {"notifications": []}
    
    existing = {n["slug"]: n for n in data["notifications"] if not n.get("notified")}
    
    for page in pages:
        if page["slug"] in existing:
            # Update existing unnotified entry
            existing[page["slug"]].update({
                "published_at": page["published_at"],
                "action": page["action"],
            })
        else:
            data["notifications"].append({
                **page,
                "notified": False,
            })
    
    NOTIFY_FILE.write_text(json.dumps(data, indent=2))
```

## Hugh (Hermes) responsibilities

Hugh's `wiki-published-report.sh` cron (or its successor) runs on schedule and:

1. **`git pull`** to get the latest signal file.
2. **Read `sources/.publish-notify.json`** — filter for `notified: false`.
3. **If there are unnotified entries:** format a Slack report (grouped by
   new vs. updated, with titles and URLs) and post it to the team channel.
4. **Flip `notified: true`** for all reported entries.
5. **Commit and push** the updated signal file.

Hugh's existing Ghost Content API polling (`wiki-published-report.sh`) remains
as a **fallback safety net** — it catches pages published without a signal file
(e.g. manual Ghost edits by trusted admins per `CONTRIBUTING.md`). The signal
file is the primary channel; the API poll is the backup.

## Integration with LOOP.md

This protocol is referenced in LOOP.md §"Related loops" as the notification
mechanism between the loop agent and Hugh's Slack reporting. The loop agent's
publish step (currently step 11: "Publishing is not the loop's job") should be
updated to include the notification append as a sub-step when the agent does
publish.

## File lifecycle

```
Loop agent publishes to Ghost
  → appends to sources/.publish-notify.json (notified: false)
  → commits + pushes

Hugh cron wakes (every 48h or on-demand)
  → git pull
  → reads sources/.publish-notify.json
  → filters notified: false
  → formats + posts Slack report
  → flips notified: true
  → commits + pushes

Periodic cleanup (Hugh):
  → notifications with notified: true older than 30 days are pruned
  → prevents the file from growing unbounded
```