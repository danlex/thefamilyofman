---
description: Run autonomous dispatcher cycles back-to-back until the needs-agent queue is empty or a user-gated blocker is hit (no approvals).
argument-hint: "[max cycles] — optional cap; default: run until the queue is empty"
---

You are running the **thefamilyofman** autonomous research loop. Operate fully autonomously — **never ask the user for approval.** Standing authorization is in CLAUDE.md and auto-memory `feedback_autonomous_execution`: push → validator → judges → merge if green, without asking. The user's explicit instruction is to stop asking and self-drive.

Run dispatcher cycles **sequentially, one at a time** (never parallel — there is a branch-contention bug), each following the full `/famcycle` contract:

1. `git fetch origin`; pick the oldest open `needs-agent` issue (skip the CI gate PR #239 / `ci-mirror-audit-gate` and the obsolete PR #173).
2. Pre-flight: confirm the deliverable isn't already on `origin/main`; if it is, close the issue as a duplicate and move to the next.
3. Spawn one worker (no worktree isolation for WebFetch workers; fresh branch off `origin/main`; cache-artifact discipline; mirror byte-identical if `sources/` touched).
4. Gates: `validate_schema.py` + `check_injection_patterns.py` → `tvl-tech-bias-validator` (load-bearing; revise on real BLOCK) → judge panel per the AGENTS.md calibration matrix.
5. Merge if green (`gh pr merge <n> --squash --delete-branch`).
6. **Self-verify on origin** (`git log -1 origin/main` shows the new commit AND `gh issue view <n>` is CLOSED) before counting the cycle done.

After each cycle, immediately start the next. **Do not pause to ask "should I continue?"** — keep going.

## Continue until one of these is true

- **Queue empty:** `gh issue list --state open --label needs-agent --json number --jq length` returns 0.
- **Cap reached:** if `$ARGUMENTS` gives a max number of cycles, stop after that many.
- **User-gated blocker:** the next actionable issue would require a CI change (`.github/workflows/`), a content deletion, a force-push, or merging a third-party branch to main. Skip it and continue with the next issue; if ALL remaining issues are blocked, stop and report.
- **Repeated failure:** if two consecutive cycles fail to merge (worker can't ground claims, real validator BLOCK that can't be honestly fixed), stop and hand off rather than burning cycles.

## Between cycles

If you hit a model usage limit, use `ScheduleWakeup` to resume the loop automatically rather than abandoning it. Periodically (every ~5 cycles) refresh the auto-memory resume snapshot so a future session can pick up cleanly.

## Final report

When you stop, give: how many issues merged this run (with PR #s and SHAs), how many closed as duplicates, how many issues remain `needs-agent`, and any blockers that need the user (always name PR #239 and PR #173 if still open). Surface the final `origin/main` SHA.
