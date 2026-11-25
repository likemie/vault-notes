const MINUTE = 60_000;
const HOUR = 60 * MINUTE;
const PROVIDERS = {
  codex: { title: "GPT / Codex", scope: "Codex 订阅", source: "Codex CLI" },
  claude: { title: "Claude", scope: "Claude Code 订阅", source: "Claude Code" },
  antigravity: { title: "Antigravity", scope: "", source: "Antigravity 桌面端" },
  grok: { title: "Grok", scope: "SuperGrok 积分", source: "Grok Build" },
};
const KEYS = Object.keys(PROVIDERS);
const INTERVALS = [0, 1, 5, 10, 15, 30];
const STATUSES = {
  auth: "需登录",
  unsupported: "来源待验证",
  offline: "暂不可用",
  stale: "旧数据",
};
const AVAILABLE_SOURCES = new Set([...KEYS.map(id => PROVIDERS[id].source), "Antigravity Tools 快照"]);
const isObject = value => value !== null && typeof value === "object" && !Array.isArray(value);
const text = (value, limit = 100) => typeof value === "string" ? value.trim().slice(0, limit) : "";
const percent = value => typeof value === "number" && Number.isFinite(value) && value >= 0 && value <= 100 ? value : null;
const timestamp = value => Number.isFinite(value) && value > 0 && value < 8.64e15 ? value : null;
const isoTimestamp = value => typeof value === "string" && /T.*(?:Z|[+-]\d{2}:\d{2})$/i.test(value) ? timestamp(Date.parse(value)) : null;
const isAntigravityId = id => typeof id === "string" && /^[a-f0-9]{24}$/.test(id);
const savedSize = value => Number.isFinite(value) && value > 0 ? value : null;
const antigravityProfileName = value => {
  const name = text(value, 60).replace(/\s+/g, " ");
  return name.includes("@") ? "" : name;
};
const dateFormatter = new Intl.DateTimeFormat("zh-CN", { month: "numeric", day: "numeric" });
const timeLabel = new Intl.DateTimeFormat("zh-CN", { hour: "2-digit", minute: "2-digit", hourCycle: "h23" });

function dateLabel(time) {
  return dateFormatter.format(time);
}

function resetLabel(time, now = Date.now()) {
  if (time === null) return "重置时间未知";
  const date = dateLabel(time);
  const day = date === dateLabel(now) ? "今天" : date;
  return day + " " + timeLabel.format(time) + " 重置";
}

function freshness(time, now = Date.now()) {
  const date = dateLabel(time);
  return date === dateLabel(now) ? timeLabel.format(time) : date + " " + timeLabel.format(time);
}

function settings(raw) {
  const data = isObject(raw) ? raw : {};
  const names = isObject(data.antigravityNames) ? Object.entries(data.antigravityNames) : [];
  return {
    interval: INTERVALS.includes(data.interval) ? data.interval : 5,
    pinned: data.pinned === true,
    collapsed: typeof data.collapsed === "boolean" ? data.collapsed : false,
    left: typeof data.left === "number" && Number.isFinite(data.left) ? data.left : null,
    top: typeof data.top === "number" && Number.isFinite(data.top) ? data.top : null,
    width: savedSize(data.width),
    height: savedSize(data.height),
    antigravityNames: Object.fromEntries(names.flatMap(([id, rawName]) => {
      const name = text(rawName, 60);
      return isAntigravityId(id) && name ? [[id, name]] : [];
    })),
    enabled: Object.fromEntries(KEYS.map(id => [id, data.enabled?.[id] !== false])),
  };
}

function accountName(provider, account, preferences) {
  if (provider !== "antigravity") return account.label;
  return preferences.antigravityNames[account.id] ?? (account.profileName || account.label);
}

function geminiWeekly(row) {
  return row.windows.find(quota => quota.id === "gemini-weekly");
}

function retainAntigravitySnapshots(current, previous) {
  const saved = new Map(previous.filter(row => isAntigravityId(row.id) && row.windows.length).map(row => [row.id, row]));
  if (!saved.size) return current;
  const stale = row => ({
    ...row,
    issue: { status: "offline", message: "此账号的额度尚未更新，显示上次采集的快照。" },
  });
  const rows = current.map(row => {
    const old = saved.get(row.id);
    saved.delete(row.id);
    if (!old) return row;
    const missingWeekly = row.source === "Antigravity Tools 快照" && geminiWeekly(old) && !geminiWeekly(row);
    const latest = missingWeekly || old.fetchedAt > (row.fetchedAt ?? 0) ? stale(old) : row;
    const profileName = row.profileName || old.profileName;
    return profileName && !latest.profileName ? { ...latest, profileName } : latest;
  });
  const remembered = [...rows, ...[...saved.values()].map(stale)];
  return remembered.some(row => isAntigravityId(row.id))
    ? remembered.filter(row => row.id !== "antigravity") : remembered;
}

function normalizeWindow(raw) {
  if (!isObject(raw)) return [];
  const name = text(raw.name);
  const id = text(raw.id);
  const remaining = percent(raw.remaining);
  const resetAt = timestamp(raw.resetAt);
  return id && name && (remaining !== null || resetAt !== null) ? [{ id, name, remaining, resetAt }] : [];
}

function cacheFrom(raw) {
  const stored = isObject(raw?.cache) ? raw.cache : {};
  return Object.fromEntries(KEYS.map(id => {
    const accounts = Array.isArray(stored[id]) ? stored[id] : [];
    return [id, accounts.flatMap(row => {
      if (!isObject(row) || !/^[a-z0-9-]{1,64}$/.test(row.id) || !AVAILABLE_SOURCES.has(row.source)
          || !Array.isArray(row.windows) || !timestamp(row.fetchedAt)) return [];
      const windows = row.windows.flatMap(normalizeWindow);
      if (!windows.length) return [];
      const profileName = id === "antigravity" ? antigravityProfileName(row.profileName) : "";
      return [{
        id: row.id, label: text(row.label), source: row.source, plan: text(row.plan),
        fetchedAt: row.fetchedAt, windows, ...(profileName ? { profileName } : {}),
      }];
    })];
  }));
}

function accountStatus(row, now, interval) {
  if (row.issue && !row.windows.length) return row.issue.status;
  if (row.issue || row.fetchedAt === null || row.fetchedAt > now + MINUTE || now - row.fetchedAt > Math.max(15, interval * 2) * MINUTE) return "stale";
  return null;
}

function usableWindows(row, now, interval) {
  if (accountStatus(row, now, interval)) return [];
  return row.windows.filter(quota => quota.resetAt === null || quota.resetAt > now);
}

function quotaText(value) {
  if (value === null) return "—";
  if (value > 0 && value < 1) return "<1%";
  if (value > 99 && value < 100) return ">99%";
  return Math.round(value) + "%";
}

module.exports = {
  MINUTE, HOUR, PROVIDERS, KEYS, INTERVALS, STATUSES, isObject, text, percent, timestamp, isoTimestamp,
  dateLabel, resetLabel, freshness, settings, cacheFrom, normalizeWindow, accountStatus, usableWindows, quotaText,
  isAntigravityId, antigravityProfileName, accountName, geminiWeekly, retainAntigravitySnapshots,
};
