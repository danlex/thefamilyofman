#!/usr/bin/env python3
"""
Scan sources/ and research/ for known prompt-injection markers.

Non-zero exit if any marker is found. Surfaces the file + line + pattern
for human review — does not auto-reject. False positives are expected
(e.g. a source file may legitimately quote a historical passage that
happens to contain "ignore") so the human decides.

Run as part of the pre-PR checklist for museum-grade accuracy. See
CLAUDE.md § Prompt-injection defense.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCAN_ROOTS = [REPO_ROOT / "sources", REPO_ROOT / "research"]

# (pattern, label, flags). Keep each pattern narrow to reduce false positives.
PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"ignore\s+(?:all\s+)?previous\s+instructions", re.I), "ignore-previous-instructions"),
    (re.compile(r"you\s+are\s+now\s+(?:a|an)\s+\w", re.I), "you-are-now"),
    (re.compile(r"(?:^|\n)\s*(?:system|assistant|user)\s*:\s", re.I), "role-prefix-line"),
    (re.compile(r"<\|im_start\|>|<\|im_end\|>"), "chatml-control-token"),
    (re.compile(r"\[INST\]|\[/INST\]"), "llama-inst-token"),
    (re.compile(r"<script[\s>]", re.I), "script-tag"),
    (re.compile(r"javascript:", re.I), "javascript-uri"),
    (re.compile(r"data:text/html", re.I), "data-html-uri"),
    (re.compile(r"<!--.+?-->", re.S), "html-comment"),
    # Zero-width and directional override characters.
    (re.compile(r"[​-‏‪-‮⁦-⁩]"), "zero-width-or-bidi"),
    # Unicode tag characters (often used for steganographic prompt injection).
    (re.compile(r"[\U000E0020-\U000E007F]"), "unicode-tag-char"),
    # Claimed identity.
    (re.compile(r"(?:from|as)\s+(?:anthropic|openai)\s+(?:engineer|admin|staff)", re.I), "vendor-authority-claim"),
]


def scan_file(path: Path) -> list[tuple[int, str, str]]:
    hits: list[tuple[int, str, str]] = []
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return hits
    for i, line in enumerate(text.splitlines(), start=1):
        for pattern, label in PATTERNS:
            if pattern.search(line):
                hits.append((i, label, line.strip()[:200]))
    return hits


def main() -> int:
    any_hit = False
    for root in SCAN_ROOTS:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.md")):
            hits = scan_file(path)
            if not hits:
                continue
            any_hit = True
            rel = path.relative_to(REPO_ROOT)
            for lineno, label, snippet in hits:
                print(f"{rel}:{lineno}: [{label}] {snippet}")

    if any_hit:
        print(
            "\ninjection-scan: matches found. Review each match — this is a surface, "
            "not a verdict. See CLAUDE.md § Prompt-injection defense.",
            file=sys.stderr,
        )
        return 1

    print("injection-scan OK — no markers matched")
    return 0


if __name__ == "__main__":
    sys.exit(main())
