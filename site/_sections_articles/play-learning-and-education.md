---
title: "Play, learning, and education"
theme: "Growing up: play and education"
order: 5
section_id: sec-play-learning
checklist_section: "Section 26 (plates #328–#347) and Section 35 (plates #414–#433, approximate)"
photo_count: 36
---

"Education" is one of the themes CNA Luxembourg's education portal explicitly names in its account of the exhibition's 37 themes.[^1] Play, learning, and education appear here as one cluster in the flow from childhood toward adulthood and work. MoMA's archives-highlights summary does not isolate education as a named narrative stage;[^2] the thematic cluster is reconstructed from the checklist's own section headings — Section 26 LEARNING and Section 35 TEENS — and from secondary summaries of the exhibition's mid-to-late arc.

The two sub-sections that constitute this cluster sit apart from each other in the checklist's plate numbering. Section 26 Learning (plates #328–#347, mapped here as photo-0317 through photo-0334) falls within the exhibition's mid-sequence social-life arc; Section 35 Teens (plates #414–#433, mapped as photo-0401 through photo-0418) is a later section closer to the political arc of Revolt and War. Grouping both under a single "Play, learning, and education" cluster is an editorial simplification; the mapping of Section 35 TEENS to this cluster is recorded as approximate, not canonical, in `data/sections.csv`.

One photographer with a documented deep-dive note in this repository has a plate assigned to this cluster. Esther Bubley contributes plate #334 (photo-0323, England, Section 26 Learning), one of three Bubley plates in the exhibition — all three placed in the Learning and Teens sections (two set in England, one in the USA).[^3] Her LIFE magazine credit on this plate is consistent with her documented freelance LIFE work beginning in 1951. The Bubley estate site's image filenames include a reference that may identify the England plate as a school-setting photograph — noted in the research file as an open lead, not a confirmed fact.

## Sandburg prologue excerpt

No verbatim Sandburg passage is associated with this section in `data/sections.csv`. Per the catalog reconciliation work documented in [`research/sections.md`](https://github.com/danlex/thefamilyofman/blob/main/research/sections.md), the 1955 catalog interior text was access-restricted in the Internet Archive scans consulted in earlier sessions and has not been re-fetched. The `sandburg_prologue_excerpt` field will be populated when the physical catalog or an unrestricted digital copy can be consulted.

## Plate gallery

The 36 plates assigned to this cluster, in checklist order. Plate IDs are repository identifiers, not the original 1955 plate numbers; the underlying mapping (e.g. `photo-0323` ↔ checklist plate #334) is recorded in each photograph's catalog notes.

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

The boundaries of this cluster are less clean than those of, for example, the Lovers or Death and Mourning sections. Section 26 Learning is cleanly documented in the checklist; its assignment to `sec-play-learning` is recorded as **canonical**. Section 35 Teens, mapped here as an approximate fit, is recorded as **approximate**: the section's thematic character overlaps with both "growing up" and the exhibition's later political arc, and some researchers might reasonably assign it to the rededication-future cluster instead. The checklist section heading — "TEENS" — is the only primary-source designation; "play" and "education" are thematic labels supplied by this repository's cluster scheme, not by the 1955 catalog.

Ernst Haas contributes one plate to Section 26 Learning (photo-0329, checklist #339, noted in `data/photographs.csv` as carrying a Magnum / VOGUE credit) — one of three Haas plates in sub-sections adjacent to this cluster (photo-0235 in Section 21 Dance and photo-0329 here). These three plates represent the Haas presence in the mid-flow social and learning arc of the exhibition.

Roland Barthes's 1957 critique names "knowledge" alongside birth, death, and work as one of the categories the exhibition universalizes: these are treated as eternal human experiences rather than historically conditioned practices shaped by class, access, colonial history, and economic structure.[^4] The Learning section, with its cross-cultural photographs of schoolchildren, occupies precisely the place in the exhibition where the humanist claim — that education is a universal human aspiration — is most explicit.

[^1]: CNA Luxembourg, *The Family of Man, the book of humanity* — `src-cna-education`.
[^2]: MoMA Archives, *Edward Steichen at The Family of Man, 1955* — `src-moma-archives-highlights-1955`.
[^3]: Research note: `research/photographs/photo-0323.md`, read this session. Sources cited there include `src-moma-exh-0569-master-checklist` (Tier-1, in-repo), `src-icp-esther-bubley-archive`, and `src-yochelson-estherbubley-com-biography`.
[^4]: Roland Barthes, "The Great Family of Man," in *Mythologies* (1957) — `src-barthes-1957`.
