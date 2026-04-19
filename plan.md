# Plan — thefamilyofman research infrastructure

Research project documenting Edward Steichen's *The Family of Man* (1955 MoMA; permanently housed at Clervaux Castle, Luxembourg since 1994; UNESCO Memory of the World, 2003).

**Status:** planning. No implementation has started. Await approval on the open questions in §33 before building.

---

## 1. Goals

- Catalog **all 503 original photographs** of the exhibition (user decision 2026-04-19). Cross-reference the permanent installation at Clervaux Castle.
- Document the story/provenance of each photograph.
- Build a comprehensive bibliography of **credible sources** from 1950 to present.
- Build a **training dataset** to finetune an AI on this corpus.
- Run the research through a multi-agent, issue-driven workflow with a 4-judge review panel.

## 2. Repository layout

```
.
├── README.md                    # project overview + how it works
├── plan.md                      # this document
├── AGENTS.md                    # workflow contract: issue → agent → PR
├── CREDIBILITY.md               # source-quality rubric
├── .github/
│   ├── ISSUE_TEMPLATE/          # one form per investigation type
│   │   ├── photograph.yml
│   │   ├── photographer.yml
│   │   ├── source.yml
│   │   ├── research-topic.yml
│   │   └── config.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── .claude/
│   └── agents/                  # subagent definitions (one .md per role)
├── data/
│   ├── photographs.csv          # catalog of 503 photographs
│   ├── photographers.csv        # 273 contributors
│   └── sections.csv             # thematic sections of the exhibition
├── sources/
│   └── {decade}/{slug}.md       # one source per file, frontmatter + notes
├── research/
│   ├── exhibition-1955.md
│   ├── world-tour.md
│   ├── clervaux.md
│   ├── unesco.md
│   └── reception.md
├── templates/
│   ├── source-entry.md
│   └── photograph-entry.md
├── training/
│   ├── schema.md
│   ├── raw/                     # curator-proposed examples, pre-review
│   ├── curated/                 # approved examples
│   ├── eval/eval.jsonl          # held-out evaluation set
│   ├── dataset.jsonl            # built from curated/
│   └── versions/v{n}.jsonl      # immutable release snapshots
└── scripts/
    ├── validate_schema.py       # CSV shape + required fields
    ├── check_credibility.py     # every citation meets tier rubric
    ├── build_dataset.py         # curated/ → dataset.jsonl
    ├── audit_dataset.py         # duplicates, tier violations, bias report
    ├── eval_runner.py           # scores a model against eval set
    └── merge_if_ready.py        # auto-merge when all judges approve
```

## 3. Data schemas

**`data/photographs.csv`**: `id, title, photographer, year, country, section, moma_object_id, clervaux_on_display, source_ids, notes`

**`data/photographers.csv`**: `name, birth_year, death_year, nationality, photo_count, bio_url, source_ids`

**`data/sections.csv`**: `id, title, theme, photo_ids, sandburg_prologue_excerpt, source_ids`

**`sources/*/*.md`**: YAML frontmatter (`title, author, year, type, url, accessed, tier, language`) + body notes.

## 4. Credibility rubric (full detail in `CREDIBILITY.md`)

- **Tier 1 — primary / archival**: MoMA archives, CNA Luxembourg (steichencollections.lu), UNESCO Memory of the World, the 1955 catalog, Steichen's own writings, archival photographs with museum provenance.
- **Tier 2 — peer-reviewed / academic**: University presses (Sandeen 1995, Stimson 2006, Turner 2013), journals (*History of Photography*, *October*, *Aperture*).
- **Tier 3 — reputable museums / press**: Met, Tate, National Gallery publications; major newspapers with named authors (NYT, Guardian, Le Monde).
- **Rejected**: blogs, Pinterest, social media, unverified Wikipedia claims (Wikipedia allowed only as a pointer to cited primary sources).

Every citation records: author, year, publisher/venue, URL (if online), accessed date, tier, language.

## 5. Workflow — issue → agent → PR → panel → merge

1. **Seed issues**: one GitHub issue per investigation. Labels: `investigation` + category + status + priority.
2. **Dispatcher**: polls open `needs-agent` issues, claims the oldest by priority, assigns itself, flips label to `in-progress`, spawns the right **Worker** subagent with the issue body as brief.
3. **Worker**: creates branch `agent/<slug>-#<n>`, produces files, opens PR with `Closes #<n>` and a standardized checklist.
4. **Panel of 4 judges** (§7) reviews in parallel. Unanimous structural approval + no bias REJECT → auto-merge.
5. **Mixed verdict** → revision loop (max 2 cycles) → escalate to user.
6. **Dataset Curator** runs on merge, proposes training examples → curation batch issue → your approval → merged into `training/curated/`.

## 6. Label taxonomy

- Type: `investigation`
- Category: `catalog`, `photographer-bio`, `provenance`, `clervaux`, `world-tour`, `reception`, `sources`, `training-curation`
- Decade (for source issues): `era-1950s` … `era-2020s`
- Status: `needs-agent`, `in-progress`, `needs-review`, `rejected-by-panel`, `blocked`
- Priority: `p0-foundational`, `p1-core`, `p2-enrichment`
- Verdict signals: `judges-passed`, `bias-notes-pending`

## 7. Judge panel (4 judges)

| Judge | Mandate | Model | Verdict |
|---|---|---|---|
| **Judge-Credibility** | Every claim has ≥1 valid, credible source citation; sources meet tier rubric; no broken links. | Opus 4.7 | APPROVE / REJECT |
| **Judge-Grounding** | Samples cited sources; verifies statements in PR actually appear in (or faithfully paraphrase) the cited sources. Catches hallucination. | Sonnet 4.6 | APPROVE / REJECT |
| **Judge-Schema** | `validate_schema.py` passes; CSV shape correct; required metadata fields present; file naming conforms; no orphan source_ids. | Haiku 4.5 | APPROVE / REJECT |
| **Judge-Bias** | Detects **(a) confirmation bias**, **(b) confabulation**, **(c) hallucination**, plus framing bias, omitted counter-perspectives, representational imbalance, untagged perspective. | Opus 4.7 | APPROVE / APPROVE-WITH-NOTES / REJECT |

**Why a bias judge for this subject in particular:** *The Family of Man* is a classic subject of bias critique (Barthes 1957, Sontag 1977, Sekula, Sandeen 1995, Stimson 2006, Turner 2013). Any output that restates the exhibition's self-presentation without acknowledging established counter-readings reproduces the bias.

**Three epistemic-integrity checks (explicit):**
- **Confirmation bias** — selectively citing sources that support a preferred narrative while ignoring credible sources that contradict or complicate it. Check: does the worker's source list include at least one source that challenges the claim, where such sources exist? Are omissions acknowledged?
- **Confabulation** — plausible-sounding fabrication that fills gaps where no source exists. Check: every non-trivial factual statement must trace to a specific `source_id`; statements without citation are flagged. Quotes, dates, names, and numbers are the highest-risk surfaces.
- **Hallucination** — stated facts, citations, titles, URLs, or quotes that do not exist in any real source. Check: sample-verify citations (does the paper/book/photo actually exist at the cited reference?). Complements Judge-Grounding: Grounding asks *"does this source say this?"*; Bias asks *"does this source exist, and is it the right kind of source to support this claim?"*

Division of labor with Judge-Grounding: Grounding performs literal sentence-to-source verification on provided citations. Judge-Bias performs the higher-level epistemic check: source selection, gap-filling, and existence of cited references.

**Judge-Bias verdict semantics:**
- **APPROVE** — perspective handled well.
- **APPROVE-WITH-NOTES** — does not block merge; appends a perspective note block to the affected file (e.g., *"This summary follows the 1955 curatorial framing; for critique see Barthes 1957, Sekula 1984, Sandeen 1995."*). Note is a committable diff the worker must accept before merge.
- **REJECT** — contested claims stated as settled fact, or an established critical perspective that the topic requires is systematically excluded.

**Consensus rule**
- Merge requires: all 3 structural judges APPROVE **AND** Judge-Bias ≠ REJECT.
- 1 rejecting judge → worker revises. Max 2 revision cycles, then escalated to user.
- 2+ rejecting judges → PR closed with `rejected-by-panel`, follow-up issue opened with combined rationale.
- User is final arbiter — can force-merge or force-close at any time.

**Model diversity matters** — three Opus judges correlate their errors more than judges on different model families. Haiku handles the mechanical check cheaply; Sonnet handles grounding; Opus handles the two judgment-heavy calls (credibility, bias).

## 8. Agent roster (17 roles)

**Operational (2)**
- Dispatcher — polls issues, claims, spawns workers, spawns judge panel.
- Worker — generic executor; the right `subagent_type` is picked by category.

**Review panel (4)** — see §7.

**Research — structural (3)**
- Catalog Builder — produces `data/photographs.csv` (all 503).
- Photographer Biographer — batched (~25 per issue); produces `data/photographers.csv` rows + source entries.
- Sections Cartographer — Steichen's thematic groupings; `data/sections.csv` + `research/sections.md`.

**Research — narrative (5)**
- Exhibition Historian — 1955 MoMA opening, Paul Rudolph installation, Sandburg prologue.
- Tour Historian — 1955–62 USIA world tour (91 venues, 37 countries, ~9M visitors).
- Clervaux Historian — Steichen's 1964 gift to Luxembourg, 1994 installation, 2010–13 restoration.
- UNESCO / Legacy Historian — 2003 Memory of the World inscription, anniversaries.
- Critical Reception Analyst — Barthes, Sontag, Sekula, Sandeen, Stimson, Turner.

**Research — bibliography (3)**
- Sources Librarian — Primary era (1950–1969).
- Sources Librarian — Critical era (1970–1999).
- Sources Librarian — Contemporary era (2000–2026).

**Training pipeline (3)**
- Dataset Curator — converts merged research into Q&A pairs (3–5 paraphrases per fact, source_ids attached).
- Eval Designer — builds and maintains `training/eval/eval.jsonl` (~200 held-out questions at v0.1).
- Dataset Auditor — duplicates, tier violations, answer-grounding checks, bias distribution report.

## 9. Training dataset pipeline

**Example schema (provider-agnostic JSONL):**
```json
{
  "id": "ex-00042",
  "messages": [
    {"role": "user", "content": "Who photographed the cover image of The Family of Man?"},
    {"role": "assistant", "content": "Wayne Miller photographed his son David…"}
  ],
  "metadata": {
    "topic": "catalog | photographer | exhibition-history | reception | clervaux | tour | unesco",
    "source_ids": ["src-moma-1955-catalog", "src-sandeen-1995"],
    "min_tier": 1,
    "perspective": "curatorial | critical | historical | institutional | archival | biographical",
    "perspective_sources": ["src-..."],
    "contested": false,
    "counter_perspective_id": null,
    "generated_by": "agent-dataset-curator",
    "generated_at": "2026-04-19",
    "reviewed": true,
    "version": "v0.1"
  }
}
```

**Rules**
- No example enters `dataset.jsonl` without ≥1 Tier-1 or Tier-2 `source_id`.
- `contested: true` → example must be paired with a counter-perspective (`counter_perspective_id`) OR answer acknowledges contestation inline.
- Dataset Auditor refuses to build a release where any `contested: true` example is orphaned.

**Release cadence** — git tags `dataset-v0.1`, `v0.2`, … aligned to research milestones. Each tag ships: `versions/v{n}.jsonl`, a changelog, baseline eval scores, and a bias report.

## 10. Continuous learning loop

- **Trigger:** every merged PR that modifies `data/`, `sources/`, or `research/`.
- **Flow:** merge → Curator opens batch issue → Auditor comments → user approves/edits → merged into `training/curated/` → `build_dataset.py` regenerates `dataset.jsonl`.
- **Refresh cadence:** `/schedule` cron (weekly/monthly) triggers a re-crawl agent that revisits primary-source pages, detects changes/new publications, opens new investigation issues.
- **Corrections:** when a source is superseded, correction PR updates the research file AND flags affected training examples (tracked via `source_ids`) for regeneration.

## 11. Evaluation harness

- `eval_runner.py` takes any chat-completions endpoint (Claude API, OpenAI, local model) + `training/eval/eval.jsonl` + a rubric.
- LLM-judge scoring uses Opus 4.7 with original source excerpts in context.
- Each release ships `versions/v{n}-eval.md` with per-topic accuracy.

## 12. Bias audit in the dataset

`scripts/audit_dataset.py` produces `versions/v{n}-bias.md`:

- Photographer distribution by nationality, gender (where documented), era — with exhibition baseline and transparent acknowledgment where our data inherits the baseline's imbalance.
- Source distribution: by tier, decade, language, institutional affiliation.
- Perspective distribution: curatorial vs critical vs historical — **target ≥25% of interpretive examples carry a critical perspective** (open question #15).
- Flags any topic with zero critical-perspective examples.

## 13. Finetuning target

Anthropic doesn't expose general Claude finetuning via public API today (Claude Haiku finetuning is available via AWS Bedrock). Provider-agnostic JSONL works for:
- AWS Bedrock — Claude Haiku finetune (closest to a Claude model)
- OpenAI — GPT-4o-mini / GPT-4o finetune
- Google — Gemini via Vertex
- Open models — Llama, Mistral, Qwen via HF / Unsloth / Axolotl

Recommendation: keep data provider-agnostic; pick target at v0.2 once volume justifies a run. Small RAG-over-the-repo prototype can run earlier as sanity check.

## 14. Phased execution

- **Phase 0 — Build infra** *(this plan, pending approval)*: directories, schemas, templates, `.github/` templates, labels, agent briefs, judge configs. No research yet.
- **Phase 1 — Foundational**: Catalog Builder + Sections Cartographer run first. Outputs unblock everything else.
- **Phase 2 — Parallel breadth**: Photographer Biographer batches, Sources Librarians × 3, narrative Historians × 5 run concurrently.
- **Phase 3 — Enrichment**: Provenance per-photograph deep dives (one issue per photo, ~503 issues — low priority long tail).
- **Phase 4 — Synthesis**: Reception Analyst + Legacy Historian weave narrative across all data.
- **Training pipeline** runs continuously from Phase 1 onward; v0.1 dataset release targets end of Phase 2.

## 15. GitHub mechanics

- Judges post PR reviews via `gh pr review` with a structured comment:
  ```
  ### Judge: <name>
  Verdict: APPROVE | APPROVE-WITH-NOTES | REJECT
  Findings: …
  Blocking items: …
  ```
- Branch protection: require 3 structural approvals + `judges-passed` label before merge.
- `scripts/merge_if_ready.py` runs after every review; `gh pr merge --squash` when: 3 structural approvals + bias not REJECT + schema CI passed + label present.
- Initial identity model: single GitHub account (danlex) posting four distinct review comments. GitHub Apps with separate identities can be added later.

## 16. Decisions made

- **Repo visibility:** public (`github.com/danlex/thefamilyofman`).
- **Catalog scope:** all 503 original photographs (user decision 2026-04-19).

## 17. Open questions

1. **PR-based workflow** — confirm PRs against `main` (recommended) vs. direct commits.
2. **Dispatcher cadence** — manual invocation, `/loop` every N minutes, or scheduled cron trigger?
3. **Issue seeding scope** — seed all ~60 Phase 1–2 issues up front, or seed Phase 1 only and let agents open later issues?
4. ~~**Catalog scope**~~ — **decided: 503.**
5. **Languages** — English only, or also French / German / Luxembourgish for CNA primary sources?
6. **Finetuning target** — pick now (slightly shapes dataset nuances) or defer to v0.2?
7. **Eval size at v0.1** — 200 questions (recommended); raise/lower?
8. **Re-crawl cadence** — weekly, monthly, or quarterly?
9. **Curation-batch approval** — user only, or auto-approve when all checks pass?
10. **Judge consensus rule** — unanimous structural (recommended) or 2-of-3 majority with dissent noted?
11. **Max revision cycles** — 2 (recommended), or different?
12. **Judge models** — mixed Opus / Sonnet / Haiku (recommended) or all-Opus for max quality?
13. **GitHub identities** — single account with four comment voices (recommended) or separate GitHub Apps from day one?
14. **Judge-Bias verdict scheme** — tri-state APPROVE / APPROVE-WITH-NOTES / REJECT (recommended) or binary?
15. **Critical-perspective floor** — ≥25% of interpretive examples (recommended), or different threshold?
16. **Photographer demographic tagging** — tag gender/ethnicity only where self-identified or documented in reputable source; leave blank otherwise. Confirm?

## 18. Next step

Once open questions are answered, Phase 0 build begins: scaffolding, templates, labels, agent briefs, judge configs. No research or issue seeding until Phase 0 is committed and approved.
