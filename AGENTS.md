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

## Governance

Humans (you) retain:
- Final merge authority — can force-merge or force-close any PR
- Curation-batch approval for training examples
- Labeling and scope decisions (e.g., which decade to prioritize)
