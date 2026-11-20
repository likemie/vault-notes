import { setIcon } from "obsidian";
import { dateDescription, displayDate, LIMIT, type ArgumentNote } from "./recent-store";
import type { PanelState } from "./settings";

const MARGIN = 8;
const ROW_HEIGHT = 26;
const LEAVE_DELAY = 150;

function clampTop(top: number, height: number, viewport: number): number {
  return Math.min(Math.max(MARGIN, top), Math.max(MARGIN, viewport - height - MARGIN));
}

function append<K extends keyof HTMLElementTagNameMap>(
  parent: HTMLElement, tag: K, className?: string, text?: string,
): HTMLElementTagNameMap[K] {
  const node = parent.ownerDocument.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined) node.textContent = text;
  parent.append(node);
  return node;
}

function button(parent: HTMLElement, className: string, label: string): HTMLButtonElement {
  const control = append(parent, "button", className);
  control.type = "button";
  control.setAttribute("aria-label", label);
  return control;
}

interface ViewData {
  rows: (ArgumentNote & { firstSeen?: number; unread?: boolean })[];
  badge: number;
  count: string;
  countDescription?: string;
  active: string | null;
  now: number;
  empty: string;
  context?: string | null;
}

interface PanelOptions {
  id: "links" | "arguments";
  label: string;
  title: string;
  listLabel: string;
  badgeUnit: string;
}

export class HoverDock {
  private readonly root: HTMLElement;
  private readonly events = new AbortController();
  private readonly panels: HoverPanel[] = [];
  private active: HoverPanel | null = null;

  constructor(private readonly window: Window, private readonly state: PanelState, private readonly save: () => void) {
    this.root = append(window.document.body, "aside", "ras-dock");
    this.root.setAttribute("aria-label", "笔记切换工具");
    window.addEventListener("resize", () => this.place(), { signal: this.events.signal });
  }

  add(options: PanelOptions, open: (path: string) => Promise<void>): HoverPanel {
    const panel = new HoverPanel(this.window, this.root, options, open, () => {
      if (this.active !== panel) this.active?.collapse();
      this.active = panel;
    }, center => this.place(center), () => {
      this.state.centerY = this.center();
      this.save();
    });
    this.panels.push(panel);
    this.place();
    return panel;
  }

  destroy(): void {
    this.events.abort();
    for (const panel of this.panels) panel.destroy();
    this.root.remove();
  }

  private anchorOffset(): number {
    const lastRail = this.root.lastElementChild as HTMLElement;
    return this.root.offsetHeight - lastRail.offsetHeight / 2;
  }

  private center(): number {
    return this.root.getBoundingClientRect().top + this.anchorOffset();
  }

  private place(center = this.state.centerY): void {
    if (!this.panels.length) return;
    const viewport = this.window.innerHeight;
    const top = clampTop((center ?? viewport * .68) - this.anchorOffset(), this.root.offsetHeight, viewport);
    this.root.style.top = top + "px";
    for (const panel of this.panels) panel.placeBody();
  }
}

export class HoverPanel {
  private readonly root: HTMLElement;
  private readonly rail: HTMLButtonElement;
  private readonly railCount: HTMLElement;
  private readonly body: HTMLElement;
  private readonly count: HTMLElement;
  private readonly list: HTMLElement;
  private readonly status: HTMLElement;
  private readonly events = new AbortController();
  private rowButtons: HTMLButtonElement[] = [];
  private data: ViewData | null = null;
  private shown = LIMIT;
  private expanded = false;
  private closeTimer: number | null = null;
  private drag: { pointer: number; startY: number; center: number; moved: boolean } | null = null;

  constructor(
    private readonly window: Window,
    private readonly parent: HTMLElement,
    private readonly options: PanelOptions,
    private readonly open: (path: string) => Promise<void>,
    private readonly onExpand: () => void,
    private readonly onMove: (center: number) => void,
    private readonly onMoveEnd: () => void,
  ) {
    this.root = append(parent, "section", "ras-float");
    this.root.dataset.kind = options.id;
    this.root.setAttribute("aria-label", options.title);
    this.rail = button(this.root, "ras-rail", "展开" + options.title);
    this.rail.setAttribute("aria-controls", "ras-expanded-" + options.id);
    const railIcon = append(this.rail, "span", "ras-rail-icon");
    railIcon.setAttribute("aria-hidden", "true");
    if (options.id === "links") setIcon(railIcon, "link-2");
    else for (let i = 0; i < 3; i++) append(railIcon, "span");
    append(this.rail, "span", "ras-rail-label", options.label);
    this.railCount = append(this.rail, "span", "ras-rail-count", "0");

    this.body = append(this.root, "section", "ras-body");
    this.body.id = "ras-expanded-" + options.id;
    const header = append(this.body, "header", "ras-header");
    const handle = append(header, "div", "ras-handle");
    setIcon(append(handle, "span", "ras-grip"), "grip-horizontal");
    const title = append(handle, "h2", "ras-heading", options.title);
    title.id = "ras-heading-" + options.id;
    this.body.setAttribute("aria-labelledby", title.id);
    handle.title = "沿右边移动两个入口";
    this.count = append(handle, "span", "ras-today");
    this.list = append(this.body, "ul", "ras-items");
    this.list.setAttribute("aria-label", options.listLabel);
    this.status = append(this.body, "p", "ras-status");
    this.status.setAttribute("role", "status");
    this.status.hidden = true;

    const signal = this.events.signal;
    this.rail.addEventListener("click", () => this.toggle(true), { signal });
    this.rail.addEventListener("pointerenter", event => {
      if (event.pointerType !== "mouse") return;
      this.cancelClose();
      this.setExpanded(true);
    }, { signal });
    this.root.addEventListener("pointerenter", event => {
      if (event.pointerType === "mouse") this.cancelClose();
    }, { signal });
    this.root.addEventListener("pointerleave", event => {
      if (event.pointerType !== "mouse" || !this.expanded) return;
      this.cancelClose();
      this.closeTimer = this.window.setTimeout(() => {
        this.closeTimer = null;
        this.setExpanded(false);
      }, LEAVE_DELAY);
    }, { signal });
    this.list.addEventListener("click", event => { void this.openRow(event); }, { signal });
    this.root.addEventListener("keydown", event => this.onKey(event), { signal });
    this.bindDrag(handle, signal);
    this.setExpanded(false);
  }

  render(data: ViewData): void {
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
    this.railCount.textContent = data.badge > 999 ? Math.floor(data.badge / 1000) + "k+" : String(data.badge);
    this.updateRail();
    if (this.expanded) this.renderRows(samePage);
  }

  private renderRows(preservePosition: boolean, focusMore = false): void {
    const data = this.data;
    if (!data) return;
    const activeElement = this.window.document.activeElement;
    const focusedRowBefore = this.rowButtons.find(control => control === activeElement);
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
      const control = button(item, "ras-row", note.title + "，" + date + (note.unread ? "，未读" : ""));
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
      button(item, "ras-more", "显示更多链接").textContent = "显示更多链接";
      fragment.append(item);
    }
    this.list.replaceChildren(fragment);
    // A single delegated click handler lives with the list instead of one handler per repaint.
    const focusedRow = focusMore ? this.rowButtons[this.shown - LIMIT] :
      this.rowButtons.find(control => control.dataset.path === focused);
    const tabbable = focusedRow ?? this.rowButtons.find(control => control.dataset.path === data.active) ?? this.rowButtons[0];
    if (tabbable) tabbable.tabIndex = 0;
    if (oldScroll && firstPath) {
      const anchor = this.rowButtons.findIndex(control => control.dataset.path === firstPath);
      this.list.scrollTop = anchor < 0 ? oldScroll : anchor * ROW_HEIGHT + oldScroll % ROW_HEIGHT;
    }
    if (!preservePosition) this.list.scrollTop = 0;
    if (focusMore) focusedRow?.focus();
    else if (focusedRowBefore) (tabbable ?? this.rail).focus({ preventScroll: true });
    this.placeBody();
  }

  private async openRow(event: MouseEvent): Promise<void> {
    const target = event.target as HTMLElement;
    if (target.closest(".ras-more")) {
      this.shown += LIMIT;
      this.renderRows(true, true);
      return;
    }
    const control = target.closest<HTMLButtonElement>(".ras-row");
    const path = control?.dataset.path;
    if (!control || !path) return;
    this.setTabStop(control);
    this.status.hidden = true;
    try {
      await this.open(path);
    } catch {
      this.status.textContent = "文件可能已移动，稍候再试。";
      this.status.hidden = false;
      this.placeBody();
    }
  }

  toggle(focus: boolean): void {
    this.cancelClose();
    this.setExpanded(!this.expanded);
    if (focus) {
      const target = this.expanded ? this.rowButtons.find(control => control.tabIndex === 0) ?? this.rail : this.rail;
      target.focus({ preventScroll: true });
    }
  }

  destroy(): void {
    this.cancelClose();
    this.events.abort();
    this.root.remove();
  }

  collapse(): void {
    this.cancelClose();
    this.setExpanded(false);
  }

  private cancelClose(): void {
    if (this.closeTimer === null) return;
    this.window.clearTimeout(this.closeTimer);
    this.closeTimer = null;
  }

  private setExpanded(expanded: boolean): void {
    if (expanded === this.expanded && this.root.dataset.open !== undefined) return;
    if (expanded && !this.expanded) this.onExpand();
    const restoreFocus = !expanded && this.body.contains(this.window.document.activeElement);
    this.expanded = expanded;
    this.body.hidden = !expanded;
    this.root.dataset.open = String(expanded);
    this.updateRail();
    if (expanded) this.renderRows(true);
    if (restoreFocus) this.rail.focus({ preventScroll: true });
  }

  private updateRail(): void {
    const action = (this.expanded ? "收起" : "展开") + this.options.title;
    const description = (this.data?.badge ?? 0) + " " + this.options.badgeUnit;
    this.rail.setAttribute("aria-expanded", String(this.expanded));
    this.rail.setAttribute("aria-label", action + "，" + description);
    this.rail.title = action + " · " + description;
  }

  placeBody(): void {
    if (!this.expanded) return;
    const rail = this.root.getBoundingClientRect();
    const bodyHeight = this.body.offsetHeight;
    const top = clampTop(rail.top + (rail.height - bodyHeight) / 2, bodyHeight, this.window.innerHeight);
    this.body.style.top = top - rail.top + "px";
  }

  private bindDrag(handle: HTMLElement, signal: AbortSignal): void {
    handle.addEventListener("pointerdown", event => {
      if (event.button !== 0 || this.drag) return;
      const center = this.parent.getBoundingClientRect().bottom - this.rail.offsetHeight / 2;
      this.drag = { pointer: event.pointerId, startY: event.clientY - center, center, moved: false };
      handle.setPointerCapture(event.pointerId);
    }, { signal });
    handle.addEventListener("pointermove", event => {
      if (!this.drag || event.pointerId !== this.drag.pointer) return;
      const center = event.clientY - this.drag.startY;
      this.drag.moved ||= Math.abs(center - this.drag.center) >= 4;
      if (this.drag.moved) this.drag.center = center;
      if (this.drag.moved) this.onMove(center);
    }, { signal });
    const end = (event: PointerEvent) => {
      if (!this.drag || event.pointerId !== this.drag.pointer) return;
      const moved = this.drag.moved;
      this.drag = null;
      if (moved) this.onMoveEnd();
    };
    handle.addEventListener("pointerup", end, { signal });
    handle.addEventListener("pointercancel", end, { signal });
    handle.addEventListener("lostpointercapture", end, { signal });
  }

  private setTabStop(selected: HTMLButtonElement): void {
    for (const control of this.rowButtons) control.tabIndex = control === selected ? 0 : -1;
  }

  private onKey(event: KeyboardEvent): void {
    if (event.key === "Escape" && this.expanded) {
      event.preventDefault();
      event.stopPropagation();
      this.toggle(true);
      return;
    }
    if (!this.expanded || !this.rowButtons.length ||
        (event.key !== "ArrowDown" && event.key !== "ArrowUp")) return;
    event.preventDefault();
    event.stopPropagation();
    const current = this.rowButtons.indexOf(event.target as HTMLButtonElement);
    const index = current < 0 ? 0 :
      Math.max(0, Math.min(this.rowButtons.length - 1, current + (event.key === "ArrowDown" ? 1 : -1)));
    const next = this.rowButtons[index];
    this.setTabStop(next);
    next.focus();
  }
}
