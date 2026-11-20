import { setIcon } from "obsidian";
import { clamp, type SearchState } from "./settings";
import { RESULT_LIMIT, searchTitles, titleRange, type TitleMatch } from "./search";
import type { TitleEntry } from "./title-index";

const MARGIN = 8;
const LEAVE_DELAY = 150;
const TYPE_DELAY = 50;

function el<K extends keyof HTMLElementTagNameMap>(
  parent: HTMLElement, tag: K, className = "", label = "",
): HTMLElementTagNameMap[K] {
  const node = parent.ownerDocument.createElement(tag);
  if (className) node.className = className;
  if (label) node.textContent = label;
  parent.append(node);
  return node;
}

function button(parent: HTMLElement, className: string, label: string): HTMLButtonElement {
  const node = el(parent, "button", className);
  node.type = "button";
  node.setAttribute("aria-label", label);
  node.title = label;
  return node;
}

export class FloatingSearch {
  private readonly root: HTMLElement;
  private readonly rail: HTMLButtonElement;
  private readonly body: HTMLElement;
  private readonly input: HTMLInputElement;
  private readonly list: HTMLElement;
  private readonly status: HTMLElement;
  private readonly events = new AbortController();
  private expanded = false;
  private pointerInside = false;
  private composing = false;
  private leaving: number | null = null;
  private pending: number | null = null;
  private rows: TitleMatch[] = [];
  private options: HTMLButtonElement[] = [];
  private selected = -1;
  private lastQuery = "";
  private opening = false;

  constructor(
    private readonly host: Window,
    private readonly state: SearchState,
    private readonly entries: () => Iterable<TitleEntry>,
    private readonly openNote: (path: string) => Promise<void>,
    private readonly save: () => void,
  ) {
    this.root = el(host.document.body, "aside", "fts-float");
    this.root.setAttribute("aria-label", "标题搜索");
    this.root.hidden = state.hidden;
    this.rail = button(this.root, "fts-rail", "展开标题搜索");
    this.rail.setAttribute("aria-controls", "fts-panel");
    setIcon(el(this.rail, "span", "fts-rail-icon"), "search");
    el(this.rail, "span", "fts-rail-label", "搜索");

    this.body = el(this.root, "section", "fts-body");
    this.body.id = "fts-panel";
    this.body.hidden = true;
    this.body.setAttribute("aria-labelledby", "fts-heading");
    const header = el(this.body, "header", "fts-header");
    const handle = el(header, "div", "fts-handle");
    handle.title = "沿右侧拖动搜索入口";
    setIcon(el(handle, "span", "fts-grip"), "grip-horizontal");
    el(handle, "h2", "fts-heading", "标题搜索").id = "fts-heading";
    const minimize = button(header, "fts-icon-button", "收起标题搜索");
    setIcon(minimize, "minus");
    const hide = button(header, "fts-icon-button", "隐藏标题搜索");
    setIcon(hide, "x");

    const field = el(this.body, "div", "fts-field");
    this.input = el(field, "input", "fts-input");
    this.input.type = "search";
    this.input.placeholder = "输入标题…";
    this.input.spellcheck = false;
    this.input.autocomplete = "off";
    this.input.setAttribute("aria-label", "搜索标题");
    this.input.setAttribute("role", "combobox");
    this.input.setAttribute("aria-autocomplete", "list");
    this.input.setAttribute("aria-controls", "fts-results");
    this.input.setAttribute("aria-expanded", "false");

    this.status = el(this.body, "p", "fts-status", "输入标题关键词");
    this.status.setAttribute("role", "status");
    this.list = el(this.body, "div", "fts-results");
    this.list.id = "fts-results";
    this.list.setAttribute("role", "listbox");
    this.list.setAttribute("aria-label", "笔记搜索结果");
    this.list.hidden = true;

    const footer = el(this.body, "footer", "fts-footer");
    const label = el(footer, "label", "fts-alias-option");
    const aliases = el(label, "input");
    aliases.type = "checkbox";
    aliases.checked = state.exactAliases;
    el(label, "span", "", "匹配完整别名");
    const resize = el(footer, "span", "fts-resize");
    resize.title = "拖动调整面板宽度和最大高度";

    const signal = this.events.signal;
    this.rail.addEventListener("pointerenter", event => {
      if (event.pointerType === "mouse") this.show(false);
    }, { signal });
    this.rail.addEventListener("click", () => this.show(true), { signal });
    this.root.addEventListener("pointerenter", event => {
      if (event.pointerType !== "mouse") return;
      this.pointerInside = true;
      this.cancelLeave();
    }, { signal });
    this.root.addEventListener("pointerleave", event => {
      if (event.pointerType !== "mouse") return;
      this.pointerInside = false;
      this.deferCollapse();
    }, { signal });
    this.root.addEventListener("focusout", () => this.deferCollapse(), { signal });
    this.root.addEventListener("keydown", event => this.onKey(event), { signal });
    this.input.addEventListener("input", () => { if (!this.composing) this.refresh(); }, { signal });
    this.input.addEventListener("compositionstart", () => {
      this.composing = true;
      this.cancelSearch();
    }, { signal });
    this.input.addEventListener("compositionend", () => {
      this.composing = false;
      this.refresh();
    }, { signal });
    this.list.addEventListener("click", event => {
      const row = (event.target as HTMLElement).closest<HTMLButtonElement>(".fts-row");
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

  show(focus: boolean): void {
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

  refresh(): void {
    if (!this.expanded || this.pending !== null || this.composing) return;
    this.pending = this.host.setTimeout(() => {
      this.pending = null;
      this.render();
    }, TYPE_DELAY);
  }

  destroy(): void {
    this.cancelLeave();
    this.cancelSearch();
    this.events.abort();
    this.root.remove();
  }

  private render(): void {
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
        meta.append("别名 ");
        el(meta, "mark", "", match.alias);
        meta.append(" · ");
      }
      meta.append(match.entry.path);
      this.options.push(row);
    }

    if (!query) this.status.textContent = "输入标题关键词";
    else if (!total) this.status.textContent = "未找到匹配标题";
    else this.status.textContent = total > RESULT_LIMIT ? "显示 " + RESULT_LIMIT + " 项，共 " + total + " 项" : total + " 项结果";
    this.status.classList.toggle("fts-has-results", total > 0);
    if (!sameQuery) this.list.scrollTop = 0;
    if (rows.length) this.select(Math.max(0, rows.findIndex(match => match.entry.path === path)), false);
    else {
      this.selected = -1;
      this.input.removeAttribute("aria-activedescendant");
    }
    this.place();
  }

  private select(index: number, scroll = true): void {
    this.selected = index;
    const active = this.options[index];
    for (const row of this.options) row.setAttribute("aria-selected", String(row === active));
    this.input.setAttribute("aria-activedescendant", active.id);
    if (scroll) active.scrollIntoView({ block: "nearest" });
  }

  private async openAt(index: number): Promise<void> {
    if (this.opening || !this.rows[index]) return;
    this.opening = true;
    try {
      await this.openNote(this.rows[index].entry.path);
      this.collapse(false);
    } catch {
      this.status.textContent = "笔记可能已移动或删除";
      this.refresh();
    } finally {
      this.opening = false;
    }
  }

  private onKey(event: KeyboardEvent): void {
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

  private collapse(focus: boolean): void {
    this.cancelLeave();
    this.cancelSearch();
    this.expanded = false;
    this.body.hidden = true;
    this.root.dataset.open = "false";
    this.rail.setAttribute("aria-expanded", "false");
    if (focus) this.rail.focus({ preventScroll: true });
    this.place();
  }

  private cancelSearch(): void {
    if (this.pending === null) return;
    this.host.clearTimeout(this.pending);
    this.pending = null;
  }

  private cancelLeave(): void {
    if (this.leaving === null) return;
    this.host.clearTimeout(this.leaving);
    this.leaving = null;
  }

  private deferCollapse(): void {
    if (!this.expanded || this.leaving !== null) return;
    this.leaving = this.host.setTimeout(() => {
      this.leaving = null;
      if (!this.pointerInside && !this.body.contains(this.host.document.activeElement)) this.collapse(false);
    }, LEAVE_DELAY);
  }

  private place(): void {
    if (this.root.hidden) return;
    const height = this.rail.offsetHeight;
    const viewport = this.host.innerHeight;
    // Keep the search entrance above the note tools on the right.
    const defaultCenter = Math.min(viewport * .34, viewport * .68 - 148);
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

  private bindDrag(handle: HTMLElement, startDrag: () => (dx: number, dy: number) => void): void {
    let drag: { pointer: number; x: number; y: number; move: (dx: number, dy: number) => void; moved: boolean } | null = null;
    const signal = this.events.signal;
    handle.addEventListener("pointerdown", event => {
      if (event.button !== 0) return;
      drag = { pointer: event.pointerId, x: event.clientX, y: event.clientY,
        move: startDrag(), moved: false };
      handle.setPointerCapture(event.pointerId);
      this.cancelLeave();
    }, { signal });
    handle.addEventListener("pointermove", event => {
      if (!drag || event.pointerId !== drag.pointer) return;
      const dx = event.clientX - drag.x;
      const dy = event.clientY - drag.y;
      drag.moved ||= Math.abs(dx) + Math.abs(dy) > 3;
      if (drag.moved) drag.move(dx, dy);
    }, { signal });
    const finish = (event: PointerEvent) => {
      if (!drag || event.pointerId !== drag.pointer) return;
      if (drag.moved) this.save();
      drag = null;
    };
    handle.addEventListener("pointerup", finish, { signal });
    handle.addEventListener("pointercancel", finish, { signal });
    handle.addEventListener("lostpointercapture", finish, { signal });
  }
}
