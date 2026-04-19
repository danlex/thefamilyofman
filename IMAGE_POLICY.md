# Image policy

## The rule

**thefamilyofman does not host the 503 photographs of the exhibition.** Each photograph is copyrighted by its photographer or estate; most works from the 1940s–50s remain under copyright for decades to come. Articles about individual photographs link out to institutions that hold prints and license their reproductions — primarily the **Museum of Modern Art** (New York) and the **Centre national de l'audiovisuel** (Luxembourg, Clervaux Castle).

Every photograph article uses this pattern in place of an embedded image:

> *For the image, view the photograph at [MoMA](https://moma.org/collection/works/<id>) or at [the Clervaux collection](https://steichencollections.lu/…).*

## What this repository does host

The repository hosts only assets that fall into one of these categories:

1. **Creative Commons–licensed** — CC0, CC-BY, or CC-BY-SA, with the license and attribution recorded in a companion `license.json` file next to the asset.
2. **Public domain** — either by age, by explicit release, or by U.S. federal government authorship.
3. **Original work produced for this project** — diagrams, maps, timelines, data visualizations, screenshots of our own interfaces. We own these; they are released under the project's content license (CC-BY-SA 4.0).
4. **Fair use for identification or scholarly commentary** — book covers and catalog covers at thumbnail size, used with citation for identification; short text quotations for critical commentary, with full attribution. Fair use is applied narrowly and conservatively.

Hosted assets live under `site/assets/` (and the analogous location for any future subproject). Each must ship with a sibling `license.json`:

```json
{
  "source": "https://commons.wikimedia.org/wiki/File:Clervaux_Castle.jpg",
  "license": "CC-BY-SA-3.0",
  "rights_holder": "Example Contributor",
  "attribution": "Photo by Example Contributor, CC BY-SA 3.0",
  "url_verified_at": "2026-04-19",
  "basis": "creative_commons | public_domain | original | fair_use"
}
```

`scripts/check_credibility.py` can be extended to enforce the existence of `license.json` for every asset (see the Copyright check in the judge panel below).

## What this repository does not host

- The 503 exhibition photographs (in any resolution).
- Scans or reproductions of copyrighted material without a license or a defensible fair-use basis.
- Long excerpts from copyrighted prose (more than a few sentences at a time). Our quotations stay short, attributed, and serve critical commentary.
- Any image whose provenance we cannot verify to a named source.
- Uploads from contributors via "Edit this page" flows — the editing surface is text-only by design.

## Review

Every pull request touching `site/assets/` passes through the judge panel (see [`AGENTS.md`](AGENTS.md)):

- **Judge-Credibility** verifies `license.json` exists for each asset and cross-checks its fields.
- **Judge-Bias** flags assets that risk misrepresentation (for example, a photographer portrait from a disputed source).
- A copyright-focused check can be folded into Judge-Credibility or promoted to a fifth judge once asset volume grows.

## Takedown and contact

If you believe material in this repository infringes your rights:

1. **Open an issue** labeled `dmca` describing the material and your claim. We respond within 7 days.
2. **Or use GitHub's DMCA takedown process** at <https://github.com/contact/dmca>. GitHub acts as the designated agent for content hosted on its platform.

See [`SECURITY.md`](SECURITY.md) for the full contact and response process.

## Why this policy is strict

*The Family of Man* is a collective work owned by its many contributors. Respecting each photographer's copyright is both a legal requirement and an ethical one — the exhibition's argument about shared human experience does not give us a license to appropriate any image within it. The link-out policy preserves the photographers' and institutions' rights while still letting this wiki do its job: catalog, describe, analyze, and cite.
