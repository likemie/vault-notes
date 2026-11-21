const { spawn, execFile } = require("node:child_process");
const { createHash } = require("node:crypto");
const { constants, promises: fs } = require("node:fs");
const http = require("node:http");
const { homedir, tmpdir } = require("node:os");
const { join, isAbsolute } = require("node:path");
const {
  HOUR, PROVIDERS, text, percent, timestamp, isoTimestamp, normalizeWindow, antigravityProfileName,
} = require("./model");

const MAX_OUTPUT = 1024 * 1024;
const ANTI_CACHE = join(homedir(), ".antigravity_tools");
const ANTI_DAEMON = join(homedir(), ".gemini", "antigravity", "daemon");
const TOKEN_PATTERN = /^[A-Za-z0-9_-]{6,256}$/;
const ANTI_APPS = new Set([
  "/Applications/Antigravity.app/Contents/Resources/bin/language_server",
  join(homedir(), "Applications/Antigravity.app/Contents/Resources/bin/language_server"),
]);
const LIMIT_METHOD = "account/rateLimits/read";

class SourceError extends Error {
  constructor(status, message) {
    super(message);
    this.status = status;
  }
}

function issue(error) {
  return error instanceof SourceError
    ? { status: error.status, message: error.message }
    : { status: "offline", message: "采集失败，请稍后重试。" };
}

function rpcError(provider, content) {
  const message = text(content?.message, 400).toLowerCase();
  if (content?.code === -32601) return new SourceError("unsupported", "当前客户端缺少额度查询接口。");
  if (content?.code === 401 || /authenticat|unauthoriz|log(?:ged)? in|sign in|login/.test(message)) {
    return new SourceError("auth", "请在 " + PROVIDERS[provider].source + " 中登录订阅账号。");
  }
  return new SourceError("offline", PROVIDERS[provider].source + " 未能返回订阅额度。");
}

function cliDirectories() {
  const base = homedir();
  return [...new Set([
    ...(process.env.PATH ?? "").split(":").filter(isAbsolute),
    join(base, ".local/bin"), join(base, ".grok/bin"), "/opt/homebrew/bin", "/usr/local/bin", "/usr/bin",
  ])];
}

async function executable(bin, provider) {
  for (const dir of cliDirectories()) {
    const path = join(dir, bin);
    try {
      const file = await fs.stat(path);
      if (!file.isFile()) continue;
      await fs.access(path, constants.X_OK);
      return path;
    } catch {}
  }
  throw new SourceError("offline", "找不到 " + PROVIDERS[provider].source + "。");
}

function command(path, args, signal, options = {}) {
  return new Promise((resolve, reject) => {
    execFile(path, args, {
      cwd: tmpdir(), signal, timeout: 5000, maxBuffer: MAX_OUTPUT, ...options,
    }, (error, stdout) => error ? reject(error) : resolve(stdout));
  });
}

function rpc(provider, path, args, initialize, method, signal) {
  return new Promise((resolve, reject) => {
    signal.throwIfAborted();
    const child = spawn(path, args, {
      cwd: tmpdir(), stdio: ["pipe", "pipe", "ignore"],
      // GUI launches can omit the runtime needed by an executable's env shebang.
      env: { ...process.env, PATH: cliDirectories().join(":") },
    });
    const timer = setTimeout(() => finish(new SourceError("offline", "额度查询超时。")), 14_000);
    let pending = "";
    let total = 0;
    let settled = false;
    const onAbort = () => finish(new SourceError("offline", "额度查询已取消。"));

    function finish(error, result) {
      if (settled) return;
      settled = true;
      clearTimeout(timer);
      signal.removeEventListener("abort", onAbort);
      child.stdin.destroy();
      if (child.exitCode === null && child.signalCode === null) child.kill("SIGKILL");
      if (error) reject(error);
      else resolve(result);
    }

    function send(id, name, params) {
      child.stdin.write(JSON.stringify({ jsonrpc: "2.0", id, method: name, params }) + "\n");
    }

    signal.addEventListener("abort", onAbort, { once: true });
    child.on("error", finish);
    child.on("close", () => finish(new SourceError("offline", "额度查询提前结束。")));
    child.stdin.on("error", finish);
    child.stdout.setEncoding("utf8");
    child.stdout.on("data", chunk => {
      total += Buffer.byteLength(chunk);
      if (total > MAX_OUTPUT) return finish(new SourceError("offline", "客户端返回的额度数据过大。"));
      pending += chunk;
      const lines = pending.split("\n");
      pending = lines.pop();
      for (const line of lines) {
        let data;
        try { data = JSON.parse(line); } catch { continue; }
        if (!data || (data.id !== 1 && data.id !== 2)) continue;
        if (data.error) return finish(rpcError(provider, data.error));
        if (data.id === 2) return finish(null, data.result);
        if (provider === "codex") send(undefined, "initialized");
        send(2, method, {});
      }
    });
    send(1, "initialize", initialize);
  });
}

function row(provider, windows, { id = provider, label = "", plan = "", profileName, source = PROVIDERS[provider].source,
  fetchedAt = Date.now(), error } = {}) {
  const clean = windows.flatMap(normalizeWindow);
  return {
    id, label, plan, source, fetchedAt: clean.length ? fetchedAt : null, windows: clean,
    ...(profileName ? { profileName } : {}),
    ...(error ? { issue: error } : {}),
  };
}

function defaultFailure(provider, error) {
  return row(provider, [], { error: issue(error) });
}

function requireReading(windows) {
  if (windows.some(window => window.remaining !== null)) return windows;
  throw new SourceError("unsupported", "客户端没有发布可用的剩余额度。");
}

function minutesLabel(minutes, fallback) {
  if (!Number.isInteger(minutes) || minutes < 1) return fallback;
  if (minutes === 10080) return "每周";
  if (minutes % 1440 === 0) return minutes / 1440 + " 天";
  if (minutes % 60 === 0) return minutes / 60 + " 小时";
  return minutes + " 分钟";
}

function codexWindows(result) {
  const limits = result?.rateLimitsByLimitId?.codex ?? result?.rateLimits;
  if (!limits || (limits.limitId && limits.limitId !== "codex")) {
    throw new SourceError("unsupported", "Codex CLI 没有提供 Codex 订阅窗口。");
  }
  return ["primary", "secondary"].flatMap((id, index) => {
    const quota = limits[id];
    if (!quota) return [];
    const used = percent(quota.usedPercent);
    return [{
      id, name: minutesLabel(quota.windowDurationMins, ["主要窗口", "次要窗口"][index]),
      remaining: used === null ? null : 100 - used, resetAt: timestamp(typeof quota.resetsAt === "number" ? quota.resetsAt * 1000 : null),
    }];
  });
}

async function codex(signal) {
  const path = await executable("codex", "codex");
  const result = await rpc("codex", path, ["app-server", "--listen", "stdio://"], {
    clientInfo: { name: "obsidian-ai-usage", version: "1.0.0" },
  }, LIMIT_METHOD, signal);
  return [row("codex", requireReading(codexWindows(result)))];
}

function grokWindows(result) {
  const plan = text(result?.subscription_tier);
  if (!/^supergrok(?: heavy)?$/i.test(plan)) {
    throw new SourceError("unsupported", "本地 Grok 未确认 SuperGrok 订阅积分。");
  }
  const config = result.config;
  const used = percent(config?.creditUsagePercent);
  const period = config?.currentPeriod;
  const label = {
    USAGE_PERIOD_TYPE_WEEKLY: "每周积分",
    USAGE_PERIOD_TYPE_MONTHLY: "每月积分",
  }[period?.type] ?? "当前周期积分";
  return { plan, windows: [{
    id: "credits", name: label, remaining: used === null ? null : 100 - used,
    resetAt: isoTimestamp(period?.end) ?? isoTimestamp(config?.billingPeriodEnd),
  }] };
}

async function grok(signal) {
  const path = await executable("grok", "grok");
  const result = await rpc("grok", path, ["agent", "stdio"], {
    protocolVersion: "1", clientCapabilities: { fs: { readTextFile: false, writeTextFile: false }, terminal: false },
  }, "_x.ai/billing", signal);
  const { plan, windows } = grokWindows(result);
  const missing = windows[0].remaining === null
    ? { status: "unsupported", message: "Grok 公布了积分周期，剩余积分未知。" } : undefined;
  return [row("grok", windows, { plan, error: missing })];
}

function accountId(email) {
  return createHash("sha256").update(email.toLowerCase().trim()).digest("hex").slice(0, 24);
}

function loopback(port, csrf, method, signal) {
  const body = JSON.stringify({
    metadata: { ideName: "antigravity", extensionName: "antigravity", ideVersion: "unknown", locale: "en" },
  });
  return new Promise((resolve, reject) => {
    const req = http.request({
      hostname: "127.0.0.1", port, agent: false, method: "POST", signal,
      path: "/exa.language_server_pb.LanguageServerService/" + method,
      headers: {
        "Content-Type": "application/json", "Content-Length": Buffer.byteLength(body),
        "Connect-Protocol-Version": "1", "X-Codeium-Csrf-Token": csrf,
      },
    }, response => {
      if (response.statusCode !== 200) {
        response.resume();
        reject(new SourceError(response.statusCode === 401 ? "auth" : "offline", "Antigravity 桌面额度接口暂不可用。"));
        return;
      }
      let size = 0;
      response.on("error", reject);
      const chunks = [];
      response.on("data", chunk => {
        size += chunk.length;
        if (size > MAX_OUTPUT) req.destroy(new Error("Response too large"));
        else chunks.push(chunk);
      });
      response.on("end", () => {
        try { resolve(JSON.parse(Buffer.concat(chunks).toString("utf8"))); } catch (error) { reject(error); }
      });
    });
    req.on("error", reject);
    req.setTimeout(2300, () => req.destroy(new Error("Timeout")));
    req.end(body);
  });
}

async function antigravityProcessIds(signal) {
  if (process.platform !== "darwin") return [];
  try {
    const output = await command("/usr/bin/pgrep", ["-x", "language_server"], signal);
    return output.trim().split(/\s+/).filter(pid => /^\d+$/.test(pid)).slice(0, 12);
  } catch (error) {
    if (error.code === 1 && !signal.aborted) return [];
    throw error;
  }
}

async function desktopDaemonToken(pid, port) {
  let file;
  try {
    file = await fs.open(join(ANTI_DAEMON, `hub_${port}.json`), constants.O_RDONLY | constants.O_NOFOLLOW | constants.O_NONBLOCK);
    const info = await file.stat();
    if (!info.isFile() || info.uid !== process.getuid() || (info.mode & 0o077) !== 0 || info.size > 4096) return null;
    const buffer = Buffer.alloc(4097);
    const { bytesRead } = await file.read(buffer, 0, buffer.length, 0);
    if (bytesRead >= buffer.length) return null;
    const descriptor = JSON.parse(buffer.toString("utf8", 0, bytesRead));
    if (descriptor?.pid !== Number(pid) || descriptor.httpPort !== port) return null;
    return typeof descriptor.csrfToken === "string" && TOKEN_PATTERN.test(descriptor.csrfToken)
      ? descriptor.csrfToken : null;
  } catch {
    return null;
  } finally {
    if (file) await file.close().catch(() => {});
  }
}

async function localAntigravity(pid, signal) {
  const args = await command("/bin/ps", ["-ww", "-p", pid, "-o", "uid=,args="], signal);
  const [uid, invocation] = args.trim().split(/\s+(.*)/s, 2);
  if (uid !== String(process.getuid()) || ![...ANTI_APPS].some(path => invocation?.startsWith(path + " "))) return null;
  const legacyToken = /(?:^|\s)--csrf_token(?:=|\s+)([A-Za-z0-9_-]{6,256})(?=\s|$)/.exec(invocation)?.[1];
  const sockets = await command("/usr/sbin/lsof",
    ["-a", "-nP", "-p", pid, "-iTCP", "-sTCP:LISTEN", "-Fn"], signal);
  const ports = [...sockets.matchAll(/^n127\.0\.0\.1:(\d{1,5})$/gm)].map(match => Number(match[1])).slice(0, 6);
  // Newer desktop builds advertise their HTTP endpoint in a same-user daemon descriptor.
  const listeners = await Promise.all(ports.map(async port => ({ port, csrf: legacyToken ?? await desktopDaemonToken(pid, port) })));
  const targets = listeners.filter(listener => listener.csrf);
  if (!targets.length) {
    throw new SourceError("unsupported", "当前 Antigravity 桌面端未提供可读取的本地额度接口。请在桌面端的 Models & Usage 查看。");
  }
  const answers = await Promise.allSettled(targets.map(async ({ port, csrf }) => {
    const first = (await loopback(port, csrf, "GetUserStatus", signal))?.userStatus;
    const email = text(first?.email);
    if (!email) throw new SourceError("auth", "请在 Antigravity 桌面端登录。");
    let windows = [];
    let error;
    try {
      const payload = await loopback(port, csrf, "RetrieveUserQuotaSummary", signal);
      windows = requireReading(antiWindows(payload));
    } catch (failure) {
      signal.throwIfAborted();
      error = issue(failure);
    }
    const current = (await loopback(port, csrf, "GetUserStatus", signal))?.userStatus;
    if (text(current?.email).toLowerCase() !== email.toLowerCase()) {
      throw new SourceError("offline", "检测到账号切换，请重新刷新。");
    }
    const profileName = [current.displayName, current.name, current.userName,
      [text(current.firstName), text(current.lastName)].filter(Boolean).join(" ")]
      .map(antigravityProfileName).find(Boolean);
    return row("antigravity", windows, {
      id: accountId(email), label: "桌面账号", profileName, plan: text(current.userTier?.name), error,
    });
  }));
  const verified = answers.flatMap(answer => answer.status === "fulfilled" ? [answer.value] : []);
  if (verified.length) return verified.find(account => !account.issue) ?? verified[0];
  const fault = answers.find(answer => answer.status === "rejected" && answer.reason instanceof SourceError);
  throw fault?.reason ?? new SourceError("offline", "无法读取 Antigravity 桌面端额度。");
}

function antiWindows(raw) {
  const payload = raw?.response ?? raw?.summary ?? raw;
  if (!Array.isArray(payload?.groups)) return [];
  return payload.groups.flatMap(group => {
    if (!Array.isArray(group?.buckets)) return [];
    const label = text(group.displayName ?? group.name) || "额度组";
    return group.buckets.flatMap(bucket => {
      const id = text(bucket?.bucketId ?? bucket?.id);
      if (!id || bucket.disabled) return [];
      const value = bucket.remainingFraction ?? bucket.remaining?.remainingFraction
        ?? (bucket.remaining?.case === "remainingFraction" ? bucket.remaining.value : null);
      const remaining = typeof value === "number" ? percent(100 * value) : null;
      const scope = { weekly: "每周", "5h": "5 小时" }[bucket.window]
        ?? (text(bucket.displayName ?? bucket.name) || id);
      return [{ id, name: label + " · " + scope, remaining, resetAt: isoTimestamp(bucket.resetTime) }];
    });
  });
}

async function readJSON(path) {
  const info = await fs.stat(path);
  if (info.size > MAX_OUTPUT || !info.isFile()) throw new Error("Invalid local snapshot");
  const bytes = await fs.readFile(path, "utf8");
  if (Buffer.byteLength(bytes) > MAX_OUTPUT) throw new Error("Invalid local snapshot");
  return JSON.parse(bytes);
}

async function managerAccounts() {
  try {
    const { accounts } = await readJSON(join(ANTI_CACHE, "accounts.json"));
    if (!Array.isArray(accounts)) throw new Error("Invalid account index");
    return accounts.flatMap((account, index) => {
      const email = text(account?.email);
      const fileId = text(account?.id);
      if (!email || !/^[a-f0-9-]{36}$/i.test(fileId)) return [];
      return [{ id: accountId(email), fileId, label: "账号 " + (index + 1), profileName: antigravityProfileName(account.name) }];
    });
  } catch (error) {
    if (error.code === "ENOENT") return [];
    throw error;
  }
}

async function managerSnapshot(account) {
  const provider = "antigravity";
  const options = { id: account.id, label: account.label, profileName: account.profileName, source: "Antigravity Tools 快照" };
  try {
    const data = await readJSON(join(ANTI_CACHE, "accounts", account.fileId + ".json"));
    if (!data?.email || accountId(data.email) !== account.id) throw new Error("Account mismatch");
    const quota = data.quota;
    if (quota?.is_forbidden) {
      return row(provider, [], { ...options, error: { status: "offline", message: "Antigravity Tools 报告无法读取此账号的额度。" } });
    }
    const fetchedAt = timestamp(typeof quota?.last_updated === "number" ? quota.last_updated * 1000 : null);
    const windows = fetchedAt && Array.isArray(quota?.models)
      ? quota.models.flatMap(model => [{
        id: text(model?.name), name: text(model?.display_name) || text(model?.name),
        remaining: percent(model?.percentage), resetAt: isoTimestamp(model?.reset_time),
      }]) : [];
    return row(provider, windows, {
      ...options, fetchedAt, plan: text(quota?.subscription_tier),
      error: windows.length ? undefined : { status: "offline", message: "请在 Antigravity Tools 中刷新此账号的额度。" },
    });
  } catch {
    return row(provider, [], { ...options, error: { status: "offline", message: "此账号的 Antigravity Tools 快照无法读取。" } });
  }
}

async function antigravity(signal, previous, onlyId) {
  const registered = await managerAccounts().catch(() => null);
  const live = [];
  let problem;
  try {
    const pids = await antigravityProcessIds(signal);
    const patients = await Promise.allSettled(pids.map(pid => localAntigravity(pid, signal)));
    for (const answer of patients) {
      if (answer.status === "fulfilled" && answer.value) live.push(answer.value);
      if (answer.status === "rejected") problem = issue(answer.reason);
    }
  } catch (error) {
    problem = issue(error);
  }
  signal.throwIfAborted();
  const byId = new Map();
  for (const account of live) {
    if (!byId.has(account.id) || !account.issue) byId.set(account.id, account);
  }
  const currentId = byId.size === 1 ? live[0].id : null;
  if (!live.length) {
    for (const saved of previous.filter(account => account.source === PROVIDERS.antigravity.source && account.windows.length)) {
      byId.set(saved.id, {
        ...saved,
        issue: problem ?? { status: "offline", message: "打开 Antigravity 桌面端以刷新当前账号。" },
      });
    }
  }
  for (const entry of registered ?? []) {
    if (onlyId && onlyId !== entry.id) continue;
    const known = byId.get(entry.id);
    if (known && !known.issue) continue;
    const snapshot = await managerSnapshot(entry);
    if (!known || (snapshot.fetchedAt ?? 0) > (known.fetchedAt ?? 0)) byId.set(entry.id, snapshot);
  }
  if (registered === null) {
    for (const saved of previous.filter(account => account.source === "Antigravity Tools 快照")) {
      if (!byId.has(saved.id)) byId.set(saved.id, {
        ...saved, issue: { status: "offline", message: "Antigravity Tools 账号索引无法读取。" },
      });
    }
  }
  if (onlyId) {
    const selected = byId.get(onlyId) ?? {
      ...(previous.find(account => account.id === onlyId) ?? row("antigravity", [], { id: onlyId })),
      issue: { status: "offline", message: "无法刷新此账号，当前登录可能已切换。" },
    };
    return { rows: [selected], currentId };
  }
  const rows = [...byId.values()];
  if (!rows.length) {
    rows.push(row("antigravity", [], { error: problem ?? {
      status: "offline", message: "打开并登录 Antigravity 桌面端，或在 Antigravity Tools 中刷新已登记账号。",
    } }));
  }
  return { rows, currentId };
}

async function claude(signal) {
  const path = await executable("claude", "claude");
  const env = Object.fromEntries(Object.entries(process.env).filter(([key]) =>
    !key.startsWith("ANTHROPIC_") && !key.startsWith("CLAUDE_CODE_")));
  const auth = JSON.parse(await command(path, ["auth", "status", "--json"], signal, { env }));
  if (!auth.loggedIn || auth.authMethod !== "claude.ai") {
    throw new SourceError("auth", "请在 Claude Code 中登录 claude.ai 订阅账号。");
  }
  throw new SourceError("offline", "Claude Code 已登录，当前没有可显示的订阅额度。");
}

const collectors = { codex, claude, antigravity, grok };
module.exports = { collectors, issue, defaultFailure, codexWindows, grokWindows, antiWindows };
