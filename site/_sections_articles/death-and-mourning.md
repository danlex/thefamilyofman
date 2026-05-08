---
title: Death and mourning
theme: "End of life, grief"
order: 10
section_id: sec-death-mourning
checklist_section: "Section 27 (plates #348–#360, contiguous, with one out-of-order plate at #358)"
photo_count: 13
---

Death is one of the exhibition's canonical late-flow clusters. MoMA's archives-highlights summary names "Death" as a discrete stage in the narrative progression before the rededication sequence on children and new life.[^1]

Roland Barthes, writing in 1957, makes this section the core of his critique: "to reproduce death or birth tells us, literally, nothing. For these natural facts to gain access to a true language, they must be inserted into a category of knowledge ... whether or not he is threatened by a high mortality rate, whether or not such and such a type of future is open to him: this is what your Exhibitions should be telling people, instead of an eternal lyricism of birth [and death]."[^2] Eric Sandeen (1995) reconstructs how the exhibition's death sequence was built and how it functioned within the humanist argument of the whole, and is the standard Tier-2 anchor for interpretive readings of this cluster.[^3]

In the MoMA Master Checklist (Exhibition #569, `src-moma-exh-0569-master-checklist`), Section 27 DEATH runs across plates #348–#360 — a contiguous range of 13 plate numbers — with one plate (#358) printed out of numerical order. The 13 photographs listed below are the catalog rows mapped to `sec-death-mourning` in `data/photographs.csv`.

## Sandburg prologue excerpt

No verbatim Sandburg passage is associated with this section in `data/sections.csv`. Per the catalog reconciliation work documented in [`research/sections.md`](https://github.com/danlex/thefamilyofman/blob/main/research/sections.md), the 1955 catalog interior text was access-restricted in the Internet Archive scans consulted in earlier sessions and has not been re-fetched. The `sandburg_prologue_excerpt` field will be populated when the physical catalog or an unrestricted digital copy can be consulted.

## Plate gallery

The 13 plates assigned to this cluster, in checklist order. Plate IDs are repository identifiers, not the original 1955 plate numbers; the underlying mapping (e.g. `photo-0335` ↔ checklist plate #348) is recorded in each photograph's catalog notes.

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

Section 27 DEATH is one of the cleaner mappings between the MoMA checklist and this repo's 11-cluster scheme: the cluster contains exactly the 13 plates the checklist labels Section 27 (with documented checklist gaps), and no plates are borrowed in from neighbouring sections. The mapping certainty in [`research/sections.md`](https://github.com/danlex/thefamilyofman/blob/main/research/sections.md) is recorded as **canonical**. Note that this cluster sits adjacent to the much larger `sec-rededication-future` (87 plates spanning checklist Sections 28–30 and 36–42), which absorbs several closing-arc sections under approximate, not canonical, mappings — so the boundary between "Death and mourning" and "Rededication, peace, and the future" is precise on the early side (Section 27 ↔ Section 28 transition is a clean hand-off) but coarse on the later side.

[^1]: MoMA Archives, *Edward Steichen at The Family of Man, 1955* — `src-moma-archives-highlights-1955`.
[^2]: Roland Barthes, "The Great Family of Man," in *Mythologies* (1957) — `src-barthes-1957`.
[^3]: Eric J. Sandeen, *Picturing an Exhibition: The Family of Man and 1950s America* (University of New Mexico Press, 1995) — `src-sandeen-1995`.
