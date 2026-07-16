#!/usr/bin/env python3
"""
mirror_gaffney_r2.py — mirror ALL of masongaffney.org's archive files to R2 for
preservation (Floyd's directive 2026-07-16; hosting permission from the site's
webmaster, Gaffney d. 2020).

Stage 1 (--download): fetch every file in the site inventory (publications/,
workpapers/, essays/, plus the homepage and tributes page) into
scratchpad/cache/gaffney-mirror/ preserving paths, and write
sources/gaffney-r2-manifest.csv (path, bytes, sha256, source url, r2 key).
Stage 2 (--upload BUCKET): upload the local mirror to R2 under gaffney/<path>,
verifying each object's ETag/size after upload.

Credentials (never printed): AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY /
R2_ENDPOINT env, resolved from 1Password item "R2 API Token - Progress.org".

The wiki repo keeps only worked texts (sources/gaffney/); the full mirror lives
in R2 + the manifest here.
"""
import argparse, csv, hashlib, json, os, re, subprocess, sys, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIRROR = os.path.join(ROOT, "scratchpad", "cache", "gaffney-mirror")
MANIFEST = os.path.join(ROOT, "sources", "gaffney-r2-manifest.csv")
BASE = "https://masongaffney.org/"
DIRS = ["publications/", "workpapers/", "essays/"]
EXTRA = ["index.html", "tributes.html", "style.css"]


def listing(path):
    html = subprocess.run(["curl", "-sL", BASE + path], capture_output=True, text=True).stdout
    return sorted(set(re.findall(r'href="([^"]+\.(?:pdf|PDF|doc|docx|htm|html))"', html)))


def sha256(fn):
    h = hashlib.sha256()
    with open(fn, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def download():
    rows, total = [], 0
    targets = [(p, f) for p in DIRS for f in listing(p)] + [("", e) for e in EXTRA]
    print(f"{len(targets)} files to mirror")
    for path, f in targets:
        rel = os.path.join(path, urllib.parse.unquote(f))
        local = os.path.join(MIRROR, rel)
        os.makedirs(os.path.dirname(local), exist_ok=True)
        url = BASE + path + f
        if not os.path.exists(local) or os.path.getsize(local) == 0:
            r = subprocess.run(["curl", "-sL", "--max-time", "120", url, "-o", local])
            if r.returncode != 0 or not os.path.exists(local):
                print(f"  FAIL {url}"); continue
        size = os.path.getsize(local)
        total += size
        rows.append({"path": rel, "bytes": size, "sha256": sha256(local),
                     "source_url": url, "r2_key": f"gaffney/{rel}"})
    with open(MANIFEST, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["path", "bytes", "sha256", "source_url", "r2_key"])
        w.writeheader(); w.writerows(rows)
    print(f"mirrored {len(rows)} files, {total/1e6:.1f} MB -> {MIRROR}; manifest -> {MANIFEST}")


def upload(bucket):
    import boto3
    s3 = boto3.client("s3", endpoint_url=os.environ["R2_ENDPOINT"])
    rows = list(csv.DictReader(open(MANIFEST)))
    ok = 0
    for r in rows:
        local = os.path.join(MIRROR, r["path"])
        s3.upload_file(local, bucket, r["r2_key"])
        head = s3.head_object(Bucket=bucket, Key=r["r2_key"])
        if head["ContentLength"] != int(r["bytes"]):
            print(f"  SIZE MISMATCH {r['r2_key']}"); continue
        ok += 1
        if ok % 25 == 0:
            print(f"  … {ok}/{len(rows)}")
    print(f"uploaded+verified {ok}/{len(rows)} objects to {bucket}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--download", action="store_true")
    ap.add_argument("--upload", metavar="BUCKET")
    a = ap.parse_args()
    if a.download:
        download()
    if a.upload:
        upload(a.upload)
    if not (a.download or a.upload):
        ap.print_help()
