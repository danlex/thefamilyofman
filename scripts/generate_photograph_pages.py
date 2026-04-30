#!/usr/bin/env python3
"""Generate one Jekyll page per row of data/photographs.csv.

Output: site/_photographs/<id>.md

Regenerated (overwritten) on every run. The CSV remains the
authoritative source for catalog metadata; if `research/photographs/<id>.md`
exists, the user-friendly prose sections (Subject and context, Reception,
Open questions) are extracted and rendered above the technical catalog
notes — readers see the story first, the cataloging detail after.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "data" / "photographs.csv"
OUT_DIR = ROOT / "site" / "_photographs"
RESEARCH_DIR = ROOT / "research" / "photographs"

# Sections of the research note that are rendered as user-facing prose.
# The first row metadata table and the "Provenance" section are not
# user-friendly and remain in the research note for researchers.
USER_FACING_SECTIONS = [
    "Subject and context",
    "Reception / analysis",
    "Reception",
    "Story",
    "Perspective notes",
    "Open questions",
]


def yaml_scalar(s: str | None) -> str:
    """Return a value safe for YAML frontmatter — always quoted."""
    if s is None:
        return '""'
    s = s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")
    return f'"{s}"'


def extract_user_facing_sections(research_md: str) -> str:
    """Return the user-facing markdown extracted from a research note.

    Pulls only the H2 sections named in USER_FACING_SECTIONS, in the order
    they appear in the source file. Non-prose sections (the title row,
    the metadata table, the Provenance section) are skipped.
    """
    if not research_md.strip():
        return ""

    # Split on lines that look like H2 headings.
    parts = re.split(r"^(##\s+.+)$", research_md, flags=re.MULTILINE)
    # parts looks like: [preamble, "## Header", "body", "## Header2", "body2", ...]
    blocks: list[tuple[str, str]] = []
    for i in range(1, len(parts), 2):
        header = parts[i].strip()
        body = parts[i + 1] if i + 1 < len(parts) else ""
        # Strip the leading "## " for matching
        header_text = header[3:].strip() if header.startswith("##") else header.strip()
        blocks.append((header_text, body))

    # Filter for user-facing sections, preserving order.
    rendered: list[str] = []
    for header_text, body in blocks:
        if header_text in USER_FACING_SECTIONS:
            # Trim trailing whitespace; skip empty bodies.
            body_stripped = body.strip()
            if body_stripped:
                rendered.append(f"### {header_text}\n\n{body_stripped}")
    return "\n\n".join(rendered)


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
    with_stories = 0
    with CSV_PATH.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            pid = row.get("id", "").strip()
            if not pid:
                continue

            title = row.get("title") or "Untitled"
            catalog_notes = (row.get("notes") or "").strip()

            # Look for a research note with user-facing prose.
            research_path = RESEARCH_DIR / f"{pid}.md"
            story_md = ""
            if research_path.exists():
                research_text = research_path.read_text(encoding="utf-8")
                story_md = extract_user_facing_sections(research_text)
                if story_md:
                    with_stories += 1

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
                f"has_story: {'true' if story_md else 'false'}\n"
                "layout: photograph\n"
                "namespace: Photograph\n"
                "edit_dir: data\n"
                "generated: true\n"
                "---\n"
            )

            body_parts: list[str] = []
            if story_md:
                body_parts.append("## The story\n")
                body_parts.append(
                    "_Drawn from `research/photographs/" + pid + ".md` — "
                    "the canonical research note. Provenance and primary-source "
                    "documentation live there; this is the reader-friendly summary._\n"
                )
                body_parts.append(story_md)
            if catalog_notes:
                body_parts.append("## Catalog notes\n")
                body_parts.append(catalog_notes)

            body = ("\n\n".join(body_parts) + "\n") if body_parts else ""
            out_file = OUT_DIR / f"{pid}.md"
            out_file.write_text(frontmatter + "\n" + body, encoding="utf-8")
            written += 1

    print(f"generated {written} photograph pages at {OUT_DIR}")
    print(f"  {with_stories} have research-note 'story' sections")
    print(f"  {written - with_stories} are catalog-notes-only (no research note yet)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
