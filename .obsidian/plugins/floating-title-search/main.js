"use strict";
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

// src/main.ts
var main_exports = {};
__export(main_exports, {
  default: () => FloatingTitleSearch
});
module.exports = __toCommonJS(main_exports);
var import_obsidian2 = require("obsidian");

// src/floating-panel.ts
var import_obsidian = require("obsidian");

// src/settings.ts
function clamp(value, min, max) {
  return Math.min(Math.max(value, min), Math.max(min, max));
}
function readSettings(saved) {
  function dimension(value, fallback, min, max) {
    return typeof value === "number" && Number.isFinite(value) ? clamp(value, min, max) : fallback;
  }
  return {
    centerY: typeof saved?.centerY === "number" && Number.isFinite(saved.centerY) ? saved.centerY : null,
    width: dimension(saved?.width, 320, 240, 600),
    height: dimension(saved?.height, 330, 156, 720),
    hidden: saved?.hidden === true,
    exactAliases: saved?.exactAliases === true
  };
}

// src/search.ts
var RESULT_LIMIT = 30;
var PATH_ORDER = new Intl.Collator("zh-CN", { numeric: true });
function searchTitles(entries, input, exactAliases) {
  const query = input.trim().toLowerCase();
  const rows = [];
  if (!query) return { rows, total: 0, query };
  for (const entry of entries) {
    if (entry.foldedTitle === query) {
      rows.push({ entry, tier: 0, foldedStart: 0 });
      continue;
    }
    const alias = exactAliases ? entry.aliases.get(query) : void 0;
    if (alias) {
      rows.push({ entry, tier: 1, foldedStart: -1, alias });
      continue;
    }
    const start = entry.foldedTitle.indexOf(query);
    if (start >= 0) rows.push({ entry, tier: 2, foldedStart: start });
  }
  rows.sort((a, b) => a.tier - b.tier || b.entry.mtime - a.entry.mtime || PATH_ORDER.compare(a.entry.path, b.entry.path) || (a.entry.path < b.entry.path ? -1 : a.entry.path > b.entry.path ? 1 : 0));
  return { rows: rows.slice(0, RESULT_LIMIT), total: rows.length, query };
}
function titleRange(title, foldedTitle, start, length) {
  if (title.length === foldedTitle.length) return [start, start + length];
  let original = 0;
  let folded = 0;
  let from = 0;
  for (const character of title) {
    const next = folded + character.toLowerCase().length;
    if (folded <= start && start < next) from = original;
    original += character.length;
    if (next >= start + length) return [from, original];
    folded = next;
  }
  return [from, title.length];
}

// src/floating-panel.ts
var MARGIN = 8;
var LEAVE_DELAY = 150;
var TYPE_DELAY = 50;
function el(parent, tag, className = "", label = "") {
  const node = parent.ownerDocument.createElement(tag);
  if (className) node.className = className;
  if (label) node.textContent = label;
  parent.append(node);
  return node;
}
function button(parent, className, label) {
  const node = el(parent, "button", className);
  node.type = "button";
  node.setAttribute("aria-label", label);
  node.title = label;
  return node;
}
var FloatingSearch = class {
  constructor(host, state, entries, openNote, save) {
    this.host = host;
    this.state = state;
    this.entries = entries;
    this.openNote = openNote;
    this.save = save;
    this.events = new AbortController();
    this.expanded = false;
    this.pointerInside = false;
    this.composing = false;
    this.leaving = null;
    this.pending = null;
    this.rows = [];
    this.options = [];
    this.selected = -1;
    this.lastQuery = "";
    this.opening = false;
    this.root = el(host.document.body, "aside", "fts-float");
    this.root.setAttribute("aria-label", "\u6807\u9898\u641C\u7D22");
    this.root.hidden = state.hidden;
    this.rail = button(this.root, "fts-rail", "\u5C55\u5F00\u6807\u9898\u641C\u7D22");
    this.rail.setAttribute("aria-controls", "fts-panel");
    (0, import_obsidian.setIcon)(el(this.rail, "span", "fts-rail-icon"), "search");
    el(this.rail, "span", "fts-rail-label", "\u641C\u7D22");
    this.body = el(this.root, "section", "fts-body");
    this.body.id = "fts-panel";
    this.body.hidden = true;
    this.body.setAttribute("aria-labelledby", "fts-heading");
    const header = el(this.body, "header", "fts-header");
    const handle = el(header, "div", "fts-handle");
    handle.title = "\u6CBF\u53F3\u4FA7\u62D6\u52A8\u641C\u7D22\u5165\u53E3";
    (0, import_obsidian.setIcon)(el(handle, "span", "fts-grip"), "grip-horizontal");
    el(handle, "h2", "fts-heading", "\u6807\u9898\u641C\u7D22").id = "fts-heading";
    const minimize = button(header, "fts-icon-button", "\u6536\u8D77\u6807\u9898\u641C\u7D22");
    (0, import_obsidian.setIcon)(minimize, "minus");
    const hide = button(header, "fts-icon-button", "\u9690\u85CF\u6807\u9898\u641C\u7D22");
    (0, import_obsidian.setIcon)(hide, "x");
    const field = el(this.body, "div", "fts-field");
    this.input = el(field, "input", "fts-input");
    this.input.type = "search";
    this.input.placeholder = "\u8F93\u5165\u6807\u9898\u2026";
    this.input.spellcheck = false;
    this.input.autocomplete = "off";
    this.input.setAttribute("aria-label", "\u641C\u7D22\u6807\u9898");
    this.input.setAttribute("role", "combobox");
    this.input.setAttribute("aria-autocomplete", "list");
    this.input.setAttribute("aria-controls", "fts-results");
    this.input.setAttribute("aria-expanded", "false");
    this.status = el(this.body, "p", "fts-status", "\u8F93\u5165\u6807\u9898\u5173\u952E\u8BCD");
    this.status.setAttribute("role", "status");
    this.list = el(this.body, "div", "fts-results");
    this.list.id = "fts-results";
    this.list.setAttribute("role", "listbox");
    this.list.setAttribute("aria-label", "\u7B14\u8BB0\u641C\u7D22\u7ED3\u679C");
    this.list.hidden = true;
    const footer = el(this.body, "footer", "fts-footer");
    const label = el(footer, "label", "fts-alias-option");
    const aliases = el(label, "input");
    aliases.type = "checkbox";
    aliases.checked = state.exactAliases;
    el(label, "span", "", "\u5339\u914D\u5B8C\u6574\u522B\u540D");
    const resize = el(footer, "span", "fts-resize");
    resize.title = "\u62D6\u52A8\u8C03\u6574\u9762\u677F\u5BBD\u5EA6\u548C\u6700\u5927\u9AD8\u5EA6";
    const signal = this.events.signal;
    this.rail.addEventListener("pointerenter", (event) => {
      if (event.pointerType === "mouse") this.show(false);
    }, { signal });
    this.rail.addEventListener("click", () => this.show(true), { signal });
    this.root.addEventListener("pointerenter", (event) => {
      if (event.pointerType !== "mouse") return;
      this.pointerInside = true;
      this.cancelLeave();
    }, { signal });
    this.root.addEventListener("pointerleave", (event) => {
      if (event.pointerType !== "mouse") return;
      this.pointerInside = false;
      this.deferCollapse();
    }, { signal });
    this.root.addEventListener("focusout", () => this.deferCollapse(), { signal });
    this.root.addEventListener("keydown", (event) => this.onKey(event), { signal });
    this.input.addEventListener("input", () => {
      if (!this.composing) this.refresh();
    }, { signal });
    this.input.addEventListener("compositionstart", () => {
      this.composing = true;
      this.cancelSearch();
    }, { signal });
    this.input.addEventListener("compositionend", () => {
      this.composing = false;
      this.refresh();
    }, { signal });
    this.list.addEventListener("click", (event) => {
      const row = event.target.closest(".fts-row");
      if (row) void this.openAt(Number(row.dataset.index));
    }, { signal });
    aliases.addEventListener("change", () => {
      this.state.exactAliases = aliases.checked;
      this.render();
      this.save();
    }, { signal });
    minimize.addEventListener("click", () => this.collapse(true), { signal });
    hide.addEventListener("click", () => {
      this.collapse(false);
      this.state.hidden = true;
      this.root.hidden = true;
      this.pointerInside = false;
      this.save();
    }, { signal });
    host.addEventListener("resize", () => this.place(), { signal });
    this.bindDrag(handle, () => {
      const original = this.rail.getBoundingClientRect();
      return (_dx, dy) => {
        this.state.centerY = original.top + original.height / 2 + dy;
        this.place();
      };
    });
    this.bindDrag(resize, () => {
      const original = this.body.getBoundingClientRect();
      return (dx, dy) => {
        this.state.width = clamp(original.width - dx, 240, 600);
        this.state.height = clamp(original.height + dy, 156, 720);
        this.place();
      };
    });
    this.collapse(false);
  }
  show(focus) {
    this.cancelLeave();
    if (this.state.hidden) {
      if (!focus) return;
      this.state.hidden = false;
      this.root.hidden = false;
      this.save();
    }
    if (!this.expanded) {
      this.expanded = true;
      this.body.hidden = false;
      this.root.dataset.open = "true";
      this.rail.setAttribute("aria-expanded", "true");
      this.render();
    }
    if (focus) this.input.focus({ preventScroll: true });
  }
  refresh() {
    if (!this.expanded || this.pending !== null || this.composing) return;
    this.pending = this.host.setTimeout(() => {
      this.pending = null;
      this.render();
    }, TYPE_DELAY);
  }
  destroy() {
    this.cancelLeave();
    this.cancelSearch();
    this.events.abort();
    this.root.remove();
  }
  render() {
    this.cancelSearch();
    const { rows, total, query } = searchTitles(this.entries(), this.input.value, this.state.exactAliases);
    const sameQuery = query === this.lastQuery;
    const path = sameQuery ? this.rows[this.selected]?.entry.path : null;
    this.lastQuery = query;
    this.rows = rows;
    this.options = [];
    this.list.replaceChildren();
    this.list.hidden = !rows.length;
    this.input.setAttribute("aria-expanded", String(Boolean(rows.length)));
    for (const [index, match] of rows.entries()) {
      const row = el(this.list, "button", "fts-row");
      row.type = "button";
      row.id = "fts-result-" + index;
      row.tabIndex = -1;
      row.dataset.index = String(index);
      row.setAttribute("role", "option");
      row.title = match.entry.title + "\n" + match.entry.path;
      const title = el(row, "span", "fts-result-title");
      if (match.foldedStart < 0) title.textContent = match.entry.title;
      else {
        const [from, to] = titleRange(match.entry.title, match.entry.foldedTitle, match.foldedStart, query.length);
        title.append(match.entry.title.slice(0, from));
        el(title, "mark", "", match.entry.title.slice(from, to));
        title.append(match.entry.title.slice(to));
      }
      const meta = el(row, "span", "fts-result-path");
      if (match.alias) {
        meta.append("\u522B\u540D ");
        el(meta, "mark", "", match.alias);
        meta.append(" \xB7 ");
      }
      meta.append(match.entry.path);
      this.options.push(row);
    }
    if (!query) this.status.textContent = "\u8F93\u5165\u6807\u9898\u5173\u952E\u8BCD";
    else if (!total) this.status.textContent = "\u672A\u627E\u5230\u5339\u914D\u6807\u9898";
    else this.status.textContent = total > RESULT_LIMIT ? "\u663E\u793A " + RESULT_LIMIT + " \u9879\uFF0C\u5171 " + total + " \u9879" : total + " \u9879\u7ED3\u679C";
    this.status.classList.toggle("fts-has-results", total > 0);
    if (!sameQuery) this.list.scrollTop = 0;
    if (rows.length) this.select(Math.max(0, rows.findIndex((match) => match.entry.path === path)), false);
    else {
      this.selected = -1;
      this.input.removeAttribute("aria-activedescendant");
    }
    this.place();
  }
  select(index, scroll = true) {
    this.selected = index;
    const active = this.options[index];
    for (const row of this.options) row.setAttribute("aria-selected", String(row === active));
    this.input.setAttribute("aria-activedescendant", active.id);
    if (scroll) active.scrollIntoView({ block: "nearest" });
  }
  async openAt(index) {
    if (this.opening || !this.rows[index]) return;
    this.opening = true;
    try {
      await this.openNote(this.rows[index].entry.path);
      this.collapse(false);
    } catch {
      this.status.textContent = "\u7B14\u8BB0\u53EF\u80FD\u5DF2\u79FB\u52A8\u6216\u5220\u9664";
      this.refresh();
    } finally {
      this.opening = false;
    }
  }
  onKey(event) {
    if (!this.expanded || event.isComposing || this.composing) return;
    if (event.key === "Escape") {
      event.preventDefault();
      event.stopPropagation();
      if (this.input.value) {
        this.input.value = "";
        this.render();
        this.input.focus({ preventScroll: true });
      } else this.collapse(true);
      return;
    }
    if (event.target !== this.input || !["ArrowDown", "ArrowUp", "Enter"].includes(event.key)) return;
    event.preventDefault();
    event.stopPropagation();
    if (this.pending !== null || this.lastQuery !== this.input.value.trim().toLowerCase()) this.render();
    if (!this.rows.length) return;
    if (event.key === "Enter") void this.openAt(this.selected);
    else this.select(clamp(this.selected + (event.key === "ArrowDown" ? 1 : -1), 0, this.rows.length - 1));
  }
  collapse(focus) {
    this.cancelLeave();
    this.cancelSearch();
    this.expanded = false;
    this.body.hidden = true;
    this.root.dataset.open = "false";
    this.rail.setAttribute("aria-expanded", "false");
    if (focus) this.rail.focus({ preventScroll: true });
    this.place();
  }
  cancelSearch() {
    if (this.pending === null) return;
    this.host.clearTimeout(this.pending);
    this.pending = null;
  }
  cancelLeave() {
    if (this.leaving === null) return;
    this.host.clearTimeout(this.leaving);
    this.leaving = null;
  }
  deferCollapse() {
    if (!this.expanded || this.leaving !== null) return;
    this.leaving = this.host.setTimeout(() => {
      this.leaving = null;
      if (!this.pointerInside && !this.body.contains(this.host.document.activeElement)) this.collapse(false);
    }, LEAVE_DELAY);
  }
  place() {
    if (this.root.hidden) return;
    const height = this.rail.offsetHeight;
    const viewport = this.host.innerHeight;
    const defaultCenter = Math.min(viewport * 0.34, viewport * 0.68 - 148);
    const top = clamp((this.state.centerY ?? defaultCenter) - height / 2, MARGIN, viewport - height - MARGIN);
    this.root.style.top = top + "px";
    this.body.style.setProperty("--fts-width", this.state.width + "px");
    this.body.style.setProperty("--fts-height", this.state.height + "px");
    if (this.expanded) {
      const panelHeight = this.body.offsetHeight;
      const panelTop = clamp(top + (height - panelHeight) / 2, MARGIN, viewport - panelHeight - MARGIN);
      this.body.style.top = panelTop - top + "px";
    }
  }
  bindDrag(handle, startDrag) {
    let drag = null;
    const signal = this.events.signal;
    handle.addEventListener("pointerdown", (event) => {
      if (event.button !== 0) return;
      drag = {
        pointer: event.pointerId,
        x: event.clientX,
        y: event.clientY,
        move: startDrag(),
        moved: false
      };
      handle.setPointerCapture(event.pointerId);
      this.cancelLeave();
    }, { signal });
    handle.addEventListener("pointermove", (event) => {
      if (!drag || event.pointerId !== drag.pointer) return;
      const dx = event.clientX - drag.x;
      const dy = event.clientY - drag.y;
      drag.moved || (drag.moved = Math.abs(dx) + Math.abs(dy) > 3);
      if (drag.moved) drag.move(dx, dy);
    }, { signal });
    const finish = (event) => {
      if (!drag || event.pointerId !== drag.pointer) return;
      if (drag.moved) this.save();
      drag = null;
    };
    handle.addEventListener("pointerup", finish, { signal });
    handle.addEventListener("pointercancel", finish, { signal });
    handle.addEventListener("lostpointercapture", finish, { signal });
  }
};

// src/title-index.ts
function isBackupPath(path) {
  const folders = path.split("/").slice(0, -1);
  return folders.some((folder) => /(?:^|[._ -])(?:backups?|备份)(?:$|[._ -])/i.test(folder));
}
var TitleIndex = class {
  constructor() {
    this.byPath = /* @__PURE__ */ new Map();
  }
  entries() {
    return this.byPath.values();
  }
  set(path, mtime, properties) {
    if (isBackupPath(path)) return this.byPath.delete(path);
    const title = typeof properties?.title === "string" ? properties.title.trim() : "";
    if (!title) return this.byPath.delete(path);
    const raw = properties?.aliases;
    const aliases = /* @__PURE__ */ new Map();
    for (const item of Array.isArray(raw) ? raw : [raw]) {
      if (typeof item !== "string" || !item.trim()) continue;
      const alias = item.trim();
      if (!aliases.has(alias.toLowerCase())) aliases.set(alias.toLowerCase(), alias);
    }
    const old = this.byPath.get(path);
    if (old?.title === title && old.mtime === mtime && old.aliases.size === aliases.size && [...aliases].every(([key, val]) => old.aliases.get(key) === val)) return false;
    this.byPath.set(path, { path, title, foldedTitle: title.toLowerCase(), aliases, mtime });
    return true;
  }
  updateTime(path, mtime) {
    const entry = this.byPath.get(path);
    if (!entry || entry.mtime === mtime) return false;
    entry.mtime = mtime;
    return true;
  }
  move(oldPath, path, mtime) {
    const cached = this.byPath.get(oldPath);
    if (!cached || oldPath === path) return false;
    this.byPath.delete(oldPath);
    if (!isBackupPath(path)) this.byPath.set(path, { ...cached, path, mtime });
    return true;
  }
  remove(path, folder = false) {
    if (!folder) return this.byPath.delete(path);
    const prefix = path + "/";
    let changed = false;
    for (const key of this.byPath.keys()) {
      if (key.startsWith(prefix)) changed = this.byPath.delete(key) || changed;
    }
    return changed;
  }
};

// src/main.ts
var FloatingTitleSearch = class extends import_obsidian2.Plugin {
  constructor() {
    super(...arguments);
    this.index = new TitleIndex();
    this.panel = null;
    this.state = readSettings(null);
    this.saving = Promise.resolve();
    this.disposed = false;
    this.focusWhenReady = false;
  }
  async onload() {
    this.state = readSettings(await this.loadData());
    this.addCommand({
      id: "open-title-search",
      name: "\u6253\u5F00\u6807\u9898\u641C\u7D22",
      hotkeys: [{ modifiers: ["Mod", "Shift"], key: "K" }],
      callback: () => {
        if (this.panel) this.panel.show(true);
        else this.focusWhenReady = true;
      }
    });
    this.app.workspace.onLayoutReady(() => {
      if (!this.disposed) this.mount();
    });
  }
  onunload() {
    this.disposed = true;
    this.panel?.destroy();
    this.panel = null;
  }
  mount() {
    const { metadataCache, vault } = this.app;
    for (const file of vault.getMarkdownFiles()) this.update(file);
    this.panel = new FloatingSearch(
      window,
      this.state,
      () => this.index.entries(),
      (path) => this.openFile(path),
      () => this.persist()
    );
    this.registerEvent(metadataCache.on("changed", (file, _, cache) => {
      if (this.isMarkdown(file) && this.index.set(file.path, file.stat.mtime, cache.frontmatter)) this.panel?.refresh();
    }));
    this.registerEvent(vault.on("create", (file) => {
      if (this.update(file)) this.panel?.refresh();
    }));
    this.registerEvent(vault.on("modify", (file) => {
      if (this.isMarkdown(file) && this.index.updateTime(file.path, file.stat.mtime)) this.panel?.refresh();
    }));
    this.registerEvent(vault.on("rename", (file, oldPath) => {
      if (this.rename(file, oldPath)) this.panel?.refresh();
    }));
    this.registerEvent(vault.on("delete", (file) => {
      if (this.index.remove(file.path, file instanceof import_obsidian2.TFolder)) this.panel?.refresh();
    }));
    if (this.focusWhenReady) this.panel.show(true);
  }
  isMarkdown(file) {
    return file instanceof import_obsidian2.TFile && file.extension.toLowerCase() === "md";
  }
  update(file) {
    if (!this.isMarkdown(file)) return false;
    const cache = this.app.metadataCache.getFileCache(file);
    return cache ? this.index.set(file.path, file.stat.mtime, cache.frontmatter) : false;
  }
  rename(file, oldPath) {
    if (file instanceof import_obsidian2.TFolder) {
      let changed = false;
      for (const child of file.children) {
        changed = this.rename(child, oldPath + child.path.slice(file.path.length)) || changed;
      }
      return changed;
    }
    if (!this.isMarkdown(file)) return this.index.remove(oldPath);
    const moved = this.index.move(oldPath, file.path, file.stat.mtime);
    return this.update(file) || moved;
  }
  async openFile(path) {
    const file = this.app.vault.getFileByPath(path);
    if (!file || !this.isMarkdown(file)) throw new Error("Invalid Markdown note");
    const workspace = this.app.workspace;
    const current = workspace.getMostRecentLeaf();
    const leaf = current?.view.getViewType() === "markdown" ? current : workspace.getLeaf("tab");
    await leaf.openFile(file);
  }
  persist() {
    const state = { ...this.state };
    this.saving = this.saving.then(() => this.saveData(state)).catch((error) => {
      console.error("Floating Title Search could not save preferences", error);
    });
  }
};
