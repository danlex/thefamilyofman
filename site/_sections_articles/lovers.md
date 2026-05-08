---
title: Lovers
theme: "Love and courtship"
order: 2
section_id: sec-lovers
checklist_section: "Section 2 (plates #12–#25)"
photo_count: 14
---

After the entrance-archway prologue, the exhibition moved into photographs of courting and lovers.[^1] "Love" is one of the themes explicitly named on CNA Luxembourg's educational portal as part of its count of 37 themes.[^2]

The boundaries of this cluster are not canonical: the 1955 catalog does not present a numbered table of contents, and different institutional sources parse the same flow into different numbers of sub-themes. This article documents a thematic cluster reconstructed from MoMA's own narrative summary of the sequence.[^1] In the MoMA Master Checklist (Exhibition #569, `src-moma-exh-0569-master-checklist`), Section 2 LOVERS is canonical and runs from plate #12 through plate #25 — the 14 photographs listed below.

## Sandburg prologue excerpt

No verbatim Sandburg passage is associated with this section in `data/sections.csv`. Per the catalog reconciliation work documented in [`research/sections.md`](https://github.com/danlex/thefamilyofman/blob/main/research/sections.md), the 1955 catalog interior text was access-restricted in the Internet Archive scans consulted in earlier sessions and has not been re-fetched. Sandburg's prose prologue was distributed in full as a leaflet to visitors and reprinted in both editions of the catalog;[^3] which lines, if any, were placed beside the LOVERS sequence on the gallery wall is a documented open question.

## Plate gallery

The 14 plates assigned to this cluster, in checklist order. Plate IDs are repository identifiers, not the original 1955 plate numbers; the underlying mapping (e.g. `photo-0009` ↔ checklist plate #12) is recorded in each photograph's catalog notes.

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

Section 2 LOVERS is one of the cleaner mappings between the MoMA checklist and this repo's 11-cluster scheme: the cluster contains exactly the 14 plates the checklist labels Section 2, with no out-of-section borrowings or approximate-fit cases. The mapping certainty in [`research/sections.md`](https://github.com/danlex/thefamilyofman/blob/main/research/sections.md) is recorded as **canonical**.

[^1]: MoMA Archives, *Edward Steichen at The Family of Man, 1955* — `src-moma-archives-highlights-1955`.
[^2]: CNA Luxembourg, *The Family of Man, the book of humanity* — `src-cna-education`.
[^3]: MoMA, press release for the 1955 exhibition — `src-moma-1955-press-release-book`. Distribution-as-leaflet is documented there and in `src-moma-1955-catalog`.
