#!/usr/bin/env python3
"""Audit a JSONL training batch or the built dataset.

Checks:
- No duplicate ids
- No duplicate (user-message, perspective) pairs
- Every example has ≥1 source_id with min_tier ≤ 2
- Declared min_tier matches the actual minimum tier among cited sources
  (i.e. `min_tier == min(tier(src) for src in source_ids)`, where the
  per-source tier is read from the YAML frontmatter of the matching file
  in `sources/`)
- contested==true examples either have counter_perspective_id OR assistant message acknowledges contestation
- perspective_sources ⊆ source_ids
- ≥25% of interpretive examples carry perspective=critical (soft check — warns)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = ROOT / "sources"

INTERPRETIVE_TOPICS = {"reception", "exhibition-history"}

CONTESTATION_PATTERNS = [
    re.compile(r"\bcontested\b", re.I),
    re.compile(r"\bcritiqued\b", re.I),
    re.compile(r"\bargue[ds]?\b", re.I),
    re.compile(r"\bBarthes\b"),
    re.compile(r"\bSontag\b"),
    re.compile(r"\bSekula\b"),
    re.compile(r"\bSandeen\b"),
    re.compile(r"\bStimson\b"),
    re.compile(r"\bTurner\b"),
]

# Pattern to extract `id:` and `tier:` from YAML frontmatter without pulling
# in PyYAML as a dependency.
_FRONT_ID_RE = re.compile(r"^id:\s*([^\s#]+)", re.MULTILINE)
_FRONT_TIER_RE = re.compile(r"^tier:\s*([0-9]+)", re.MULTILINE)


def build_source_tier_map(sources_dir: Path = SOURCES_DIR) -> dict[str, int]:
    """Scan `sources/**/*.md` once and return {src_id: tier_int}.

    Reads the YAML frontmatter of each source file. Files missing either
    `id:` or `tier:` are skipped silently — those are caught by
    `scripts/validate_schema.py`, not here.
    """
    tier_map: dict[str, int] = {}
    if not sources_dir.exists():
        return tier_map
    for path in sources_dir.rglob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        # Only inspect the frontmatter block (between the first two `---`)
        if not text.startswith("---"):
            continue
        end = text.find("\n---", 3)
        front = text[:end] if end != -1 else text
        m_id = _FRONT_ID_RE.search(front)
        m_tier = _FRONT_TIER_RE.search(front)
        if not m_id or not m_tier:
            continue
        tier_map[m_id.group(1).strip()] = int(m_tier.group(1))
    return tier_map


def _row_source_ids(obj: dict) -> list[str]:
    """Return source_ids for a row, supporting both the eval format
    (`metadata.source_ids`) and the legacy/training top-level format
    (`source_ids`)."""
    meta = obj.get("metadata", {}) or {}
    if isinstance(meta.get("source_ids"), list):
        return list(meta["source_ids"])
    if isinstance(obj.get("source_ids"), list):
        return list(obj["source_ids"])
    return []


def _row_min_tier(obj: dict):
    """Return declared min_tier for a row, supporting both row formats."""
    meta = obj.get("metadata", {}) or {}
    if "min_tier" in meta:
        return meta.get("min_tier")
    return obj.get("min_tier")


def _acknowledges_contestation(obj: dict) -> bool:
    for msg in obj.get("messages", []):
        if msg.get("role") == "assistant":
            text = msg.get("content", "") or ""
            if any(p.search(text) for p in CONTESTATION_PATTERNS):
                return True
    return False


def audit_jsonl(
    path: Path,
    src_tier_map: dict[str, int] | None = None,
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    ids: set[str] = set()
    pairs: set[tuple[str, str]] = set()
    all_ids: set[str] = set()
    contested_examples: list[dict] = []
    interpretive_total = 0
    interpretive_critical = 0
    if src_tier_map is None:
        src_tier_map = build_source_tier_map()

    examples: list[tuple[int, dict]] = []
    with path.open() as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                examples.append((i, json.loads(line)))
            except json.JSONDecodeError as e:
                errors.append(f"{path}:{i} invalid JSON: {e}")

    for _, obj in examples:
        if (ex_id := obj.get("id")):
            all_ids.add(ex_id)

    for i, obj in examples:
        ex_id = obj.get("id", f"<row-{i}>")
        if ex_id in ids:
            errors.append(f"{path}:{i} duplicate id {ex_id}")
        ids.add(ex_id)

        meta = obj.get("metadata", {}) or {}
        source_ids_list = _row_source_ids(obj)
        source_ids = set(source_ids_list)
        perspective_sources = set(meta.get("perspective_sources") or [])
        if not source_ids:
            errors.append(f"{path}:{i} {ex_id} missing source_ids")
            continue

        min_tier = _row_min_tier(obj)
        if not isinstance(min_tier, int) or min_tier > 2:
            errors.append(f"{path}:{i} {ex_id} min_tier must be ≤ 2, got {min_tier!r}")

        # Cross-check the declared min_tier against the actual minimum tier
        # among the cited sources (read from sources/**/*.md frontmatter).
        # This catches rows that declare a credibility floor stronger than
        # their citations actually support — see issue #138.
        if isinstance(min_tier, int):
            per_source: list[tuple[str, int | None]] = [
                (sid, src_tier_map.get(sid)) for sid in source_ids_list
            ]
            unknown = [sid for sid, t in per_source if t is None]
            if unknown:
                errors.append(
                    f"{path}:{i} {ex_id} unknown source_ids (no matching "
                    f"sources/**/*.md): {sorted(unknown)}"
                )
            known_tiers = [t for _, t in per_source if t is not None]
            if known_tiers:
                actual_min_tier = min(known_tiers)
                if actual_min_tier != min_tier:
                    breakdown = ", ".join(
                        f"{sid}:{t if t is not None else '?'}"
                        for sid, t in per_source
                    )
                    errors.append(
                        f"{path}:{i} {ex_id} min_tier mismatch: declared "
                        f"{min_tier}, actual {actual_min_tier} "
                        f"(sources: {breakdown})"
                    )

        if not perspective_sources.issubset(source_ids):
            errors.append(
                f"{path}:{i} {ex_id} perspective_sources must be subset of source_ids: "
                f"{sorted(perspective_sources - source_ids)}"
            )

        # dedupe key: first user content + perspective
        user_text = ""
        for msg in obj.get("messages", []):
            if msg.get("role") == "user":
                user_text = msg.get("content", "")
                break
        pair = (user_text.strip().lower(), meta.get("perspective", ""))
        if pair in pairs and user_text:
            errors.append(f"{path}:{i} {ex_id} duplicate (user-message, perspective) pair")
        pairs.add(pair)

        if meta.get("contested"):
            contested_examples.append(obj)
            counter = meta.get("counter_perspective_id")
            if counter:
                if counter not in all_ids:
                    errors.append(
                        f"{path}:{i} {ex_id} counter_perspective_id {counter!r} does not resolve"
                    )
            else:
                if not _acknowledges_contestation(obj):
                    errors.append(
                        f"{path}:{i} {ex_id} contested=true but no counter_perspective_id and no "
                        f"inline contestation acknowledgment"
                    )

        topic = meta.get("topic")
        if topic in INTERPRETIVE_TOPICS:
            interpretive_total += 1
            if meta.get("perspective") == "critical":
                interpretive_critical += 1

    if interpretive_total and interpretive_critical / interpretive_total < 0.25:
        warnings.append(
            f"critical-perspective floor: {interpretive_critical}/{interpretive_total} "
            f"({interpretive_critical/interpretive_total:.0%}) — target ≥25%"
        )

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path",
        nargs="?",
        default=str(ROOT / "training" / "dataset.jsonl"),
        help="Path to a jsonl file to audit (default: training/dataset.jsonl)",
    )
    args = parser.parse_args()
    path = Path(args.path)
    if not path.exists():
        print(f"no file at {path}", file=sys.stderr)
        return 0  # empty is fine at Phase 0

    errors, warnings = audit_jsonl(path)

    for w in warnings:
        print(f"WARN: {w}")

    if errors:
        print("AUDIT FAILED")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"audit OK ({path})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
