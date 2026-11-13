const { Plugin } = require("obsidian");

const entryMap = '.callout[data-callout="entry-map"]';
const tableSelector = `${entryMap} > .callout-content table`;
const kinds = new Map([
  ["概念", "concept"], ["concept", "concept"],
  ["理论", "theory"], ["theory", "theory"],
  ["方法", "method"], ["method", "method"],
  ["工具", "instrument"], ["量表", "instrument"], ["测量工具", "instrument"], ["instrument", "instrument"],
  ["人物", "person"], ["person", "person"],
  ["事实", "fact"], ["机构", "fact"], ["组织", "fact"], ["政策", "fact"], ["事件", "fact"], ["fact", "fact"],
]);

function decorate(table) {
  if (table.closest(".callout")?.dataset.callout !== "entry-map") return;
  const header = table.tHead?.rows[0];
  const rows = Array.from(table.tBodies).flatMap(body => Array.from(body.rows));
  const eligible = header?.cells.length === 3 &&
    /^(类型|type)$/i.test(header.cells[1].textContent.trim()) &&
    rows.every(row => row.cells.length === 3 && Array.from(row.cells).every(cell => cell.colSpan === 1));

  table.classList.toggle("entry-map-colors", Boolean(eligible));
  for (const row of rows) {
    if (row.dataset.entryMapTooltip !== undefined) {
      if (row.title === row.dataset.entryMapTooltip) row.removeAttribute("title");
      delete row.dataset.entryMapTooltip;
    }
    delete row.dataset.entryMapKind;
    if (!eligible) continue;
    const label = row.cells[1].textContent.trim();
    row.dataset.entryMapKind = kinds.get(label.toLowerCase()) || "other";
    if (label && !row.hasAttribute("title")) {
      row.title = label;
      row.dataset.entryMapTooltip = label;
    }
  }
}

module.exports = class EntryMapView extends Plugin {
  onload() {
    // Live Preview can replace its table widget without a Markdown post-process event.
    this.app.workspace.onLayoutReady(() => {
      if (this.stopped) return;
      const tables = new Set();
      const collect = node => {
        const element = node.nodeType === 1 ? node : node.parentElement;
        if (!element) return;
        const parentTable = element.closest(tableSelector);
        if (parentTable) tables.add(parentTable);
        for (const table of element.querySelectorAll(tableSelector)) tables.add(table);
      };
      const refresh = () => {
        for (const table of tables) if (table.isConnected) decorate(table);
        tables.clear();
      };
      const observer = new MutationObserver(records => {
        for (const record of records) {
          if (record.target.parentElement?.closest(entryMap) || record.target.matches?.(entryMap)) {
            collect(record.target);
          }
          for (const node of record.addedNodes) collect(node);
        }
        refresh();
      });
      observer.observe(document.body, { childList: true, subtree: true, characterData: true });
      this.register(() => observer.disconnect());
      collect(document.body);
      refresh();
    });
  }

  onunload() {
    this.stopped = true;
    for (const table of document.querySelectorAll("table.entry-map-colors")) {
      table.classList.remove("entry-map-colors");
      for (const row of table.querySelectorAll("tr[data-entry-map-kind]")) {
        if (row.title === row.dataset.entryMapTooltip) row.removeAttribute("title");
        delete row.dataset.entryMapTooltip;
        delete row.dataset.entryMapKind;
      }
    }
  }
};
