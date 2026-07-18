#!/usr/bin/env python3
"""
archive_sources_r2.py — preservation archive of the wiki's PRIMARY SOURCES to R2
(Floyd 2026-07-16: "why not use that for all PDFs of all research on the wiki").

Walks sources/registry.csv, downloads every reachable PDF source, and uploads to the
PRIVATE bucket (default: wiki-source-archive) under sha256-prefixed keys. Writes/updates
sources/r2-archive-manifest.csv (registry title, source url, http status, bytes, sha256,
r2 key, archived date).

WHY PRIVATE: most registry sources are copyrighted papers/reports. We may keep
preservation copies against link rot (the registry's URLs die constantly — see the
link-health waves), but we must NOT publicly serve them. Public hosting stays limited to
material with permission (gaffney-archive bucket) or public domain (texts/ program).
The wiki's citation URLs keep pointing at the original publishers; the archive is the
fallback for editors when a link dies (channel: ask a session to pull from R2).

Resumable: URLs already in the manifest with status=archived are skipped.

Usage:
  export AWS_ACCESS_KEY_ID=... AWS_SECRET_ACCESS_KEY=... R2_ENDPOINT=...   (op-resolved)
  python3 scripts/archive_sources_r2.py [--bucket wiki-source-archive] [--limit N] [--dry-run]
"""
import argparse, csv, hashlib, os, subprocess, sys, tempfile, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = os.path.join(ROOT, "sources", "registry.csv")
MANIFEST = os.path.join(ROOT, "sources", "r2-archive-manifest.csv")
FIELDS = ["title", "source_url", "status", "bytes", "sha256", "r2_key", "archived"]


def load_manifest():
    if not os.path.exists(MANIFEST):
        return {}
    return {r["source_url"]: r for r in csv.DictReader(open(MANIFEST))}


def save_manifest(rows):
    with open(MANIFEST, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in sorted(rows.values(), key=lambda x: x["title"].lower()):
            w.writerow(r)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bucket", default="wiki-source-archive")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    s3 = None
    if not a.dry_run:
        import boto3
        s3 = boto3.client("s3", endpoint_url=os.environ["R2_ENDPOINT"])

    manifest = load_manifest()
    reg = list(csv.DictReader(open(REGISTRY)))
    url_field = next((k for k in reg[0] if "url" in k.lower()), None)
    title_field = next(iter(reg[0]))
    todo = []
    for r in reg:
        url = (r.get(url_field) or "").strip()
        if not url.lower().startswith("http"):
            continue
        if manifest.get(url, {}).get("status") == "archived":
            continue
        todo.append((r.get(title_field, "")[:120], url))
    if a.limit:
        todo = todo[: a.limit]
    print(f"registry rows with URLs to archive: {len(todo)} (manifest has {len(manifest)})")

    done = failed = skipped = 0
    for title, url in todo:
        try:
            with tempfile.NamedTemporaryFile(delete=False) as tf:
                local = tf.name
            r = subprocess.run(["curl", "-sL", "--max-time", "180", "-o", local,
                                "-w", "%{http_code} %{content_type}", url],
                               capture_output=True, text=True)
            code, ctype = (r.stdout.split(" ", 1) + [""])[:2]
            size = os.path.getsize(local)
            is_pdf = "pdf" in ctype.lower() or (size > 4 and open(local, "rb").read(4) == b"%PDF")
            if code != "200" or size < 1024:
                manifest[url] = dict(title=title, source_url=url, status=f"http-{code}",
                                     bytes=size, sha256="", r2_key="", archived="")
                failed += 1
            elif not is_pdf:
                manifest[url] = dict(title=title, source_url=url, status="not-pdf",
                                     bytes=size, sha256="", r2_key="", archived="")
                skipped += 1
            else:
                h = hashlib.sha256(open(local, "rb").read()).hexdigest()
                key = f"sources/{h[:2]}/{h}.pdf"
                if not a.dry_run:
                    s3.upload_file(local, a.bucket, key)
                manifest[url] = dict(title=title, source_url=url, status="archived",
                                     bytes=size, sha256=h, r2_key=key,
                                     archived=time.strftime("%Y-%m-%d"))
                done += 1
            os.unlink(local)
            if (done + failed + skipped) % 25 == 0:
                save_manifest(manifest)
                print(f"  … archived {done}, failed {failed}, non-pdf {skipped}")
        except Exception as e:
            manifest[url] = dict(title=title, source_url=url, status=f"err:{str(e)[:40]}",
                                 bytes=0, sha256="", r2_key="", archived="")
            failed += 1
    save_manifest(manifest)
    print(f"DONE: archived {done}, failed {failed}, non-pdf {skipped} -> {MANIFEST}")


if __name__ == "__main__":
    main()
