---
title: Marriage and childbirth
theme: "Union, conception, and birth"
order: 3
section_id: sec-marriage-birth
checklist_section: "Sections 3–5 and 7 (plates #26–#50, with gaps; 22 photographs)"
photo_count: 22
---

Following the lovers sequence, the exhibition turned to marriage and to childbirth — a theme MoMA's archives-highlights page names directly in its summary of the flow,[^1] and which the CNA education portal includes in its enumeration of the exhibition's themes.[^2]

This grouping is a thematic cluster; "marriage and childbirth" is not a verbatim heading from the 1955 catalog, which does not present its sequencing as titled sections. In the MoMA Master Checklist (Exhibition #569, `src-moma-exh-0569-master-checklist`), the equivalent named sections are MARRIAGE (Section 3, plates #26–#32), PREGNANCY (Section 4, plates #33–#41), CHILDBIRTH (Section 5, plates #42–#44), and BIRTHS (Section 7, plates #48–#50). These four have been collapsed into this single cluster following the MoMA archive summary's narrative logic. Note that Section 6 NURSING MOTHERS (#45–#47) was assigned instead to `sec-family-children` because it precedes rather than follows the Birth cluster in the checklist.

Roland Barthes's 1957 critique bears specifically on the curatorial logic of grouping marriage and birth under universal headings. Barthes framed the exhibition's premise as the assertion that "birth, death, work, knowledge, play, always impose the same types of behaviour; there is a family of Man," and judged this "myth of the human 'condition'" to "[rest] on a very old mystification, which always consists in placing Nature at the bottom of History."[^3]

## Sandburg prologue excerpt

No verbatim Sandburg passage is associated with this section in `data/sections.csv`. Per the catalog reconciliation work documented in [`research/sections.md`](https://github.com/danlex/thefamilyofman/blob/main/research/sections.md), the 1955 catalog interior text was access-restricted in the Internet Archive scans consulted in earlier sessions and has not been re-fetched. The `sandburg_prologue_excerpt` field will be populated when the physical catalog or an unrestricted digital copy can be consulted.

## Plate gallery

The 22 plates assigned to this cluster, in checklist order. Plate IDs are repository identifiers, not the original 1955 plate numbers; the underlying mapping (e.g. `photo-0023` ↔ checklist plate #26) is recorded in each photograph's catalog notes.

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

The cluster mapping is **canonical** per [`research/sections.md`](https://github.com/danlex/thefamilyofman/blob/main/research/sections.md). It collapses four adjacent checklist sections (3 Marriage, 4 Pregnancy, 5 Childbirth, 7 Births) into a single landing-page cluster in order to keep this repo's 11-cluster scheme aligned with the MoMA narrative summary. The collapsed mapping is explicitly documented and does not assert that Steichen treated these as a single thematic unit — only that they form a natural arc in the checklist progression. The cluster is bounded on the early side by Section 2 LOVERS (mapped to `sec-lovers`) and on the later side by Section 6 NURSING MOTHERS, which is mapped to `sec-family-children`.

[^1]: MoMA Archives, *Edward Steichen at The Family of Man, 1955* — `src-moma-archives-highlights-1955`.
[^2]: CNA Luxembourg, *The Family of Man, the book of humanity* — `src-cna-education`.
[^3]: Roland Barthes, "The Great Family of Man," in *Mythologies* (1957) — `src-barthes-1957`.
