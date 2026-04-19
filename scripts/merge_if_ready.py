#!/usr/bin/env python3
"""Auto-merge a PR when the 4-judge panel has spoken.

Rules:
- All 3 structural judges (Credibility, Grounding, Schema) APPROVE
- Judge-Bias is APPROVE or APPROVE-WITH-NOTES (not REJECT)
- If Bias is APPROVE-WITH-NOTES, refuse merge until the required perspective note
  has been committed (detected via a subsequent APPROVE verdict).

Identifies judge verdicts by scanning PR reviews for the structured header:
    ### Judge: <Credibility|Grounding|Schema|Bias>
    Verdict: APPROVE | APPROVE-WITH-NOTES | REJECT
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys

JUDGE_NAMES = {"Credibility", "Grounding", "Schema", "Bias"}
JUDGE_HEADER_RE = re.compile(r"^### Judge:\s*(\w+)", re.MULTILINE)
VERDICT_RE = re.compile(r"^Verdict:\s*(APPROVE-WITH-NOTES|APPROVE|REJECT)", re.MULTILINE)


def _gh(args: list[str]) -> str:
    return subprocess.check_output(["gh", *args], text=True)


def latest_verdicts(pr: int) -> dict[str, str]:
    raw = _gh(["pr", "view", str(pr), "--json", "reviews"])
    data = json.loads(raw)
    reviews = data.get("reviews", []) or []
    # Keep the most recent verdict per judge.
    latest: dict[str, tuple[str, str]] = {}  # judge -> (submittedAt, verdict)
    for r in reviews:
        body = r.get("body") or ""
        submitted = r.get("submittedAt") or ""
        m_judge = JUDGE_HEADER_RE.search(body)
        m_verdict = VERDICT_RE.search(body)
        if not (m_judge and m_verdict):
            continue
        judge = m_judge.group(1).strip()
        verdict = m_verdict.group(1).strip()
        if judge not in JUDGE_NAMES:
            continue
        prev = latest.get(judge)
        if prev is None or submitted >= prev[0]:
            latest[judge] = (submitted, verdict)
    return {j: v for j, (_, v) in latest.items()}


def decide(verdicts: dict[str, str]) -> tuple[bool, str]:
    missing = JUDGE_NAMES - verdicts.keys()
    if missing:
        return False, f"missing verdicts from: {sorted(missing)}"
    for j in ("Credibility", "Grounding", "Schema"):
        if verdicts[j] != "APPROVE":
            return False, f"Judge-{j} is {verdicts[j]}; structural approval required"
    bias = verdicts["Bias"]
    if bias == "REJECT":
        return False, "Judge-Bias is REJECT"
    if bias == "APPROVE-WITH-NOTES":
        return False, "Judge-Bias returned APPROVE-WITH-NOTES — worker must commit the perspective note"
    return True, "all judges approved"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pr", type=int, help="PR number")
    parser.add_argument("--merge", action="store_true", help="actually merge (squash)")
    args = parser.parse_args()

    verdicts = latest_verdicts(args.pr)
    ok, reason = decide(verdicts)
    print(f"PR #{args.pr} — {reason}")
    for j in sorted(JUDGE_NAMES):
        print(f"  Judge-{j}: {verdicts.get(j, '<no verdict>')}")

    if ok and args.merge:
        _gh(["pr", "merge", str(args.pr), "--squash", "--delete-branch"])
        print(f"merged PR #{args.pr}")

    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())
