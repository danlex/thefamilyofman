---
title: Eating and everyday life
theme: "Shared meals, daily ritual"
order: 7
section_id: sec-eating-everyday
checklist_section: "Section 23 (plates #254–#268, with gap at #261; 14 photographs)"
photo_count: 14
---

Shared meals and the rituals of daily life are a recurring motif in the exhibition's mid-flow sequence. In the MoMA Master Checklist (Exhibition #569, `src-moma-exh-0569-master-checklist`), Section 23 is labeled FOOD and runs from plate #254 through plate #268, with a gap at #261. This cluster corresponds exactly to that checklist section.

The theme of communal eating sits between the large Relationships and Community cluster (Sections 18–25) and the Play and Learning section (Section 26) in the exhibition's mid-flow sequence. "Eating and everyday life" is not named as a discrete theme in MoMA's archive-highlights narrative summary;[^1] it is included here because Section 23 FOOD is a verbatim checklist heading and the 14 photographs it covers are unambiguously assigned. The cluster is modest in size but anchored by the canonical checklist section label.

The critical literature does not treat this cluster as a primary site of contestation in the same way as Birth, Death, or Hardship clusters. Barthes's universalism critique applies to it — shared meals across cultures are among the exhibition's demonstrations that all humans share essential needs — but neither `src-barthes-1957` nor `src-sandeen-1995` singles it out for extended analysis. The cluster should be read against the curatorial logic of universalism, not as an exception to it.

## Sandburg prologue excerpt

No verbatim Sandburg passage is associated with this section in `data/sections.csv`. Per the catalog reconciliation work documented in [`research/sections.md`](https://github.com/danlex/thefamilyofman/blob/main/research/sections.md), the 1955 catalog interior text was access-restricted in the Internet Archive scans consulted in earlier sessions and has not been re-fetched. The `sandburg_prologue_excerpt` field will be populated when the physical catalog or an unrestricted digital copy can be consulted.

## Plate gallery

The 14 plates assigned to this cluster, in checklist order. Plate IDs are repository identifiers, not the original 1955 plate numbers; the underlying mapping (e.g. `photo-0244` ↔ checklist plate #254) is recorded in each photograph's catalog notes.

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

Section 23 FOOD is among the cleaner mappings: the cluster contains exactly the plates the checklist assigns to that section, with no borrowings from adjacent sections and no out-of-section plates. The mapping certainty in [`research/sections.md`](https://github.com/danlex/thefamilyofman/blob/main/research/sections.md) is recorded as **canonical**. The cluster is bounded on both sides by checklist material absorbed into `sec-relationships-community` (Sections 22 and 24 on either side).

[^1]: MoMA Archives, *Edward Steichen at The Family of Man, 1955* — `src-moma-archives-highlights-1955`.
