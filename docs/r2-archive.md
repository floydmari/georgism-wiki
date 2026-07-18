# archive.progress.org — R2 archive runbook

*Created 2026-07-16 (Floyd's directive). Two-bucket design:*

| bucket | visibility | serves | contents |
|---|---|---|---|
| `progress-archive` | PUBLIC via **archive.progress.org** | citations, readers | `gaffney/…` (193-file masongaffney.org mirror — webmaster permission, Gaffney d. 2020) + `files/…` (future permissioned/PD hosting) |
| `wiki-source-archive` | PRIVATE | editors only | `sources/<sha2>/<sha256>.pdf` — preservation copies of every reachable registry PDF (copyrighted: archive-not-serve; citations keep pointing at publishers, this is the link-rot fallback) |

Credentials: 1Password item **"R2 API Token - Progress.org"** (Floyd updates it with the new
R2-native token; field labels must stay: `Token Value`, `S3 Client Access Key ID`,
`S3 Client Secret Access Key`, `Jurisdiction Specific Endpoint (default)`).

## Runbook (when the token is ready — "R2 ready")

```bash
export AWS_ACCESS_KEY_ID=$(op item get so3ekk767jxxjfn3ka5nri7b3u --vault cupqdml5deh2x6povtmqsxdzyu --fields "label=S3 Client Access Key ID" --reveal)
export AWS_SECRET_ACCESS_KEY=$(op item get so3ekk767jxxjfn3ka5nri7b3u --vault cupqdml5deh2x6povtmqsxdzyu --fields "label=S3 Client Secret Access Key" --reveal)
export R2_ENDPOINT=$(op item get so3ekk767jxxjfn3ka5nri7b3u --vault cupqdml5deh2x6povtmqsxdzyu --fields "label=Jurisdiction Specific Endpoint (default)" --reveal)

# 1. create buckets (idempotent; needs Admin R&W token)
python3 - <<'PY'
import boto3, os
s3 = boto3.client('s3', endpoint_url=os.environ['R2_ENDPOINT'])
for b in ("progress-archive", "wiki-source-archive"):
    try: s3.create_bucket(Bucket=b); print("created", b)
    except Exception as e: print(b, e.__class__.__name__)
PY

# 2. upload the staged Gaffney mirror (193 files; manifest sources/gaffney-r2-manifest.csv)
python3 scripts/mirror_gaffney_r2.py --upload progress-archive

# 3. attach the custom domain (R2 API creates the DNS record in the progress.org zone)
export CF_TOKEN=$(op item get so3ekk767jxxjfn3ka5nri7b3u --vault cupqdml5deh2x6povtmqsxdzyu --fields "label=Token Value" --reveal)
ACCT=$(echo "$R2_ENDPOINT" | sed -E 's#https://([a-f0-9]+)\..*#\1#')
ZONE_ID=<progress.org zone id — from dashboard Overview, or API zones list>
curl -s "https://api.cloudflare.com/client/v4/accounts/$ACCT/r2/buckets/progress-archive/domains/custom" \
  -H "Authorization: Bearer $CF_TOKEN" -H 'Content-Type: application/json' \
  --data '{"domain":"archive.progress.org","zoneId":"'$ZONE_ID'","enabled":true}'

# 4. registry-wide preservation sweep into the private bucket (resumable)
python3 scripts/archive_sources_r2.py --bucket wiki-source-archive

# 5. flip wiki citations: on the 10 Gaffney research pages, add the archived URL
#    (https://archive.progress.org/gaffney/<path>) alongside the masongaffney.org
#    original; then git rm sources/gaffney/*.pdf (keep text/), commit.
#    Verify each archive URL serves 200 before flipping.
```

## Rules
- Never serve `wiki-source-archive` publicly (copyright). Only `progress-archive` gets a
  domain/r2.dev.
- Original publisher URLs remain the primary citation; archive links are supplements
  (Gaffney pages may use archive.progress.org as primary once masongaffney.org dies).
- Every upload verified (size match post-upload; sha256 in the manifests).
- New Gaffney tier-2 waves: mirror → OCR → R2 → cite, same pattern.
