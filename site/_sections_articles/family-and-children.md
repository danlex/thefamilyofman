---
title: Family and children
theme: "Household, parenting, the young"
order: 4
section_id: sec-family-children
checklist_section: "Sections 6, 8–13 (plates #45–#47, #51–#120 with gaps)"
photo_count: 69
---

After the childbirth and marriage sequences, the exhibition moved into its largest single thematic cluster: household life, parenting, and childhood. MoMA's own narrative summary of the exhibition's arc describes this movement as: entrance archway → lovers → childbirth → household life → careers.[^1] "Family" and "childhood" are both named by the CNA Luxembourg education portal among the exhibition's themes.[^2]

"Family and children" is a thematic cluster reconstructed from MoMA's institutional sequencing rather than a verbatim catalog heading. The 1955 catalog does not present a numbered table of contents, and different institutional sources parse the flow differently. In the MoMA Master Checklist (Exhibition #569, `src-moma-exh-0569-master-checklist`), this cluster spans seven numbered sections — Section 6 NURSING MOTHERS, Section 8 MOTHERS AND BABIES, Section 9 CHILDREN A, Section 10 FAMILY ACTIVITIES, Section 11 CHILDREN B, Section 12 FATHERS AND SONS, and Section 13 FAMILY GROUPS — making it the most structurally complex cluster in the exhibition, with checklist plate numbers running from #45 through approximately #120.

Two photographers with documented deep-dive notes in this repository have plates assigned here. David Seymour ("Chim"), whose four exhibition plates all carry a UNESCO commissioner credit, contributes plate #68 (photo-0064, Austria, Section 9 Children A) — thematically consistent with his "Children of War" project documenting children in post-war Europe, though the specific plate's connection to that UNESCO commission has not been confirmed from any source consulted in this round (per `research/photographs/photo-0064.md`).[^3] W. Eugene Smith contributes plate #105 (photo-0099, USA, Section 11 Children B) — one of four Smith plates in the exhibition. Two of the four (this Section 11 Children B plate and photo-0333 in Section 26 Learning) fall in the childhood-and-learning arc; photo-0367 sits in Section 29 Aloneness and Compassion (cluster `sec-rededication-future`); and photo-0488 (*A Walk to Paradise Garden*, Section 42 Childhood Magic) closes the exhibition at plate #503.[^4]

## Sandburg prologue excerpt

No verbatim Sandburg passage is associated with this section in `data/sections.csv`. Per the catalog reconciliation work documented in [`research/sections.md`](https://github.com/danlex/thefamilyofman/blob/main/research/sections.md), the 1955 catalog interior text was access-restricted in the Internet Archive scans consulted in earlier sessions and has not been re-fetched. The `sandburg_prologue_excerpt` field will be populated when the physical catalog or an unrestricted digital copy can be consulted.

## Plate gallery

The 69 plates assigned to this cluster, in checklist order. Plate IDs are repository identifiers, not the original 1955 plate numbers; the underlying mapping (e.g. `photo-0064` ↔ checklist plate #68) is recorded in each photograph's catalog notes.

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

This is the exhibition's largest and most internally differentiated cluster by plate count (69 plates across seven checklist sections). The mapping of all seven sections to a single `sec-family-children` cluster is a deliberate simplification, not a claim that the 1955 installation treated them as one undifferentiated unit. The checklist section headings — Nursing Mothers, Mothers and Babies, Children A, Family Activities, Children B, Fathers and Sons, Family Groups — describe an internal sequence, with the fathers-and-sons subsection standing out as one of the few explicitly gendered divisions in the checklist's section naming. The boundaries recorded in [`research/sections.md`](https://github.com/danlex/thefamilyofman/blob/main/research/sections.md) are recorded as **approximate** for the outer edges of each of the seven sub-sections, and **canonical** for the cluster's overall assignment to the household-life arc.

Roland Barthes, writing in 1957, is particularly pointed about the exhibition's treatment of birth and childhood: the show's claim that children are born "everywhere in the same way" and experience childhood as a universal condition was, for Barthes, the most visible example of the exhibition's project of naturalizing what is historically conditioned.[^5] David Seymour's four UNESCO-commissioned plates of post-war European children — placed in sections dedicated to children as innocent universals — are exactly the kind of images whose historical particularity, Barthes argued, the exhibition's framing suppressed.

[^1]: MoMA Archives, *Edward Steichen at The Family of Man, 1955* — `src-moma-archives-highlights-1955`.
[^2]: CNA Luxembourg, *The Family of Man, the book of humanity* — `src-cna-education`.
[^3]: Research note: `research/photographs/photo-0064.md`, read this session. Sources cited there include `src-moma-exh-0569-master-checklist` (Tier-1, in-repo) and `src-icp-1966-concerned-photography-fund-institutional`.
[^4]: Research note: `research/photographs/photo-0099.md`, read this session. Sources cited there include `src-moma-exh-0569-master-checklist` (Tier-1, in-repo), `src-icp-w-eugene-smith-archive`, and `src-magnum-w-eugene-smith`.
[^5]: Roland Barthes, "The Great Family of Man," in *Mythologies* (1957) — `src-barthes-1957`.
