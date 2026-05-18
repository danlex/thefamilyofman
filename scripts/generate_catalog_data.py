#!/usr/bin/env python3
"""
generate_catalog_data.py
Reads data/photographs.csv and site/assets/images/ and emits
the comma-separated list of photo IDs that have a licensed
in-repo image (i.e. site/assets/images/<id>.jpg exists).

Usage:
    python3 scripts/generate_catalog_data.py

Output (to stdout):
    A comma-separated string of photo IDs, e.g.:
        photo-0080,photo-0093,...

That string must be pasted into the `plate_images:` frontmatter
field of site/catalog.md whenever new plate images are added.

Exit codes:
    0 — success
    1 — data/photographs.csv not found
"""

import csv
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
PHOTOS_CSV = REPO_ROOT / "data" / "photographs.csv"
IMAGES_DIR = REPO_ROOT / "site" / "assets" / "images"


def main() -> None:
    if not PHOTOS_CSV.exists():
        print(f"ERROR: {PHOTOS_CSV} not found", file=sys.stderr)
        sys.exit(1)

    # Collect all photo IDs from the CSV
    with PHOTOS_CSV.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        photo_ids = [row["id"].strip() for row in reader if row.get("id", "").strip()]

    # Which ones have a .jpg in site/assets/images/?
    matched = []
    for pid in photo_ids:
        if not re.match(r"^photo-\d{4}$", pid):
            continue
        img_path = IMAGES_DIR / f"{pid}.jpg"
        if img_path.exists():
            matched.append(pid)

    print(",".join(matched))
    print(
        f"# {len(matched)} of {len(photo_ids)} photo IDs have an in-repo image.",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
