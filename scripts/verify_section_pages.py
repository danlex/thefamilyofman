#!/usr/bin/env python3
"""
Verify the per-section landing pages in site/_sections_articles/ against the
catalog data and the source corpus. This replaces the ad-hoc one-off checks
that were previously run inline while reviewing section-page PRs (#257 etc.).

For every site/_sections_articles/*.md the script checks:

  1. Frontmatter `section_id` names a section that actually appears in the
     `section` column of data/photographs.csv.
  2. Frontmatter `photo_count` equals the number of photographs.csv rows
     assigned to that section_id (the Liquid table renders exactly those rows,
     so a stale count is a visible bug).
  3. Every `src-*` id referenced in the page body resolves to an `id:` in some
     sources/**/*.md file (no orphan source ids).

Exit code:
  0 — all section pages pass
  non-zero — at least one mismatch; the offending file + reason is printed

Read-only. Stdlib only (no PyYAML dependency). Runs in well under a second.

Usage:
  python3 scripts/verify_section_pages.py            # human-readable
  python3 scripts/verify_section_pages.py --json     # machine-readable

See AGENTS.md § Tooling discipline and CLAUDE.md. Part of the pre-PR checklist
for any change under site/_sections_articles/.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SECTIONS_DIR = REPO_ROOT / "site" / "_sections_articles"
PHOTOGRAPHS_CSV = REPO_ROOT / "data" / "photographs.csv"
SOURCES_DIR = REPO_ROOT / "sources"

SRC_REF_RE = re.compile(r"src-[a-z0-9][a-z0-9-]*")


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Return (flat frontmatter dict, body). Only flat `key: value` lines are
    parsed — sufficient for the section-page schema (title/theme/order/
    section_id/checklist_section/photo_count)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_block = text[3:end]
    body = text[end + 4 :]
    fm: dict[str, str] = {}
    for line in fm_block.splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fm[key.strip()] = value.strip().strip('"').strip("'")
    return fm, body


def load_section_counts() -> Counter:
    counts: Counter = Counter()
    with PHOTOGRAPHS_CSV.open(newline="") as f:
        for row in csv.DictReader(f):
            counts[row.get("section", "")] += 1
    return counts


def load_defined_source_ids() -> set[str]:
    ids: set[str] = set()
    for path in SOURCES_DIR.rglob("*.md"):
        for line in path.read_text(errors="replace").splitlines():
            if line.startswith("id:"):
                ids.add(line.split(":", 1)[1].strip())
    return ids


def main(argv: list[str]) -> int:
    as_json = "--json" in argv

    section_counts = load_section_counts()
    defined_ids = load_defined_source_ids()

    results: list[dict] = []
    failures = 0

    for path in sorted(SECTIONS_DIR.glob("*.md")):
        fm, body = split_frontmatter(path.read_text())
        problems: list[str] = []

        section_id = fm.get("section_id")
        if not section_id:
            problems.append("missing frontmatter section_id")
        elif section_id not in section_counts:
            problems.append(
                f"section_id '{section_id}' not present in photographs.csv 'section' column"
            )

        declared = fm.get("photo_count")
        if declared is not None and section_id in section_counts:
            actual = section_counts[section_id]
            if not declared.isdigit() or int(declared) != actual:
                problems.append(
                    f"photo_count {declared!r} != {actual} rows in photographs.csv"
                )

        referenced = sorted(set(SRC_REF_RE.findall(body)))
        orphans = [r for r in referenced if r not in defined_ids]
        if orphans:
            problems.append("orphan source ids: " + ", ".join(orphans))

        if problems:
            failures += 1
        results.append(
            {
                "file": str(path.relative_to(REPO_ROOT)),
                "section_id": section_id,
                "ok": not problems,
                "problems": problems,
            }
        )

    if as_json:
        print(json.dumps({"failures": failures, "results": results}, indent=2))
    else:
        for r in results:
            status = "OK  " if r["ok"] else "FAIL"
            print(f"{status} {r['file']}  [{r['section_id']}]")
            for p in r["problems"]:
                print(f"       - {p}")
        if failures == 0:
            print(f"\nsection-page verify OK — {len(results)} pages, all consistent")
        else:
            print(f"\nsection-page verify FAILED — {failures}/{len(results)} pages with problems")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
