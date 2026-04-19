#!/usr/bin/env python3
"""Build training/dataset.jsonl from training/curated/*.jsonl.

Rules:
- Every curated example must have metadata.reviewed == true
- Every example must have ≥1 source_id with min_tier <= 2
- No duplicate ids
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CURATED = ROOT / "training" / "curated"
OUT = ROOT / "training" / "dataset.jsonl"


def main() -> int:
    if not CURATED.exists():
        print(f"no curated directory at {CURATED}", file=sys.stderr)
        return 1

    examples: dict[str, dict] = {}
    errors: list[str] = []

    for path in sorted(CURATED.rglob("*.jsonl")):
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
                ex_id = obj.get("id")
                meta = obj.get("metadata", {}) or {}
                if not ex_id:
                    errors.append(f"{path.relative_to(ROOT)}:{i} missing id")
                    continue
                if not meta.get("reviewed"):
                    errors.append(f"{path.relative_to(ROOT)}:{i} example {ex_id} not reviewed")
                    continue
                min_tier = meta.get("min_tier")
                if not isinstance(min_tier, int) or min_tier > 2:
                    errors.append(
                        f"{path.relative_to(ROOT)}:{i} example {ex_id} min_tier must be ≤ 2, got {min_tier!r}"
                    )
                    continue
                if not meta.get("source_ids"):
                    errors.append(f"{path.relative_to(ROOT)}:{i} example {ex_id} missing source_ids")
                    continue
                if ex_id in examples:
                    errors.append(f"{path.relative_to(ROOT)}:{i} duplicate id {ex_id}")
                    continue
                examples[ex_id] = obj

    if errors:
        print("BUILD FAILED")
        for e in errors:
            print(f"  - {e}")
        return 1

    with OUT.open("w") as f:
        for ex_id in sorted(examples):
            f.write(json.dumps(examples[ex_id], ensure_ascii=False) + "\n")

    print(f"built {OUT.relative_to(ROOT)} — {len(examples)} examples")
    return 0


if __name__ == "__main__":
    sys.exit(main())
