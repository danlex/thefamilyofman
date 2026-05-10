---
title: "Hardship, suffering, and war"
theme: "Pain, conflict, and injustice"
order: 9
section_id: sec-hardship-suffering-war
checklist_section: "Sections 31–34 (plates #390–#413) and Section 40 BOMB (plate #456)"
photo_count: 30
---

The exhibition moved from mid-flow social life into a sequence on hardship, suffering, and war. "War" and the exhibition's famously oversized hydrogen-bomb image are both attested in institutional summaries: MoMA's archives-highlights page names the H-bomb image as a late-flow pivot;[^1] the CNA education portal lists "war" as one of the exhibition's themes, paired with "peace."[^2]

The cluster aggregates five checklist sections: Section 31 HARD TIMES, Section 32 FAMINE, Section 33 INHUMANITIES, Section 34 REVOLT, and Section 40 BOMB. The five sections describe a thematic progression from structural poverty through famine, institutionalized violence, political revolt, and finally nuclear threat. Section 40 BOMB stands apart in the checklist as a single-plate section — plate #456, credited to the Atomic Energy Commission, Marshall Islands, 96 × 120 cm — separated from the Revolt sequence by several intervening plates.[^3] Its inclusion in this cluster represents an editorial judgment that it belongs to the arc of violence and destruction rather than to the closing renewal sequence. That assignment is recorded as **approximate** in `data/sections.csv`.

Three photographers with documented deep-dive notes in this repository have plates in this cluster. Werner Bischof contributes plate #395 (photo-0381, India, Section 32 Famine) — the opening image of the Famine section, consistent with his documented 1951 *LIFE* assignment on famine conditions in India (the Magnum biography records Bischof was "sent to report on famine in India by *Life* magazine in 1951"); the checklist does not explicitly link plate #395 to that 1951 assignment in any source consulted this round (per `research/photographs/photo-0381.md`). Contributed posthumously (Bischof died in the Peruvian Andes on 16 May 1954).[^4] Henri Cartier-Bresson contributes plate #409 (photo-0395, China, Section 34 Revolt) — a wide-format landscape print (18 × 27 1/4 cm) that is the only Cartier-Bresson plate set in China across his eleven plates in the exhibition.[^5] The Atomic Energy Commission's plate #456 (photo-0441) is documented in detail: it is the sole entry in Section 40 BOMB, with print dimensions of 96 × 120 cm, and its specific test origin (Ivy Mike 1952 or Castle Bravo 1954) has not been confirmed against any source accessed in this round.[^3]

## Sandburg prologue excerpt

No verbatim Sandburg passage is associated with this section in `data/sections.csv`. Per the catalog reconciliation work documented in [`research/sections.md`](https://github.com/danlex/thefamilyofman/blob/main/research/sections.md), the 1955 catalog interior text was access-restricted in the Internet Archive scans consulted in earlier sessions and has not been re-fetched. The `sandburg_prologue_excerpt` field will be populated when the physical catalog or an unrestricted digital copy can be consulted.

## Plate gallery

The 30 plates assigned to this cluster, in checklist order. Plate IDs are repository identifiers, not the original 1955 plate numbers; the underlying mapping (e.g. `photo-0381` ↔ checklist plate #395) is recorded in each photograph's catalog notes.

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

The cluster's internal boundaries between checklist sections are **canonical** for Sections 31–33 (Hard Times, Famine, and Inhumanities are clearly delimited in the checklist with contiguous plate numbers). Section 34 REVOLT is also canonical in its checklist assignment, but one plate (#422, Ralph Crane, Germany) appears out of order within its plate-number block and is recorded as an **approximate** fit. Section 40 BOMB's assignment to this cluster — rather than to the adjacent `sec-rededication-future` cluster — is **approximate**: the bomb plate functions structurally as both the endpoint of the violence arc and the turning point toward the closing renewal sequence, and different critics read it in both directions. The cluster boundary at Section 40/41 is this repository's interpretive choice, not a canonical partition. The plate numbered #422 from the Ralph Crane block is documented as an out-of-order entry in `data/sections.csv`.

This section is the one Roland Barthes's 1957 critique targets most forcefully. Barthes argues that by placing suffering within a universal humanist frame, the exhibition offers "an eternal lyricism" in place of the historical and political specificity of injustice. His test case — quoted as recorded in `research/photographs/photo-0381.md`, read this session, citing `src-barthes-1957` (Tier-2, in-repo) — is: "Why not ask the parents of Emmet Till, the young Negro assassinated by the Whites what they think of The Great Family of Man?" — an argument about precisely the Famine and Inhumanities sections, where images of historically specific violence and deprivation are received as illustrations of universal suffering rather than as records of particular injustices with causes and perpetrators.[^6]

Eric J. Sandeen (1995) reconstructs how the exhibition was received in its Cold War context, and how the H-bomb plate functioned within that reception — including at the 1959 Moscow showing, where a US government-sponsored exhibition displaying an American nuclear test image carried explicit political stakes that the humanist framing was meant to transcend.[^7] Allan Sekula's critique of the AEC plate extends the argument: a government agency's promotional image of its own weapons test, placed inside a humanist museum frame, is a paradigm case of how institutions produce and direct the meaning of photographs.[^8]

Any curatorial description of this cluster that stops at "universal suffering" without acknowledging these counter-readings reproduces the humanism Barthes, Sandeen, and Sekula problematized.

[^1]: MoMA Archives, *Edward Steichen at The Family of Man, 1955* — `src-moma-archives-highlights-1955`.
[^2]: CNA Luxembourg, *The Family of Man, the book of humanity* — `src-cna-education`.
[^3]: Research note: `research/photographs/photo-0441.md`, read this session. Sources cited there include `src-moma-exh-0569-master-checklist` (Tier-1, in-repo) and `src-moma-archives-highlights-1955`.
[^4]: Research note: `research/photographs/photo-0381.md`, read this session. Sources cited there include `src-moma-exh-0569-master-checklist` (Tier-1, in-repo), `src-magnum-werner-bischof`, and `src-icp-werner-bischof-archive`.
[^5]: Research note: `research/photographs/photo-0395.md`, read this session. Sources cited there include `src-moma-exh-0569-master-checklist` (Tier-1, in-repo). HCB biographical details noted there as not verified against a primary fetch in that round; the claim is not repeated here.
[^6]: Roland Barthes, "The Great Family of Man," in *Mythologies* (1957) — `src-barthes-1957`.
[^7]: Eric J. Sandeen, *Picturing an Exhibition: The Family of Man and 1950s America* (University of New Mexico Press, 1995) — `src-sandeen-1995`. Body text not accessed in this round; cited as the standard Tier-2 anchor for Cold War reception and Moscow-showing analysis, carried from the in-repo source file.
[^8]: Allan Sekula, "The Traffic in Photographs," *Art Journal*, 1981 — `src-sekula-1981`. Body text not accessed in this round (JSTOR returned 403 in prior research sessions); argument carried from the in-repo source file and from `research/photographs/photo-0441.md`, read this session.
