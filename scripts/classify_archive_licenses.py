#!/usr/bin/env python3
"""
classify_archive_licenses.py — license-classification pass over the PRIVATE preservation
archive (Floyd 2026-07-16: "run a license classification pass and promote any you can").

For each `archived` row in sources/r2-archive-manifest.csv: fetch the object from the
private bucket, extract text from the first 3 + last 2 pages (pdftotext; tesseract
fallback for scans), and scan for license evidence. Writes
sources/r2-license-classification.csv with a recommendation + the evidence string.

Classification rules (conservative — promote only CLEAR rights):
  PROMOTE-CC        explicit Creative Commons license statement (record variant; NC/ND
                    variants still allow verbatim redistribution)
  PROMOTE-USGOV     US federal government work (PD, 17 USC §105): .gov/.mil source or
                    federal agency imprint (Fed banks are NOT federal works — HOLD)
  PROMOTE-PD-AGE    published pre-1931 (US public domain)
  PROMOTE-PD-STATED explicit "public domain" dedication
  HOLD              everything else: ©/all-rights-reserved, Crown copyright, OA-without-
                    license, author-copyright working papers, no statement found

A human (T1) reviews the CSV before any object is copied to the public bucket —
the script only classifies; scripts/promote_to_public.py does the copy after review.

Usage: AWS_* + R2_ENDPOINT env set; python3 scripts/classify_archive_licenses.py [--limit N]
"""
import argparse, csv, os, re, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "sources", "r2-archive-manifest.csv")
OUT = os.path.join(ROOT, "sources", "r2-license-classification.csv")
BUCKET = "wiki-source-archive"

CC_RX = re.compile(r"creative\s*commons|CC[ -]BY(?:[ -](?:NC|ND|SA)){0,2}\s*(?:\d\.\d)?"
                   r"|licensed under CC|CC0", re.I)
PD_RX = re.compile(r"public\s+domain", re.I)
CROWN_RX = re.compile(r"crown\s+copyright|©\s*(?:Her|His)\s+Majesty", re.I)
ARR_RX = re.compile(r"all\s+rights\s+reserved", re.I)
USGOV_HINTS = ("congress.gov", "gao.gov", "cbo.gov", "treasury.gov", "irs.gov",
               "usda.gov", "census.gov", "bls.gov", "bea.gov", "gpo.gov", "loc.gov",
               "whitehouse.gov", "energy.gov", "epa.gov", "hud.gov")
YEAR_RX = re.compile(r"\b(1[89]\d\d|20[0-2]\d)\b")


def pdf_text(fn, first=3, last=2):
    out = subprocess.run(["pdftotext", "-f", "1", "-l", str(first), fn, "-"],
                         capture_output=True, text=True).stdout
    tail = subprocess.run(["pdftotext", "-l", "999", fn, "-"],
                          capture_output=True, text=True).stdout[-4000:]
    if len(out.split()) < 30:  # scanned — OCR page 1 only (cheap)
        subprocess.run(["pdftoppm", "-r", "150", "-f", "1", "-l", "1", "-png", fn, "/tmp/lcp"],
                       capture_output=True)
        if os.path.exists("/tmp/lcp-1.png") or os.path.exists("/tmp/lcp-01.png"):
            img = "/tmp/lcp-1.png" if os.path.exists("/tmp/lcp-1.png") else "/tmp/lcp-01.png"
            out = subprocess.run(["tesseract", img, "-"], capture_output=True, text=True).stdout
            os.unlink(img)
    return (out or "") + "\n" + (tail or "")


def classify(url, text):
    ev = []
    m = CC_RX.search(text)
    if m:
        return "PROMOTE-CC", f"license text: {m.group(0)!r}"
    if PD_RX.search(text):
        return "PROMOTE-PD-STATED", "explicit 'public domain' statement"
    host = re.sub(r"https?://([^/]+).*", r"\1", url).lower()
    # ".gov" must be the FINAL label — treasury.govt.nz / treasury.gov.za are not US federal
    if host.split(".")[-1] in ("gov", "mil") or any(host.endswith(h) or host == h for h in USGOV_HINTS):
        if "frb" in host or "federalreserve" not in host and "fed" in host.split(".")[0]:
            ev.append("fed-bank host (not a federal work)")
        else:
            return "PROMOTE-USGOV", f"US federal host: {host}"
    years = [int(y) for y in YEAR_RX.findall(text[:2000])]
    if years and max(years) < 1931:
        return "PROMOTE-PD-AGE", f"latest year on early pages: {max(years)}"
    if CROWN_RX.search(text):
        return "HOLD", "Crown copyright"
    if ARR_RX.search(text):
        return "HOLD", "all rights reserved"
    return "HOLD", "no clear license statement" + ("; " + "; ".join(ev) if ev else "")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--limit", type=int); a = ap.parse_args()
    import boto3
    s3 = boto3.client("s3", endpoint_url=os.environ["R2_ENDPOINT"])
    rows = [r for r in csv.DictReader(open(MANIFEST)) if r["status"] == "archived"]
    if a.limit: rows = rows[: a.limit]
    done = {}
    if os.path.exists(OUT):
        done = {r["r2_key"]: r for r in csv.DictReader(open(OUT))}
    out_rows = list(done.values())
    print(f"classifying {len(rows)} archived PDFs ({len(done)} already done)")
    for i, r in enumerate(rows, 1):
        if r["r2_key"] in done: continue
        try:
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tf:
                local = tf.name
            s3.download_file(BUCKET, r["r2_key"], local)
            verdict, evidence = classify(r["source_url"], pdf_text(local))
            os.unlink(local)
        except Exception as e:
            verdict, evidence = "ERROR", str(e)[:80]
        out_rows.append({"title": r["title"], "source_url": r["source_url"],
                         "r2_key": r["r2_key"], "verdict": verdict, "evidence": evidence})
        if i % 20 == 0:
            print(f"  … {i}/{len(rows)}", flush=True)
            csv.DictWriter(open(OUT, "w", newline=""), fieldnames=["title","source_url","r2_key","verdict","evidence"]).writeheader() or None
            w = csv.DictWriter(open(OUT, "w", newline=""), fieldnames=["title","source_url","r2_key","verdict","evidence"]); w.writeheader(); w.writerows(out_rows)
    w = csv.DictWriter(open(OUT, "w", newline=""), fieldnames=["title","source_url","r2_key","verdict","evidence"]); w.writeheader(); w.writerows(out_rows)
    import collections
    print(collections.Counter(r["verdict"] for r in out_rows))


if __name__ == "__main__":
    main()
