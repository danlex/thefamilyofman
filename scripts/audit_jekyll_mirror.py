#!/usr/bin/env python3
"""Audit divergence between canonical ``sources/`` and the Jekyll-collection
mirror at ``site/_sources/``.

Background: this project's Jekyll site renders the public-facing
``/sources/<era>/<slug>/`` URLs from ``site/_sources/`` rather than the
canonical ``sources/`` directory. Both trees must stay byte-identical or
the live site silently drifts away from the museum-grade source corpus.

This script enumerates:

- ``missing_in_mirror``: files present in ``sources/`` but absent from
  ``site/_sources/`` — the public site cannot render them at all.
- ``size_mismatch``: files present in both trees with different byte
  counts — the public site shows an older / shorter version of the source.
- ``orphans_in_mirror``: files present in ``site/_sources/`` but absent
  from ``sources/`` — leftover from a deleted canonical (no impact on
  live render but should be cleaned up).

Exit code: 0 if all three categories are empty; 1 otherwise. Intended to
run pre-commit on PRs that touch ``sources/`` so that the mirror is
brought along in the same PR.

Usage::

    python3 scripts/audit_jekyll_mirror.py           # human report
    python3 scripts/audit_jekyll_mirror.py --json    # machine report
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CANON = ROOT / "sources"
MIRROR = ROOT / "site" / "_sources"


def audit() -> dict:
    canon_files = {p.relative_to(CANON) for p in CANON.rglob("*.md")}
    mirror_files = {p.relative_to(MIRROR) for p in MIRROR.rglob("*.md")}

    missing_in_mirror = sorted(canon_files - mirror_files)
    orphans_in_mirror = sorted(mirror_files - canon_files)

    size_mismatch = []
    for rel in sorted(canon_files & mirror_files):
        c_bytes = (CANON / rel).stat().st_size
        m_bytes = (MIRROR / rel).stat().st_size
        if c_bytes != m_bytes:
            size_mismatch.append(
                {"path": str(rel), "canonical_bytes": c_bytes, "mirror_bytes": m_bytes}
            )

    return {
        "canonical_count": len(canon_files),
        "mirror_count": len(mirror_files),
        "missing_in_mirror": [str(p) for p in missing_in_mirror],
        "orphans_in_mirror": [str(p) for p in orphans_in_mirror],
        "size_mismatch": size_mismatch,
    }


def render_human(report: dict) -> str:
    lines = [
        f"canonical sources/ files: {report['canonical_count']}",
        f"mirror   site/_sources/ files: {report['mirror_count']}",
        "",
    ]
    if report["missing_in_mirror"]:
        lines.append(f"MISSING_IN_MIRROR ({len(report['missing_in_mirror'])} files)")
        for p in report["missing_in_mirror"]:
            lines.append(f"  - {p}")
        lines.append("")
    if report["size_mismatch"]:
        lines.append(f"SIZE_MISMATCH ({len(report['size_mismatch'])} files)")
        for e in report["size_mismatch"]:
            lines.append(f"  - {e['path']}: canonical {e['canonical_bytes']} bytes vs mirror {e['mirror_bytes']} bytes")
        lines.append("")
    if report["orphans_in_mirror"]:
        lines.append(f"ORPHANS_IN_MIRROR ({len(report['orphans_in_mirror'])} files)")
        for p in report["orphans_in_mirror"]:
            lines.append(f"  - {p}")
        lines.append("")
    total_problems = (
        len(report["missing_in_mirror"])
        + len(report["size_mismatch"])
        + len(report["orphans_in_mirror"])
    )
    if total_problems == 0:
        lines.append("jekyll-mirror audit OK — canonical and mirror are in sync")
    else:
        lines.append(f"jekyll-mirror audit FAIL — {total_problems} divergences")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--json", action="store_true", help="emit JSON instead of text")
    args = parser.parse_args()

    report = audit()
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(render_human(report))

    total = (
        len(report["missing_in_mirror"])
        + len(report["size_mismatch"])
        + len(report["orphans_in_mirror"])
    )
    return 0 if total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
