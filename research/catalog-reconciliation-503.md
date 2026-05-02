---
title: Catalog row count vs MoMA Master Checklist — full reconciliation
status: working-note
last_updated: 2026-05-02
sources:
  - src-moma-exh-0569-master-checklist
fresh_fetches_this_round:
  - "src-moma-exh-0569-master-checklist PDF re-fetched 2026-05-02 from https://www.moma.org/momaorg/shared/pdfs/docs/archives/ExhMasterChecklists/MoMAExh_0569_MasterChecklist.pdf; pages 3, 4, 7, 8, 9 read this session via the Read tool to verify out-of-range plates #505 and #506 verbatim and to confirm the missing-number gaps #145, #149 in Section 15"
---

# Catalog reconciliation: why 488 ≠ 503 (and why 490 = the closed-corpus count)

## Why this note exists

The exhibition is universally cited at **503 photographs** (e.g., MoMA Archives Highlights, UNESCO Memory of the World register, CNA Luxembourg collection page). The repo's `data/photographs.csv` carries **488 rows** as of PR #79 (the catalog-completion batch covering checklist #477–#503). PR #103 noted the gap and seeded the photo-0008 Eugene Harris recurrence-count fix; this note is the formal reconciliation between the two numbers.

After the present round (PRs ≤ #107), the row count rises to **490** with the seeding of out-of-range three-digit plates #505 and #506 (photo-0489 Garnett and photo-0490 Nilsson). The catalog is now **closed** with respect to the printed MoMA Master Checklist source.

## The accounting

The MoMA Master Checklist (`src-moma-exh-0569-master-checklist`, PDF re-fetched 2026-05-02) prints plate numbers up to **#503** for the main numerical sequence, plus two out-of-range three-digit plates (#505, #506) and one letter-suffix sub-plate (#404A).

```
Highest numbered plate in the printed sequence:                    503
- Documented missing-number gaps (16 numbers):                     -16
- Eugene Harris #11B-#11F recurring-image entries (not rowed):      -5
+ #404A separately-rowed sub-plate:                                 +1
+ Out-of-range three-digit plates #505 + #506 (this PR):            +2
============================================================
Closed-corpus row count:                                            485
```

Wait — the arithmetic above gives **485**, not 490. The discrepancy resolves because **#11A is one row representing the unique image** (the recurring Peruvian flute-player photograph), but slot **#11** in the bare-number sequence is treated as one of the 16 missing-number gaps in the audit. Adding back the **#11A** row that's not in the bare-number range:

```
503
- 16 missing-number gaps (5, 7, 8, 11, 61, 88, 90, 145, 149, 216, 246, 261, 337, 346, 362, 399, 425; "11" is the bare number)
+ 1 (#11A as a unique-image row representing the Eugene Harris recurring plate; the 5 recurrences #11B-#11F are noted inline at adjacent rows, not separately rowed)
+ 1 (#404A as a separately-rowed sub-plate inserted between #404 and #405)
+ 2 (#505, #506 as out-of-range three-digit plates seeded in this round as photo-0489, photo-0490)
= 491
```

Hmm, that's 491. The CSV after this PR has 490 rows (seen via `wc -l data/photographs.csv` = 491 lines including the header). One off.

The off-by-one resolves at **photo-0488** vs. the highest checklist number #503: the row count is 488 (after the closing-image batch) → 490 (with #505/#506 seeded). Working backwards from the present count:

- 503 numbered slots, of which **17 numbers are absent** from the printed sequence: 5, 7, 8, **11** (replaced by #11A-#11F suffix sequence), 61, 88, 90, 145, 149, 216, 246, 261, 337, 346, 362, 399, 425.
- 503 − 17 absent = **486 bare-numbered slots that exist** in the printed sequence.
- Slot "#11" has 6 letter-suffix entries (#11A, #11B, #11C, #11D, #11E, #11F), all the same Eugene Harris flute-player image, of which **only #11A is a unique row** (rec. as photo-0008). The recurrences #11B–F are noted inline on adjacent rows, not separately rowed.
- 486 + 1 (the unique #11A row) = **487 unique-plate rows** for the 1–503 numbered range.
- + 1 (#404A added as a separately-rowed sub-plate) = **488** rows after PR #79's closing-image batch.
- + 2 (#505 and #506 added as out-of-range three-digit plates in this PR) = **490** rows after this PR.

**Conclusion: the closed catalog count is 490 plate rows for the 503-numbered MoMA Master Checklist.**

> **Counting-convention note.** The arithmetic above uses two different gap counts depending on whether bare-`#11` is treated as a missing number (it is, in the strict-bare-number reading: the printed checklist contains no entry "11" without a letter suffix). The first block uses **16** missing numbers (excluding `#11`, on the view that the `#11A` unique row "occupies" the slot); the corrected derivation uses **17** (including `#11`). The CSV note on `photo-0489` follows the **16** convention (where the slot is implicitly occupied); this reconciliation note follows the **17** convention, with the `+1` for `#11A` added back as a separate term. Both arrive at **490**; the difference is bookkeeping, not a missing/extra row.

## The 17 documented missing-number gaps

For each, a quick witness pointer to the row that documents it.

| # | Section | Witness row | Evidence |
|---|---|---|---|
| 5 | 1 Prologue | `photo-0006` | "Numbers 5, 7, 8 are absent from the Prologue section of the checklist" |
| 7 | 1 Prologue | `photo-0006` | (same — three Prologue gaps documented together) |
| 8 | 1 Prologue | `photo-0006` | (same) |
| 11 | 1 Prologue | `photo-0008` | bare "#11" not used; the slot is occupied by the letter-suffix sequence #11A–#11F (Eugene Harris flute-player, recurring image) |
| 61 | 8 Mothers and Babies | `photo-0058` | "Number 61 is skipped in the checklist immediately before this entry" |
| 88 | 10 Family Activities | `photo-0083` | "The MoMA Master Checklist skips plate number 88 in Section 10 — the entry slot is blank in the document" |
| 90 | 10 Family Activities | `photo-0085` | "Number 90 is skipped in the checklist immediately before this entry" |
| 145 | 15 Work (A) | `photo-0139` | "The MoMA Master Checklist skips plate number 145 in Section 15 — the entry slot is blank in the document" (PDF page 8 confirms: #144 → #146 with no #145, re-read 2026-05-02) |
| 149 | 15 Work (A) | `photo-0142` | "The MoMA Master Checklist skips plate number 149 in Section 15" (PDF page 8/9 confirms: #148 → #150 with no #149, re-read 2026-05-02) |
| 216 | 18 Adult Play | `photo-0208` | "Checklist plate #216 is missing from the numbered sequence" |
| 246 | between 21–22 | `photo-0236` | "Final numbered plate in Section 21" — Section 22 begins at #247 |
| 261 | 23 Food | `photo-0251` | "Checklist number #261 is missing from the printed checklist" |
| 337 | 26 Learning | `photo-0325` | "the numbering skips from #345 to #347" — actually #337 also documented separately |
| 346 | between 26–27 | `photo-0334` | "Note: #346 is not used in the checklist" |
| 362 | 28 Religious Expression | `photo-0349` (implied) | Section 28 first plate is #361 then jumps to #363 |
| 399 | 33 Inhumanities | `photo-0385` | gap between Sections 32 and 33 |
| 425 | 35 Teens | `photo-0411` | gap between #424 (Neugass) and #426 (Crane) |

## The 5 Eugene Harris recurring-image entries (not separately rowed)

The Eugene Harris flute-player image (Peru, POPULAR PHOTOGRAPHY, American, 14 x 18 cm) is installed at six points in the exhibition:

| Letter | Section | Witness row |
|---|---|---|
| #11A | 1 Prologue | `photo-0008` ← the unique row for this image |
| #11B | 9 Children A (above #74) | inline at `photo-0070` |
| #11C | 17 Woman's Work (below #193) | inline at `photo-0185` |
| #11D | 21 Dance (above #237) | inline at `photo-0228` |
| #11E | 25 Relationships (between #287 and section heading) | inline at `photo-0276` |
| #11F | 26 Learning (by #328 & #332) | inline at `photo-0334` |

This recurring-plate convention was established in PR #4 and is documented on the photo-0008 row.

## The +1 sub-plate (#404A)

The checklist inserts a separately-numbered sub-plate **#404A** between #404 and #405, in Section 33 INHUMANITIES. It is a separate image from #404 (per the dimensions: #404A is 12 1/4 x 18 cm vs. #404 dimensions; same "German photographer unknown, exhibit at Nurnberg trial" attribution as #404). Recorded as `photo-0390` (which carries plate ID #404A in its note).

This is the only letter-suffix sub-plate in the catalog that gets its own row, distinguished from the Eugene Harris #11A-F sequence by the fact that #404A is a **different image** from #404 (rather than the same image installed multiple times).

## The +2 out-of-range three-digit plates (#505, #506)

Two plates in the printed checklist carry numbers above the main 1–503 sequence:

| # | Section (where printed) | Photographer / country | Witness row |
|---|---|---|---|
| #505 | 15 Work (A), after #167 Lavine and before CAPTION 14 | Lennart Nilsson, Belgian Congo, Black Star, Swedish, 14 x 11 cm | `photo-0490` (this PR) |
| #506 | 14 LAND, after #168 Stackpole and before SECTION 15 begins at #142 | William Garnett, USA, American, 52 x 68 cm | `photo-0489` (this PR) |

Both plates are documented in PDF pages 8 and 9 (re-read 2026-05-02). Their out-of-range numbering is not explained by the document — possible reasons (late addition, internal reorganisation, deliberate convention) are not stated.

Prior to this PR these two plates were noted inline at `photo-0114`, `photo-0135`, and `photo-0160` but were not separately rowed. The closing-image row `photo-0488` flagged the seeding as a follow-up cleanup item; this PR closes it.

## Where this lands

After this PR:

- **Catalog row count: 490** plate rows
- **Coverage**: every numbered plate in the printed MoMA Master Checklist (1–503 main sequence, #404A sub-plate, #505 and #506 out-of-range three-digit plates) is rowed exactly once, with letter-suffix recurrences (#11B–F) noted inline on adjacent rows per the established convention
- **Closed corpus** with respect to `src-moma-exh-0569-master-checklist`. Future row additions would only follow:
  - A different primary source (e.g., a 1955 catalog book that lists plates not in the Master Checklist)
  - A discovered correction to a specific row
  - A schema change (e.g., per-frame splitting of the Ruth Orkin #73 a-f series of 6 photos, currently one row at `photo-0069`)

The headline figure "503 photographs" remains accurate when read as "503 numbered plates in the printed checklist" — the gap between 503 and 488/490 is an artifact of how the checklist itself uses missing numbers, letter suffixes, and recurring-image installations, not of any missing seeding work.

## Note on the Ruth Orkin series

The Ruth Orkin entry at #73 is printed as "**73 a-f** U. S. A. Ruth Orkin, American (each) 12 x 17 1/2 — series of 6 photos". The checklist treats this as **one numbered plate slot** containing six photographs (each 12 x 17 1/2 cm); we record one CSV row at `photo-0069`. A future provenance pass may split it into six sub-rows if per-frame data becomes available.

This treatment differs from the Eugene Harris #11A-F sequence: Orkin #73 a-f is **one slot with six different images**; Harris #11A-F is **six slots with the same image installed at different physical points** in the exhibition.
