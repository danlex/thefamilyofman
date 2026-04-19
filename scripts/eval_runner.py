#!/usr/bin/env python3
"""Run a model against training/eval/eval.jsonl and score with an LLM judge.

Provider-agnostic: takes a callable --endpoint that runs a chat-completion.
For now this is a skeleton that loads eval.jsonl, calls a model, and writes a
scored report. Connect a real model by wiring the `call_model` function to
your provider's SDK.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def call_model(messages: list[dict], model: str) -> str:
    """Placeholder — wire to Anthropic / OpenAI / Vertex / local when ready."""
    raise NotImplementedError(
        "Connect a provider SDK here. See plan.md §13 for finetuning targets."
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="claude-opus-4-7", help="model id")
    parser.add_argument(
        "--eval",
        default=str(ROOT / "training" / "eval" / "eval.jsonl"),
        help="eval jsonl path",
    )
    parser.add_argument("--out", default=str(ROOT / "training" / "eval" / "last-run.jsonl"))
    parser.add_argument("--limit", type=int, default=0, help="0 = all")
    args = parser.parse_args()

    eval_path = Path(args.eval)
    if not eval_path.exists() or eval_path.stat().st_size == 0:
        print(f"no eval examples at {eval_path}")
        return 0

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with eval_path.open() as fin, out_path.open("w") as fout:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            ex = json.loads(line)
            messages = ex.get("messages") or []
            try:
                answer = call_model(messages, args.model)
            except NotImplementedError as e:
                print(f"eval_runner not wired: {e}", file=sys.stderr)
                return 1
            ex["model_output"] = answer
            fout.write(json.dumps(ex, ensure_ascii=False) + "\n")
            count += 1
            if args.limit and count >= args.limit:
                break

    print(f"wrote {count} outputs to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
