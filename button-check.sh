#!/usr/bin/env bash
# 🔘 button-check.sh — the ʻohana constellation button checker (CC0, fork freely!)
# Born in the OCTAVE run of 2026-08-01 when Shaka said: "B can stand for Button check."
#
# What it does, given a list of domains (one per line, arg 1 or stdin):
#   1. HTTP-checks every domain homepage (follows redirects)
#   2. Verifies the ohana-corner v4 buttons are present (flower/globe/violin/magnet)
#   3. Harvests every href on every homepage, dedupes, health-checks each target
#   4. Prints a clean report of anything that isn't smooth
#
# Usage:  button-check.sh domains.txt
#         cut -d' ' -f1 zones.txt | button-check.sh
# Notes:  ${...} and +id+ 404s are usually JS-template artifacts scraped from
#         inline scripts, not real buttons. fonts.g* roots 404 by design.
set -u
LIST="${1:-/dev/stdin}"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
UA="Mozilla/5.0 (X11; Linux x86_64) ohana-button-check"

echo "== 1/3 homepage status + corner buttons =="
while read -r d; do [ -z "$d" ] && continue
  html=$(curl -sL --max-time 25 -A "$UA" "https://$d/")
  code=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 20 -A "$UA" "https://$d/")
  f=$(grep -c 'id="oflo"'  <<<"$html"); g=$(grep -c 'id="olang"' <<<"$html")
  v=$(grep -c 'id="oviol"' <<<"$html"); m=$(grep -c 'id="cmag"'  <<<"$html")
  echo "$code $d flower=$f globe=$g violin=$v magnet=$m" | tee -a "$TMP/pages.txt"
  grep -oE 'href="[^"]+"' <<<"$html" | sed 's/href="//;s/"$//' | while read -r u; do
    case "$u" in \#*|mailto:*|javascript:*|tel:*) ;; http*) echo "$u";;
      /*) echo "https://$d$u";; *) echo "https://$d/$u";; esac
  done >> "$TMP/links.txt"
done < "$LIST"

echo; echo "== 2/3 link health (deduped) =="
sort -u "$TMP/links.txt" > "$TMP/uniq.txt"
check() { c=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 20 -A "$UA" "$1"); echo "$c $1"; }
export -f check; export UA
xargs -d '\n' -P 12 -I{} bash -c 'check "$@"' _ {} < "$TMP/uniq.txt" > "$TMP/checked.txt" 2>/dev/null
awk '{print $1}' "$TMP/checked.txt" | sort | uniq -c

echo; echo "== 3/3 THE NOT-SMOOTH LIST =="
echo "-- pages down or missing corner buttons:"
grep -vE '^200 .* flower=[1-9].* globe=[1-9].* violin=[1-9].* magnet=[1-9]' "$TMP/pages.txt" || echo "  none — every door smooth 🌺"
echo "-- broken link targets (minus known artifacts):"
grep -v '^200 ' "$TMP/checked.txt" | grep -vE '\$\{|\+id\+|fonts\.g|/cdn-cgi/l/email-protection|/'"'"'' || echo "  none — every button lands 🔘"
