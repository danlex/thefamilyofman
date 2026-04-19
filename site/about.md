---
layout: article
title: About this wiki
namespace: Meta
permalink: /about/
edit_dir: site
---

**thefamilyofman** is a public wiki documenting Edward Steichen's 1955 exhibition *The Family of Man* — its 503 photographs, 273 contributing photographers, 1955–62 world tour, permanent installation at Clervaux Castle, UNESCO Memory of the World inscription, and seven decades of critical reception.

## How it's built

The wiki is built openly on GitHub. Every article lives as a Markdown file in the repository. The site is static — plain HTML served by GitHub Pages, with no backend, no database, and no framework. Jekyll renders the Markdown at build time.

Research is produced by a team of specialized agents:

- A **Catalog Builder** compiles the list of 503 photographs.
- A **Photographer Biographer** writes biographies of the 273 contributors.
- **Five Historians** cover the 1955 exhibition, the world tour, the Clervaux installation, the UNESCO inscription, and the critical reception.
- **Three Sources Librarians** maintain the bibliography, era by era.
- A **Dataset Curator**, **Eval Designer**, and **Dataset Auditor** maintain a training dataset for future AI work.
- A **Dispatcher** coordinates issue assignment.

Every contribution — from an agent or a human — goes through a **four-judge review panel**:

| Judge | Checks |
|---|---|
| **Credibility** | Every claim cites a source; every source meets the tier rubric. |
| **Grounding** | Statements actually appear in the cited sources. |
| **Schema** | File formats, CSV shape, frontmatter all conform. |
| **Bias** | No confirmation bias, confabulation, or hallucination; counter-perspectives acknowledged. |

Unanimous structural approval and no bias rejection is required for a change to merge.

## Credibility {#credibility}

Every factual claim must cite a source. Sources are rated in three tiers:

- **Tier 1** — primary / archival: MoMA archives, CNA Luxembourg, UNESCO register, the 1955 catalog, Steichen's own writings, archival photographs with documented museum provenance.
- **Tier 2** — peer-reviewed / academic: Sandeen (1995), Stimson (2006), Turner (2013); journals like *History of Photography*, *October*, *Aperture*.
- **Tier 3** — reputable press / museum: Met, Tate, National Gallery publications; major newspapers with named authors.

Blogs, social media, unverified Wikipedia claims, and AI-generated content are **not** accepted as sources. See [CREDIBILITY.md](https://github.com/danlex/thefamilyofman/blob/main/CREDIBILITY.md) for the full rubric.

## Why no photographs on the site?

The 503 photographs are copyrighted by their photographers or estates. Most are still in copyright. Licensing 273 rights-holders is not feasible. Instead, each photograph's article links out to the MoMA or Clervaux page where the image is displayed under that institution's license.

## How to contribute

Click **✏️ Edit this page** at the bottom of any article and propose a change. See the [contributing guide](https://github.com/danlex/thefamilyofman/blob/main/CONTRIBUTING.md).

## License

- Code: [MIT](https://github.com/danlex/thefamilyofman/blob/main/LICENSE)
- Articles and research prose: [CC BY-SA 4.0](https://github.com/danlex/thefamilyofman/blob/main/LICENSE-CONTENT)
- Data (CSVs, JSONL): [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)

## Repository

<https://github.com/danlex/thefamilyofman>
