const { Modal, setIcon } = require("obsidian");
const {
  HOUR, KEYS, PROVIDERS, STATUSES, dateLabel, resetLabel, freshness, accountStatus, usableWindows, quotaText, accountName,
  isAntigravityId, geminiWeekly,
} = require("./model");

const MARGIN = 10;
const MIN_WIDTH = 240;
const MIN_HEIGHT = 150;
const PREVIEW_GAP = 6;
const LEAVE_DELAY = 160;
const WEEK = 7 * 24 * HOUR;

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

function refreshAntigravity(parent, state, actions, compact = false) {
  const busy = state.busy.has("antigravity");
  const label = busy ? "刷新中" : compact ? "刷新当前 Antigravity 账号" : "刷新当前账号";
  control(parent, label, () => actions.refresh("antigravity"), {
    icon: "refresh-cw", iconOnly: compact, name: compact ? "icon-button" : "button auf-quiet auf-refresh-current",
    id: "refresh-antigravity", disabled: busy,
  });
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

function compactService(parent, id, title, icon, detail) {
  const section = add(parent, "section", "float-service");
  section.dataset.aufProvider = id;
  section.setAttribute("aria-label", title);
  const heading = add(section, "header", "float-group");
  const mark = add(heading, "span", "icon auf-service-icon");
  mark.setAttribute("aria-hidden", "true");
  setIcon(mark, icon);
  add(heading, "h3", "", title);
  if (detail) add(heading, "small", "muted", detail);
  return { section, heading };
}

function displayCompactSubscription(parent, id, state, actions) {
  const subscription = state.rows[id][0];
  const title = id === "codex" ? "Codex" : PROVIDERS[id].title;
  const { section, heading } = compactService(parent, id, title, id === "codex" ? "terminal" : "orbit", subscription?.plan);
  const busy = state.busy.has(id);
  control(heading, busy ? title + " 刷新中" : "刷新 " + title, () => actions.refresh(id), {
    icon: "refresh-cw", iconOnly: true, name: "icon-button", id: "refresh-" + id, disabled: busy,
  });
  if (!subscription?.windows.length) {
    add(section, "p", "muted auf-account-note", subscription?.issue?.message || "暂无额度。");
    return;
  }
  const status = rowStatus(subscription, state.now, state.settings.interval);
  if (status) {
    add(section, "p", "status auf-account-note", [STATUSES[status], freshness(subscription.fetchedAt, state.now)].join(" · "));
  }
  const grid = add(section, "div", "quota-grid");
  subscription.windows.forEach(quota => quotaWindow(grid, quota, status, state.now));
}

function displayGeminiWindows(parent, row, state, snapshot = false) {
  const windows = row.windows.filter(quota => /^gemini(?:$|[-_])/i.test(quota.id));
  if (!windows.length) {
    add(parent, "p", "muted", row.issue?.message || "暂无 Gemini 额度。");
    return;
  }
  const status = snapshot ? "stale" : rowStatus({ ...row, windows }, state.now, state.settings.interval);
  if (status && !snapshot) {
    add(parent, "p", "status auf-account-note", [STATUSES[status], freshness(row.fetchedAt, state.now)].join(" · "));
  }
  const grid = add(parent, "div", "quota-grid");
  for (const quota of windows) {
    quotaWindow(grid, { ...quota, name: quota.name.replace(/^Gemini Models · /i, "") }, status, state.now);
  }
}

function displayGemini(parent, state, actions, openSnapshots) {
  const { section, heading } = compactService(parent, "antigravity", "Gemini", "sparkles", "Antigravity");
  refreshAntigravity(heading, state, actions, true);
  const accounts = state.rows.antigravity.filter(row => isAntigravityId(row.id));
  const current = accounts.find(row => row.id === state.currentAntigravityId);
  if (current) {
    const account = add(section, "div", "gemini-current");
    const title = add(account, "div", "gemini-account-head");
    add(title, "strong", "", accountName("antigravity", current, state.settings));
    add(title, "small", "muted", "当前账号");
    displayGeminiWindows(account, current, state);
  } else if (accounts.length) {
    add(section, "p", "muted auf-account-note", "尚未确认当前登录账号。");
  } else {
    add(section, "p", "empty", state.rows.antigravity[0]?.issue?.message || "暂无 Gemini 额度。");
  }
  const snapshots = accounts.filter(row => row !== current);
  if (!snapshots.length) return;
  const snapshotHeading = add(section, "h4", "gemini-snapshot-title");
  add(snapshotHeading, "span", "", "账号快照");
  add(snapshotHeading, "span", "", "每周剩余 · 重置日期");
  for (const row of snapshots) {
    const entry = add(section, "details", "gemini-snapshot");
    entry.dataset.aufAccount = row.id;
    entry.open = openSnapshots.has(row.id);
    const summary = add(entry, "summary", "gemini-snapshot-summary");
    summary.dataset.aufFocus = "snapshot-" + row.id;
    const arrow = add(summary, "span", "icon auf-snapshot-arrow");
    arrow.setAttribute("aria-hidden", "true");
    setIcon(arrow, "chevron-right");
    add(summary, "span", "snapshot-name", accountName("antigravity", row, state.settings));
    const weekly = geminiWeekly(row);
    const metrics = add(summary, "span", "snapshot-metrics");
    const resetAt = weekly?.resetAt ?? null;
    // Project a full weekly allowance in this summary until the collector supplies a new window.
    const estimated = resetAt !== null && resetAt <= state.now;
    const remaining = estimated ? 100 : (weekly?.remaining ?? null);
    const badge = add(metrics, "strong", "num auf-snapshot-quota", quotaText(remaining));
    if (remaining !== null) {
      badge.dataset.aufLevel = remaining >= 60 ? "high" : remaining >= 20 ? "medium" : "low";
    }
    if (estimated) add(badge, "span", "snapshot-estimate", "估算");
    const quotaLabel = estimated ? "重置后估算的每周剩余 " : "每周剩余 ";
    badge.setAttribute("aria-label", quotaLabel + (remaining === null ? "未知" : quotaText(remaining)));
    if (resetAt === null) {
      add(metrics, "small", "muted auf-snapshot-reset", "日期未知");
    } else {
      const nextResetAt = estimated ? resetAt + (Math.floor((state.now - resetAt) / WEEK) + 1) * WEEK : resetAt;
      const reset = add(metrics, "time", "muted auf-snapshot-reset", dateLabel(nextResetAt));
      reset.dateTime = new Date(nextResetAt).toISOString();
      const exactTime = resetLabel(nextResetAt, state.now);
      reset.title = estimated ? "预计 " + exactTime : exactTime;
    }
    const details = add(entry, "div", "snapshot-windows");
    displayGeminiWindows(details, row, state, true);
    if (row.fetchedAt !== null) add(details, "small", "muted auf-snapshot-captured", "采集于 " + freshness(row.fetchedAt, state.now));
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
        if (id === "antigravity") refreshAntigravity(head, state, this.actions);
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
    this.root.id = "auf-floating-panel";
    this.root.hidden = true;
    this.root.setAttribute("aria-label", "额度用量");
    this.launcher = control(win.document.body, "额度", actions.toggle, { name: "launcher", icon: "chart-no-axes-column" });
    this.launcher.setAttribute("aria-controls", this.root.id);
    this.header = add(this.root, "header", "float-head");
    this.handle = add(this.header, "div", "handle", "额度用量");
    this.buttons = add(this.header, "div", "head-buttons");
    this.body = add(this.root, "div", "float-body");
    this.footer = add(this.root, "footer", "float-foot");
    this.footer.setAttribute("role", "status");
    this.footer.setAttribute("aria-live", "polite");
    this.grips = [this.resizeGrip("left"), this.resizeGrip("right")];
    this.place = this.place.bind(this);
    this.bindPointer(this.handle, bounds => (dx, dy) => this.move(bounds.left + dx, bounds.top + dy));
    this.listenForPointer();
    this.listenForPreview();
    this.resize = new win.ResizeObserver(this.place);
    this.resize.observe(this.root);
    this.dockObserver = new win.MutationObserver(() => this.followDock());
    this.followDock();
    win.addEventListener("resize", this.place, { signal: this.events.signal });
  }

  render(state) {
    const { pinned } = state.settings;
    const collapsed = pinned && state.settings.collapsed;
    this.updateVisibility(pinned);
    this.root.classList.toggle("is-pinned", pinned);
    this.root.classList.toggle("is-collapsed", collapsed);
    this.handle.title = pinned ? "拖动浮窗" : "";
    this.body.hidden = this.footer.hidden = collapsed;
    this.grips.forEach(grip => { grip.hidden = !pinned || collapsed; });
    const scroll = this.body.scrollTop;
    preserveFocus(this.root, () => {
      this.buttons.replaceChildren();
      control(this.buttons, "打开额度总览", this.actions.dashboard, {
        icon: "panel-top", iconOnly: true, name: "icon-button", id: "dashboard",
      });
      if (pinned) {
        control(this.buttons, collapsed ? "展开浮窗" : "折叠浮窗", this.actions.collapse, {
          icon: collapsed ? "chevron-down" : "minus", iconOnly: true, name: "icon-button", id: "collapse",
        }).setAttribute("aria-expanded", String(!collapsed));
        control(this.buttons, "隐藏浮窗", () => this.dismiss(), { icon: "x", iconOnly: true, name: "icon-button", id: "hide" });
      }
      if (collapsed) return;
      const openSnapshots = new Set();
      if (this.currentAntigravityId === state.currentAntigravityId) {
        for (const entry of this.body.querySelectorAll(".auf-gemini-snapshot[open]")) openSnapshots.add(entry.dataset.aufAccount);
      }
      this.currentAntigravityId = state.currentAntigravityId;
      this.body.replaceChildren();
      const ids = ["codex", "grok", "antigravity"].filter(id => state.settings.enabled[id]);
      for (const id of ids) {
        if (id === "antigravity") displayGemini(this.body, state, this.actions, openSnapshots);
        else displayCompactSubscription(this.body, id, state, this.actions);
      }
      if (!ids.length) add(this.body, "p", "empty", "请在设置中启用要查看的服务。");
      this.body.scrollTop = scroll;
      this.footer.textContent = ids.some(id => state.busy.has(id)) ? "正在查询额度…" : "百分比为剩余额度";
    });
    this.place();
  }

  place() {
    this.placeLauncher();
    if (this.root.hidden || this.gesture) return;
    const { left, top, width: savedWidth, height: savedHeight, collapsed, pinned } = this.actions.state().settings;
    if (!pinned) {
      this.size(null, null);
      const rail = this.launcher.getBoundingClientRect();
      this.root.style.maxWidth = Math.max(1, rail.left - MARGIN - PREVIEW_GAP) + "px";
      this.move(rail.left - this.root.offsetWidth - PREVIEW_GAP, rail.top + (rail.height - this.root.offsetHeight) / 2);
      return;
    }
    this.root.style.maxWidth = "";
    this.size(collapsed ? null : savedWidth, collapsed ? null : savedHeight);
    const width = this.root.offsetWidth;
    const height = this.root.offsetHeight;
    this.move(left ?? this.win.innerWidth - width - 36, top ?? this.win.innerHeight * 0.35, width, height);
  }

  followDock() {
    const dock = this.win.document.querySelector(".ras-dock");
    if (dock !== this.linkDock) {
      if (this.linkDock) this.resize.unobserve(this.linkDock);
      this.linkDock = dock;
      this.dockObserver.disconnect();
      this.dockObserver.observe(this.win.document.body, { childList: true });
      if (dock) {
        this.dockObserver.observe(dock, { attributes: true, attributeFilter: ["style", "class", "hidden"] });
        this.resize.observe(dock);
      }
    }
    this.place();
  }

  updateVisibility(pinned = this.actions.state().settings.pinned) {
    const visible = pinned || this.preview === true;
    const restoreFocus = !visible && this.root.contains(this.win.document.activeElement);
    if (!visible && !this.root.hidden) {
      for (const entry of this.body.querySelectorAll(".auf-gemini-snapshot[open]")) entry.open = false;
    }
    this.root.hidden = !visible;
    this.launcher.setAttribute("aria-expanded", String(visible));
    this.launcher.setAttribute("aria-pressed", String(pinned));
    this.launcher.title = pinned ? "取消固定额度浮窗" : "悬停查看额度，点击固定";
    if (restoreFocus) this.launcher.focus({ preventScroll: true });
  }

  clearPreviewTimer() {
    this.win.clearTimeout(this.leaveTimer);
    this.leaveTimer = undefined;
  }

  dismiss() {
    this.clearPreviewTimer();
    this.preview = false;
    if (this.actions.state().settings.pinned) this.actions.hide();
    else this.updateVisibility();
  }

  listenForPreview() {
    const { signal } = this.events;
    this.launcher.addEventListener("pointerenter", event => {
      if (event.pointerType !== "mouse") return;
      this.clearPreviewTimer();
      this.preview = true;
      this.updateVisibility();
      this.place();
    }, { signal });
    this.root.addEventListener("pointerenter", event => {
      if (event.pointerType === "mouse") this.clearPreviewTimer();
    }, { signal });
    for (const region of [this.launcher, this.root]) {
      region.addEventListener("pointerleave", event => {
        if (event.pointerType !== "mouse") return;
        this.clearPreviewTimer();
        this.leaveTimer = this.win.setTimeout(() => {
          this.preview = false;
          this.updateVisibility();
        }, LEAVE_DELAY);
      }, { signal });
      region.addEventListener("keydown", event => {
        if (event.key !== "Escape" || this.root.hidden) return;
        event.stopPropagation();
        this.dismiss();
      }, { signal });
    }
  }

  placeLauncher() {
    const dock = this.linkDock?.getBoundingClientRect();
    const height = this.launcher.offsetHeight;
    const gap = 8;
    const above = dock?.height ? dock.top - height - gap : this.win.innerHeight * 0.55;
    const top = dock?.height && above < MARGIN ? dock.bottom + gap : above;
    const limit = Math.max(MARGIN, this.win.innerHeight - height - MARGIN);
    this.launcher.style.top = clamp(top, MARGIN, limit) + "px";
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
    handle.addEventListener("pointerdown", event => {
      if (event.button !== 0 || this.gesture || !this.actions.state().settings.pinned) return;
      this.gesture = {
        id: event.pointerId, x: event.clientX, y: event.clientY, patch: null,
        update: begin(this.root.getBoundingClientRect()),
      };
      handle.setPointerCapture(event.pointerId);
      event.preventDefault();
    }, { signal: this.events.signal });
  }

  listenForPointer() {
    const options = { signal: this.events.signal, capture: true };
    const finish = () => {
      const patch = this.gesture?.patch;
      this.gesture = null;
      if (patch) this.actions.geometry(patch);
    };
    this.win.addEventListener("pointermove", event => {
      const drag = this.gesture;
      if (drag?.id !== event.pointerId) return;
      if (!event.buttons) {
        finish();
        return;
      }
      drag.patch = drag.update(event.clientX - drag.x, event.clientY - drag.y);
    }, options);
    for (const name of ["pointerup", "pointercancel"]) {
      this.win.addEventListener(name, event => {
        if (this.gesture?.id === event.pointerId) finish();
      }, options);
    }
    this.win.addEventListener("blur", finish, { signal: this.events.signal });
  }

  destroy() {
    this.clearPreviewTimer();
    this.events.abort();
    this.resize.disconnect();
    this.dockObserver.disconnect();
    this.root.remove();
    this.launcher.remove();
  }
}

module.exports = { Dashboard, FloatingPanel };
