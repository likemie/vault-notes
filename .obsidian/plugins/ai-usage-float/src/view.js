const { Modal, setIcon } = require("obsidian");
const {
  HOUR, KEYS, PROVIDERS, STATUSES, resetLabel, freshness, accountStatus, usableWindows, quotaText, accountName,
} = require("./model");

const MARGIN = 10;
const MIN_WIDTH = 240;
const MIN_HEIGHT = 150;

function clamp(value, min, max) {
  return Math.max(min, Math.min(max, value));
}

function add(parent, tag, name, value) {
  const node = parent.ownerDocument.createElement(tag);
  if (name) node.className = "auf-" + name;
  if (value !== undefined) node.textContent = value;
  parent.append(node);
  return node;
}

function control(parent, label, callback, { icon, iconOnly = false, name = "button", id = label, disabled = false } = {}) {
  const button = add(parent, "button", name);
  button.type = "button";
  button.disabled = disabled;
  button.dataset.aufFocus = id;
  if (icon) {
    const item = add(button, "span", "icon");
    setIcon(item, icon);
    item.setAttribute("aria-hidden", "true");
  }
  if (iconOnly) {
    button.setAttribute("aria-label", label);
    button.title = label;
  } else {
    add(button, "span", "", label);
  }
  button.addEventListener("click", callback);
  return button;
}

function track(parent, value, old) {
  if (value === null) return;
  const bar = add(parent, "div", old ? "track auf-track-old" : "track");
  bar.setAttribute("aria-hidden", "true");
  add(bar, "span").style.width = value + "%";
}

function rowStatus(row, now, interval) {
  return accountStatus(row, now, interval) ??
    (row.windows.length && !usableWindows(row, now, interval).length ? "stale" : null);
}

function sourceLine(parent, row, now) {
  const stamp = row.fetchedAt === null ? "" : " · " + freshness(row.fetchedAt, now) + " 采集";
  add(parent, "small", "muted", row.source + stamp);
}

function quotaWindow(parent, quota, status, now) {
  const cell = add(parent, "div", "quota");
  const heading = add(cell, "div", "quota-line");
  add(heading, "span", "", quota.name);
  const value = add(heading, "strong", "num", quotaText(quota.remaining));
  value.setAttribute("aria-label", quota.remaining === null ? "剩余额度未知" : "剩余 " + quotaText(quota.remaining));
  const expired = quota.resetAt !== null && quota.resetAt <= now;
  track(cell, quota.remaining, status || expired);
  add(cell, "small", "muted", expired ? "已过重置时间 · " + freshness(quota.resetAt, now) : resetLabel(quota.resetAt, now));
}

function allWindows(state) {
  const { rows, settings, now } = state;
  return KEYS.filter(id => settings.enabled[id]).flatMap(id =>
    rows[id].flatMap(row => usableWindows(row, now, settings.interval).map(quota => ({ id, row, quota }))),
  );
}

function minimum(windows) {
  return windows.filter(item => item.quota.remaining !== null).sort((a, b) => a.quota.remaining - b.quota.remaining)[0];
}

function displayAccount(parent, id, account, state, actions) {
  const box = add(parent, "div", "account");
  const head = add(box, "div", "account-head");
  const labels = add(head, "div", "account-label");
  const status = rowStatus(account, state.now, state.settings.interval);
  const name = accountName(id, account, state.settings);
  if (name) {
    add(labels, "strong", "", [name, account.plan].filter(Boolean).join(" · "));
  }
  if (status) add(labels, "span", "status", STATUSES[status]);
  sourceLine(labels, account, state.now);
  if (id === "antigravity" && account.id !== id) {
    control(head, account.source === "Antigravity Tools 快照" ? "同步快照" : "刷新", () => actions.refresh(id, account.id), {
      icon: "refresh-cw", name: "button auf-quiet", id: account.id, disabled: state.busy.has(id),
    });
  }
  if (account.issue) add(box, "p", "muted auf-account-note", account.issue.message);
  if (account.windows.length) {
    const grid = add(box, "div", "quota-grid");
    account.windows.forEach(quota => quotaWindow(grid, quota, status, state.now));
  }
}

function card(parent, title, detail) {
  const panel = add(parent, "section", "card");
  const top = add(panel, "header", "card-head");
  add(top, "h3", "", title);
  if (detail) add(top, "small", "muted", detail);
  return panel;
}

function preserveFocus(root, render) {
  const active = root.ownerDocument.activeElement;
  const key = root.contains(active) ? active.dataset?.aufFocus : null;
  render();
  if (key) {
    const next = [...root.querySelectorAll("[data-auf-focus]")].find(node => node.dataset.aufFocus === key);
    next?.focus({ preventScroll: true });
  }
}

class Dashboard extends Modal {
  constructor(app, actions) {
    super(app);
    this.actions = actions;
    this.modalEl.addClass("auf-modal");
    this.setTitle("额度用量");
  }

  onOpen() {
    this.render(this.actions.state());
  }

  render(state) {
    if (!this.contentEl.isConnected) return;
    preserveFocus(this.contentEl, () => {
      const root = this.contentEl;
      root.replaceChildren();
      root.classList.add("auf-dashboard");
      const toolbar = add(root, "div", "toolbar");
      const clock = state.lastRefresh ? "最近查询 " + freshness(state.lastRefresh, state.now) : "等待采集";
      add(toolbar, "span", "muted", clock + " · 本地时间");
      control(toolbar, state.busy.size ? "刷新中" : "刷新全部", () => this.actions.refresh(), {
        icon: "refresh-cw", name: "button auf-primary", disabled: Boolean(state.busy.size), id: "refresh-all",
      });
      const layout = add(root, "div", "dashboard-grid");
      const services = card(layout, "服务额度", "百分比为剩余量");
      const ids = KEYS.filter(id => state.settings.enabled[id]);
      for (const id of ids) {
        const provider = PROVIDERS[id];
        const section = add(services, "section", "service");
        const head = add(section, "header", "service-head");
        add(head, "h4", "", provider.title);
        const registered = state.rows[id].filter(row => row.id !== id);
        const plan = id === "antigravity" && registered.length ? registered.length + " 个账号" :
          (id === "grok" && state.rows[id][0]?.plan ? state.rows[id][0].plan + " 积分" : provider.scope);
        if (plan) add(head, "small", "muted", plan);
        state.rows[id].forEach(row => displayAccount(section, id, row, state, this.actions));
      }
      if (!ids.length) add(services, "p", "empty", "请在设置中启用要查看的服务。");

      const right = add(layout, "div", "right");
      const windows = allWindows(state);
      const low = minimum(windows);
      const priority = card(right, "当前最低额度");
      const readout = add(priority, "div", "readout");
      if (low) {
        add(readout, "div", "priority-value", quotaText(low.quota.remaining));
        add(readout, "div", "context",
          [PROVIDERS[low.id].title, accountName(low.id, low.row, state.settings), low.quota.name].filter(Boolean).join(" · "));
        add(readout, "small", "muted", resetLabel(low.quota.resetAt, state.now));
        track(readout, low.quota.remaining, false);
      } else {
        add(readout, "p", "muted", "暂无可比较的额度。");
      }
      const resets = card(right, "即将重置", "未来 24 小时");
      const soon = windows
        .filter(({ quota }) => quota.resetAt !== null && quota.resetAt <= state.now + 24 * HOUR)
        .sort((a, b) => a.quota.resetAt - b.quota.resetAt);
      if (soon.length) {
        const list = add(resets, "ol", "resets");
        for (const { id, row, quota } of soon) {
          const item = add(list, "li");
          const label = add(item, "div");
          add(label, "div", "", PROVIDERS[id].title);
          add(label, "small", "muted", [accountName(id, row, state.settings), quota.name].filter(Boolean).join(" · "));
          add(item, "time", "num", freshness(quota.resetAt, state.now)).dateTime = new Date(quota.resetAt).toISOString();
        }
      } else {
        add(resets, "p", "empty", "暂无已知重置。");
      }
    });
  }

  onClose() {
    this.contentEl.replaceChildren();
  }
}

class FloatingPanel {
  constructor(win, actions) {
    this.win = win;
    this.actions = actions;
    this.events = new AbortController();
    this.root = add(win.document.body, "aside", "float");
    this.root.setAttribute("aria-label", "AI Usage Float");
    this.header = add(this.root, "header", "float-head");
    this.handle = add(this.header, "div", "handle", "AI Usage");
    this.handle.title = "拖动浮窗";
    this.buttons = add(this.header, "div", "head-buttons");
    this.body = add(this.root, "div", "float-body");
    this.footer = add(this.root, "footer", "float-foot");
    this.footer.setAttribute("role", "status");
    this.footer.setAttribute("aria-live", "polite");
    this.grips = [this.resizeGrip("left"), this.resizeGrip("right")];
    this.place = this.place.bind(this);
    this.bindPointer(this.handle, bounds => (dx, dy) => this.move(bounds.left + dx, bounds.top + dy));
    this.resize = new win.ResizeObserver(this.place);
    this.resize.observe(this.root);
    win.addEventListener("resize", this.place, { signal: this.events.signal });
  }

  render(state) {
    this.root.hidden = !state.settings.shown;
    this.root.classList.toggle("is-collapsed", state.settings.collapsed);
    this.body.hidden = this.footer.hidden = state.settings.collapsed;
    this.grips.forEach(grip => { grip.hidden = state.settings.collapsed; });
    const open = new Set([...this.body.querySelectorAll("details[open]")].map(el => el.dataset.account));
    const scroll = this.body.scrollTop;
    preserveFocus(this.root, () => {
      this.buttons.replaceChildren();
      control(this.buttons, "打开额度总览", this.actions.dashboard, {
        icon: "panel-top", iconOnly: true, name: "icon-button", id: "dashboard",
      });
      if (!state.settings.collapsed) {
        control(this.buttons, state.busy.size ? "刷新中" : "刷新全部", () => this.actions.refresh(), {
          icon: "refresh-cw", iconOnly: true, name: "icon-button", disabled: Boolean(state.busy.size), id: "refresh",
        });
      }
      control(this.buttons, state.settings.collapsed ? "展开浮窗" : "折叠浮窗", this.actions.collapse, {
        icon: state.settings.collapsed ? "chevron-down" : "minus", iconOnly: true, name: "icon-button", id: "collapse",
      }).setAttribute("aria-expanded", String(!state.settings.collapsed));
      control(this.buttons, "隐藏浮窗", this.actions.hide, { icon: "x", iconOnly: true, name: "icon-button", id: "hide" });
      if (state.settings.collapsed) return;
      this.body.replaceChildren();
      const ids = KEYS.filter(id => state.settings.enabled[id]);
      for (const id of ids) {
        const service = PROVIDERS[id];
        const group = add(this.body, "section", "float-service");
        if (id === "antigravity") add(group, "div", "float-group", service.title);
        for (const row of state.rows[id]) {
          const element = add(group, "details", "float-account");
          element.dataset.account = row.id;
          element.open = open.has(row.id);
          const summary = add(element, "summary", "float-row");
          summary.dataset.aufFocus = "summary-" + row.id;
          const identity = add(summary, "div", "float-label");
          add(identity, "div", "", accountName(id, row, state.settings) || service.title);
          const status = rowStatus(row, state.now, state.settings.interval);
          const valid = usableWindows(row, state.now, state.settings.interval);
          const windows = valid.length ? valid : row.windows;
          const quota = [...windows].filter(quota => quota.remaining !== null).sort((a, b) => a.remaining - b.remaining)[0];
          if (quota) {
            const cue = status ? [STATUSES[status], row.fetchedAt && freshness(row.fetchedAt, state.now)].filter(Boolean).join(" · ")
              : resetLabel(quota.resetAt, state.now);
            add(identity, "small", "muted", (id === "grok" ? "SuperGrok · " : "") + quota.name + " · " + cue);
            track(summary, quota.remaining, status);
            add(summary, "strong", "num", quotaText(quota.remaining));
          } else {
            add(summary, "small", "status", STATUSES[status] ?? "额度未知");
          }
          displayAccount(element, id, row, state, this.actions);
        }
      }
      if (!ids.length) add(this.body, "p", "empty", "请在设置中启用服务。");
      this.body.scrollTop = scroll;
      this.footer.textContent = state.busy.size ? "正在查询额度…" :
        state.lastRefresh ? "最近查询 " + freshness(state.lastRefresh, state.now) : "等待采集";
    });
    this.place();
  }

  place() {
    if (this.root.hidden || this.interacting) return;
    const { left, top, width: savedWidth, height: savedHeight, collapsed } = this.actions.state().settings;
    this.size(collapsed ? null : savedWidth, collapsed ? null : savedHeight);
    const width = this.root.offsetWidth;
    const height = this.root.offsetHeight;
    this.move(left ?? this.win.innerWidth - width - 36, top ?? this.win.innerHeight * 0.35, width, height);
  }

  move(left, top, width = this.root.offsetWidth, height = this.root.offsetHeight) {
    const maxLeft = Math.max(MARGIN, this.win.innerWidth - width - MARGIN);
    const maxTop = Math.max(MARGIN, this.win.innerHeight - height - MARGIN);
    const position = { left: clamp(left, MARGIN, maxLeft), top: clamp(top, MARGIN, maxTop) };
    this.root.style.left = position.left + "px";
    this.root.style.top = position.top + "px";
    return position;
  }

  size(width, height) {
    const maxWidth = Math.max(1, this.win.innerWidth - 2 * MARGIN);
    const maxHeight = Math.max(1, this.win.innerHeight - 2 * MARGIN);
    const nextWidth = width === null ? null : clamp(Math.round(width), Math.min(MIN_WIDTH, maxWidth), maxWidth);
    const nextHeight = height === null ? null : clamp(Math.round(height), Math.min(MIN_HEIGHT, maxHeight), maxHeight);
    this.root.classList.toggle("is-sized", nextHeight !== null);
    this.root.style.width = nextWidth === null ? "" : nextWidth + "px";
    this.root.style.height = nextHeight === null ? "" : nextHeight + "px";
    return { width: nextWidth, height: nextHeight };
  }

  resizeFrom(side, bounds, dx, dy) {
    const dimensions = this.size(bounds.width + (side === "left" ? -dx : dx), bounds.height + dy);
    const left = side === "left" ? bounds.right - dimensions.width : bounds.left;
    return { ...this.move(left, bounds.top), ...dimensions };
  }

  resizeGrip(side) {
    const grip = add(this.root, "button", "resize auf-resize-" + side);
    const corner = side === "left" ? "左下角" : "右下角";
    grip.type = "button";
    grip.setAttribute("aria-label", "从" + corner + "调整浮窗大小");
    grip.title = "拖动或按方向键调整浮窗大小";
    this.bindPointer(grip, bounds => (dx, dy) => this.resizeFrom(side, bounds, dx, dy));
    grip.addEventListener("keydown", event => {
      const step = event.shiftKey ? 24 : 8;
      const arrows = { ArrowLeft: [-step, 0], ArrowRight: [step, 0], ArrowUp: [0, -step], ArrowDown: [0, step] };
      const delta = arrows[event.key];
      if (!delta) return;
      event.preventDefault();
      this.actions.geometry(this.resizeFrom(side, this.root.getBoundingClientRect(), ...delta));
    }, { signal: this.events.signal });
    return grip;
  }

  bindPointer(handle, begin) {
    const { signal } = this.events;
    let drag;
    handle.addEventListener("pointerdown", event => {
      if (event.button !== 0 || this.interacting) return;
      drag = {
        id: event.pointerId, x: event.clientX, y: event.clientY, patch: null,
        update: begin(this.root.getBoundingClientRect()),
      };
      this.interacting = true;
      handle.setPointerCapture(event.pointerId);
      event.preventDefault();
    }, { signal });
    handle.addEventListener("pointermove", event => {
      if (drag?.id !== event.pointerId) return;
      drag.patch = drag.update(event.clientX - drag.x, event.clientY - drag.y);
    }, { signal });
    const finish = event => {
      if (drag?.id !== event.pointerId) return;
      const { patch } = drag;
      drag = null;
      this.interacting = false;
      if (patch) this.actions.geometry(patch);
    };
    for (const event of ["pointerup", "pointercancel", "lostpointercapture"]) {
      handle.addEventListener(event, finish, { signal });
    }
  }

  destroy() {
    this.events.abort();
    this.resize.disconnect();
    this.root.remove();
  }
}

module.exports = { Dashboard, FloatingPanel };
