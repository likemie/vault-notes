import { setIcon } from "obsidian";
import { dateDescription, displayDate, type RecentNote } from "./recent-store";
import type { PanelState } from "./settings";

const MARGIN = 8;
const ROW_HEIGHT = 26;

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
  rows: RecentNote[];
  unread: number;
  today: number;
  active: string | null;
  now: number;
}

export class RecentPanel {
  private readonly root: HTMLElement;
  private readonly rail: HTMLButtonElement;
  private readonly railCount: HTMLElement;
  private readonly body: HTMLElement;
  private readonly count: HTMLElement;
  private readonly list: HTMLElement;
  private readonly status: HTMLElement;
  private readonly events = new AbortController();
  private rowButtons: HTMLButtonElement[] = [];
  private unread = 0;
  private drag: { pointer: number; startY: number; center: number; moved: boolean } | null = null;

  constructor(
    private readonly window: Window,
    private readonly state: PanelState,
    private readonly open: (path: string) => Promise<void>,
    private readonly save: () => void,
  ) {
    const { document } = window;
    this.root = append(document.body, "aside", "ras-float");
    this.root.setAttribute("aria-label", "最近论证切换器");
    this.rail = button(this.root, "ras-rail", "展开最近论证");
    this.rail.setAttribute("aria-controls", "ras-expanded");
    const railIcon = append(this.rail, "span", "ras-rail-icon");
    railIcon.setAttribute("aria-hidden", "true");
    for (let i = 0; i < 3; i++) append(railIcon, "span");
    append(this.rail, "span", "ras-rail-label", "论证");
    this.railCount = append(this.rail, "span", "ras-rail-count", "0");

    this.body = append(this.root, "section", "ras-body");
    this.body.id = "ras-expanded";
    const header = append(this.body, "header", "ras-header");
    const handle = append(header, "div", "ras-handle");
    setIcon(append(handle, "span", "ras-grip"), "grip-horizontal");
    const title = append(handle, "h2", "ras-heading", "最新论证");
    title.id = "ras-heading";
    this.body.setAttribute("aria-labelledby", title.id);
    handle.title = "沿右边拖动面板";
    this.count = append(handle, "span", "ras-today", "今日 0");
    this.list = append(this.body, "ul", "ras-items");
    this.list.setAttribute("aria-label", "最近 100 条论证");
    this.status = append(this.body, "p", "ras-status");
    this.status.setAttribute("role", "status");
    this.status.hidden = true;

    const signal = this.events.signal;
    this.rail.addEventListener("click", () => this.toggle(true), { signal });
    this.list.addEventListener("click", event => { void this.openRow(event); }, { signal });
    this.root.addEventListener("keydown", event => this.onKey(event), { signal });
    window.addEventListener("resize", () => this.place(), { signal });
    this.bindDrag(handle, signal);
    this.updateVisibility();
  }

  render(data: ViewData): void {
    const activeElement = this.window.document.activeElement;
    const focused = this.rowButtons.find(control => control === activeElement)?.dataset.path;
    const oldScroll = this.list.scrollTop;
    const firstPath = this.rowButtons[Math.floor(oldScroll / ROW_HEIGHT)]?.dataset.path;
    this.count.textContent = "今日 " + data.today;
    this.count.title = "今天创建 " + data.today + " 条论证";
    this.unread = data.unread;
    this.railCount.textContent = String(data.unread);
    this.updateRail();

    const fragment = this.window.document.createDocumentFragment();
    this.rowButtons = [];
    if (!data.rows.length) {
      const empty = this.window.document.createElement("li");
      empty.className = "ras-empty";
      empty.textContent = "暂无论证";
      fragment.append(empty);
    }
    for (const note of data.rows) {
      const item = this.window.document.createElement("li");
      const date = displayDate(note, data.now);
      const control = button(item, "ras-row", note.title + "，" + date + (note.unread ? "，未读" : ""));
      control.dataset.path = note.path;
      control.dataset.unread = String(note.unread);
      control.tabIndex = -1;
      if (note.path === data.active) control.setAttribute("aria-current", "page");
      control.title = note.title + "\n" + dateDescription(note);
      append(control, "span", "ras-dot").setAttribute("aria-hidden", "true");
      append(control, "span", "ras-title", note.title);
      append(control, "span", "ras-date", date);
      this.rowButtons.push(control);
      fragment.append(item);
    }
    this.list.replaceChildren(fragment);
    // A single delegated click handler lives with the list instead of one handler per repaint.
    const focusedRow = this.rowButtons.find(control => control.dataset.path === focused);
    const tabbable = focusedRow ?? this.rowButtons.find(control => control.dataset.path === data.active) ?? this.rowButtons[0];
    if (tabbable) tabbable.tabIndex = 0;
    if (oldScroll && firstPath) {
      const anchor = this.rowButtons.findIndex(control => control.dataset.path === firstPath);
      this.list.scrollTop = anchor < 0 ? oldScroll : anchor * ROW_HEIGHT + oldScroll % ROW_HEIGHT;
    }
    focusedRow?.focus({ preventScroll: true });
    this.place();
  }

  private async openRow(event: MouseEvent): Promise<void> {
    const control = (event.target as HTMLElement).closest<HTMLButtonElement>(".ras-row");
    const path = control?.dataset.path;
    if (!control || !path) return;
    this.setTabStop(control);
    this.status.hidden = true;
    try {
      await this.open(path);
    } catch {
      this.status.textContent = "文件可能已移动，稍候再试。";
      this.status.hidden = false;
      this.place();
    }
  }

  toggle(focus: boolean): void {
    this.state.collapsed = !this.state.collapsed;
    this.updateVisibility();
    this.save();
    if (focus) {
      const target = this.state.collapsed ? this.rail : this.rowButtons.find(control => control.tabIndex === 0) ?? this.rail;
      target.focus({preventScroll: true});
    }
  }

  destroy(): void {
    this.events.abort();
    this.root.remove();
  }

  private updateVisibility(): void {
    this.body.hidden = this.state.collapsed;
    this.updateRail();
    this.place();
  }

  private updateRail(): void {
    const action = this.state.collapsed ? "展开最近论证" : "收起最近论证";
    this.rail.setAttribute("aria-expanded", String(!this.state.collapsed));
    this.rail.setAttribute("aria-label", action + "，" + this.unread + " 条未读");
    this.rail.title = action + " · " + this.unread + " 条未读";
  }

  private place(center = this.drag?.moved ? this.drag.center : this.state.centerY): number {
    const height = this.root.offsetHeight;
    const viewport = this.window.innerHeight;
    const top = Math.min(Math.max(MARGIN, (center ?? viewport * .68) - height / 2),
      Math.max(MARGIN, viewport - height - MARGIN));
    this.root.style.top = top + "px";
    return top + height / 2;
  }

  private bindDrag(handle: HTMLElement, signal: AbortSignal): void {
    handle.addEventListener("pointerdown", event => {
      if (event.button !== 0 || this.drag) return;
      const rect = this.root.getBoundingClientRect();
      this.drag = { pointer: event.pointerId, startY: event.clientY - rect.top - rect.height / 2,
        center: rect.top + rect.height / 2, moved: false };
      handle.setPointerCapture(event.pointerId);
    }, { signal });
    handle.addEventListener("pointermove", event => {
      if (!this.drag || event.pointerId !== this.drag.pointer) return;
      const center = event.clientY - this.drag.startY;
      this.drag.moved ||= Math.abs(center - this.drag.center) >= 4;
      if (this.drag.moved) this.drag.center = center;
      if (this.drag.moved) this.place();
    }, { signal });
    const end = (event: PointerEvent) => {
      if (!this.drag || event.pointerId !== this.drag.pointer) return;
      const center = this.drag.moved ? this.place() : null;
      this.drag = null;
      if (center !== null) {
        this.state.centerY = center;
        this.save();
      }
    };
    handle.addEventListener("pointerup", end, { signal });
    handle.addEventListener("pointercancel", end, { signal });
    handle.addEventListener("lostpointercapture", end, { signal });
  }

  private setTabStop(selected: HTMLButtonElement): void {
    for (const control of this.rowButtons) control.tabIndex = control === selected ? 0 : -1;
  }

  private onKey(event: KeyboardEvent): void {
    if (event.key === "Escape" && !this.state.collapsed) {
      event.preventDefault();
      event.stopPropagation();
      this.toggle(true);
      return;
    }
    if (this.state.collapsed || !this.rowButtons.length ||
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
