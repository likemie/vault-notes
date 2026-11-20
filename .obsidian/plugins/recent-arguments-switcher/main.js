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
  default: () => RecentArgumentsSwitcher
});
module.exports = __toCommonJS(main_exports);
var import_obsidian3 = require("obsidian");

// src/linked-notes.ts
var import_obsidian = require("obsidian");

// src/recent-store.ts
var LIMIT = 100;
var DAY = 864e5;
var DAY_SNAPSHOT_LIMIT = 512;
var PATH_ORDER = new Intl.Collator("zh-CN", { numeric: true });
function dayKey(value) {
  const date = new Date(value);
  return [
    date.getFullYear(),
    String(date.getMonth() + 1).padStart(2, "0"),
    String(date.getDate()).padStart(2, "0")
  ].join("-");
}
function creationDay(value) {
  if (value instanceof Date && Number.isFinite(value.getTime())) value = value.toISOString();
  if (typeof value !== "string") return null;
  const match = /^(\d{4}-\d{2}-\d{2})(?:[T ]\d{2}:\d{2}.*)?$/.exec(value.trim());
  if (!match) return null;
  const day = match[1];
  const at = Date.parse(day + "T00:00:00Z");
  return Number.isFinite(at) && new Date(at).toISOString().slice(0, 10) === day ? day : null;
}
function noteDay(note) {
  return note.created ?? (note.firstSeen ? dayKey(note.firstSeen) : null);
}
function displayDate(note, now) {
  const day = noteDay(note);
  if (!day) return "\u65E5\u671F\u672A\u77E5";
  const elapsed = Math.round((Date.parse(dayKey(now)) - Date.parse(day)) / DAY);
  const label = elapsed === 0 ? "\u4ECA\u5929" : elapsed === 1 ? "\u6628\u5929" : elapsed > 1 && elapsed < 7 ? elapsed + " \u5929\u524D" : day.slice(day.startsWith(dayKey(now).slice(0, 4)) ? 5 : 0);
  return note.created ? label : label + "\u53D1\u73B0";
}
function dateDescription(note) {
  if (note.created) return "\u521B\u5EFA\u65E5\u671F " + note.created;
  if (note.firstSeen) return "\u9996\u6B21\u53D1\u73B0\u4E8E " + dayKey(note.firstSeen) + "\uFF0C\u521B\u5EFA\u65E5\u671F\u672A\u77E5";
  return "\u521B\u5EFA\u65E5\u671F\u672A\u77E5";
}
function compareCreationDays(a, b) {
  if (a === b) return 0;
  return (a ?? "") > (b ?? "") ? -1 : 1;
}
var RecentStore = class {
  constructor(previous) {
    this.previous = previous;
    this.notes = /* @__PURE__ */ new Map();
    this.removed = /* @__PURE__ */ new Map();
    this.pendingStartup = /* @__PURE__ */ new Set();
    this.previousDayPaths = previous?.dayPaths ? new Set(previous.dayPaths) : null;
  }
  seed(notes, now) {
    const persisted = new Map(this.previous?.recent.map((entry) => [entry.path, entry]));
    for (const { note, hasMetadata } of notes) {
      const prior = persisted.get(note.path);
      const unread = prior?.unread ?? this.addedWhileAway(note, now);
      this.notes.set(note.path, { ...note, firstSeen: prior?.firstSeen ?? 0, unread, awaitingDate: false });
      if (!prior && !hasMetadata && this.previous) this.pendingStartup.add(note.path);
    }
  }
  upsert(note, at, hasMetadata) {
    this.pruneRemoved(at);
    const restored = this.removed.get(note.path);
    this.removed.delete(note.path);
    const current = this.notes.get(note.path);
    const prior = current ?? restored?.note;
    const firstSeen = prior?.firstSeen ?? at;
    const awaitingDate = !note.created && (prior?.awaitingDate ?? true);
    let unread = prior?.unread ?? (!note.created || note.created === dayKey(at));
    if (hasMetadata && this.pendingStartup.delete(note.path)) unread = this.addedWhileAway(note, at);
    if (prior?.awaitingDate && note.created && note.created < dayKey(firstSeen)) unread = false;
    if (current && current.title === note.title && current.created === note.created && current.unread === unread && current.awaitingDate === awaitingDate) return false;
    this.notes.set(note.path, { ...note, firstSeen, unread, awaitingDate });
    return true;
  }
  rename(oldPath, note, at, hasMetadata) {
    this.pruneRemoved(at);
    const prior = this.notes.get(oldPath) ?? this.removed.get(oldPath)?.note;
    this.notes.delete(oldPath);
    this.removed.delete(oldPath);
    if (this.pendingStartup.delete(oldPath)) this.pendingStartup.add(note.path);
    if (prior) {
      this.notes.set(note.path, { ...prior, path: note.path });
      if (!hasMetadata) return true;
    }
    return this.upsert(note, at, hasMetadata) || oldPath !== note.path;
  }
  remove(path, at) {
    this.pendingStartup.delete(path);
    const note = this.notes.get(path);
    if (!note) return false;
    this.pruneRemoved(at);
    this.removed.set(path, { note, at });
    this.notes.delete(path);
    return true;
  }
  removeFolder(path, at) {
    let changed = false;
    for (const file of this.notes.keys()) {
      if (file.startsWith(path + "/")) changed = this.remove(file, at) || changed;
    }
    return changed;
  }
  read(path) {
    const note = this.notes.get(path);
    if (!note) return false;
    this.pendingStartup.delete(path);
    if (!note.unread) return false;
    note.unread = false;
    return true;
  }
  snapshot(now) {
    const day = dayKey(now);
    const todayPaths = [];
    const sorted = Array.from(this.notes.values(), (note) => ({ note, day: noteDay(note) }));
    for (const { note } of sorted) {
      if (note.created === day) todayPaths.push(note.path);
    }
    sorted.sort((a, b) => {
      return compareCreationDays(a.day, b.day) || b.note.firstSeen - a.note.firstSeen || PATH_ORDER.compare(a.note.path, b.note.path);
    });
    const rows = sorted.slice(0, LIMIT).map(({ note }) => note);
    const checkpoint = {
      at: now,
      day,
      dayPaths: todayPaths.length <= DAY_SNAPSHOT_LIMIT ? todayPaths : null,
      recent: rows.map(({ path, firstSeen, unread }) => ({ path, firstSeen, unread }))
    };
    return {
      rows,
      unread: rows.filter((row) => row.unread).length,
      today: todayPaths.length,
      checkpoint
    };
  }
  addedWhileAway(note, now) {
    const previous = this.previous;
    if (!previous || !note.created || note.created > dayKey(now)) return false;
    return note.created > previous.day || note.created === previous.day && this.previousDayPaths !== null && !this.previousDayPaths.has(note.path);
  }
  pruneRemoved(now) {
    for (const [path, entry] of this.removed) {
      if (now - entry.at <= 2e3) break;
      this.removed.delete(path);
    }
  }
};

// src/linked-notes.ts
var PATH_ORDER2 = new Intl.Collator("zh-CN", { numeric: true });
function noteTitle(file, cache) {
  const fields = cache?.frontmatter;
  for (const value of [fields?.argument_display_title, fields?.title]) {
    if (typeof value === "string" && value.trim()) return value.trim();
  }
  return file.basename;
}
function linkedNotes(file, metadata) {
  const source = metadata.getFileCache(file);
  if (!source) return [];
  const linkpaths = /* @__PURE__ */ new Set();
  const destinations = /* @__PURE__ */ new Map();
  for (const reference of [...source.links ?? [], ...source.embeds ?? []]) {
    const { path } = (0, import_obsidian.parseLinktext)(reference.link);
    if (!path || /^(?:[a-z][a-z\d+.-]*:|\/\/)/i.test(path) || linkpaths.has(path)) continue;
    linkpaths.add(path);
    const target = metadata.getFirstLinkpathDest(path, file.path);
    if (!target || target.path === file.path || target.extension.toLowerCase() !== "md" || destinations.has(target.path)) continue;
    const cache = metadata.getFileCache(target);
    const fields = cache?.frontmatter;
    const isSource = target.path.startsWith("sources/") || target.path.startsWith("books/");
    const created = creationDay(fields?.created) ?? (isSource ? creationDay(fields?.processed_date) : null);
    destinations.set(target.path, { path: target.path, title: noteTitle(target, cache), created });
  }
  return [...destinations.values()].sort((a, b) => compareCreationDays(a.created, b.created) || PATH_ORDER2.compare(a.path, b.path));
}

// src/settings.ts
var ARGUMENT_ROOT = "wiki/arguments/";
var BATCH_MS = 200;
function readSaved(value) {
  const panel = value?.panel;
  const docked = panel?.dock === "right";
  const old = value?.checkpoint;
  const checkpoint = old && Number.isFinite(old.at) && typeof old.day === "string" && Array.isArray(old.recent) ? {
    at: old.at,
    day: old.day,
    dayPaths: Array.isArray(old.dayPaths) ? old.dayPaths.filter((path) => typeof path === "string").slice(0, 512) : null,
    recent: old.recent.filter((row) => row && typeof row.path === "string" && Number.isFinite(row.firstSeen) && typeof row.unread === "boolean").slice(0, 100)
  } : null;
  return {
    panel: {
      dock: "right",
      centerY: docked && typeof panel.centerY === "number" && Number.isFinite(panel.centerY) ? panel.centerY : null
    },
    checkpoint
  };
}

// src/panel.ts
var import_obsidian2 = require("obsidian");
var MARGIN = 8;
var ROW_HEIGHT = 26;
var LEAVE_DELAY = 150;
function clampTop(top, height, viewport) {
  return Math.min(Math.max(MARGIN, top), Math.max(MARGIN, viewport - height - MARGIN));
}
function append(parent, tag, className, text) {
  const node = parent.ownerDocument.createElement(tag);
  if (className) node.className = className;
  if (text !== void 0) node.textContent = text;
  parent.append(node);
  return node;
}
function button(parent, className, label) {
  const control = append(parent, "button", className);
  control.type = "button";
  control.setAttribute("aria-label", label);
  return control;
}
var HoverDock = class {
  constructor(window2, state, save) {
    this.window = window2;
    this.state = state;
    this.save = save;
    this.events = new AbortController();
    this.panels = [];
    this.active = null;
    this.root = append(window2.document.body, "aside", "ras-dock");
    this.root.setAttribute("aria-label", "\u7B14\u8BB0\u5207\u6362\u5DE5\u5177");
    window2.addEventListener("resize", () => this.place(), { signal: this.events.signal });
  }
  add(options, open) {
    const panel = new HoverPanel(this.window, this.root, options, open, () => {
      if (this.active !== panel) this.active?.collapse();
      this.active = panel;
    }, (center) => this.place(center), () => {
      this.state.centerY = this.center();
      this.save();
    });
    this.panels.push(panel);
    this.place();
    return panel;
  }
  destroy() {
    this.events.abort();
    for (const panel of this.panels) panel.destroy();
    this.root.remove();
  }
  anchorOffset() {
    const lastRail = this.root.lastElementChild;
    return this.root.offsetHeight - lastRail.offsetHeight / 2;
  }
  center() {
    return this.root.getBoundingClientRect().top + this.anchorOffset();
  }
  place(center = this.state.centerY) {
    if (!this.panels.length) return;
    const viewport = this.window.innerHeight;
    const top = clampTop((center ?? viewport * 0.68) - this.anchorOffset(), this.root.offsetHeight, viewport);
    this.root.style.top = top + "px";
    for (const panel of this.panels) panel.placeBody();
  }
};
var HoverPanel = class {
  constructor(window2, parent, options, open, onExpand, onMove, onMoveEnd) {
    this.window = window2;
    this.parent = parent;
    this.options = options;
    this.open = open;
    this.onExpand = onExpand;
    this.onMove = onMove;
    this.onMoveEnd = onMoveEnd;
    this.events = new AbortController();
    this.rowButtons = [];
    this.data = null;
    this.shown = LIMIT;
    this.expanded = false;
    this.closeTimer = null;
    this.drag = null;
    this.root = append(parent, "section", "ras-float");
    this.root.dataset.kind = options.id;
    this.root.setAttribute("aria-label", options.title);
    this.rail = button(this.root, "ras-rail", "\u5C55\u5F00" + options.title);
    this.rail.setAttribute("aria-controls", "ras-expanded-" + options.id);
    const railIcon = append(this.rail, "span", "ras-rail-icon");
    railIcon.setAttribute("aria-hidden", "true");
    if (options.id === "links") (0, import_obsidian2.setIcon)(railIcon, "link-2");
    else for (let i = 0; i < 3; i++) append(railIcon, "span");
    append(this.rail, "span", "ras-rail-label", options.label);
    this.railCount = append(this.rail, "span", "ras-rail-count", "0");
    this.body = append(this.root, "section", "ras-body");
    this.body.id = "ras-expanded-" + options.id;
    const header = append(this.body, "header", "ras-header");
    const handle = append(header, "div", "ras-handle");
    (0, import_obsidian2.setIcon)(append(handle, "span", "ras-grip"), "grip-horizontal");
    const title = append(handle, "h2", "ras-heading", options.title);
    title.id = "ras-heading-" + options.id;
    this.body.setAttribute("aria-labelledby", title.id);
    handle.title = "\u6CBF\u53F3\u8FB9\u79FB\u52A8\u4E24\u4E2A\u5165\u53E3";
    this.count = append(handle, "span", "ras-today");
    this.list = append(this.body, "ul", "ras-items");
    this.list.setAttribute("aria-label", options.listLabel);
    this.status = append(this.body, "p", "ras-status");
    this.status.setAttribute("role", "status");
    this.status.hidden = true;
    const signal = this.events.signal;
    this.rail.addEventListener("click", () => this.toggle(true), { signal });
    this.rail.addEventListener("pointerenter", (event) => {
      if (event.pointerType !== "mouse") return;
      this.cancelClose();
      this.setExpanded(true);
    }, { signal });
    this.root.addEventListener("pointerenter", (event) => {
      if (event.pointerType === "mouse") this.cancelClose();
    }, { signal });
    this.root.addEventListener("pointerleave", (event) => {
      if (event.pointerType !== "mouse" || !this.expanded) return;
      this.cancelClose();
      this.closeTimer = this.window.setTimeout(() => {
        this.closeTimer = null;
        this.setExpanded(false);
      }, LEAVE_DELAY);
    }, { signal });
    this.list.addEventListener("click", (event) => {
      void this.openRow(event);
    }, { signal });
    this.root.addEventListener("keydown", (event) => this.onKey(event), { signal });
    this.bindDrag(handle, signal);
    this.setExpanded(false);
  }
  render(data) {
    const samePage = this.data?.context === data.context;
    if (!samePage) {
      this.shown = LIMIT;
      this.status.hidden = true;
      if (!this.expanded) {
        this.list.replaceChildren();
        this.rowButtons = [];
      }
    }
    this.data = data;
    this.count.textContent = data.count;
    this.count.title = data.countDescription ?? "";
    this.railCount.textContent = data.badge > 999 ? Math.floor(data.badge / 1e3) + "k+" : String(data.badge);
    this.updateRail();
    if (this.expanded) this.renderRows(samePage);
  }
  renderRows(preservePosition, focusMore = false) {
    const data = this.data;
    if (!data) return;
    const activeElement = this.window.document.activeElement;
    const focusedRowBefore = this.rowButtons.find((control) => control === activeElement);
    const focused = preservePosition ? focusedRowBefore?.dataset.path : null;
    const oldScroll = preservePosition ? this.list.scrollTop : 0;
    const firstPath = this.rowButtons[Math.floor(oldScroll / ROW_HEIGHT)]?.dataset.path;
    const fragment = this.window.document.createDocumentFragment();
    this.rowButtons = [];
    if (!data.rows.length) {
      const empty = this.window.document.createElement("li");
      empty.className = "ras-empty";
      empty.textContent = data.empty;
      fragment.append(empty);
    }
    for (const note of data.rows.slice(0, this.shown)) {
      const item = this.window.document.createElement("li");
      const date = displayDate(note, data.now);
      const control = button(item, "ras-row", note.title + "\uFF0C" + date + (note.unread ? "\uFF0C\u672A\u8BFB" : ""));
      control.dataset.path = note.path;
      if (note.unread) control.dataset.unread = "true";
      control.tabIndex = -1;
      if (note.path === data.active) control.setAttribute("aria-current", "page");
      control.title = note.title + "\n" + dateDescription(note);
      if (this.options.id === "arguments") append(control, "span", "ras-dot").setAttribute("aria-hidden", "true");
      append(control, "span", "ras-title", note.title);
      append(control, "span", "ras-date", date);
      this.rowButtons.push(control);
      fragment.append(item);
    }
    if (data.rows.length > this.shown) {
      const item = this.window.document.createElement("li");
      button(item, "ras-more", "\u663E\u793A\u66F4\u591A\u94FE\u63A5").textContent = "\u663E\u793A\u66F4\u591A\u94FE\u63A5";
      fragment.append(item);
    }
    this.list.replaceChildren(fragment);
    const focusedRow = focusMore ? this.rowButtons[this.shown - LIMIT] : this.rowButtons.find((control) => control.dataset.path === focused);
    const tabbable = focusedRow ?? this.rowButtons.find((control) => control.dataset.path === data.active) ?? this.rowButtons[0];
    if (tabbable) tabbable.tabIndex = 0;
    if (oldScroll && firstPath) {
      const anchor = this.rowButtons.findIndex((control) => control.dataset.path === firstPath);
      this.list.scrollTop = anchor < 0 ? oldScroll : anchor * ROW_HEIGHT + oldScroll % ROW_HEIGHT;
    }
    if (!preservePosition) this.list.scrollTop = 0;
    if (focusMore) focusedRow?.focus();
    else if (focusedRowBefore) (tabbable ?? this.rail).focus({ preventScroll: true });
    this.placeBody();
  }
  async openRow(event) {
    const target = event.target;
    if (target.closest(".ras-more")) {
      this.shown += LIMIT;
      this.renderRows(true, true);
      return;
    }
    const control = target.closest(".ras-row");
    const path = control?.dataset.path;
    if (!control || !path) return;
    this.setTabStop(control);
    this.status.hidden = true;
    try {
      await this.open(path);
    } catch {
      this.status.textContent = "\u6587\u4EF6\u53EF\u80FD\u5DF2\u79FB\u52A8\uFF0C\u7A0D\u5019\u518D\u8BD5\u3002";
      this.status.hidden = false;
      this.placeBody();
    }
  }
  toggle(focus) {
    this.cancelClose();
    this.setExpanded(!this.expanded);
    if (focus) {
      const target = this.expanded ? this.rowButtons.find((control) => control.tabIndex === 0) ?? this.rail : this.rail;
      target.focus({ preventScroll: true });
    }
  }
  destroy() {
    this.cancelClose();
    this.events.abort();
    this.root.remove();
  }
  collapse() {
    this.cancelClose();
    this.setExpanded(false);
  }
  cancelClose() {
    if (this.closeTimer === null) return;
    this.window.clearTimeout(this.closeTimer);
    this.closeTimer = null;
  }
  setExpanded(expanded) {
    if (expanded === this.expanded && this.root.dataset.open !== void 0) return;
    if (expanded && !this.expanded) this.onExpand();
    const restoreFocus = !expanded && this.body.contains(this.window.document.activeElement);
    this.expanded = expanded;
    this.body.hidden = !expanded;
    this.root.dataset.open = String(expanded);
    this.updateRail();
    if (expanded) this.renderRows(true);
    if (restoreFocus) this.rail.focus({ preventScroll: true });
  }
  updateRail() {
    const action = (this.expanded ? "\u6536\u8D77" : "\u5C55\u5F00") + this.options.title;
    const description = (this.data?.badge ?? 0) + " " + this.options.badgeUnit;
    this.rail.setAttribute("aria-expanded", String(this.expanded));
    this.rail.setAttribute("aria-label", action + "\uFF0C" + description);
    this.rail.title = action + " \xB7 " + description;
  }
  placeBody() {
    if (!this.expanded) return;
    const rail = this.root.getBoundingClientRect();
    const bodyHeight = this.body.offsetHeight;
    const top = clampTop(rail.top + (rail.height - bodyHeight) / 2, bodyHeight, this.window.innerHeight);
    this.body.style.top = top - rail.top + "px";
  }
  bindDrag(handle, signal) {
    handle.addEventListener("pointerdown", (event) => {
      if (event.button !== 0 || this.drag) return;
      const center = this.parent.getBoundingClientRect().bottom - this.rail.offsetHeight / 2;
      this.drag = { pointer: event.pointerId, startY: event.clientY - center, center, moved: false };
      handle.setPointerCapture(event.pointerId);
    }, { signal });
    handle.addEventListener("pointermove", (event) => {
      var _a;
      if (!this.drag || event.pointerId !== this.drag.pointer) return;
      const center = event.clientY - this.drag.startY;
      (_a = this.drag).moved || (_a.moved = Math.abs(center - this.drag.center) >= 4);
      if (this.drag.moved) this.drag.center = center;
      if (this.drag.moved) this.onMove(center);
    }, { signal });
    const end = (event) => {
      if (!this.drag || event.pointerId !== this.drag.pointer) return;
      const moved = this.drag.moved;
      this.drag = null;
      if (moved) this.onMoveEnd();
    };
    handle.addEventListener("pointerup", end, { signal });
    handle.addEventListener("pointercancel", end, { signal });
    handle.addEventListener("lostpointercapture", end, { signal });
  }
  setTabStop(selected) {
    for (const control of this.rowButtons) control.tabIndex = control === selected ? 0 : -1;
  }
  onKey(event) {
    if (event.key === "Escape" && this.expanded) {
      event.preventDefault();
      event.stopPropagation();
      this.toggle(true);
      return;
    }
    if (!this.expanded || !this.rowButtons.length || event.key !== "ArrowDown" && event.key !== "ArrowUp") return;
    event.preventDefault();
    event.stopPropagation();
    const current = this.rowButtons.indexOf(event.target);
    const index = current < 0 ? 0 : Math.max(0, Math.min(this.rowButtons.length - 1, current + (event.key === "ArrowDown" ? 1 : -1)));
    const next = this.rowButtons[index];
    this.setTabStop(next);
    next.focus();
  }
};

// src/main.ts
var RecentArgumentsSwitcher = class extends import_obsidian3.Plugin {
  constructor() {
    super(...arguments);
    this.model = null;
    this.dock = null;
    this.panel = null;
    this.links = null;
    this.currentLinkPaths = /* @__PURE__ */ new Set();
    this.currentLinkPage = null;
    this.state = readSaved(null);
    this.refreshTimer = null;
    this.linksTimer = null;
    this.midnightTimer = null;
    this.writes = Promise.resolve();
    this.disposed = false;
  }
  async onload() {
    this.state = readSaved(await this.loadData());
    this.addCommand({
      id: "toggle-recent-arguments",
      name: "\u5C55\u5F00\u6216\u6536\u8D77\u6700\u8FD1\u8BBA\u8BC1",
      callback: () => this.panel?.toggle(true)
    });
    this.addCommand({
      id: "toggle-current-note-links",
      name: "\u5C55\u5F00\u6216\u6536\u8D77\u672C\u9875\u94FE\u63A5",
      callback: () => this.links?.toggle(true)
    });
    this.app.workspace.onLayoutReady(() => {
      if (!this.disposed) this.mount();
    });
  }
  onunload() {
    this.disposed = true;
    if (this.refreshTimer !== null) window.clearTimeout(this.refreshTimer);
    if (this.linksTimer !== null) window.clearTimeout(this.linksTimer);
    if (this.midnightTimer !== null) window.clearTimeout(this.midnightTimer);
    if (this.model) this.persist(this.model.snapshot(Date.now()).checkpoint);
    this.dock?.destroy();
    this.dock = null;
    this.panel = null;
    this.links = null;
    this.model = null;
  }
  mount() {
    const { vault, workspace, metadataCache } = this.app;
    const model = this.model = new RecentStore(this.state.checkpoint);
    const notes = vault.getMarkdownFiles().flatMap((file) => {
      const candidate = this.note(file);
      return candidate ? [candidate] : [];
    });
    model.seed(notes, Date.now());
    const active = workspace.getActiveFile();
    if (active) model.read(active.path);
    this.dock = new HoverDock(window, this.state.panel, () => this.schedule());
    this.links = this.dock.add({
      id: "links",
      label: "\u94FE\u63A5",
      title: "\u672C\u9875\u94FE\u63A5",
      listLabel: "\u5F53\u524D\u7B14\u8BB0\u94FE\u63A5\u7684\u6761\u76EE",
      badgeUnit: "\u6761\u94FE\u63A5"
    }, (path) => this.open(path));
    this.panel = this.dock.add({
      id: "arguments",
      label: "\u8BBA\u8BC1",
      title: "\u6700\u65B0\u8BBA\u8BC1",
      listLabel: "\u6700\u8FD1 100 \u6761\u8BBA\u8BC1",
      badgeUnit: "\u6761\u672A\u8BFB"
    }, (path) => this.open(path, true));
    this.registerEvent(vault.on("create", (file) => {
      this.update(file);
      if (file instanceof import_obsidian3.TFile && file.extension === "md") this.scheduleLinks();
    }));
    this.registerEvent(vault.on("modify", (file) => this.update(file)));
    this.registerEvent(vault.on("delete", (file) => {
      const now = Date.now();
      const changed = file instanceof import_obsidian3.TFolder ? model.removeFolder(file.path, now) : model.remove(file.path, now);
      if (changed) this.schedule();
      this.scheduleLinks();
    }));
    this.registerEvent(vault.on("rename", (file, oldPath) => {
      this.rename(file, oldPath);
      this.scheduleLinks();
    }));
    this.registerEvent(metadataCache.on("changed", (file) => {
      this.update(file);
      if (file.path === this.currentLinkPage || this.currentLinkPaths.has(file.path)) this.scheduleLinks();
    }));
    this.registerEvent(metadataCache.on("resolve", (file) => {
      if (file.path === this.currentLinkPage) this.scheduleLinks();
    }));
    this.registerEvent(workspace.on("file-open", (file) => {
      if (file) model.read(file.path);
      this.schedule();
      this.scheduleLinks();
    }));
    this.registerEvent(workspace.on("active-leaf-change", () => this.scheduleLinks()));
    this.flush();
    this.refreshLinks();
    this.untilMidnight();
  }
  note(file) {
    if (!(file instanceof import_obsidian3.TFile) || file.extension.toLowerCase() !== "md" || !file.path.startsWith(ARGUMENT_ROOT) || file.basename === "index") return null;
    const cache = this.app.metadataCache.getFileCache(file);
    const fields = cache?.frontmatter;
    if (typeof fields?.type === "string" && fields.type.trim().toLowerCase() !== "argument") return null;
    return {
      note: { path: file.path, title: noteTitle(file, cache), created: creationDay(fields?.created) },
      hasMetadata: Boolean(cache)
    };
  }
  update(file) {
    if (!this.model || !(file instanceof import_obsidian3.TFile) || !file.path.startsWith(ARGUMENT_ROOT)) return;
    const candidate = this.note(file);
    const now = Date.now();
    const changed = candidate ? this.model.upsert(candidate.note, now, candidate.hasMetadata) : this.model.remove(file.path, now);
    if (changed) this.schedule();
  }
  rename(file, oldPath) {
    const model = this.model;
    if (!model) return;
    if (file instanceof import_obsidian3.TFolder) {
      if (!file.path.startsWith(ARGUMENT_ROOT) && !oldPath.startsWith(ARGUMENT_ROOT) && !ARGUMENT_ROOT.startsWith(file.path + "/") && !ARGUMENT_ROOT.startsWith(oldPath + "/")) return;
      for (const child of file.children) this.rename(child, oldPath + child.path.slice(file.path.length));
      return;
    }
    if (!oldPath.startsWith(ARGUMENT_ROOT) && !file.path.startsWith(ARGUMENT_ROOT)) return;
    const now = Date.now();
    const candidate = this.note(file);
    const changed = candidate ? model.rename(oldPath, candidate.note, now, candidate.hasMetadata) : model.remove(oldPath, now);
    if (changed) this.schedule();
  }
  async open(path, argumentOnly = false) {
    const file = this.app.vault.getFileByPath(path);
    if (!file || file.extension.toLowerCase() !== "md" || argumentOnly && !this.note(file)) {
      throw new Error("The note is no longer available");
    }
    const { workspace } = this.app;
    const current = workspace.getMostRecentLeaf();
    const leaf = current?.view.getViewType() === "markdown" ? current : workspace.getLeaf("tab");
    await leaf.openFile(file);
    if (this.model?.read(file.path)) this.schedule();
  }
  schedule() {
    if (this.disposed || this.refreshTimer !== null) return;
    this.refreshTimer = window.setTimeout(() => {
      this.refreshTimer = null;
      this.flush();
    }, BATCH_MS);
  }
  flush() {
    if (!this.model || !this.panel) return;
    const now = Date.now();
    const active = this.app.workspace.getActiveFile()?.path ?? null;
    const { checkpoint, rows, unread, today } = this.model.snapshot(now);
    this.panel.render({
      rows,
      badge: unread,
      count: "\u4ECA\u65E5 " + today,
      countDescription: "\u4ECA\u5929\u521B\u5EFA " + today + " \u6761\u8BBA\u8BC1",
      empty: "\u6682\u65E0\u8BBA\u8BC1",
      active,
      now
    });
    this.persist(checkpoint);
  }
  scheduleLinks() {
    if (this.disposed || this.linksTimer !== null) return;
    this.linksTimer = window.setTimeout(() => {
      this.linksTimer = null;
      this.refreshLinks();
    }, BATCH_MS);
  }
  refreshLinks() {
    if (!this.links) return;
    const { workspace, metadataCache } = this.app;
    const file = workspace.getActiveViewOfType(import_obsidian3.MarkdownView)?.file ?? null;
    const rows = file ? linkedNotes(file, metadataCache) : [];
    this.currentLinkPage = file?.path ?? null;
    this.currentLinkPaths = new Set(rows.map((note) => note.path));
    this.links.render({
      rows,
      badge: rows.length,
      count: rows.length + " \u6761",
      active: null,
      context: this.currentLinkPage,
      empty: file ? "\u672C\u9875\u6CA1\u6709\u53EF\u6253\u5F00\u7684\u7B14\u8BB0\u94FE\u63A5" : "\u6253\u5F00\u4E00\u7BC7\u7B14\u8BB0\u5373\u53EF\u67E5\u770B\u94FE\u63A5",
      now: Date.now()
    });
  }
  persist(checkpoint) {
    const snapshot = { panel: { ...this.state.panel }, checkpoint };
    this.writes = this.writes.then(() => this.saveData(snapshot)).catch((error) => {
      console.error("Recent Arguments Switcher could not save its state", error);
    });
  }
  untilMidnight() {
    const midnight = /* @__PURE__ */ new Date();
    midnight.setHours(24, 0, 0, 100);
    this.midnightTimer = window.setTimeout(() => {
      this.schedule();
      this.scheduleLinks();
      this.untilMidnight();
    }, midnight.getTime() - Date.now());
  }
};
