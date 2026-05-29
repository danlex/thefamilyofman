# AGENTS — workflow contract

How investigations move from a GitHub issue to merged, validated research.

## Roles

- **Dispatcher** — polls issues, claims the next one, spawns workers and judges.
- **Worker** — a specialized research subagent (catalog builder, photographer biographer, historian, sources librarian, etc.). 11 research roles + a generic wrapper.
- **Judges (4)** — review every PR in parallel:
  - **Judge-Credibility** (Opus): citations are valid and meet the tier rubric
  - **Judge-Grounding** (Sonnet): statements faithfully paraphrase cited sources
  - **Judge-Schema** (Haiku): CSVs, frontmatter, and file layout conform
  - **Judge-Bias** (Opus): confirmation bias, confabulation, hallucination, framing bias, omitted counter-perspectives
- **Dataset Curator** — converts merged research into training examples.
- **Eval Designer** — maintains the held-out evaluation set.
- **Dataset Auditor** — checks duplicates, tier violations, bias distribution before release.

Full role definitions live in `.claude/agents/`.

## Lifecycle of an investigation

1. **Seed.** A human or another agent creates a GitHub issue using one of the templates in `.github/ISSUE_TEMPLATE/`. Labels: `investigation` + category + `needs-agent` + priority.
2. **Claim.** Dispatcher (`gh issue list --label needs-agent --state open`) picks the highest-priority oldest issue, assigns itself, replaces `needs-agent` with `in-progress`.
3. **Work.** Dispatcher spawns a Worker subagent matched to the category. Worker:
   - Reads the issue body as its brief
   - Creates branch `agent/<slug>-#<n>`
   - Produces files per the issue's acceptance criteria
   - Opens a PR titled `[#<n>] <summary>` with body `Closes #<n>` + the PR checklist
4. **Review.** Dispatcher spawns the 4 judges in parallel, each with the PR diff as input. Each posts a structured review.
5. **Verdict.**
   - All 3 structural judges APPROVE **and** Judge-Bias ≠ REJECT → `scripts/merge_if_ready.py` auto-merges (`gh pr merge --squash`).
   - Judge-Bias returns APPROVE-WITH-NOTES → worker commits the required perspective-note block, then merge proceeds.
   - 1 REJECT → worker revises with that judge's rationale. Max **2 revision cycles**. If still not unanimous, label `escalated` and notify user.
   - 2+ REJECT → PR closed with `rejected-by-panel`; follow-up issue opened summarizing blockers.
6. **Curate.** On merge that touches `data/`, `sources/`, or `research/`, Dataset Curator opens a `training-curation` issue proposing new training examples. Dataset Auditor comments. User approves. Examples merge into `training/curated/`. `scripts/build_dataset.py` regenerates `training/dataset.jsonl`.

## Branch & PR conventions

- Branch: `agent/<slug>-#<issue-number>` — e.g., `agent/photog-batch-01-#12`
- PR title: `[#<n>] <imperative summary>`
- PR body must include:
  - `Closes #<n>`
  - **Summary** — what the PR does
  - **Sources used** — bullet list of `source_ids`
  - **Schema checks** — confirm `validate_schema.py` passes locally
  - **Perspective tagging** — declare perspective(s) touched; note any contested claims

## Judge-panel calibration by PR type

Not every PR needs all 4 judges. Apply the matrix below; spawn only the judges marked ✓.

| PR type | Schema | Credibility | Grounding | Bias |
|---|:---:|:---:|:---:|:---:|
| Sources / research bibliography (sources/, research/*reception*) | ✓ | ✓ | ✓ | ✓ |
| Per-photograph research notes (research/photographs/) | ✓ | spot-check | ✓ | only if ≥2 high-stakes plates (H-bomb, closing image, Section 40, contested photographers) |
| Site infrastructure (scripts/, site/_layouts/, site/_includes/) — pure code, no factual claims | ✓ | — | — | — |
| Site content pages with prose claims (site/*.md outside _photographs/) | ✓ | ✓ | ✓ | ✓ |
| Photographer biography batches (data/photographers.csv + research/photographers/) | ✓ | ✓ | ✓ | ✓ |
| Mindmap / progress.yml / dashboards | ✓ | — | spot-check | — |

**Spot-check** = the orchestrator (not a spawned judge) greps the diff for the recurring failure modes: fabricated-verbatim quotes, orphan src-ids, tier inflation, Wayne Miller curatorial-assistant claim. If clean, skip the judge; if anything suspicious, spawn the relevant judge.

**Rationale:** the Schema judge is fast and mechanical (Haiku model). The Credibility / Grounding / Bias judges are heavier and have shown the same recurring catches across batches. Always running all 4 spends coordination cycles on already-known failure modes; calibrating by PR type focuses the heavier judges on PRs where their unique value lands.

## Pre-judge audit

Before spawning the judge panel on a PR that touches `sources/` or `research/`,
the dispatcher (or a human reviewer) should run the cache-artifact audit
script against the PR's worktree:

```
python3 scripts/check_cache_artifacts.py <path-to-worktree>
# or, for machine-readable output:
python3 scripts/check_cache_artifacts.py <path-to-worktree> --json
```

The script enforces the rule codified after PR #173 (see
`feedback_subagent_cache_artifacts.md`): every "fresh-fetch 2026-MM-DD"
claim in a changed `sources/<era>/*.md` or `research/**/*.md` file must
have a matching cache artifact (`.cache-*.html`, `.cache-*.pdf`,
`.scratch/*.{html,pdf}`, `.tmp_fetched/*.{html,pdf}`) whose filename
contains the cited domain. It also flags `verified: false` sources
annotated as `NOT fetched` that are nonetheless block-quoted by a
research essay in the same diff — the exact PR #173 confabulation
shape.

Exit code:
- `0` — both fail buckets empty (the audit is a *floor*, not a guarantee
  — quote-vs-cache content match remains Judge-Grounding's job)
- non-zero — at least one unmatched fresh-fetch URL or one unverified
  blockquote candidate; surface to the human and revise before judging

The check is read-only on the repo and runs in a few seconds against a
typical PR worktree. The dataset-curator queue script may also call it
in batch mode against merged PRs.

## Judge review format

Every judge posts exactly one PR review comment with this structure:

```
### Judge: <Credibility|Grounding|Schema|Bias>
Verdict: APPROVE | APPROVE-WITH-NOTES | REJECT
Findings:
- <bullet>
Blocking items:
- <bullet>  (empty if APPROVE)
Suggested revision:
<free text; only when REJECT>
```

## Labels

Type:
- `investigation` — every research issue

Category:
- `catalog`, `photographer-bio`, `provenance`, `clervaux`, `world-tour`, `reception`, `sources`, `training-curation`

Decade (for `sources` category):
- `era-1950s`, `era-1960s`, `era-1970s`, `era-1980s`, `era-1990s`, `era-2000s`, `era-2010s`, `era-2020s`

Status:
- `needs-agent`, `in-progress`, `needs-review`, `rejected-by-panel`, `blocked`, `escalated`

Priority:
- `p0-foundational`, `p1-core`, `p2-enrichment`

Verdict signals:
- `judges-passed`, `bias-notes-pending`

## Credibility bar

All claims must meet `CREDIBILITY.md`. Judge-Credibility and Judge-Bias both enforce this — the former mechanically, the latter epistemically.

## Escalation

When a PR hits the revision cap without unanimity, the Dispatcher adds label `escalated` and stops work on the issue. A human decides whether to force-merge, re-scope the brief, or close.

## Running the pipeline

- Seed issues: see `plan.md §14` for phased execution.
- Manual tick: `gh issue list --label needs-agent --state open` then invoke the Dispatcher subagent.
- Scheduled tick: the `/loop` skill or a cron trigger can run the Dispatcher on a cadence.

## Tooling discipline — no ad-hoc scripts

Verification, data inspection, and audits must run through **committed, reusable
scripts in `scripts/`** — never through ad-hoc inline logic (`python3 -c "..."`,
throwaway `awk`/`sed`/`jq` checks, or multi-statement shell pipelines that encode
checking/analysis logic). Inline scripts are unreviewable, unversioned,
irreproducible, and force the user to approve opaque one-off executions.

Rules:
- **If a check is worth running, it is worth committing.** Add or extend a script
  in `scripts/` (docstring, `--json` where useful, meaningful exit code), then
  invoke that file.
- **Reuse before writing.** Existing audits / pre-flights:
  `validate_schema.py`, `check_injection_patterns.py`,
  `check_cache_artifacts.py`, `audit_jekyll_mirror.py`,
  `sync_photo_counts.py`, `verify_section_pages.py`,
  `photographer_anchors.py` (pre-flight for issue-#184 deep-research cycles —
  plate count, per-plate table, existing bio size, candidate sources),
  `check_credibility.py`, `merge_if_ready.py`.
- **Plain commands are fine.** `git`, `gh`, `ls`, a single-pattern `grep`/`git grep`,
  and running a committed script are not "scripts" in this sense. The line is
  *encoding checking/analysis logic inline* vs. *invoking a reviewed artifact*.
- The moment a check gates a commit or would be run more than once, it must be a
  committed script — not pasted into the Bash tool.

## Governance

Humans (you) retain:
- Final merge authority — can force-merge or force-close any PR
- Curation-batch approval for training examples
- Labeling and scope decisions (e.g., which decade to prioritize)
