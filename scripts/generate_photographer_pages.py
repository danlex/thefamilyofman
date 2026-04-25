#!/usr/bin/env python3
"""Generate one Jekyll page per row of data/photographers.csv.

Output: site/_photographers/<id>.md

Regenerated (overwritten) on every run. The CSV remains the
authoritative source; these pages are a rendering convenience.
The layout (_layouts/photographer.html) does the photo lookup.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "data" / "photographers.csv"
OUT_DIR = ROOT / "site" / "_photographers"


def yaml_scalar(s: str | None) -> str:
    """Return a value safe for YAML frontmatter — always quoted."""
    if s is None:
        return '""'
    s = s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")
    return f'"{s}"'


def main() -> int:
    if not CSV_PATH.exists():
        print(f"missing {CSV_PATH}", file=sys.stderr)
        return 1

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    # Remove previously-generated pher-*.md so deletions in the CSV
    # propagate cleanly. Leave .gitkeep alone.
    for f in OUT_DIR.glob("pher-*.md"):
        f.unlink()

    written = 0
    with CSV_PATH.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            pid = row.get("id", "").strip()
            if not pid:
                continue

            name = row.get("name") or pid
            body = (row.get("notes") or "").strip()

            frontmatter = (
                "---\n"
                f"id: {yaml_scalar(pid)}\n"
                f"name: {yaml_scalar(name)}\n"
                f"birth_year: {yaml_scalar(row.get('birth_year'))}\n"
                f"death_year: {yaml_scalar(row.get('death_year'))}\n"
                f"nationality: {yaml_scalar(row.get('nationality'))}\n"
                f"gender: {yaml_scalar(row.get('gender'))}\n"
                f"photo_count: {yaml_scalar(row.get('photo_count'))}\n"
                f"bio_url: {yaml_scalar(row.get('bio_url'))}\n"
                f"source_ids: {yaml_scalar(row.get('source_ids'))}\n"
                f"title: {yaml_scalar(name)}\n"
                "layout: photographer\n"
                "namespace: Photographer\n"
                "edit_dir: data\n"
                "generated: true\n"
                "---\n"
            )

            out_file = OUT_DIR / f"{pid}.md"
            out_file.write_text(frontmatter + "\n" + (body + "\n" if body else ""), encoding="utf-8")
            written += 1

    print(f"generated {written} photographer pages at {OUT_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
