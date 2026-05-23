---
description: Run ONE autonomous dispatcher cycle on a needs-agent issue (no approvals).
argument-hint: "[issue number] — optional; defaults to the oldest needs-agent issue"
---

You are running a single autonomous research cycle for the **thefamilyofman** project. Operate fully autonomously — **do not ask the user for approval at any point.** The user has standing authorization (see CLAUDE.md and auto-memory `feedback_autonomous_execution`): push → validator → judges → merge if green, without asking.

## Pick the issue

If `$ARGUMENTS` names an issue number, use it. Otherwise pick the oldest open issue:

```
gh issue list --state open --label needs-agent --json number,title,createdAt --jq 'sort_by(.createdAt) | .[0]'
```

**Never** select: PR #239 / the `ci-mirror-audit-gate` branch (CI changes are user-gated), or PR #173 (obsolete, user-gated). Skip any issue labelled CI/infra that would modify `.github/workflows/`.

## Pre-flight (avoid duplicate work)

Many needs-agent issues were silently completed by earlier PRs but never relabelled. BEFORE building anything, verify the deliverable doesn't already exist on `origin/main` (`git fetch origin` first; check the target files / CSV rows / source ids named in the issue body). If it's already done, close the issue with a pointer comment to the delivering PR and stop — do not duplicate. If partially done, scope the worker to only the missing parts.

## Spawn the worker (single, sequential)

Spawn exactly one worker subagent matched to the issue category (catalog-builder, photographer-biographer, provenance-researcher, reception-analyst, tour-historian, sections-cartographer, sources-librarian-*, eval-designer, dataset-curator, or a site/general worker). Rules:

- Source-touching workers that need WebFetch → **no worktree isolation**; spawn in the main session (the worktree tool layer still denies WebFetch — see CLAUDE.md). Read-only judges may use `isolation: "worktree"`.
- Fresh branch off `origin/main`.
- The worker MUST persist `.cache-*` / `.scratch/*` artifacts for every WebFetch. Every claim naming a source (author, date, archive, institution, URL, number) must rest on a page actually fetched this session, or be explicitly labelled "not consulted in this round". **Zero artifacts on a Tier-1/2 claim = confabulation BLOCK.**
- Cross-check any `photo_count` / plate number / date against the in-repo CSVs and the MoMA master checklist — never guess.
- If it touches `sources/`, keep the `site/_sources/` mirror byte-identical (`python3 scripts/audit_jekyll_mirror.py`).

## Gates (in order)

1. `python3 scripts/validate_schema.py` and `python3 scripts/check_injection_patterns.py` — must pass.
2. **`tvl-tech-bias-validator` on the PR diff BEFORE judges.** It is load-bearing — it has caught misattributed quotes, ungrounded rosters, tier inflation, and an untested template conditional. If it BLOCKs on real museum-grade confabulation, **revise the worker output** before continuing. Do not merge through a real BLOCK. (Genuine false positives may be overridden with a logged reason.)
3. Judge panel per the AGENTS.md calibration matrix: photographer-bio batches and high-stakes plates get the FULL 4-judge panel; low-stakes per-photograph notes get Schema+Grounding full, Credibility spot, Bias light. Contested/interpretive claims (Barthes/Sontag/Sekula territory) escalate Bias to full.

## Merge + self-verify

If green, merge: `gh pr merge <n> --squash --delete-branch`. Then **independently verify origin ground truth** before reporting success:

```
git fetch origin && git log --oneline -1 origin/main   # new commit present?
gh issue view <n> --json state                          # CLOSED?
```

Only claim success if BOTH are true. A dispatcher's report is not proof — the origin check is.

## Stop conditions (return a clean handoff, never silently retry)

- The change would modify CI (`.github/workflows/`), delete content, force-push, or merge a third-party branch to main → **stop and surface to the user** (these remain user-gated).
- The worker fails twice or can't ground its claims after one revision → return a handoff note describing the defect.
- A real validator BLOCK that can't be honestly fixed → return with the finding.

## Report

One tight summary: issue #, PR #, validator verdict, judge verdicts, merged SHA (or stop reason), and whether the issue is CLOSED on origin. Then **stop — exactly one cycle.** (For continuous operation the caller uses `/famloop`.)
