#!/usr/bin/env python3
"""
export_registry_for_sheet.py — produce the Google-Sheet-ready export of sources/registry.csv,
with a delta column derived from git (not from anyone's memory).

Why this exists: the master source index lives in Floyd's Google Sheet, but the loop's source of
truth is sources/registry.csv in git. The available Drive tooling can CREATE spreadsheet files but
cannot edit cells in the existing Sheet, so the sync mechanism is: generate this export → upload it
to Drive as a dated snapshot spreadsheet (or import the CSV into the master Sheet:
File → Import → Upload → Replace current sheet).

The delta column compares the working-tree registry against the registry at a base git ref
(default origin/main), marking each row NEW / UPDATED / (blank). This is mechanical — if a loop
changed a row, the diff shows it, whether or not anyone remembered to report it.

Usage:
    python3 scripts/export_registry_for_sheet.py                  # base = origin/main
    python3 scripts/export_registry_for_sheet.py --base <ref>     # any git ref
Output: preview/registry-export.csv (git-ignored) + a summary on stdout.
"""
import csv
import io
import os
import subprocess
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = os.path.join(ROOT, "sources", "registry.csv")
OUT = os.path.join(ROOT, "preview", "registry-export.csv")


def rows_from(text):
    return {r["Title"]: r for r in csv.DictReader(io.StringIO(text))}


def main():
    base = "origin/main"
    if "--base" in sys.argv:
        base = sys.argv[sys.argv.index("--base") + 1]

    current_text = open(REGISTRY, encoding="utf-8").read()
    current = list(csv.DictReader(io.StringIO(current_text)))
    cols = list(current[0].keys())

    try:
        base_text = subprocess.run(
            ["git", "-C", ROOT, "show", f"{base}:sources/registry.csv"],
            capture_output=True, text=True, check=True).stdout
        old = rows_from(base_text)
    except subprocess.CalledProcessError:
        old = {}   # registry didn't exist at base → everything is NEW
        print(f"note: sources/registry.csv not found at {base}; marking all rows NEW")

    delta_col = f"Δ vs {base} ({date.today().isoformat()})"
    n_new = n_upd = 0
    out_rows = []
    for r in current:
        prev = old.get(r["Title"])
        if prev is None:
            mark, n_new = "NEW", n_new + 1
        elif any((prev.get(c) or "") != (r.get(c) or "") for c in cols):
            changed = [c for c in cols if (prev.get(c) or "") != (r.get(c) or "")]
            mark, n_upd = "UPDATED: " + ", ".join(changed), n_upd + 1
        else:
            mark = ""
        out_rows.append([r.get(c, "") for c in cols] + [mark])

    removed = [t for t in old if t not in {r["Title"] for r in current}]

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(cols + [delta_col])
        w.writerows(out_rows)

    print(f"export_registry_for_sheet: {len(out_rows)} rows → {os.path.relpath(OUT, ROOT)}")
    print(f"  NEW: {n_new}   UPDATED: {n_upd}   REMOVED-at-base (retitled?): {len(removed)}")
    for t in removed:
        print(f"  removed/retitled vs {base}: {t}")
    print("Upload the CSV to Drive as a dated snapshot spreadsheet, or import into the master "
          "Sheet (File → Import → Replace current sheet).")


if __name__ == "__main__":
    main()
