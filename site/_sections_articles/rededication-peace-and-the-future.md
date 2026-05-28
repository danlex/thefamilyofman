---
title: "Rededication, peace, and the future"
theme: "New life; the child, democracy, peace"
order: 11
section_id: sec-rededication-future
checklist_section: "Sections 28–30 and 36–42 (plates #361–#503, with gaps; 87 photographs, mostly approximate)"
photo_count: 87
---

The exhibition closed by returning to children and new life. MoMA's archives-highlights summary names W. Eugene Smith's *A Walk to Paradise Garden* (1946) as the closing photograph, placed after the H-bomb image as a deliberate turn from apocalypse back to the possibility of the future.[^1] The CNA education portal lists "peace" among the exhibition's themes.[^2]

In the MoMA Master Checklist (Exhibition #569, `src-moma-exh-0569-master-checklist`), the closing arc spans eight sections: Section 28 RELIGIOUS EXPRESSION (#361–#374 with gap at #362), Section 29 ALONENESS AND COMPASSION (#375–#385), Section 30 ASPIRATIONS (#386–#389), Section 36 MAN'S JUDGMENT (#434–#436), Section 37 VOTING (#437–#440), Section 38 GOVERNMENT (#441–#445), Section 41 COMRADES (#457–#464), and Section 42 CHILDHOOD MAGIC (#465–#503). This is by far the most heterogeneous cluster in the 11-cluster scheme: it absorbs eight distinct checklist sections whose themes range from religion and solitude through civic life and democracy to comradeship and childhood wonder. The grouping under "Rededication, peace, and the future" is an approximation that follows the MoMA archive summary's narrative endpoint, not a claim that Steichen treated these eight sections as a single thematic unit.

The critical literature reads this closing sequence as the exhibition's humanist resolution — the move from the H-bomb image back to a child held up into sunlight. Barthes (1957) contests whether that resolution is earned: by placing the hydrogen bomb as an aberration between the continuity of daily life and the promise of the child, the exhibition proposes that the bomb is a deviation from the human story rather than a product of it, suppressing the political and military conditions that made it possible.[^3] Sandeen (1995) documents how the closing sequence was choreographed as a Cold War argument and how it was received by 1950s American audiences — `src-sandeen-1995` not re-consulted in this session; page-level citations deferred.[^4]

## Sandburg prologue excerpt

No verbatim Sandburg passage is associated with this section in `data/sections.csv`. Per the catalog reconciliation work documented in [`research/sections.md`](https://github.com/danlex/thefamilyofman/blob/main/research/sections.md), the 1955 catalog interior text was access-restricted in the Internet Archive scans consulted in earlier sessions and has not been re-fetched. The `sandburg_prologue_excerpt` field will be populated when the physical catalog or an unrestricted digital copy can be consulted.

## Plate gallery

The 87 plates assigned to this cluster, in checklist order. Plate IDs are repository identifiers, not the original 1955 plate numbers; the underlying mapping is recorded in each photograph's catalog notes.

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

This is the most approximate cluster in the 11-cluster scheme. No individual checklist section among the eight collapsed here is a clean one-to-one match to the "Rededication, peace, and the future" label. Each is assigned here because it belongs to the exhibition's closing arc and has no more specific cluster home. In [`research/sections.md`](https://github.com/danlex/thefamilyofman/blob/main/research/sections.md) all eight section-to-cluster mappings are recorded as **approximate, not canonical**. Of the eight, Sections 28–30 (RELIGIOUS EXPRESSION, ALONENESS AND COMPASSION, ASPIRATIONS) are contiguous and sit squarely in the pre-bomb closing arc, which makes them the least contestable of the assignments — but the certainty table flags them, like the other five, as approximate rather than canonical. The cluster closes with `photo-0488` (checklist #503, W. Eugene Smith, *A Walk to Paradise Garden*, 1946), the canonical closing image per `src-moma-archives-highlights-1955`.

A finer-grained schema revision — splitting this cluster into `sec-religious-expression`, `sec-civic-life`, and `sec-childhood-close` — is an identified future-work item in `research/sections.md` and may be warranted if per-section landing pages need to distinguish the closing arc more precisely. Any such revision would require re-assigning the 87 photographs.

[^1]: MoMA Archives, *Edward Steichen at The Family of Man, 1955* — `src-moma-archives-highlights-1955`.
[^2]: CNA Luxembourg, *The Family of Man, the book of humanity* — `src-cna-education`.
[^3]: Roland Barthes, "The Great Family of Man," in *Mythologies* (1957) — `src-barthes-1957`.
[^4]: Eric J. Sandeen, *Picturing an Exhibition: The Family of Man and 1950s America* (University of New Mexico Press, 1995) — `src-sandeen-1995`.
