const { Notice, Plugin, PluginSettingTab, Setting } = require("obsidian");
const {
  KEYS, PROVIDERS, MINUTE, INTERVALS, cacheFrom, settings, text, isAntigravityId, accountName, retainAntigravitySnapshots,
} = require("./model");
const { collectors, issue, defaultFailure } = require("./collectors");
const { Dashboard, FloatingPanel } = require("./view");

class UsageSettings extends PluginSettingTab {
  constructor(app, plugin) {
    super(app, plugin);
    this.plugin = plugin;
  }

  display() {
    const { containerEl, plugin } = this;
    containerEl.empty();
    new Setting(containerEl).setName("固定额度浮窗")
      .setDesc("固定后，鼠标移开时仍可查看和调整浮窗。")
      .addToggle(control => control.setValue(plugin.preferences.pinned).onChange(value => plugin.configure({ pinned: value })));
    new Setting(containerEl).setName("自动刷新")
      .setDesc("遇到采集失败时延长自动重试间隔。手动刷新可随时重试。")
      .addDropdown(control => {
        for (const interval of INTERVALS) control.addOption(String(interval), interval ? interval + " 分钟" : "仅手动");
        control.setValue(String(plugin.preferences.interval)).onChange(value => plugin.configure({ interval: Number(value) }));
      });
    new Setting(containerEl).setName("监控服务").setHeading();
    for (const provider of KEYS) {
      const { title, scope } = PROVIDERS[provider];
      new Setting(containerEl).setName(title)
        .setDesc(scope || "显示已验证的桌面账号及 Antigravity Tools 注册账号的本地快照。")
        .addToggle(control => control.setValue(plugin.preferences.enabled[provider])
          .onChange(value => plugin.enableProvider(provider, value)));
    }
    new Setting(containerEl).setName("重置浮窗位置")
      .addButton(button => button.setButtonText("重置位置").onClick(() => plugin.configure({ left: null, top: null })));
    new Setting(containerEl).setName("重置浮窗大小")
      .addButton(button => button.setButtonText("恢复默认大小").onClick(() => plugin.configure({ width: null, height: null })));
    const accounts = plugin.rows.antigravity.filter(row => isAntigravityId(row.id));
    if (accounts.length) {
      new Setting(containerEl).setName("Antigravity 账号名称").setHeading();
      for (const row of accounts) {
        new Setting(containerEl).setName(accountName("antigravity", row, plugin.preferences)).setDesc(row.source)
          .addText(input => input.setPlaceholder(row.profileName || row.label)
            .setValue(plugin.preferences.antigravityNames[row.id] ?? "")
            .onChange(value => plugin.nameAntigravityAccount(row.id, value)));
      }
    }
  }
}

class UsageFloatPlugin extends Plugin {
  async onload() {
    const saved = await this.loadData();
    this.preferences = settings(saved?.preferences);
    const cache = cacheFrom(saved);
    this.rows = Object.fromEntries(KEYS.map(id => [
      id,
      cache[id].length
        ? cache[id].map(row => ({ ...row, issue: { status: "offline", message: "等待本次采集。" } }))
        : [defaultFailure(id, new Error())],
    ]));
    for (const id of KEYS) {
      if (!cache[id].length) this.rows[id][0].issue.message = "等待首次采集。";
    }
    this.lifetime = new AbortController();
    this.busy = new Map();
    this.due = new Map();
    this.writes = Promise.resolve();
    this.lastRefresh = null;
    this.actions = {
      state: () => this.state(),
      dashboard: () => this.openDashboard(),
      toggle: () => this.toggle(),
      refresh: (id, account) => void this.refreshFromControl(id, account),
      collapse: () => this.configure({ collapsed: !this.preferences.collapsed }),
      hide: () => this.configure({ pinned: false }),
      geometry: patch => this.configure(patch),
    };

    this.addSettingTab(new UsageSettings(this.app, this));
    this.addRibbonIcon("chart-no-axes-column", "显示或隐藏额度浮窗", () => this.toggle());
    this.addCommand({ id: "toggle", name: "显示或隐藏额度浮窗", callback: () => this.toggle() });
    this.addCommand({ id: "dashboard", name: "打开额度总览", callback: this.actions.dashboard });
    this.addCommand({ id: "refresh", name: "刷新订阅额度", callback: () => void this.refreshFromControl() });
    this.app.workspace.onLayoutReady(() => {
      if (this.lifetime.signal.aborted) return;
      this.panel = new FloatingPanel(window, this.actions);
      this.render();
      if (this.preferences.interval) void this.refresh();
      this.registerInterval(window.setInterval(() => this.tick(), 30_000));
    });
  }

  onunload() {
    this.lifetime?.abort();
    for (const controller of this.busy?.values() ?? []) controller.abort();
    this.dashboard?.close();
    this.panel?.destroy();
  }

  state() {
    return {
      settings: this.preferences, rows: this.rows, busy: this.busy,
      lastRefresh: this.lastRefresh, now: Date.now(),
    };
  }

  render() {
    const state = this.state();
    this.panel?.render(state);
    this.dashboard?.render(state);
  }

  openDashboard() {
    if (!this.dashboard?.modalEl.isConnected) {
      this.dashboard = new Dashboard(this.app, this.actions);
      this.dashboard.open();
    }
  }

  toggle() {
    this.configure({ pinned: !this.preferences.pinned, collapsed: false });
  }

  configure(patch) {
    const previous = this.preferences.interval;
    this.preferences = { ...this.preferences, ...patch };
    this.render();
    this.persist();
    if (patch.interval && patch.interval !== previous) {
      this.due.clear();
      this.tick();
    }
  }

  enableProvider(id, enabled) {
    this.configure({ enabled: { ...this.preferences.enabled, [id]: enabled } });
    if (!enabled) this.busy.get(id)?.abort();
    else if (this.preferences.interval) void this.refresh(id);
  }

  nameAntigravityAccount(id, value) {
    if (!isAntigravityId(id)) return;
    const names = { ...this.preferences.antigravityNames };
    const name = text(value, 60);
    if (name) names[id] = name;
    else delete names[id];
    this.configure({ antigravityNames: names });
  }

  tick() {
    if (this.lifetime.signal.aborted) return;
    this.render();
    if (!this.preferences.interval) return;
    for (const id of KEYS) {
      if (Date.now() >= (this.due.get(id)?.at ?? 0)) void this.refresh(id);
    }
  }

  async refresh(onlyProvider, accountId) {
    const selected = onlyProvider ? [onlyProvider] : KEYS;
    await Promise.all(selected.filter(id => this.preferences.enabled[id]).map(id => this.refreshProvider(id, accountId)));
  }

  async refreshFromControl(onlyProvider, accountId) {
    const id = onlyProvider ?? "antigravity";
    if (!this.preferences.enabled[id]) return this.refresh(onlyProvider, accountId);
    const title = id === "codex" ? "Codex" : PROVIDERS[id].title;
    if (this.busy.has(id)) {
      new Notice(title + " 正在查询额度。");
      return;
    }
    const previous = new Map(this.rows[id].map(row => [row.id, row.fetchedAt]));
    await this.refresh(onlyProvider, accountId);
    if (this.lifetime.signal.aborted || !this.preferences.enabled[id]) return;
    const rows = this.rows[id].filter(row => !accountId || row.id === accountId);
    if (rows.some(row => !row.issue && row.fetchedAt > (previous.get(row.id) ?? 0))) {
      new Notice(title + " 额度已更新。");
      return;
    }
    const reason = rows.find(row => row.issue)?.issue?.message;
    const summary = title + (rows.some(row => row.windows.length) ? " 保留了上次快照。" : " 未取得额度。");
    new Notice([summary, reason].filter(Boolean).join("\n"), 7000);
  }

  async refreshProvider(id, accountId) {
    if (this.busy.has(id) || this.lifetime.signal.aborted) return;
    const controller = new AbortController();
    const { signal } = controller;
    this.busy.set(id, controller);
    this.render();
    const prior = this.rows[id];
    let failed = false;
    try {
      const fresh = await collectors[id](signal, prior, accountId);
      if (signal.aborted) return;
      const byId = new Map(prior.map(row => [row.id, row]));
      const merged = fresh.map(row => {
        const last = byId.get(row.id);
        if (last?.windows.some(window => window.remaining !== null)
            && row.issue && !row.windows.some(window => window.remaining !== null)) {
          return { ...last, issue: row.issue };
        }
        return row;
      });
      const resolved = id === "antigravity"
        ? retainAntigravitySnapshots(merged, accountId ? prior.filter(row => row.id === accountId) : prior)
        : merged;
      failed = resolved.every(row => row.issue || !row.windows.length);
      this.rows[id] = accountId
        ? prior.map(row => row.id === accountId ? (resolved[0] ?? row) : row)
        : resolved;
    } catch (error) {
      if (signal.aborted) return;
      failed = true;
      this.rows[id] = prior.map(row => !accountId || row.id === accountId ? { ...row, issue: issue(error) } : row);
    } finally {
      this.busy.delete(id);
      if (!this.lifetime.signal.aborted) {
        if (!signal.aborted) {
          const misses = failed ? Math.min((this.due.get(id)?.misses ?? 0) + 1, 3) : 0;
          this.due.set(id, { misses, at: Date.now() + Math.max(1, this.preferences.interval) * 2 ** misses * MINUTE });
          this.lastRefresh = Date.now();
          this.persist();
        }
        this.render();
      }
    }
  }

  persist() {
    const cache = Object.fromEntries(KEYS.map(id => [id, this.rows[id]
      .filter(row => row.windows.length && row.fetchedAt !== null)
      .map(({ issue: _issue, ...row }) => row)]));
    const data = { preferences: this.preferences, cache };
    this.writes = this.writes.then(() => this.saveData(data)).catch(() => {
      console.warn("AI Usage Float: could not save local preferences and quota snapshots");
    });
  }
}

module.exports = UsageFloatPlugin;
