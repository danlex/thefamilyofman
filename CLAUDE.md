# Project context for Claude Code

This repository documents Edward Steichen's 1955 exhibition *The Family of Man* and its Luxembourg collection at Clervaux Castle. Its outputs (`data/`, `sources/`, `research/`, `site/`) will be shared with the Family of Man museum at Clervaux and cited by researchers. **The accuracy bar is museum-grade.**

## Museum-grade accuracy — mandatory protocol

The single non-negotiable rule:

> **Never write, in any committed file, a claim that names a specific source (URL, book, archive, author, publication, institution) as corroborating a fact unless that source was actually fetched / read / opened in the current working session.**

This is a stronger bar than the Tier-1/2/3 credibility rubric in `CREDIBILITY.md`. Credibility tells you what sources are allowed. Anti-confabulation tells you what you are allowed to *claim about* sources.

### Before writing a note that cites a source, you must one of:

1. **Have just fetched it in this session** — WebFetch, Read of an in-repo file, or the user pasted its content. The note should name what was returned, not what you expected.
2. **Explicitly label it as not consulted this round** — use phrases like "NOT consulted in this round", "not re-fetched", "claim carried from the pre-existing citation", "cited in secondary literature but not accessed here".
3. **Not name it at all** — prefer silence over a plausible-sounding but unverified reference.

### Phrases that ARE confabulation and must never appear:

- *"also recorded on [site.com]"* — when you didn't fetch [site.com] this session
- *"well-attested in [archive/publication]"* — when you didn't fetch it
- *"corroborated by [scholar's 1985 biography]"* — when you didn't open it
- *"the [institution] collection confirms"* — when that collection was blocked / 403 / 404 this session
- *"held on the [NYT citation + X authority]"* — where X is a source you didn't actually consult

### Phrases that ARE safe:

- *"not re-verified in this round"*
- *"[URL] was attempted and returned 403; no alternative source fetched"*
- *"fetched 2026-04-24 at [URL]; returned [exact quoted content]"*
- *"cited in secondary literature ([author year]) but not consulted in this round"*
- *"Flagged `verified: false` pending a future pass"*

## Required pre-delivery audit

Any PR that adds or modifies content in `sources/`, `research/`, or `data/` must be audited by the `tvl-tech-bias-validator` skill **before commit** when the changes include claims about external sources. The validator's CoVe stage catches exactly the class of confabulation described above.

A real audit from this project (2026-04-24, issue #9): the validator caught a committed note claiming Wayne Miller's curatorial-assistant role was "abundantly attested in the primary 1955 exhibition record (MoMA Exh-0569 press release, MoMA Master Checklist)". Direct inspection of those two in-repo files showed the press release did not name Miller at all, and the checklist recorded him only as a plate photographer. The claim was materially false and would have shipped to the museum unchallenged without the audit. **This is why the validator gate exists.**

## Citation provenance checklist (for every source-touching commit)

For each claim you add to a source file, research note, or CSV `notes` field, you must be able to answer yes to all of:

- [ ] Did I open this source in the current session, or can I point to a prior fact-check commit that did?
- [ ] Does the source actually contain the specific claim as written (not a plausible paraphrase)?
- [ ] If the claim names a date/number/name, is that exact token present in what I fetched?
- [ ] If I am marking `verified: true`, can a museum researcher click the URL and see the same content I quoted?
- [ ] If I am marking `verified: false`, have I said *why* (403 / 404 / paywall / no Wayback / not attempted) rather than leaving the reason implicit?

Any "no" → the claim does not go in the file.

## Subagent spawning — worktree permission caveat

Subagents spawned with `isolation: worktree` + `run_in_background: true` do not currently inherit this repo's `.claude/settings.local.json` allowlist. The `bypassPermissions` spawn mode does not propagate to the worktree tool layer. As of 2026-04-24, the workaround is to do short source-verification work directly in the main session until a `SubagentStart` hook is added to copy settings into new worktrees.

## Links

- `CREDIBILITY.md` — tier rubric for allowed sources
- `AGENTS.md` — multi-agent workflow contract
- `IMAGE_POLICY.md` — licensing rules for hero imagery
- `plan.md` — phased execution plan for the overall research
