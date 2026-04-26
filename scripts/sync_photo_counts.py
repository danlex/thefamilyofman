#!/usr/bin/env python3
"""Re-tally the photo_count column in data/photographers.csv from data/photographs.csv.

Catalog-builder PRs add more plates by photographers whose row already exists, but
the CSV photo_count column does not auto-update. The homepage leaderboard
("Most-photographed contributors") reads photo_count directly, so a stale CSV
makes the homepage display wrong numbers.

Run this script after every catalog-builder PR. It is idempotent — re-running with
no plate-CSV changes is a no-op.

Name-variant normalisation: the MoMA Master Checklist spells some photographers
inconsistently (e.g., "Roy De Carava" at plate 18 and "Roy DeCarava" at plate 147),
and OCR has reproduced the variants verbatim per the project convention. We
normalise those here on a per-photographer-id basis. The canonical photographer
name is whatever appears in data/photographers.csv `name` column; variants are
declared in NAME_VARIANTS below.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PHOTOGRAPHERS = ROOT / "data" / "photographers.csv"
PHOTOGRAPHS = ROOT / "data" / "photographs.csv"

# id -> list of accepted name spellings (canonical first, variants follow).
# Add new entries here when OCR or scholarly variants are documented in
# data/photographers.csv `notes` columns.
NAME_VARIANTS: dict[str, list[str]] = {
    "pher-roy-decarava": ["Roy DeCarava", "Roy De Carava"],
    "pher-laurence-le-guay": ["Laurence Le Guay", "Laurence LeGuay"],
}


def main() -> int:
    if not PHOTOGRAPHERS.exists():
        print(f"missing {PHOTOGRAPHERS}", file=sys.stderr)
        return 1
    if not PHOTOGRAPHS.exists():
        print(f"missing {PHOTOGRAPHS}", file=sys.stderr)
        return 1

    # Load photographs (just the photographer column, stripped).
    with PHOTOGRAPHS.open(newline="", encoding="utf-8") as fh:
        photos = [row["photographer"].strip() for row in csv.DictReader(fh)]

    # Load photographers, recompute photo_count, write back preserving header.
    with PHOTOGRAPHERS.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    if "photo_count" not in fieldnames:
        print("photographers.csv has no photo_count column", file=sys.stderr)
        return 1

    changed = 0
    for row in rows:
        pid = row["id"].strip()
        accepted = NAME_VARIANTS.get(pid, [row["name"].strip()])
        live = sum(1 for ph in photos if ph in accepted)
        old = (row.get("photo_count") or "0").strip() or "0"
        if str(live) != old:
            print(f"  {pid}: {old} -> {live}")
            row["photo_count"] = str(live)
            changed += 1

    if changed == 0:
        print("no changes — photo_count is in sync")
        return 0

    with PHOTOGRAPHERS.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(rows)

    print(f"updated {changed} photo_count values in {PHOTOGRAPHERS}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
