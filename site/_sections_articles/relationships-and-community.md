---
title: Relationships and community
theme: "Friendship, society, celebration"
order: 8
section_id: sec-relationships-community
checklist_section: "Sections 18–25 (plates #195–#327) and Section 39 Faces (plates #446–#451, approximate); 123 photographs"
photo_count: 123
---

Mid-exhibition, the photographs turned to social life — adult play, music, dance, folk celebration, shared meals, and the bonds of friendship and community — before the harder material of hardship, war, and death that closes the sequence. This is the exhibition's widest cluster by plate count, spanning eight consecutive checklist sections plus one approximate borrowing from Section 39 FACES.

In the MoMA Master Checklist (Exhibition #569, `src-moma-exh-0569-master-checklist`), the eight canonical sections covered here are: Section 18 ADULT PLAY (#195–#221), Section 19 CLASSICAL MUSIC (#194 out-of-order + #222–#226), Section 20 JAZZ AND BLUES (#227–#232), Section 21 DANCE (#233–#245), Section 22 FOLK MUSIC (#247–#253 with gap at #246), Section 23 — absorbed into the separate `sec-eating-everyday` cluster — Section 24 RING AROUND THE ROSY (#270–#287), and Section 25 RELATIONSHIPS (#269 out-of-order + #288–#327). The Section 39 FACES group (#446–#451) is mapped here as approximate because it depicts individual human faces without the social-gathering framing of Sections 18–25, but it has no closer cluster home.

MoMA's archive-highlights narrative summary does not name this mid-flow group as a discrete stage — the institutional summary moves from "careers" directly to "death" — but "relationships" and "play" are recognized motifs in the wider critical literature on the exhibition's humanist argument.[^1]

Barthes's universalism critique applies with particular force to this cluster: the exhibition's scenes of communal music, dance, and play across cultures are presented as evidence of universal human joy, flattening the specific social and historical conditions (class, segregation, colonialism) under which those scenes of togetherness were captured. The exhibition's stated aim, Barthes wrote in 1957, was to show "the universality of human actions in the daily life of all the countries of the world"; he argued that from an insistence on human difference "a type of unity is magically produced: man is born, works, laughs and dies everywhere in the same way."[^2] Sandeen's reconstruction of the exhibition's structure contextualizes the mid-flow social-life sequence within the Cold War diplomatic frame of the touring show.[^3]

## Sandburg prologue excerpt

No verbatim Sandburg passage is associated with this section in `data/sections.csv`. Per the catalog reconciliation work documented in [`research/sections.md`](https://github.com/danlex/thefamilyofman/blob/main/research/sections.md), the 1955 catalog interior text was access-restricted in the Internet Archive scans consulted in earlier sessions and has not been re-fetched. The `sandburg_prologue_excerpt` field will be populated when the physical catalog or an unrestricted digital copy can be consulted.

## Plate gallery

The 123 plates assigned to this cluster, in checklist order. Plate IDs are repository identifiers, not the original 1955 plate numbers; the underlying mapping is recorded in each photograph's catalog notes.

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

Sections 18–22 and 24–25 are **canonical** mappings; each is a verbatim checklist section header and falls cleanly within this cluster. The Section 39 FACES borrowing (#446–#451) is **approximate**: those 6 photographs sit near the end of the checklist — in Section 39, immediately before the Section 40 BOMB plate (#456) — in a sequence that does not correspond to any of the 11 standard clusters with high confidence, and are assigned here provisionally. See [`research/sections.md`](https://github.com/danlex/thefamilyofman/blob/main/research/sections.md) for the full certainty table.

The cluster is bounded on the early side by `sec-work` (ending at Section 17 WOMAN'S WORK) and on the later side by `sec-eating-everyday` (Section 23 FOOD, extracted as a separate cluster) and then `sec-play-learning` (Section 26 LEARNING).

[^1]: MoMA Archives, *Edward Steichen at The Family of Man, 1955* — `src-moma-archives-highlights-1955`.
[^2]: Roland Barthes, "The Great Family of Man," in *Mythologies* (1957) — `src-barthes-1957`.
[^3]: Eric J. Sandeen, *Picturing an Exhibition: The Family of Man and 1950s America* (University of New Mexico Press, 1995) — `src-sandeen-1995`.
