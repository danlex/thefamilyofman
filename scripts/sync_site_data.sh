#!/usr/bin/env bash
# Copy the authoritative data files into Jekyll's _data and _sources
# directories so the list pages render real content.
#
#   data/*.csv        -> site/_data/*.csv      (available as site.data.*)
#   sources/**/*.md   -> site/_sources/**/*.md (available as site.sources)
#
# Run from the repo root or via the deploy workflow.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# --- CSVs into _data ---------------------------------------------------
mkdir -p "$ROOT/site/_data"
for f in photographs photographers sections; do
  src="$ROOT/data/${f}.csv"
  if [ -f "$src" ]; then
    cp "$src" "$ROOT/site/_data/${f}.csv"
  fi
done

# --- Sources into the Jekyll collection --------------------------------
# Rebuild the mirror to avoid stale files.
rm -rf "$ROOT/site/_sources"
mkdir -p "$ROOT/site/_sources"
if [ -d "$ROOT/sources" ]; then
  cd "$ROOT/sources"
  find . -type f -name '*.md' | while read -r f; do
    rel="${f#./}"
    dst="$ROOT/site/_sources/${rel}"
    mkdir -p "$(dirname "$dst")"
    cp "$ROOT/sources/$rel" "$dst"
  done
fi

echo "wrote:"
echo "  site/_data/photographs.csv"
echo "  site/_data/photographers.csv"
echo "  site/_data/sections.csv"
echo "  site/_sources/ ($(find "$ROOT/site/_sources" -type f -name '*.md' 2>/dev/null | wc -l | tr -d ' ') files)"
