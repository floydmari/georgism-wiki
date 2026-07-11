#!/bin/bash
# Wayback Save-Page-Now sweep over registry.csv external URLs (link-rot insurance).
# Resumable: skips URLs already in the log. Run from repo root; log defaults to
# sources/exports/spn-sweep.log (override with $1). Polite: 10s between saves.
LOG="${1:-sources/exports/spn-sweep.log}"
touch "$LOG"
awk -F',' '{print $NF}' sources/registry.csv | grep -E '^https?://' | sort -u | \
grep -vE 'archive\.org|gutenberg\.org|doi\.org|progress\.org|wikipedia\.org|google\.com' | \
while read -r u; do
  grep -qF "$u" "$LOG" && continue
  code=$(curl -s -m 120 -A "Mozilla/5.0" -o /dev/null -w "%{http_code}" "https://web.archive.org/save/$u")
  rc=$?
  if [ "$rc" = "28" ]; then echo "TIMEOUT-MAYBE-SAVED $u" >> "$LOG"
  elif [ "$code" = "200" ] || [ "$code" = "302" ]; then echo "SAVED($code) $u" >> "$LOG"
  elif [ "$code" = "429" ]; then echo "RATE-LIMITED $u" >> "$LOG"; sleep 120
  else echo "FAILED($code) $u" >> "$LOG"; fi
  sleep 10
done
echo "SWEEP-COMPLETE $(date -u +%Y-%m-%dT%H:%MZ)" >> "$LOG"
