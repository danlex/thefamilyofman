#!/usr/bin/env python3
"""Credibility check: every referenced source_id resolves to a real source file.

This is the structural half of credibility. Tier-rubric enforcement (is this
source actually credible?) is Judge-Credibility's job.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
SRC_ID_RE = re.compile(r"\bsrc-[a-z0-9][a-z0-9-]*\b")


def _source_ids_from_frontmatter() -> set[str]:
    ids: set[str] = set()
    for path in sorted((ROOT / "sources").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        m = FRONTMATTER_RE.match(text)
        if not m:
            continue
        for line in m.group(1).splitlines():
            if line.strip().startswith("id:"):
                value = line.split(":", 1)[1].strip().strip('"').strip("'")
                if value:
                    ids.add(value)
    return ids


def _referenced_in_csvs() -> set[str]:
    refs: set[str] = set()
    for name in ("photographs.csv", "photographers.csv", "sections.csv"):
        path = ROOT / "data" / name
        if not path.exists():
            continue
        with path.open(newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                cell = row.get("source_ids", "") or ""
                for rid in SRC_ID_RE.findall(cell):
                    refs.add(rid)
    return refs


def _referenced_in_research() -> set[str]:
    refs: set[str] = set()
    for path in sorted((ROOT / "research").rglob("*.md")):
        for rid in SRC_ID_RE.findall(path.read_text(encoding="utf-8")):
            refs.add(rid)
    return refs


def _referenced_in_training() -> set[str]:
    refs: set[str] = set()
    for rel in ("training/dataset.jsonl", "training/eval/eval.jsonl"):
        path = ROOT / rel
        if not path.exists():
            continue
        with path.open() as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:
                    continue
                meta = obj.get("metadata", {}) or {}
                for key in ("source_ids", "perspective_sources"):
                    for rid in meta.get(key, []) or []:
                        if isinstance(rid, str):
                            refs.add(rid)
    for raw_dir in ("training/raw", "training/curated"):
        for path in sorted((ROOT / raw_dir).rglob("*.jsonl")):
            with path.open() as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        obj = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    meta = obj.get("metadata", {}) or {}
                    for key in ("source_ids", "perspective_sources"):
                        for rid in meta.get(key, []) or []:
                            if isinstance(rid, str):
                                refs.add(rid)
    return refs


def main() -> int:
    declared = _source_ids_from_frontmatter()
    referenced = _referenced_in_csvs() | _referenced_in_research() | _referenced_in_training()

    orphans = referenced - declared
    unused = declared - referenced  # informational, not a failure

    errors: list[str] = []
    if orphans:
        errors.append("Referenced source_ids with no matching file in sources/:")
        for rid in sorted(orphans):
            errors.append(f"  - {rid}")

    if errors:
        print("CREDIBILITY CHECK FAILED")
        for e in errors:
            print(e)
        return 1

    print(f"credibility OK — {len(declared)} sources declared, {len(referenced)} referenced")
    if unused:
        print(f"  (note: {len(unused)} sources declared but not yet referenced — not a failure)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
