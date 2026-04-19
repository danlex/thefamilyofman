#!/usr/bin/env python3
"""Validate CSV schemas and source-entry frontmatter."""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PHOTOGRAPHS_COLUMNS = [
    "id", "title", "photographer", "year", "country", "section",
    "moma_object_id", "clervaux_on_display", "source_ids", "notes",
]
PHOTOGRAPHERS_COLUMNS = [
    "id", "name", "birth_year", "death_year", "nationality", "gender",
    "photo_count", "bio_url", "source_ids", "notes",
]
SECTIONS_COLUMNS = [
    "id", "title", "theme", "order", "photo_ids",
    "sandburg_prologue_excerpt", "source_ids", "notes",
]

SOURCE_REQUIRED_FIELDS = {"id", "title", "year", "type", "tier", "language"}
SOURCE_TYPES = {"book", "article", "catalog", "archive", "website", "interview", "film"}
SOURCE_TIERS = {1, 2, 3}
SOURCE_LANGS = {"en", "fr", "de", "lb", "it", "es", "pt", "nl", "ja", "ru"}
CLERVAUX_VALUES = {"yes", "no", "rotating", "unknown", ""}

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


class ValidationError(Exception):
    pass


def _parse_yaml_like(text: str) -> dict:
    """Lightweight frontmatter parser — supports scalars and simple lists."""
    out: dict = {}
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            items = [v.strip().strip('"').strip("'") for v in value[1:-1].split(",") if v.strip()]
            out[key] = items
        else:
            out[key] = value.strip('"').strip("'")
    return out


def validate_csv(path: Path, expected_columns: list[str], errors: list[str]) -> set[str]:
    """Return the set of IDs in the CSV (column `id`)."""
    if not path.exists():
        errors.append(f"missing CSV: {path.relative_to(ROOT)}")
        return set()
    with path.open(newline="") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            errors.append(f"{path.relative_to(ROOT)}: empty file (no header)")
            return set()
        if header != expected_columns:
            errors.append(
                f"{path.relative_to(ROOT)}: header mismatch\n    expected: {expected_columns}\n    got:      {header}"
            )
            return set()
        ids: set[str] = set()
        for i, row in enumerate(reader, start=2):
            if len(row) != len(expected_columns):
                errors.append(
                    f"{path.relative_to(ROOT)}:{i} row has {len(row)} cols, expected {len(expected_columns)}"
                )
                continue
            row_dict = dict(zip(expected_columns, row))
            rid = row_dict.get("id", "").strip()
            if not rid:
                errors.append(f"{path.relative_to(ROOT)}:{i} missing id")
                continue
            if rid in ids:
                errors.append(f"{path.relative_to(ROOT)}:{i} duplicate id: {rid}")
            ids.add(rid)
            if path.name == "photographs.csv":
                val = row_dict.get("clervaux_on_display", "")
                if val and val not in CLERVAUX_VALUES:
                    errors.append(
                        f"{path.relative_to(ROOT)}:{i} clervaux_on_display must be one of {sorted(CLERVAUX_VALUES)}, got {val!r}"
                    )
        return ids


def validate_source_entry(path: Path, errors: list[str]) -> str | None:
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        errors.append(f"{path.relative_to(ROOT)}: missing or malformed YAML frontmatter")
        return None
    data = _parse_yaml_like(m.group(1))
    missing = SOURCE_REQUIRED_FIELDS - data.keys()
    if missing:
        errors.append(f"{path.relative_to(ROOT)}: missing required frontmatter fields: {sorted(missing)}")
    src_type = data.get("type")
    if src_type and src_type not in SOURCE_TYPES:
        errors.append(f"{path.relative_to(ROOT)}: type must be one of {sorted(SOURCE_TYPES)}, got {src_type!r}")
    try:
        tier = int(data.get("tier", ""))
        if tier not in SOURCE_TIERS:
            raise ValueError
    except ValueError:
        errors.append(f"{path.relative_to(ROOT)}: tier must be 1 | 2 | 3, got {data.get('tier')!r}")
    lang = data.get("language")
    if lang and lang not in SOURCE_LANGS:
        errors.append(f"{path.relative_to(ROOT)}: language must be one of {sorted(SOURCE_LANGS)}, got {lang!r}")
    sid = data.get("id")
    if sid and not sid.startswith("src-"):
        errors.append(f"{path.relative_to(ROOT)}: id must start with 'src-', got {sid!r}")
    return sid


def validate_training_jsonl(path: Path, errors: list[str]) -> None:
    if not path.exists():
        return
    with path.open() as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as e:
                errors.append(f"{path.relative_to(ROOT)}:{i} invalid JSON: {e}")
                continue
            for key in ("id", "messages", "metadata"):
                if key not in obj:
                    errors.append(f"{path.relative_to(ROOT)}:{i} missing key: {key}")


def main() -> int:
    errors: list[str] = []

    # CSVs
    validate_csv(ROOT / "data" / "photographs.csv", PHOTOGRAPHS_COLUMNS, errors)
    validate_csv(ROOT / "data" / "photographers.csv", PHOTOGRAPHERS_COLUMNS, errors)
    validate_csv(ROOT / "data" / "sections.csv", SECTIONS_COLUMNS, errors)

    # Sources
    source_ids: set[str] = set()
    for path in sorted((ROOT / "sources").rglob("*.md")):
        sid = validate_source_entry(path, errors)
        if sid:
            if sid in source_ids:
                errors.append(f"{path.relative_to(ROOT)}: duplicate source id: {sid}")
            source_ids.add(sid)

    # Training files
    validate_training_jsonl(ROOT / "training" / "dataset.jsonl", errors)
    validate_training_jsonl(ROOT / "training" / "eval" / "eval.jsonl", errors)

    if errors:
        print("SCHEMA VALIDATION FAILED")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("schema OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
