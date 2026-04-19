// Client-side filter for list pages. No dependencies. No build step.
// Works on any <table> with class="entity-table" that has id="<name>-table".
// Reads the search input #q and optional <select> filters.

(function () {
  "use strict";

  const q = document.getElementById("q");
  const table = document.querySelector(".entity-table");
  if (!table) return;

  const tbody = table.querySelector("tbody");
  if (!tbody) return;

  const selects = Array.from(document.querySelectorAll(".list-filters select"));
  const rows = Array.from(tbody.querySelectorAll("tr"));

  // Build <select> options from column values so the filters are always
  // in sync with the table contents.
  for (const sel of selects) {
    const column = sel.id;
    if (!column) continue;
    const th = Array.from(table.querySelectorAll("th")).find(
      (el) => el.textContent.trim().toLowerCase() === column.toLowerCase()
    );
    const colIndex = th ? Array.from(th.parentNode.children).indexOf(th) : -1;
    if (colIndex === -1) continue;
    const values = new Set();
    rows.forEach((r) => {
      const v = (r.children[colIndex]?.textContent || "").trim();
      if (v) values.add(v);
    });
    const sorted = Array.from(values).sort((a, b) => a.localeCompare(b));
    for (const v of sorted) {
      const opt = document.createElement("option");
      opt.value = v;
      opt.textContent = v;
      sel.appendChild(opt);
    }
    sel.dataset.colIndex = String(colIndex);
    sel.addEventListener("change", apply);
  }

  if (q) q.addEventListener("input", apply);

  function apply() {
    const needle = (q?.value || "").toLowerCase().trim();
    const constraints = selects
      .filter((s) => s.value)
      .map((s) => ({ col: Number(s.dataset.colIndex), val: s.value }));
    let visible = 0;
    for (const row of rows) {
      const cells = Array.from(row.children);
      const text = cells.map((c) => c.textContent.trim()).join(" ").toLowerCase();
      let ok = !needle || text.includes(needle);
      if (ok) {
        for (const c of constraints) {
          if ((cells[c.col]?.textContent || "").trim() !== c.val) {
            ok = false;
            break;
          }
        }
      }
      row.style.display = ok ? "" : "none";
      if (ok) visible++;
    }
    // Empty-state swap
    let empty = document.getElementById("filter-empty");
    if (visible === 0 && rows.length > 0) {
      if (!empty) {
        empty = document.createElement("div");
        empty.id = "filter-empty";
        empty.className = "empty";
        empty.textContent = "No matches.";
        table.parentNode.insertBefore(empty, table.nextSibling);
      }
      table.style.display = "none";
    } else {
      table.style.display = "";
      if (empty) empty.remove();
    }
  }
})();
