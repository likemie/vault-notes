const CONFIG_PATH = "_system/dashboard/config.json";
const DAY = 86_400_000;
const COUNTS = new Intl.NumberFormat("zh-CN");
const CLOCK = new Intl.DateTimeFormat("zh-CN", { hour: "2-digit", minute: "2-digit" });
const EXACT_TIME = new Intl.DateTimeFormat("zh-CN", {
  year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", second: "2-digit",
});
const SHORT_DATE = new Intl.DateTimeFormat("zh-CN", { month: "numeric", day: "numeric" });
const COLLATOR = new Intl.Collator("zh-CN", { numeric: true });
const ACTIVITY_MODES = { created: "新建", modified: "修改", today: "今天" };
const WINDOWS = { all: "全部时间", today: "今天", 7: "最近 7 天", 30: "最近 30 天" };
const HEALTH_LABELS = { isolated: "孤立笔记", unresolved: "未解析链接", missing: "缺少必需字段" };

const SAFE_CONFIG = {
  includeFolders: ["wiki"],
  excludeFolders: ["wiki/templates", "wiki/assets"],
  excludeFiles: [],
  typeRules: [],
  requiredFieldsByType: {},
  quickLinks: [],
  allNotesPath: "wiki/index.md",
  pageSize: 20,
  trendDays: 30,
};

function normalizedPath(path) {
  return path.trim().replaceAll("\\", "/").replace(/^\/+|\/+$/g, "").normalize("NFC");
}

function pathWithin(path, folder) {
  return path === folder || path.startsWith(folder + "/");
}

function validateConfig(config) {
  const strings = value => Array.isArray(value) && value.every(item => typeof item === "string" && item.trim());
  const record = value => value && typeof value === "object" && !Array.isArray(value);
  if (!record(config) ||
      !["includeFolders", "excludeFolders", "excludeFiles"].every(key => strings(config[key])) ||
      !Array.isArray(config.typeRules) ||
      !config.typeRules.every(rule => record(rule) && strings([rule.id, rule.label]) &&
        strings(rule.folders) && (rule.fieldValue === undefined || strings([rule.fieldValue]))) ||
      new Set(config.typeRules.map(rule => rule.id)).size !== config.typeRules.length ||
      !record(config.requiredFieldsByType) || !Object.values(config.requiredFieldsByType).every(strings) ||
      !Array.isArray(config.quickLinks) ||
      !config.quickLinks.every(link => record(link) && strings([link.label, link.path])) ||
      !strings([config.allNotesPath]) || ![20, 50].includes(config.pageSize) ||
      ![7, 30, 90].includes(config.trendDays)) {
    throw new Error("配置字段格式不正确");
  }
  return config;
}

async function loadConfig(vault) {
  try {
    const file = vault.getFileByPath(CONFIG_PATH);
    if (!file) throw new Error("找不到配置文件");
    return { config: validateConfig(JSON.parse(await vault.cachedRead(file))) };
  } catch (error) {
    console.warn("Knowledge Dashboard", error);
    return { config: SAFE_CONFIG, message: "看板配置无法读取，暂时只显示 wiki 目录。" };
  }
}

function classifyNote(path, type, rules) {
  const fieldType = typeof type === "string" ? type.trim().toLowerCase() : "";
  const match = rules.byField.get(fieldType) ??
    rules.byFolder.find(rule => rule.folders.some(folder => pathWithin(path, folder)));
  return match?.id ?? "other";
}

function collectNotes(paths, vault, metadata, config) {
  const include = config.includeFolders.map(normalizedPath);
  const exclude = config.excludeFolders.map(normalizedPath);
  const excludeFiles = new Set(config.excludeFiles.map(normalizedPath));
  const rules = {
    byField: new Map(config.typeRules.filter(rule => rule.fieldValue).reverse()
      .map(rule => [rule.fieldValue.trim().toLowerCase(), rule])),
    byFolder: config.typeRules.map(rule => ({ ...rule, folders: rule.folders.map(normalizedPath) })),
  };
  const notes = [];
  for (const path of paths) {
    const key = normalizedPath(path);
    if (excludeFiles.has(key) || exclude.some(folder => pathWithin(key, folder)) ||
        (include.length && !include.some(folder => pathWithin(key, folder)))) continue;
    const file = vault.getFileByPath(path);
    if (file?.extension !== "md") continue;
    const fields = metadata.getFileCache(file)?.frontmatter ?? {};
    const folder = path.slice(0, Math.max(0, path.lastIndexOf("/")));
    const name = [fields.argument_display_title, fields.title]
      .find(value => typeof value === "string" && value.trim())?.trim() || file.basename;
    const createdMs = file.stat.ctime > 0 && Number.isFinite(file.stat.ctime) ? file.stat.ctime : null;
    const modifiedMs = file.stat.mtime > 0 && Number.isFinite(file.stat.mtime) ? file.stat.mtime : null;
    notes.push({
      path, name, folder, createdMs, modifiedMs, fields,
      type: classifyNote(key, fields.type, rules),
      search: (name + "\n" + path).normalize("NFC").toLowerCase(),
    });
  }
  return notes;
}

function localDay(now, offset = 0) {
  const date = new Date(now);
  date.setHours(0, 0, 0, 0);
  date.setDate(date.getDate() + offset);
  return date.getTime();
}

function withinTime(ms, start, end) {
  return ms !== null && ms >= start && ms <= end;
}

function computeOverview(notes, now) {
  const today = localDay(now);
  const week = localDay(now, -((new Date(now).getDay() + 6) % 7));
  const overview = { total: notes.length, created: 0, modified: 0, week: 0 };
  for (const note of notes) {
    const createdToday = withinTime(note.createdMs, today, now);
    if (createdToday) overview.created++;
    else if (withinTime(note.modifiedMs, today, now)) overview.modified++;
    if (withinTime(note.createdMs, week, now)) overview.week++;
  }
  return overview;
}

function activityTime(note, mode, now) {
  if (mode === "created") return note.createdMs;
  if (mode === "modified") return note.modifiedMs;
  const start = localDay(now);
  const created = withinTime(note.createdMs, start, now) ? note.createdMs : null;
  const modified = withinTime(note.modifiedMs, start, now) ? note.modifiedMs : null;
  return Math.max(created ?? 0, modified ?? 0) || null;
}

function queryActivity(notes, filters, now, activityOrders) {
  const orderKey = filters.mode + filters.sort;
  if (!activityOrders.has(orderKey)) {
    const direction = filters.sort === "asc" ? 1 : -1;
    const entries = notes.map(note => ({ note, time: activityTime(note, filters.mode, now) }));
    entries.sort((a, b) => {
      if (a.time === null || b.time === null) {
        if (a.time !== b.time) return a.time === null ? 1 : -1;
      }
      return direction * (a.time - b.time) || COLLATOR.compare(a.note.path, b.note.path);
    });
    activityOrders.set(orderKey, entries);
  }
  const query = filters.search.trim().normalize("NFC").toLowerCase();
  const start = filters.window === "all" ? -Infinity : localDay(now, filters.window === "today" ? 0 : 1 - Number(filters.window));
  const matches = activityOrders.get(orderKey).filter(({ note, time }) =>
    (filters.mode !== "today" || time !== null) &&
    (filters.window === "all" || withinTime(time, start, now)) &&
    (!filters.type || filters.type === note.type) &&
    (!filters.folder || pathWithin(note.folder, filters.folder)) &&
    (!query || note.search.includes(query))
  );
  return pageOf(matches, filters.page, filters.size);
}

function pageOf(items, page, size) {
  const pages = Math.max(1, Math.ceil(items.length / size));
  const current = Math.min(Math.max(page, 1), pages);
  return {
    rows: items.slice((current - 1) * size, current * size),
    total: items.length, current, pages,
  };
}

function computeDailySeries(notes, now, days, mode) {
  const counts = new Map();
  for (let offset = 1 - days; offset <= 0; offset++) counts.set(localDay(now, offset), 0);
  const start = localDay(now, 1 - days);
  for (const note of notes) {
    const time = mode === "created" ? note.createdMs : note.modifiedMs;
    if (!withinTime(time, start, now)) continue;
    const day = localDay(time);
    counts.set(day, counts.get(day) + 1);
  }
  return Array.from(counts, ([date, count]) => ({ date, count }));
}

function computeComposition(notes, group) {
  const counts = new Map();
  for (const note of notes) {
    const key = group === "type" ? note.type : note.folder.split("/", 1)[0] || "根目录";
    counts.set(key, (counts.get(key) ?? 0) + 1);
  }
  return Array.from(counts).sort((a, b) => b[1] - a[1] || COLLATOR.compare(a[0], b[0]));
}

function computeHealth(notes, resolved, unresolved, rules) {
  const inScope = new Set(notes.map(note => note.path));
  const connected = new Set();
  const broken = [];
  const missing = [];
  let sources = 0;
  let checked = 0;
  for (const note of notes) {
    for (const target of Object.keys(resolved[note.path] ?? {})) {
      if (target === note.path || !inScope.has(target)) continue;
      connected.add(target);
      connected.add(note.path);
    }
    const targets = Object.keys(unresolved[note.path] ?? {});
    if (targets.length) sources++;
    for (const target of targets) broken.push({ note, detail: target });
    const keys = Object.hasOwn(rules, note.type) ? rules[note.type] : [];
    if (keys.length) checked++;
    const absent = keys.filter(key => {
      const value = Object.hasOwn(note.fields, key) ? note.fields[key] : null;
      return value == null || (typeof value === "string" && !value.trim()) || (Array.isArray(value) && !value.length);
    });
    if (absent.length) missing.push({ note, detail: absent.join("、") });
  }
  return {
    isolated: notes.filter(note => !connected.has(note.path)).map(note => ({ note })),
    unresolved: broken, missing, sources, checked,
  };
}

function timeLabel(ms, now) {
  if (ms === null) return "—";
  if (ms > now) return EXACT_TIME.format(ms);
  const days = Math.round((localDay(now) - localDay(ms)) / DAY);
  if (days === 0) return "今天 " + CLOCK.format(ms);
  if (days === 1) return "昨天 " + CLOCK.format(ms);
  if (days < 7) return days + " 天前";
  if (days < 365) return SHORT_DATE.format(ms);
  return EXACT_TIME.format(ms).split(" ")[0];
}

function element(parent, tag, className, value) {
  const node = parent.ownerDocument.createElement(tag);
  if (className) node.className = className;
  if (value !== undefined) node.textContent = value;
  parent.append(node);
  return node;
}

function button(parent, label, action, className) {
  const node = element(parent, "button", className, label);
  node.type = "button";
  node.addEventListener("click", action);
  return node;
}

function select(parent, label, choices, value, action) {
  const node = element(parent, "select");
  node.setAttribute("aria-label", label);
  for (const [id, name] of choices) element(node, "option", "", name).value = id;
  node.value = value;
  node.addEventListener("change", () => action(node.value));
  return node;
}

function noteLink(app, parent, path, title, fullTitle = title) {
  const link = element(parent, "a", "internal-link kd-link", title);
  link.href = path;
  link.dataset.href = path;
  link.title = fullTitle;
  link.addEventListener("click", async event => {
    if (event.altKey) return;
    event.preventDefault();
    event.stopPropagation();
    const file = app.vault.getFileByPath(path);
    const status = parent.closest(".kd-dashboard")?.querySelector(".kd-message");
    if (!file) {
      if (status) status.textContent = "这个文件已移动或删除，请刷新看板。";
      return;
    }
    try {
      await app.workspace.getLeaf(event.metaKey || event.ctrlKey ? "tab" : false).openFile(file);
    } catch (error) {
      if (status) status.textContent = "无法打开这个文件，请刷新看板后重试。";
      console.error("Knowledge Dashboard", error);
    }
  });
  return link;
}

function panel(parent, title, className = "") {
  const section = element(parent, "section", "kd-panel " + className);
  const head = element(section, "div", "kd-section-heading");
  element(head, "h2", "", title);
  return { section, head };
}

function pagination(parent, result, changePage) {
  const nav = element(parent, "div", "kd-pagination");
  const count = element(nav, "span", "kd-muted", COUNTS.format(result.total) + " 条");
  count.setAttribute("role", "status");
  const controls = element(nav, "div", "kd-paging-controls");
  const previous = button(controls, "上一页", () => changePage(result.current - 1, "previous"));
  previous.dataset.page = "previous";
  previous.disabled = result.current === 1;
  element(controls, "span", "kd-muted", result.current + " / " + result.pages);
  const next = button(controls, "下一页", () => changePage(result.current + 1, "next"));
  next.dataset.page = "next";
  next.disabled = result.current === result.pages;
}

function restorePagingFocus(host, focus) {
  if (!focus) return;
  const target = host.querySelector('[data-page="' + focus + '"]:not(:disabled)') ??
    host.querySelector("[data-page]:not(:disabled)");
  target?.focus();
}

function renderActivity(parent, data, state, save, app) {
  const { section, head } = panel(parent, "最近活动", "kd-activity");
  const { notes, types, now } = data;
  const filters = state.activity;
  const orders = new Map();
  const dirs = Array.from(new Set(notes.map(note => note.folder).filter(Boolean))).sort(COLLATOR.compare);
  const actualTypes = new Set(notes.map(note => note.type));
  if (filters.folder && !dirs.includes(filters.folder)) filters.folder = "";
  if (filters.type && !actualTypes.has(filters.type)) filters.type = "";
  const tabs = element(head, "div", "kd-segments");
  tabs.setAttribute("role", "group");
  tabs.setAttribute("aria-label", "活动类型");
  const tabButtons = new Map();
  for (const [id, label] of Object.entries(ACTIVITY_MODES)) {
    tabButtons.set(id, button(tabs, label, () => apply("mode", id)));
  }

  const controls = element(section, "div", "kd-filters");
  const search = element(controls, "input", "kd-search");
  search.type = "search";
  search.placeholder = "搜索标题或路径";
  search.setAttribute("aria-label", search.placeholder);
  search.value = filters.search;
  let searchTimer;
  search.addEventListener("input", () => {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => {
      if (section.isConnected) apply("search", search.value);
    }, 120);
  });
  const ranges = ["all", "today", "7", "30"].map(id => [id, WINDOWS[id]]);
  const rangeSelect = select(controls, "时间范围", ranges, filters.window, value => apply("window", value));
  select(controls, "笔记类型",
    [["", "所有类型"], ...Array.from(types).filter(([id]) => actualTypes.has(id))],
    filters.type, value => apply("type", value));
  select(controls, "笔记目录",
    [["", "所有目录"], ...dirs.map(dir => [dir, dir])], filters.folder, value => apply("folder", value));
  select(controls, "时间排序", [["desc", "最新优先"], ["asc", "最早优先"]],
    filters.sort, value => apply("sort", value));
  select(controls, "每页条数", [[20, "20 条/页"], [50, "50 条/页"]],
    filters.size, value => apply("size", Number(value)));
  const output = element(section, "div", "kd-results");

  function apply(key, value) {
    clearTimeout(searchTimer);
    filters.search = search.value;
    filters[key] = value;
    filters.page = 1;
    draw();
  }

  function draw(focus) {
    for (const [id, node] of tabButtons) node.setAttribute("aria-pressed", String(filters.mode === id));
    rangeSelect.disabled = filters.mode === "today";
    rangeSelect.value = rangeSelect.disabled ? "today" : filters.window;
    const usedFilters = filters.mode === "today" ? { ...filters, window: "today" } : filters;
    const result = queryActivity(notes, usedFilters, now, orders);
    filters.page = result.current;
    save();
    output.replaceChildren();
    if (!result.total) {
      element(output, "p", "kd-empty", notes.length ? "没有符合条件的笔记。" : "索引中暂无符合范围的笔记。");
    } else {
      renderActivityTable(output, result.rows, filters.mode, types, now, app);
    }
    pagination(output, result, (page, nextFocus) => {
      filters.page = page;
      draw(nextFocus);
    });
    restorePagingFocus(output, focus);
  }
  draw();
}

function renderActivityTable(parent, rows, mode, types, now, app) {
  const table = element(parent, "table", "kd-table");
  table.setAttribute("aria-label", "最近活动列表");
  const heading = element(table.createTHead(), "tr");
  const timeHeading = mode === "created" ? "创建时间" : mode === "modified" ? "修改时间" : "活动时间";
  for (const label of ["笔记标题", "类型", "所在目录", timeHeading]) {
    const th = element(heading, "th", "", label);
    th.scope = "col";
  }
  const body = table.createTBody();
  for (const { note, time } of rows) {
    const row = element(body, "tr");
    const title = element(row, "td", "kd-title-cell");
    noteLink(app, title, note.path, note.name, note.name + "\n" + note.path);
    element(title, "span", "kd-mobile-meta", (types.get(note.type) ?? "其他") + " · " + (note.folder || "根目录"))
      .title = note.folder || "根目录";
    element(row, "td", "kd-muted", types.get(note.type) ?? "其他");
    element(row, "td", "kd-muted", note.folder || "根目录").title = note.folder || "根目录";
    const timeCell = element(row, "td", "kd-time-cell");
    const date = element(timeCell, time === null ? "span" : "time", "kd-muted", timeLabel(time, now));
    if (time !== null) {
      date.dateTime = new Date(time).toISOString();
      date.title = EXACT_TIME.format(time);
    }
  }
}

function renderOverview(parent, notes, now) {
  const box = element(parent, "dl", "kd-overview");
  const overview = computeOverview(notes, now);
  const metrics = [
    ["知识总量", overview.total, "统计范围内的 Markdown 笔记"],
    ["今日新增", overview.created, "今天创建的笔记"],
    ["今日更新", overview.modified, "今天修改的旧笔记"],
    ["本周新增", overview.week, "本周一零时起创建的笔记"],
  ];
  for (const [label, value, hint] of metrics) {
    const cell = element(box, "div", "kd-metric");
    element(cell, "dt", "", label).title = hint;
    element(cell, "dd", "", COUNTS.format(value));
  }
  element(parent, "p", "kd-overview-note kd-caption", "新增按文件创建时间统计，迁移或同步可能影响计数。");
}

function svgElement(parent, tag, attributes) {
  const node = parent.ownerDocument.createElementNS("http://www.w3.org/2000/svg", tag);
  for (const [key, value] of Object.entries(attributes)) node.setAttribute(key, value);
  parent.append(node);
  return node;
}

function renderTrend(parent, data, state, save) {
  const { section, head } = panel(parent, "活动趋势");
  const { notes, now } = data;
  const trend = state.trend;
  const controls = element(head, "div", "kd-section-controls");
  select(controls, "趋势指标", [["created", "新增"], ["modified", "最后修改"]], trend.mode, value => {
    trend.mode = value;
    draw();
  });
  select(controls, "趋势天数", [[7, "7 天"], [30, "30 天"], [90, "90 天"]], trend.days, value => {
    trend.days = Number(value);
    draw();
  });
  const chart = element(section, "div", "kd-chart");

  function draw() {
    save();
    chart.replaceChildren();
    const series = computeDailySeries(notes, now, trend.days, trend.mode);
    const peak = Math.max(...series.map(day => day.count));
    const targetStep = Math.max(1, (peak + 1) / 3);
    const magnitude = 10 ** Math.floor(Math.log10(targetStep));
    const step = [1, 2, 5, 10].find(multiplier => multiplier * magnitude >= targetStep) * magnitude;
    const top = step * 3;
    const label = trend.mode === "created" ? "新增" : "最后修改";
    const total = series.reduce((sum, day) => sum + day.count, 0);
    const summary = element(chart, "p", "kd-chart-summary", "共 " + COUNTS.format(total) + " 条" + label);
    const layout = element(chart, "div", "kd-plot");
    const axis = element(layout, "div", "kd-y-axis");
    axis.setAttribute("aria-hidden", "true");
    for (let tick = 3; tick >= 0; tick--) element(axis, "span", "", COUNTS.format(step * tick));

    const svg = svgElement(layout, "svg", {
      viewBox: "0 0 " + series.length + " 90", preserveAspectRatio: "none", role: "img", tabindex: "0",
      "aria-label": "每日" + label + "笔记数。使用方向键查看每日数值。",
    });
    const barWidth = series.length > 30 ? 0.82 : 0.65;
    for (const y of [0, 30, 60, 90]) {
      svgElement(svg, "line", { x1: 0, x2: series.length, y1: y, y2: y, class: "kd-gridline" });
    }
    const highlights = series.map((day, index) => {
      const group = svgElement(svg, "g", {});
      const height = day.count / top * 90;
      svgElement(group, "rect", { x: index + (1 - barWidth) / 2, y: 90 - height,
        width: barWidth, height, class: "kd-bar" });
      const area = svgElement(group, "rect", { x: index, y: 0, width: 1, height: 90, class: "kd-hit" });
      area.addEventListener("pointerenter", () => show(index));
      area.addEventListener("pointerdown", () => show(index));
      return group;
    });
    const labels = element(layout, "div", "kd-x-axis");
    labels.setAttribute("aria-hidden", "true");
    for (const fraction of [0, 1 / 3, 2 / 3, 1]) {
      element(labels, "span", "", SHORT_DATE.format(series[Math.round(fraction * (series.length - 1))].date));
    }
    const caption = element(chart, "p", "kd-caption", "按当前文件时间估算");
    const detail = element(chart, "span", "kd-sr-only");
    detail.setAttribute("role", "status");
    let selected = null;

    function show(index, announce = false) {
      if (selected !== null) highlights[selected].removeAttribute("data-active");
      selected = index;
      highlights[index].setAttribute("data-active", "");
      const day = series[index];
      summary.textContent = SHORT_DATE.format(day.date) + " · " + label + " " + COUNTS.format(day.count) + " 条";
      if (announce) detail.textContent = summary.textContent;
    }
    function clear() {
      if (selected !== null) highlights[selected].removeAttribute("data-active");
      selected = null;
      summary.textContent = "共 " + COUNTS.format(total) + " 条" + label;
    }
    svg.addEventListener("pointerleave", clear);
    svg.addEventListener("blur", clear);
    svg.addEventListener("keydown", event => {
      const index = selected ?? series.length - 1;
      const next = { ArrowLeft: index - 1, ArrowRight: index + 1, Home: 0, End: series.length - 1 }[event.key];
      if (next === undefined) return;
      event.preventDefault();
      show(Math.min(series.length - 1, Math.max(0, next)), true);
    });
    caption.title = "每天汇总仍在库中的笔记。修改序列只记录各文件最后一次修改。";
  }
  draw();
}

function renderComposition(parent, data, state, save) {
  const { section, head } = panel(parent, "知识构成");
  const choices = [["type", "按类型"], ["folder", "按目录"]];
  select(head, "构成分组", choices, state.composition, value => {
    state.composition = value;
    draw();
  });
  const body = element(section, "div", "kd-composition");
  function draw() {
    save();
    body.replaceChildren();
    const composition = computeComposition(data.notes, state.composition);
    if (!composition.length) {
      element(body, "p", "kd-empty", "统计范围内暂无笔记。");
      return;
    }
    const list = element(body, "ul", "kd-breakdown");
    for (const [key, count] of composition) {
      const item = element(list, "li");
      const label = state.composition === "type" ? data.types.get(key) ?? "其他" : key;
      element(item, "span", "kd-breakdown-label", label).title = label;
      const track = element(item, "span", "kd-track");
      track.setAttribute("aria-hidden", "true");
      element(track, "span", "kd-fill").style.width = count / data.notes.length * 100 + "%";
      element(item, "span", "kd-number", COUNTS.format(count));
    }
  }
  draw();
}

function renderHealth(parent, notes, app, config, state, save) {
  const { section } = panel(parent, "知识库健康");
  const checks = element(section, "div", "kd-health-checks");
  const details = element(section, "div", "kd-health-details");
  const status = element(section, "p", "kd-caption", "正在读取链接索引…");
  status.setAttribute("role", "status");
  const rules = config.requiredFieldsByType;
  const { metadataCache } = app;

  function load() {
    if (!section.closest(".kd-dashboard")?.parentElement) return;
    if (!metadataCache.resolvedLinks || !metadataCache.unresolvedLinks) {
      status.textContent = "Obsidian 的链接索引尚未就绪，稍后刷新看板再试。";
      return;
    }
    const health = computeHealth(notes, metadataCache.resolvedLinks, metadataCache.unresolvedLinks, rules);
    status.remove();
    const configured = Object.values(rules).some(keys => keys.length);
    const buttons = new Map();
    for (const [key, label] of Object.entries(HEALTH_LABELS)) {
      const isMissing = key === "missing";
      const check = button(checks, "", () => {
        state.health = state.health === key ? null : key;
        save();
        draw(1);
      }, "kd-health-check");
      check.disabled = isMissing && !configured;
      element(check, "span", "", label);
      const count = isMissing && !configured ? "未配置" : COUNTS.format(health[key].length);
      element(check, "span", "kd-number", count);
      if (key === "unresolved") {
        check.title = COUNTS.format(health.sources) + " 个来源文件，" + count + " 个来源与目标组合";
      }
      buttons.set(key, check);
    }
    draw(1);

    function draw(page, focus) {
      details.replaceChildren();
      const active = state.health;
      for (const [key, check] of buttons) check.setAttribute("aria-expanded", String(key === active));
      if (!active || (active === "missing" && !configured)) return;
      element(details, "h3", "", HEALTH_LABELS[active]);
      if (active === "unresolved") {
        element(details, "p", "kd-caption", COUNTS.format(health.sources) + " 个来源文件 · " +
          COUNTS.format(health.unresolved.length) + " 个来源与目标组合");
      } else if (active === "missing") {
        element(details, "p", "kd-caption", "已检查 " + COUNTS.format(health.checked) + " 条笔记");
      }
      const result = pageOf(health[active], page, 10);
      if (!result.total) {
        element(details, "p", "kd-empty", "当前范围内没有此类笔记。");
        return;
      }
      const list = element(details, "ul", "kd-health-list");
      for (const { note, detail } of result.rows) {
        const item = element(list, "li");
        noteLink(app, item, note.path, note.name, note.path);
        if (detail) element(item, "span", "kd-muted", detail).title = detail;
      }
      pagination(details, result, draw);
      restorePagingFocus(details, focus);
    }
  }

  // Let the activity table paint first. A detached view has no pending work to apply.
  section.ownerDocument.defaultView.requestAnimationFrame(() => setTimeout(load, 0));
}

function readState(container, config) {
  try {
    return JSON.parse(container.dataset.kdState ?? "null") ?? defaultState(config);
  } catch {
    return defaultState(config);
  }
}

function defaultState(config) {
  return {
    activity: { mode: "created", sort: "desc", window: "all", type: "", folder: "", search: "", page: 1, size: config.pageSize },
    trend: { mode: "created", days: config.trendDays },
    composition: "type",
    health: null,
  };
}

async function mount() {
  const { app, container } = dv;
  const root = element(container, "div", "kd-dashboard");
  root.dataset.ui = "";
  const loading = element(root, "p", "kd-empty", "正在读取笔记索引…");
  loading.setAttribute("role", "status");
  const { config, message } = await loadConfig(app.vault);
  if (root.parentElement !== container) return;

  const state = readState(container, config);
  const save = () => { container.dataset.kdState = JSON.stringify(state); };
  const types = new Map(config.typeRules.map(rule => [rule.id, rule.label]));
  types.set("other", "其他");

  function refresh() {
    const now = Date.now();
    const notes = collectNotes(dv.pagePaths(), app.vault, app.metadataCache, config);
    const data = { notes, now, types };
    root.replaceChildren();
    const header = element(root, "header", "kd-header");
    const identity = element(header, "div", "kd-identity");
    const mark = element(identity, "span", "kd-mark");
    mark.setAttribute("aria-hidden", "true");
    const title = element(identity, "div");
    element(title, "h1", "", "知识库看板");
    const stamp = element(title, "p", "kd-muted", "索引读取于 " + CLOCK.format(now));
    stamp.title = EXACT_TIME.format(now);
    const actions = element(header, "div", "kd-actions");
    if (app.vault.getFileByPath(config.allNotesPath)) {
      noteLink(app, actions, config.allNotesPath, "Wiki 总索引");
    }
    button(actions, "刷新", () => {
      update();
      root.querySelector(".kd-refresh")?.focus();
    }, "kd-refresh");
    const notice = element(root, "p", "kd-message", message ?? "");
    notice.setAttribute("role", "status");
    renderOverview(root, notes, now);
    const quick = config.quickLinks.filter(link => app.vault.getFileByPath(link.path));
    if (quick.length) {
      const nav = element(root, "nav", "kd-quick");
      nav.setAttribute("aria-label", "快速入口");
      for (const link of quick) noteLink(app, nav, link.path, link.label);
    }
    const columns = element(root, "div", "kd-columns");
    const main = element(columns, "div", "kd-main");
    renderActivity(main, data, state, save, app);
    const side = element(columns, "div", "kd-side");
    renderTrend(side, data, state, save);
    renderHealth(side, notes, app, config, state, save);
    renderComposition(side, data, state, save);
  }

  function update() {
    try {
      refresh();
    } catch (error) {
      root.replaceChildren();
      element(root, "h1", "", "知识库看板");
      const alert = element(root, "p", "kd-empty", "暂时无法读取索引。Dataview 初始化后可以重试。");
      alert.setAttribute("role", "alert");
      button(root, "重试", update);
      console.error("Knowledge Dashboard", error);
    }
  }
  update();
}

await mount();
