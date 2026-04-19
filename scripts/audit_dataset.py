#!/usr/bin/env python3
"""Audit a JSONL training batch or the built dataset.

Checks:
- No duplicate ids
- No duplicate (user-message, perspective) pairs
- Every example has ≥1 source_id with min_tier ≤ 2
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


def _acknowledges_contestation(obj: dict) -> bool:
    for msg in obj.get("messages", []):
        if msg.get("role") == "assistant":
            text = msg.get("content", "") or ""
            if any(p.search(text) for p in CONTESTATION_PATTERNS):
                return True
    return False


def audit_jsonl(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    ids: set[str] = set()
    pairs: set[tuple[str, str]] = set()
    all_ids: set[str] = set()
    contested_examples: list[dict] = []
    interpretive_total = 0
    interpretive_critical = 0

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
        source_ids = set(meta.get("source_ids") or [])
        perspective_sources = set(meta.get("perspective_sources") or [])
        if not source_ids:
            errors.append(f"{path}:{i} {ex_id} missing source_ids")
            continue

        min_tier = meta.get("min_tier")
        if not isinstance(min_tier, int) or min_tier > 2:
            errors.append(f"{path}:{i} {ex_id} min_tier must be ≤ 2, got {min_tier!r}")

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
