---
title: Work
theme: "Labor across cultures"
order: 6
section_id: sec-work
checklist_section: "Sections 14–17 (plates #115–#193, with out-of-order entries at #168, #506, #505)"
photo_count: 74
---

Work is one of the exhibition's central thematic clusters. MoMA's archives-highlights summary names "careers" as the mid-flow section following household life;[^1] the CNA education portal names "work" in its list of themes.[^2]

The cluster aggregates four checklist sections that together constitute the exhibition's sustained treatment of human labor: Section 14 LAND, Section 15 WORK (A), Section 16 WORK (B), and Section 17 WOMAN'S WORK. This four-section grouping places agrarian labor alongside industrial and domestic work, spanning continents and productive modes. Of the 74 plates, the majority fall in Sections 14 and 15; Section 17 Woman's Work (checklist plates #189–#193) is among the exhibition's few sections with an explicitly gendered designation.

Three photographers with documented deep-dive notes in this repository have plates in this cluster. Robert Capa contributes two USSR plates to Section 14 Land (photo-0118, checklist #124; photo-0131, checklist #137) — both posthumous contributions, as Capa died in Indochina on 25 May 1954, eight months before the exhibition opened.[^3] G. H. Metcalf contributes two Ireland plates to Section 14 Land (photo-0125, checklist #131; photo-0135, checklist #141), both carrying a Black Star agency and *LIFE* magazine dual credit.[^4] Ernst Haas contributes plate #154 (photo-0147, USA, Section 15 Work A), credited to Magnum and *Argosy*.[^5]

## Sandburg prologue excerpt

No verbatim Sandburg passage is associated with this section in `data/sections.csv`. Per the catalog reconciliation work documented in [`research/sections.md`](https://github.com/danlex/thefamilyofman/blob/main/research/sections.md), the 1955 catalog interior text was access-restricted in the Internet Archive scans consulted in earlier sessions and has not been re-fetched. The `sandburg_prologue_excerpt` field will be populated when the physical catalog or an unrestricted digital copy can be consulted.

## Plate gallery

The 74 plates assigned to this cluster, in checklist order. Plate IDs are repository identifiers, not the original 1955 plate numbers; the underlying mapping (e.g. `photo-0131` ↔ checklist plate #137) is recorded in each photograph's catalog notes.

<div class="entity-table-wrap">
{% assign cluster_plates = site.data.photographs | where: "section", page.section_id %}
<table class="entity-table">
  <thead>
    <tr>
      <th style="width: 14%;">ID</th>
      <th>Photographer</th>
      <th>Country</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    {% for p in cluster_plates %}
    <tr>
      <td><a href="{{ '/photographs/' | append: p.id | append: '/' | relative_url }}">{{ p.id }}</a></td>
      <td>
        {%- assign pher_match = site.data.photographers | where: "name", p.photographer | first -%}
        {%- assign pher_doc = nil -%}
        {%- if pher_match -%}
          {%- assign pher_doc = site.photographers | where: "id", pher_match.id | first -%}
        {%- endif -%}
        {%- if pher_doc -%}
          <a href="{{ pher_doc.url | relative_url }}">{{ p.photographer }}</a>
        {%- else -%}
          {{ p.photographer }}
        {%- endif -%}
      </td>
      <td>{{ p.country | default: "—" }}</td>
      <td>{{ p.year | default: "—" }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
</div>

<p style="font-family: var(--sans); font-size: 0.85rem; color: var(--mid);">
Showing {{ cluster_plates.size }} {% if cluster_plates.size == 1 %}plate{% else %}plates{% endif %} mapped to <code>{{ page.section_id }}</code> in <code>data/photographs.csv</code>. Anchor: <code>src-moma-exh-0569-master-checklist</code> (MoMA Exhibition #569 master checklist, Tier-1 in-repo).
</p>

## Cluster boundaries and certainty

The four-section grouping (Sections 14–17) collapses distinctions the checklist preserves: Land is not Work A is not Work B is not Woman's Work. The cluster boundaries recorded in [`research/sections.md`](https://github.com/danlex/thefamilyofman/blob/main/research/sections.md) are recorded as **approximate** for the Section 14/15 split and for the two out-of-order entries (#168 and #506 assigned to Section 14 Land; #505 assigned to Section 15 Work A), and as **canonical** for the four-section cluster's assignment to the mid-flow labor arc. Two plates (photo-0489, photo-0490) are out-of-sequence checklist entries within Sections 14–15; their cluster assignment is approximate rather than canonical.

The critical weight placed on this cluster is substantial. Roland Barthes's 1957 essay names "work" alongside "birth, death, work, knowledge, play" as universal categories the exhibition presents as imposing "the same types of behaviour" (verbatim per `src-barthes-1957`, in-repo, read this session via `research/photographs/photo-0147.md`).[^6] In Barthes's reading, this list is the heart of the exhibition's ideological project — categories whose historicity the show converts into Nature. Longer Barthes passages on the work category specifically would require a fresh fetch of the *Mythologies* chapter and were NOT consulted in this round. Allan Sekula's subsequent critique of the "traffic in photographs" extends the argument: the labor images in this section circulate through agencies such as Magnum and Black Star, and through publications such as *LIFE*, *Argosy*, and *Ladies' Home Journal*, before arriving at MoMA — a circulation history the exhibition frame renders invisible.[^7]

Any curatorial description of this cluster that presents labor as a universal essence without acknowledging the Barthes–Sekula counter-reading reproduces the humanist framing those critics problematized.

[^1]: MoMA Archives, *Edward Steichen at The Family of Man, 1955* — `src-moma-archives-highlights-1955`.
[^2]: CNA Luxembourg, *The Family of Man, the book of humanity* — `src-cna-education`.
[^3]: Research note: `research/photographs/photo-0131.md`, read this session. Sources cited there include `src-moma-exh-0569-master-checklist` (Tier-1, in-repo), `src-icp-capa-archive`, and `src-nyt-1954-capa-obit`.
[^4]: Research note: `research/photographs/photo-0125.md`, read this session. Sources cited there include `src-moma-exh-0569-master-checklist` (Tier-1, in-repo). No additional Tier-1/2 source for G. H. Metcalf was accessed in this round.
[^5]: Research note: `research/photographs/photo-0147.md`, read this session. Sources cited there include `src-moma-exh-0569-master-checklist` (Tier-1, in-repo), `src-icp-ernst-haas-archive`, and `src-haas-estate-biography`.
[^6]: Roland Barthes, "The Great Family of Man," in *Mythologies* (1957) — `src-barthes-1957`.
[^7]: Allan Sekula, "The Traffic in Photographs," *Art Journal*, 1981 — `src-sekula-1981`. The body text of Sekula 1981 was not accessed in this round (JSTOR returned 403 in prior research sessions); the argument is cited as carried from the in-repo source file, not from a primary reading of the essay's text in this session.
