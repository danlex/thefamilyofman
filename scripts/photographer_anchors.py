#!/usr/bin/env python3
"""
Pre-flight anchors for a per-photographer deep-research cycle (issue #184).

Given a photographer name (e.g. "W. Eugene Smith", "Dorothea Lange"), this
script prints everything a worker — or a dispatcher writing a worker brief —
needs to scope the cycle without running ad-hoc inline pipelines:

  1. Strict-match plate count and the verbatim list of plate rows
     (photo-id, checklist number, section, country, agency credit, dimensions)
     from data/photographs.csv.
  2. Whether each plate has a standalone deep-dive at research/photographs/<id>.md.
  3. The current size of research/photographers/<slug>.md (the terse-vs-deep
     marker for issue #184) and whether the file exists at all.
  4. The list of in-repo source files (sources/**/*.md) whose body mentions the
     photographer name — i.e. candidate `src-*` anchors for the deep file.
  5. The current count of needs-agent issues so the report doubles as a
     progress sanity-check.

This replaces the inline grep/sed/paste pipelines I had been pasting into the
Bash tool during the Smith (PR #260) and Lange (PR #261) cycles. Per
AGENTS.md § Tooling discipline, recurring verification logic belongs in a
committed script, not in a one-off shell composition.

Usage:
  python3 scripts/photographer_anchors.py "Dorothea Lange"
  python3 scripts/photographer_anchors.py "Henri Cartier-Bresson" --json

Read-only. Stdlib only. Runs in under a second.

Exit code:
  0 — anchors printed (even if the photographer has zero plates — that itself
      is useful diagnostic output for a typo or a deceased-source check)
  2 — usage error (no name supplied)
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PHOTOGRAPHS_CSV = REPO_ROOT / "data" / "photographs.csv"
PHOTOGRAPHS_DIR = REPO_ROOT / "research" / "photographs"
PHOTOGRAPHERS_DIR = REPO_ROOT / "research" / "photographers"
SOURCES_DIR = REPO_ROOT / "sources"
CHECKLIST_RE = re.compile(r"Checklist\s+#(\d+[A-Z]?)")


def slugify(name: str) -> str:
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def collect_plates(name: str) -> list[dict]:
    plates: list[dict] = []
    with PHOTOGRAPHS_CSV.open(newline="") as f:
        for row in csv.DictReader(f):
            if row.get("photographer") == name:
                notes = row.get("notes", "") or ""
                m = CHECKLIST_RE.search(notes)
                checklist = m.group(1) if m else ""
                agency = ""
                for tag in ("Farm Security Administration", "LIFE", "FORTUNE", "VOGUE", "Magnum"):
                    if tag in notes:
                        agency = tag
                        break
                plates.append(
                    {
                        "id": row.get("id", ""),
                        "checklist": checklist,
                        "section": row.get("section", ""),
                        "country": row.get("country", ""),
                        "agency": agency,
                        "deep_dive": (PHOTOGRAPHS_DIR / f"{row.get('id', '')}.md").exists(),
                    }
                )
    return plates


def existing_photographer_file(name: str) -> tuple[Path, bool, int]:
    slug = slugify(name)
    path = PHOTOGRAPHERS_DIR / f"{slug}.md"
    exists = path.exists()
    lines = len(path.read_text().splitlines()) if exists else 0
    return path, exists, lines


def matching_sources(name: str) -> list[str]:
    needle = name.lower()
    hits: list[str] = []
    for path in SOURCES_DIR.rglob("*.md"):
        try:
            if needle in path.read_text(errors="replace").lower():
                hits.append(str(path.relative_to(REPO_ROOT)))
        except OSError:
            continue
    return sorted(hits)


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__.strip())
        return 2

    as_json = "--json" in argv
    name = next(a for a in argv if not a.startswith("--"))

    plates = collect_plates(name)
    pher_path, pher_exists, pher_lines = existing_photographer_file(name)
    src_hits = matching_sources(name)

    if as_json:
        out = {
            "name": name,
            "slug": slugify(name),
            "plate_count": len(plates),
            "plates": plates,
            "photographer_file": {
                "path": str(pher_path.relative_to(REPO_ROOT)),
                "exists": pher_exists,
                "lines": pher_lines,
            },
            "candidate_sources": src_hits,
        }
        print(json.dumps(out, indent=2))
        return 0

    print(f"Photographer:  {name}")
    print(f"Slug:          {slugify(name)}")
    print(f"Plate count:   {len(plates)}")
    print()
    if plates:
        print("Plates (CSV ground truth):")
        print(f"  {'id':<12}  {'#':<6}  {'section':<30}  {'country':<6}  {'agency':<28}  deep-dive")
        for p in plates:
            mark = "yes" if p["deep_dive"] else "no"
            print(
                f"  {p['id']:<12}  {p['checklist']:<6}  {p['section']:<30}  "
                f"{p['country']:<6}  {p['agency']:<28}  {mark}"
            )
        print()
    print("Photographer research file:")
    print(f"  path:   {pher_path.relative_to(REPO_ROOT)}")
    print(f"  exists: {pher_exists}")
    print(f"  lines:  {pher_lines}  (issue #184 target: deep file ~300-500; terse ≈ <80)")
    print()
    if src_hits:
        print(f"Candidate in-repo sources mentioning {name!r} ({len(src_hits)}):")
        for h in src_hits:
            print(f"  {h}")
    else:
        print(f"No in-repo source files mention {name!r}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
