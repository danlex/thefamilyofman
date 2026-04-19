# Contributing

thefamilyofman is a public wiki. Contributions are welcome from anyone — no technical skills required to help improve it.

Every contribution is reviewed by a panel of four automated judges (Credibility, Grounding, Schema, Bias) before it lands. See [`AGENTS.md`](AGENTS.md) for how the review works.

## Three ways to contribute

### 1. Small PR — fix or improve an article (easiest)

Every article on the published site has a footer link **✏️ Edit this page**. Click it:

1. You'll land in GitHub's web editor on the article's source file.
2. Make your edit. Add a source citation if you're adding a factual claim — every claim needs a source (see [`CREDIBILITY.md`](CREDIBILITY.md)).
3. Scroll to **Propose changes** → enter a short message → **Create pull request**.
4. The 4-judge panel runs automatically. You'll see their verdicts in the PR.
5. If everyone approves, the change merges and the site rebuilds.

This is the fastest path for typos, missing citations, clearer wording, broken links, small factual corrections.

### 2. Open an issue — suggest an improvement

If you're not sure how to fix something, open an issue instead. Every article footer has **🐛 Suggest improvement**, which pre-fills an issue template with the article's path.

Explain what's wrong or what's missing. An agent (or a human contributor) will pick it up.

### 3. Start a discussion — ask or debate

Every article has a comment section (via Giscus, backed by GitHub Discussions). Use it for:
- "What does this mean?"
- "Does this source really say that?"
- "Is there a better citation?"
- General conversation that doesn't have a clear edit to propose.

## What makes a good contribution

- **Every factual claim is sourced.** See [`CREDIBILITY.md`](CREDIBILITY.md) for what counts as a credible source (Tier 1 archival, Tier 2 peer-reviewed, Tier 3 reputable press).
- **Perspective tagging.** If the claim is interpretive (e.g., "the exhibition represents humanism"), say whose perspective that is and cite them. Don't present contested readings as settled fact.
- **No image uploads.** We do not host the 503 photographs — each rights-holder keeps their copyright. Articles link to MoMA or CNA Luxembourg for the images.
- **Small PRs preferred.** One article, one fix per PR. Makes review fast.

## What happens after you submit

```
Your PR is opened
    ↓
4 judges review in parallel:
  Judge-Credibility  — sources meet the tier rubric, no broken links
  Judge-Grounding    — your statements actually appear in the cited sources
  Judge-Schema       — file format conforms (CSV shape, frontmatter, etc.)
  Judge-Bias         — no confirmation bias, confabulation, or hallucination;
                       counter-perspectives acknowledged where they exist
    ↓
All 3 structural judges APPROVE + Judge-Bias ≠ REJECT
    ↓
Merged. Site rebuilds. Your contribution is live.
```

If a judge requests changes, you'll see their specific feedback. Two revision cycles are allowed before the PR is escalated to a human.

## License

By submitting a contribution, you agree that:

- Code contributions are licensed under the MIT License (see [`LICENSE`](LICENSE)).
- Content contributions (articles, notes, research prose) are licensed under CC-BY-SA 4.0 (see [`LICENSE-CONTENT`](LICENSE-CONTENT)).
- Data contributions (CSV rows) are released into the public domain under CC0 (see [`data/README.md`](data/README.md)).
- Any third-party quotations you include must be compatible with fair use for scholarly commentary.

## Questions

Open a GitHub Discussion or file an issue. This is an open research project — curiosity welcome.
