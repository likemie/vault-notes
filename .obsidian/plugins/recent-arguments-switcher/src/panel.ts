import { setIcon } from "obsidian";
import { dateDescription, displayDate, type RecentNote } from "./recent-store";
import type { PanelState, Position } from "./settings";

const MARGIN = 8;
const ROW_HEIGHT = 28;

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
  private readonly capsule: HTMLButtonElement;
  private readonly capsuleCount: HTMLElement;
  private readonly body: HTMLElement;
  private readonly count: HTMLElement;
  private readonly list: HTMLElement;
  private readonly status: HTMLElement;
  private readonly events = new AbortController();
  private rowButtons: HTMLButtonElement[] = [];
  private drag: { pointer: number; x: number; y: number; origin: Position; moved: boolean } | null = null;

  constructor(
    private readonly window: Window,
    private readonly state: PanelState,
    private readonly open: (path: string) => Promise<void>,
    private readonly save: () => void,
  ) {
    const { document } = window;
    this.root = append(document.body, "aside", "ras-float");
    this.root.setAttribute("aria-label", "最近论证切换器");
    this.capsule = button(this.root, "ras-capsule", "展开最近论证");
    this.capsule.setAttribute("aria-controls", "ras-expanded");
    setIcon(append(this.capsule, "span", "ras-icon"), "history");
    append(this.capsule, "span", "", "论证");
    this.capsuleCount = append(this.capsule, "span", "ras-capsule-count", "0");

    this.body = append(this.root, "section", "ras-body");
    this.body.id = "ras-expanded";
    const header = append(this.body, "header", "ras-header");
    const handle = append(header, "div", "ras-handle");
    setIcon(append(handle, "span", "ras-grip"), "grip-horizontal");
    const title = append(handle, "h2", "ras-heading", "最新论证");
    title.id = "ras-heading";
    this.body.setAttribute("aria-labelledby", title.id);
    handle.title = "拖动调整位置";
    this.count = append(handle, "span", "ras-today", "今日 0");
    const collapse = button(header, "ras-collapse", "收起最近论证");
    collapse.title = "收起（Esc）";
    setIcon(collapse, "chevron-down");
    this.list = append(this.body, "ul", "ras-items");
    this.list.setAttribute("aria-label", "最近 100 条论证");
    this.status = append(this.body, "p", "ras-status");
    this.status.setAttribute("role", "status");
    this.status.hidden = true;

    const signal = this.events.signal;
    this.capsule.addEventListener("click", () => this.toggle(true), { signal });
    collapse.addEventListener("click", () => this.toggle(true), { signal });
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
    this.capsuleCount.textContent = String(data.unread);
    this.capsule.setAttribute("aria-label", "展开最近论证，" + data.unread + " 条未读");

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
      if (this.state.collapsed) this.capsule.focus();
      else (this.rowButtons.find(control => control.tabIndex === 0) ?? this.body.querySelector("button"))?.focus();
    }
  }

  destroy(): void {
    this.events.abort();
    this.root.remove();
  }

  private updateVisibility(): void {
    this.body.hidden = this.state.collapsed;
    this.capsule.hidden = !this.state.collapsed;
    this.capsule.setAttribute("aria-expanded", String(!this.state.collapsed));
    this.place();
  }

  private place(position = this.drag?.moved ? this.currentDragPosition() : this.state.position): Position {
    const width = this.root.offsetWidth;
    const height = this.root.offsetHeight;
    const right = this.window.innerWidth - width;
    const bottom = this.window.innerHeight - height;
    const x = Math.min(Math.max(MARGIN, position?.x ?? right - 18), Math.max(MARGIN, right - MARGIN));
    const y = Math.min(Math.max(MARGIN, position?.y ?? bottom - 36), Math.max(MARGIN, bottom - MARGIN));
    this.root.style.left = x + "px";
    this.root.style.top = y + "px";
    return { x, y };
  }

  private currentDragPosition(): Position | null {
    if (!this.drag) return null;
    return { x: this.drag.origin.x + this.drag.x, y: this.drag.origin.y + this.drag.y };
  }

  private bindDrag(handle: HTMLElement, signal: AbortSignal): void {
    let start: Position | null = null;
    handle.addEventListener("pointerdown", event => {
      if (event.button !== 0 || this.drag) return;
      const rect = this.root.getBoundingClientRect();
      start = { x: event.clientX, y: event.clientY };
      this.drag = { pointer: event.pointerId, x: 0, y: 0, origin: { x: rect.x, y: rect.y }, moved: false };
      handle.setPointerCapture(event.pointerId);
    }, { signal });
    handle.addEventListener("pointermove", event => {
      if (!start || !this.drag || event.pointerId !== this.drag.pointer) return;
      this.drag.x = event.clientX - start.x;
      this.drag.y = event.clientY - start.y;
      this.drag.moved ||= Math.abs(this.drag.x) + Math.abs(this.drag.y) >= 4;
      if (this.drag.moved) this.place();
    }, { signal });
    const end = (event: PointerEvent) => {
      if (!this.drag || event.pointerId !== this.drag.pointer) return;
      const position = this.drag.moved ? this.place() : null;
      this.drag = null;
      start = null;
      if (position) {
        this.state.position = position;
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
