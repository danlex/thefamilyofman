#!/usr/bin/env python3
"""Generate one Jekyll page per row of data/photographs.csv.

Output: site/_photographs/<id>.md

Regenerated (overwritten) on every run. The CSV remains the
authoritative source; these pages are a rendering convenience.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "data" / "photographs.csv"
OUT_DIR = ROOT / "site" / "_photographs"


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
    # Remove any previously-generated photo-*.md so deletions in the
    # CSV propagate cleanly. Leave the .gitkeep alone.
    for f in OUT_DIR.glob("photo-*.md"):
        f.unlink()

    written = 0
    with CSV_PATH.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            pid = row.get("id", "").strip()
            if not pid:
                continue

            title = row.get("title") or "Untitled"
            body = (row.get("notes") or "").strip()

            frontmatter = (
                "---\n"
                f"id: {yaml_scalar(pid)}\n"
                f"title: {yaml_scalar(title)}\n"
                f"photographer: {yaml_scalar(row.get('photographer'))}\n"
                f"year: {yaml_scalar(row.get('year'))}\n"
                f"country: {yaml_scalar(row.get('country'))}\n"
                f"section: {yaml_scalar(row.get('section'))}\n"
                f"moma_object_id: {yaml_scalar(row.get('moma_object_id'))}\n"
                f"clervaux_on_display: {yaml_scalar(row.get('clervaux_on_display') or 'unknown')}\n"
                f"source_ids: {yaml_scalar(row.get('source_ids'))}\n"
                "layout: photograph\n"
                "namespace: Photograph\n"
                "edit_dir: data\n"
                "generated: true\n"
                "---\n"
            )

            out_file = OUT_DIR / f"{pid}.md"
            out_file.write_text(frontmatter + "\n" + (body + "\n" if body else ""), encoding="utf-8")
            written += 1

    print(f"generated {written} photograph pages at {OUT_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
