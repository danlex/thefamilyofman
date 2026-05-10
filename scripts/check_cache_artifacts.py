#!/usr/bin/env python3
"""Pre-judge / pre-merge cache-artifact audit.

Detects the failure mode caught in PR #173: a worker claiming "fresh-fetch
2026-MM-DD" verbatim quotes while leaving zero cache artifacts in its
worktree. See `feedback_subagent_cache_artifacts.md` and CLAUDE.md
§ "Museum-grade accuracy".

Usage:
    python3 scripts/check_cache_artifacts.py <worktree-path>
    python3 scripts/check_cache_artifacts.py . --json

Pure stdlib. Read-only on the repo. Exits non-zero when:
  - a changed source/research file claims a fresh fetch (`fetched 2026-MM-DD`,
    `Fresh fetch`, `Direct fetch`) for a URL whose domain has no matching cache
    artifact, OR
  - a changed `research/*.md` essay block-quotes (`> "..."`) a `src-*` ID whose
    `sources/*.md` file is `verified: false` and explicitly annotated as
    `NOT fetched` / `not consulted in this round`.

The check is a *floor*, not a guarantee — quote-vs-cache content match remains
the grounding judge's job. False positives are expected (a worker may legitimately
re-quote a previously-cached source, or annotate a fetch with a non-standard
phrase). The script names the file + line + cited URL or src-id so a human can
disambiguate quickly.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

# ---------------------------------------------------------------------------
# Patterns
# ---------------------------------------------------------------------------

# Fresh-fetch attribution patterns that workers use in research / source notes.
# Match a date-bearing claim of having pulled the bytes in *this* round.
FRESH_FETCH_RE = re.compile(
    r"(?:"
    r"fetched\s+20\d{2}-\d{2}-\d{2}"
    r"|Fresh\s+fetch\s+20\d{2}-\d{2}-\d{2}"
    r"|Direct\s+fetch\s+20\d{2}-\d{2}-\d{2}"
    r"|retrieved\s+(?:via\s+\w+\s+)?(?:on\s+)?20\d{2}-\d{2}-\d{2}"
    r"|20\d{2}-\d{2}-\d{2}\s+via\s+curl"
    r")",
    re.IGNORECASE,
)

# A URL — captured greedily up to whitespace, closing-bracket / paren, or quote.
URL_RE = re.compile(r"https?://[^\s\)\]\>\"'`]+", re.IGNORECASE)

# A src-id reference. Matches CLAUDE.md / check_credibility.py convention.
SRC_ID_RE = re.compile(r"\bsrc-[a-z0-9][a-z0-9-]*\b")

# A blockquote line — markdown `> ...`. We check for *any* blockquote near the
# src-id; verbatim-vs-paraphrase is the grounding judge's call.
BLOCKQUOTE_RE = re.compile(r"^\s*>\s")

# Frontmatter block at the top of a markdown file.
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)

# Annotations workers use to flag "I did NOT actually fetch this in this round".
NOT_FETCHED_RE = re.compile(
    r"(?:NOT\s+fetched|not\s+(?:re-)?fetched|not\s+consulted\s+in\s+this\s+round"
    r"|NOT\s+consulted\s+(?:in\s+)?this\s+round|claim\s+carried\s+from"
    r"|cited\s+in\s+secondary\s+literature\s+but\s+not\s+(?:accessed|consulted))",
    re.IGNORECASE,
)

# Cache-artifact glob roots. Workers may stash either at the worktree root
# (`.cache-<slug>.{html,pdf}`) or under `.scratch/` / `.tmp_fetched/`.
CACHE_GLOBS = (
    ".cache-*.html",
    ".cache-*.pdf",
    ".scratch/*.html",
    ".scratch/*.pdf",
    ".tmp_fetched/*.html",
    ".tmp_fetched/*.pdf",
)

# When a cited domain is a generic CDN / archive shim, a literal-substring
# domain match in cache filenames is unfair (cached files almost never embed
# `archive.org`-style hostnames). Normalize to the canonical authority.
DOMAIN_ALIASES: dict[str, tuple[str, ...]] = {
    "web.archive.org": ("archive", "wayback"),
    "doi.org": ("doi",),
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _run(cmd: list[str], cwd: Path) -> str:
    """Run a subprocess, returning stdout. Empty string on non-zero / OSError."""
    try:
        out = subprocess.run(
            cmd, cwd=str(cwd), capture_output=True, text=True, check=False
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    return out.stdout


def changed_files(worktree: Path) -> list[Path]:
    """Files changed vs origin/main in this worktree.

    Falls back to all sources/ + research/ markdown files when the diff
    command produces no output (detached HEAD, no remote, or the script is
    being run as a one-shot audit on a clean tree).
    """
    raw = _run(
        ["git", "diff", "origin/main...HEAD", "--name-only"], cwd=worktree
    )
    names = [n.strip() for n in raw.splitlines() if n.strip()]
    if not names:
        # Fall back to porcelain: covers staged, unstaged, and untracked.
        raw = _run(["git", "status", "--porcelain"], cwd=worktree)
        names = []
        for line in raw.splitlines():
            line = line.rstrip("\n")
            # porcelain v1: " M path" / "?? path" / "A  path" — strip first 3 chars.
            if len(line) > 3:
                names.append(line[3:].strip())
    candidates: list[Path] = []
    for n in names:
        # `git status --porcelain` may emit `orig -> new` for renames; take new.
        if " -> " in n:
            n = n.split(" -> ", 1)[1]
        # Untracked-directory entries appear as `dir/`; expand them.
        if n.endswith("/"):
            sub_root = (worktree / n).resolve()
            if sub_root.is_dir():
                candidates.extend(
                    f for f in sub_root.rglob("*.md") if f.is_file()
                )
            continue
        p = (worktree / n).resolve()
        if p.exists():
            candidates.append(p)
    # Restrict to markdown under sources/ or research/.
    paths: list[Path] = []
    wt_resolved = worktree.resolve()
    for p in candidates:
        try:
            rel = p.relative_to(wt_resolved)
        except ValueError:
            continue
        if rel.suffix != ".md":
            continue
        parts = rel.parts
        if not parts:
            continue
        if parts[0] not in ("sources", "research"):
            continue
        paths.append(p)
    return sorted(set(paths))


def list_cache_artifacts(worktree: Path) -> list[Path]:
    """Return all cache-artifact files matching the recognized globs."""
    found: list[Path] = []
    for glob in CACHE_GLOBS:
        # Path.glob handles `dir/*.ext`; root globs work directly.
        for p in worktree.glob(glob):
            if p.is_file():
                found.append(p)
    return sorted(set(found))


def domain_of(url: str) -> str:
    """Return the registrable-ish hostname for `url` — strips `www.` and port."""
    try:
        netloc = urlparse(url).netloc.lower()
    except ValueError:
        return ""
    if not netloc:
        return ""
    # Drop user:pass@ and port.
    if "@" in netloc:
        netloc = netloc.rsplit("@", 1)[1]
    if ":" in netloc:
        netloc = netloc.split(":", 1)[0]
    if netloc.startswith("www."):
        netloc = netloc[4:]
    return netloc


def domain_keys(url: str) -> list[str]:
    """Return candidate substrings for matching against cache filenames.

    We try the full hostname, then progressively shorter labels (so
    `journalpanorama.org` also matches a cache file named `panorama-2024.pdf`).
    Aliases (web.archive.org → archive / wayback) are appended so a cache file
    named `.cache-wayback-foo.html` matches a `web.archive.org/...` URL.
    """
    netloc = domain_of(url)
    if not netloc:
        return []
    parts = netloc.split(".")
    keys: list[str] = []
    if netloc:
        keys.append(netloc)
    # The 2nd-level label is usually the most distinctive (`panorama`,
    # `steichencollections-cna`). Add it explicitly.
    if len(parts) >= 2:
        keys.append(parts[-2])
    # Hyphenated 2LDs — `steichencollections-cna` — are already in netloc;
    # also seed each hyphen-segment as a fallback.
    if len(parts) >= 2 and "-" in parts[-2]:
        keys.extend(seg for seg in parts[-2].split("-") if seg)
    keys.extend(DOMAIN_ALIASES.get(netloc, ()))
    # De-duplicate while preserving order; drop empties and 1-char strings
    # (would match almost anything).
    seen: set[str] = set()
    out: list[str] = []
    for k in keys:
        k = k.lower()
        if len(k) < 2 or k in seen:
            continue
        seen.add(k)
        out.append(k)
    return out


def cache_matches_url(url: str, cache_paths: list[Path]) -> list[Path]:
    """Cache files whose name contains any domain-key for `url`."""
    keys = domain_keys(url)
    if not keys:
        return []
    matches: list[Path] = []
    for c in cache_paths:
        name = c.name.lower()
        if any(k in name for k in keys):
            matches.append(c)
    return matches


def parse_frontmatter(text: str) -> dict[str, str]:
    """Best-effort YAML-ish frontmatter parse — keys → string values.

    Pure stdlib; we only need a few scalar fields (id, verified). Lists and
    nested dicts are not parsed.
    """
    out: dict[str, str] = {}
    m = FRONTMATTER_RE.match(text)
    if not m:
        return out
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        if line.lstrip().startswith("- "):
            continue
        key, _, val = line.partition(":")
        out[key.strip()] = val.strip().strip('"').strip("'")
    return out


# ---------------------------------------------------------------------------
# Audit passes
# ---------------------------------------------------------------------------


def find_fresh_fetch_claims(
    paths: list[Path], worktree: Path
) -> list[dict[str, object]]:
    """For each file with a fresh-fetch line, record the URL(s) on the
    same or adjacent lines (a 1-line look-back / look-ahead window).
    """
    claims: list[dict[str, object]] = []
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        lines = text.splitlines()
        for i, line in enumerate(lines):
            if not FRESH_FETCH_RE.search(line):
                continue
            window = "\n".join(lines[max(0, i - 1) : i + 2])
            urls = URL_RE.findall(window)
            # Also collect URLs from up-to-3-line look-back, which catches
            # `[src-foo; PDF fetched 2026-05-09 at\nhost/path]` patterns.
            if not urls:
                window = "\n".join(lines[max(0, i - 3) : i + 4])
                urls = URL_RE.findall(window)
            urls = [u.rstrip(".,;:)") for u in urls]
            urls = sorted(set(urls))
            try:
                rel = str(path.relative_to(worktree.resolve()))
            except ValueError:
                rel = str(path)
            claims.append(
                {
                    "file": rel,
                    "line": i + 1,
                    "snippet": line.strip()[:200],
                    "urls": urls,
                }
            )
    return claims


def find_unverified_quote_pattern(
    paths: list[Path], worktree: Path
) -> list[dict[str, object]]:
    """For each changed `research/*.md` file, pair `src-*` references with
    nearby blockquotes; if the cited source file is `verified: false` AND
    annotated with a `NOT fetched` phrase, flag the pairing.

    Heuristic: a source-id is "near" a blockquote if a `> ` line appears
    within 8 lines after the source-id mention, OR the source-id appears
    within 8 lines before/after a blockquote line.
    """
    # Build a map of src-id → (verified-flag, has_not_fetched_annotation, file).
    src_state: dict[str, dict[str, object]] = {}
    sources_root = worktree / "sources"
    if sources_root.exists():
        for sp in sources_root.rglob("*.md"):
            try:
                text = sp.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            fm = parse_frontmatter(text)
            sid = fm.get("id", "")
            if not sid:
                continue
            verified = fm.get("verified", "").strip().lower()
            has_not_fetched = bool(NOT_FETCHED_RE.search(text))
            try:
                rel = str(sp.relative_to(worktree.resolve()))
            except ValueError:
                rel = str(sp)
            src_state[sid] = {
                "verified": verified,
                "has_not_fetched": has_not_fetched,
                "file": rel,
            }

    findings: list[dict[str, object]] = []
    for path in paths:
        try:
            rel = path.relative_to(worktree.resolve())
        except ValueError:
            continue
        if rel.parts[0] != "research":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        lines = text.splitlines()
        # Index blockquote line numbers for fast proximity test.
        blockquote_lines = [
            i for i, ln in enumerate(lines) if BLOCKQUOTE_RE.match(ln)
        ]
        if not blockquote_lines:
            continue
        bq_set = sorted(set(blockquote_lines))
        for i, line in enumerate(lines):
            for sid in SRC_ID_RE.findall(line):
                state = src_state.get(sid)
                if not state:
                    continue
                if state["verified"] != "false":
                    continue
                if not state["has_not_fetched"]:
                    continue
                # Proximity check: any blockquote within +/- 8 lines.
                window = range(max(0, i - 8), min(len(lines), i + 9))
                if not any(b in window for b in bq_set):
                    continue
                # Find nearest blockquote line for the report.
                nearest_bq = min(bq_set, key=lambda b: abs(b - i))
                findings.append(
                    {
                        "research_file": str(rel),
                        "line": i + 1,
                        "src_id": sid,
                        "source_file": state["file"],
                        "nearest_blockquote_line": nearest_bq + 1,
                        "blockquote_snippet": lines[nearest_bq].strip()[:200],
                    }
                )
    # De-duplicate (file, src_id, blockquote-line) triples.
    seen: set[tuple[str, str, int]] = set()
    deduped: list[dict[str, object]] = []
    for f in findings:
        key = (
            str(f["research_file"]),
            str(f["src_id"]),
            int(f["nearest_blockquote_line"]),
        )
        if key in seen:
            continue
        seen.add(key)
        deduped.append(f)
    return deduped


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def audit(worktree: Path) -> dict[str, object]:
    worktree = worktree.resolve()
    cache_paths = list_cache_artifacts(worktree)
    cache_total_bytes = sum(p.stat().st_size for p in cache_paths if p.exists())

    paths = changed_files(worktree)

    fresh_claims = find_fresh_fetch_claims(paths, worktree)

    unmatched: list[dict[str, object]] = []
    matched: list[dict[str, object]] = []
    for claim in fresh_claims:
        urls = list(claim.get("urls") or [])  # type: ignore[arg-type]
        for url in urls:
            hits = cache_matches_url(url, cache_paths)
            entry = {
                "file": claim["file"],
                "line": claim["line"],
                "url": url,
                "domain": domain_of(url),
                "snippet": claim["snippet"],
                "matching_cache_files": [
                    str(p.relative_to(worktree)) for p in hits
                ],
            }
            if hits:
                matched.append(entry)
            else:
                unmatched.append(entry)

    confab_candidates = find_unverified_quote_pattern(paths, worktree)

    return {
        "worktree": str(worktree),
        "changed_files_audited": [
            str(p.relative_to(worktree)) for p in paths
        ],
        "cache_artifacts": {
            "count": len(cache_paths),
            "total_bytes": cache_total_bytes,
            "files": [str(p.relative_to(worktree)) for p in cache_paths],
        },
        "fresh_fetch_claims_total": len(fresh_claims),
        "fresh_fetch_urls_matched": matched,
        "fresh_fetch_urls_unmatched": unmatched,
        "unverified_quote_candidates": confab_candidates,
    }


def render_human(report: dict[str, object]) -> str:
    out: list[str] = []
    cache = report["cache_artifacts"]  # type: ignore[index]
    out.append(f"worktree: {report['worktree']}")
    out.append(
        f"cache artifacts: {cache['count']} file(s), "  # type: ignore[index]
        f"{cache['total_bytes']} bytes"  # type: ignore[index]
    )
    files = cache.get("files") or []  # type: ignore[union-attr]
    for f in files:  # type: ignore[union-attr]
        out.append(f"  - {f}")
    audited = report.get("changed_files_audited") or []
    out.append(f"changed source/research files audited: {len(audited)}")
    for f in audited:  # type: ignore[union-attr]
        out.append(f"  - {f}")
    out.append(
        f"fresh-fetch claims found: {report['fresh_fetch_claims_total']}"
    )

    matched = report.get("fresh_fetch_urls_matched") or []
    unmatched = report.get("fresh_fetch_urls_unmatched") or []
    out.append(
        f"  - URLs with matching cache file: {len(matched)}"  # type: ignore[arg-type]
    )
    out.append(
        f"  - URLs without matching cache file: {len(unmatched)}"  # type: ignore[arg-type]
    )

    if unmatched:
        out.append("")
        out.append("FAIL: fresh-fetch URLs with no matching cache artifact:")
        for entry in unmatched:  # type: ignore[union-attr]
            out.append(
                f"  - {entry['file']}:{entry['line']}  "
                f"[{entry['domain']}]  {entry['url']}"
            )
            out.append(f"      ⤷ {entry['snippet']}")

    confabs = report.get("unverified_quote_candidates") or []
    if confabs:
        out.append("")
        out.append(
            "FAIL: research blockquote near a src-id whose source is "
            "verified:false + annotated NOT fetched:"
        )
        for c in confabs:  # type: ignore[union-attr]
            out.append(
                f"  - {c['research_file']}:{c['line']}  src-id "
                f"{c['src_id']} (source: {c['source_file']})"
            )
            out.append(
                f"      blockquote @ line {c['nearest_blockquote_line']}: "
                f"{c['blockquote_snippet']}"
            )

    if not unmatched and not confabs:
        out.append("")
        out.append("cache-artifact audit OK")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Pre-judge cache-artifact audit. Detects fresh-fetch claims "
            "with no cache file and verbatim quotes against verified:false "
            "sources. See feedback_subagent_cache_artifacts.md."
        )
    )
    parser.add_argument(
        "worktree",
        nargs="?",
        default=".",
        help="path to the worktree to audit (default: current directory)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit the structured report as JSON instead of human-readable text",
    )
    args = parser.parse_args(argv)

    worktree = Path(args.worktree)
    if not worktree.exists() or not worktree.is_dir():
        print(
            f"check_cache_artifacts: not a directory: {worktree}",
            file=sys.stderr,
        )
        return 2

    report = audit(worktree)

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(render_human(report))

    fail = bool(report.get("fresh_fetch_urls_unmatched")) or bool(
        report.get("unverified_quote_candidates")
    )
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
