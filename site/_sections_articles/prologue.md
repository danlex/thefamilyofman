---
title: Prologue
theme: "Entry — crowds and the human collective"
order: 1
section_id: sec-prologue
checklist_section: "Section 1 (plates #1–#11A, 8 photographs)"
photo_count: 8
---

The exhibition opened with an entrance archway and crowd imagery, a visual prelude that asked visitors to see themselves as one among many before entering the thematic sequence that followed.[^1] Carl Sandburg's prologue — the source of the exhibition's title, drawn from his 1944 poem *The Long Shadow of Lincoln: A Litany* — was distributed in full to visitors as a leaflet and reprinted in both the paperback and deluxe editions of the 1955 catalog.[^2] Its closing sentence, quoted in MoMA's June 21, 1955 press release, reads: "A camera testament, a drama of the grand canyon of humanity, an epic woven of fun, mystery and holiness — here is the Family of Man."[^2]

This article treats the prologue as a thematic cluster rather than as a canonical numbered section; the 1955 catalog does not label its sections numerically, and institutional counts of the exhibition's themes differ (UNESCO lists 32; the CNA Luxembourg education portal lists 37).[^3] See [Sections](/sections/) for the overall structure.

## Sandburg prologue excerpt

No verbatim Sandburg passage is associated with this section in `data/sections.csv`. Per the catalog reconciliation work documented in [`research/sections.md`](https://github.com/danlex/thefamilyofman/blob/main/research/sections.md), the 1955 catalog interior text was access-restricted in the Internet Archive scans consulted in earlier sessions and has not been re-fetched. The `sandburg_prologue_excerpt` field will be populated when the physical catalog or an unrestricted digital copy can be consulted.

## Plate gallery

The 8 plates assigned to this cluster, in checklist order. Plate IDs are repository identifiers, not the original 1955 plate numbers; the underlying mapping (e.g. `photo-0001` ↔ checklist plate #1) is recorded in each photograph's catalog notes.

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

Section 1 PROLOGUE is a canonical checklist section in `src-moma-exh-0569-master-checklist`. The 8 photographs assigned here (plates #1–#11A with documented gaps at #5, #7, #8, #11) are those mapped to `sec-prologue` in `data/photographs.csv`. Gaps at #5, #7, #8, and the bare slot #11 are documented missing numbers in the current catalog; the Eugene Harris Peruvian flute-player image is roweed separately as #11A. The certainty of this mapping is **canonical** per [`research/sections.md`](https://github.com/danlex/thefamilyofman/blob/main/research/sections.md).

[^1]: MoMA Archives, *Edward Steichen at The Family of Man, 1955* — `src-moma-archives-highlights-1955`.
[^2]: Museum of Modern Art, press release for the book editions of *The Family of Man*, June 21, 1955 — `src-moma-1955-press-release-book`; *The Family of Man*, Edward Steichen (ed.), MoMA, 1955 — `src-moma-1955-catalog`.
[^3]: UNESCO Memory of the World register, 2003 — `src-unesco-mow-2003`; CNA Luxembourg, *The Family of Man, the book of humanity* — `src-cna-education`.
