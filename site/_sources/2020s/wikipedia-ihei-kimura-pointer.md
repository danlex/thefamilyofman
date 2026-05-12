---
id: src-wikipedia-kimura-pointer
title: "Ihei Kimura [Wikipedia article — fetched 2026-05-10; pointer-only per CREDIBILITY.md]"
author: ""
year: 2026
type: website
publisher: "Wikipedia / Wikimedia Foundation"
url: "https://en.wikipedia.org/wiki/Ihei_Kimura"
accessed: 2026-05-10
tier: 3
language: en
verified: true
tags: [ihei-kimura, photographer-biography, japanese-photography, leica, akita, tokyo, family-of-man, pointer-source]
---

## Citation

*Ihei Kimura.* Wikipedia. Fetched 2026-05-10 from `https://en.wikipedia.org/wiki/Ihei_Kimura`.

## Tier justification

Tier 3: Wikipedia is **pointer-only** per `CREDIBILITY.md`. Used here strictly to record the year-and-day tokens (12 December 1901 / 31 May 1974), the *Family of Man* attribution, and the broad biographical narrative (Tokyo birth, Taiwan early career, *Kōga* magazine 1932, Nippon Kōbō 1933 with Yōnosuke Natori, mid-1950s Europe trips, and posthumous Kimura Ihei Award). The connection to the FoM Tokyo executive committee is independently anchored at Tier 2 in this repo via `src-takenaka-2020-popular-inquiry-japan` and `src-takenaka-2022-atomic-bombings`.

## Key excerpts / pages

Verbatim claims from the article (fetched 2026-05-10):

- **Short description:** "Japanese photographer (1901–1974)"
- **Lead (verbatim):** "Ihei Kimura (木村 伊兵衛, Kimura Ihei; 12 December 1901 – 31 May 1974) was a Japanese photographer, known for his portrayal of Tokyo and Akita Prefecture."
- **Birthplace and early career (verbatim):** "Born on 12 December 1901 in Shitaya-ku (now Taitō-ku), Tokyo, Kimura started taking photographs when very young but his interest intensified when he was around 20 and living in Tainan, Taiwan, where he was working for a sugar wholesaler. He opened a photographic studio in Nippori, Tokyo in 1924. In 1930, he joined the advertising section of the soap and cosmetics company Kaō, concentrating on informal photographs made with his Leica camera."
- **Kōga / New Photography movement (verbatim):** "In 1932, Kimura was a central figure in the coterie magazine *Kōga* (光画; 1932–1933), which helped spur the development of Shinkō shashin ('New Photography') in Japan. In 1933, he joined Yōnosuke Natori and others in forming the group Nippon Kōbō ('Japan workshop'), which emphasized 'realism' in photography using 35mm cameras; but this rapidly broke up and Kimura formed an alternative group, Chūō Kōbō ('central workshop') with Nobuo Ina and others."
- **Family of Man inclusion (verbatim):** "In the mid-fifties, Kimura made several trips to Europe, providing photographs for the camera magazines. His work was included by Edward Steichen in the world-touring 1955 MoMA exhibition *The Family of Man*."
- **Death and award (verbatim):** "Kimura died at his home in Nippori on 31 May 1974; the Kimura Ihei Award for new photographers was promptly set up in his honor."

## Notes

- Per `CREDIBILITY.md`, Wikipedia is treated as a pointer source. The 12 December 1901 / 31 May 1974 day-month tokens are corroborated by the structured-data record at Wikidata Q3106591 (`+1901-12-12` / `+1974-05-31`, fetched 2026-05-10 to `.scratch/wikidata-kimura.json`), but Wikidata and Wikipedia share the same community-editor pool and are not strictly independent. Day-level resolution remains pointer-only.
- The 1901 / 1974 year-only resolution is **independently anchored at Tier 1** in this repo by the MoMA Master Checklist (`src-moma-exh-0569-master-checklist`) plate note for photo-0130, which records "Kimura, 1901-1974, was a major postwar Japanese documentary photographer" — though this is itself a downstream note added during the catalog-builder pass, not a primary date attribution from the 1955 catalog itself. Stronger Tier-1 institutional date corroboration (Eastman Museum, MoMA collection page, J. Paul Getty, Tate) was attempted this round and **all returned HTTP 403 / 404 / no-results**: see "Access barriers" section below.
- Wikipedia explicitly names *The Family of Man* on Kimura's biography page; this is the strongest Tier-3 attestation we have for the curatorial inclusion. The Tier-2 in-repo anchor for Kimura's role in the **Tokyo executive committee** (per `src-takenaka-2020-popular-inquiry-japan` p. 46 and `src-takenaka-2022-atomic-bombings`, both verbatim listing "Ihee Kimura" among the Japanese committee photographers) is independent of this Wikipedia record and is the load-bearing scholarly anchor for Kimura's involvement.
- The Master Checklist credits Kimura's single FoM plate (photo-0130, Section 14 Land) with no agency / publication, just "Ihei Kimura, Japan, 20 x 14 cm" — meaning the print reached MoMA directly from the photographer rather than via an agency.

## Access barriers (Japanese-photography institutional sources)

The hard-rule for this batch flagged that "Japanese / Indian institutional archives often 403/redirect" — confirmed in this round for Kimura:

- **MoMA artist page** (`https://www.moma.org/artists/3107`): HTTP 403 with all User-Agent variants tried (Mozilla/5.0, Chrome/120). Saved 5,354-byte error page at `.scratch/moma-kimura.html`.
- **MoMA collection search** (`https://www.moma.org/collection/?artists=3107`): HTTP 403 (3,195-byte block page).
- **George Eastman Museum collections** (`https://collections.eastman.org/people/16519/ihei-kimura`): HTTP 403 (5,488-byte block page) saved at `.scratch/eastman-kimura.html`.
- **SFMOMA** (`https://www.sfmoma.org/artist/Ihei_Kimura/`): HTTP 403 (5,472-byte block page) saved at `.scratch/sfmoma-kimura.html`.
- **ICP constituent archive** (`https://www.icp.org/browse/archive/constituents/ihei-kimura` and `/kimura-ihei`): both HTTP 200 but **canonical-URL is the ICP "Page not found" template** — ICP's archive does not hold a Kimura entry.
- **Tate Museum search** (`https://www.tate.org.uk/search?q=ihei+kimura`): HTTP 200, "No results found for 'ihei kimura'" verbatim. Saved at `.scratch/tate-kimura-search.html`.
- **Britannica search** (`https://www.britannica.com/search?query=Ihei+Kimura`): HTTP 200 but no `/biography/Kimura-` entry exists. Saved at `.scratch/britannica-search-kimura.html`.
- **J. Paul Getty Museum** (`https://www.getty.edu/art/search/?q=Ihei+Kimura&category=person`): HTTP 404. Saved at `.scratch/getty-search-kimura.html`.
- **Tokyo Photographic Art Museum (TOP) Kimura Ihei Award page** (`https://topmuseum.jp/e/contents/award/award_kimuraihei.html`): HTTP 200 but page is JS-rendered and the static HTML body returned by curl is essentially empty / template-only with no biographical text. Saved at `.scratch/topmuseum-kimura.html`.
- **Maison Européenne de la Photographie search** (`https://www.mep-fr.org/?s=kimura`): HTTP 200, no biographical entry returned in search results.
- **Grove Art Online** (`https://www.oxfordartonline.com/groveart/search?q=ihei+kimura`): HTTP 302 → SAMS-Sigma OAuth login redirect (`oup2-idp.sams-sigma.com`). Subscription-only; not consulted this round.

The combined result: outside of Wikipedia, the only **in-repo Tier-1/2 anchors for Kimura's role in the FoM exhibition** are the MoMA Master Checklist plate-level entry (Tier 1, in repo) and the two Takenaka articles which name him as Tokyo executive-committee photographer (Tier 2, in repo). A future pass via library / subscription access (Grove Art, JSTOR, IIPC) should be attempted to add a non-Wikipedia biographical Tier-1/2 source.

- Verified against fetched source on 2026-05-10 via `curl -fsSL https://en.wikipedia.org/wiki/Ihei_Kimura` (HTTP 200, 121,240 bytes). Saved at `.scratch/wikipedia-kimura.html`. Wikidata structured-data backup saved at `.scratch/wikidata-kimura.json`.
