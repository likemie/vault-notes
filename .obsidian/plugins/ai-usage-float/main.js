var __getOwnPropNames = Object.getOwnPropertyNames;
var __commonJS = (cb, mod) => function __require() {
  return mod || (0, cb[__getOwnPropNames(cb)[0]])((mod = { exports: {} }).exports, mod), mod.exports;
};

// src/model.js
var require_model = __commonJS({
  "src/model.js"(exports2, module2) {
    var MINUTE2 = 6e4;
    var HOUR = 60 * MINUTE2;
    var PROVIDERS2 = {
      codex: { title: "GPT / Codex", scope: "Codex \u8BA2\u9605", source: "Codex CLI" },
      claude: { title: "Claude", scope: "Claude Code \u8BA2\u9605", source: "Claude Code" },
      antigravity: { title: "Antigravity", scope: "", source: "Antigravity \u684C\u9762\u7AEF" },
      grok: { title: "Grok", scope: "SuperGrok \u79EF\u5206", source: "Grok Build" }
    };
    var KEYS2 = Object.keys(PROVIDERS2);
    var INTERVALS2 = [0, 1, 5, 10, 15, 30];
    var STATUSES = {
      auth: "\u9700\u767B\u5F55",
      unsupported: "\u6765\u6E90\u5F85\u9A8C\u8BC1",
      offline: "\u6682\u4E0D\u53EF\u7528",
      stale: "\u65E7\u6570\u636E"
    };
    var AVAILABLE_SOURCES = /* @__PURE__ */ new Set([...KEYS2.map((id) => PROVIDERS2[id].source), "Antigravity Tools \u5FEB\u7167"]);
    var isObject = (value) => value !== null && typeof value === "object" && !Array.isArray(value);
    var text2 = (value, limit = 100) => typeof value === "string" ? value.trim().slice(0, limit) : "";
    var percent = (value) => typeof value === "number" && Number.isFinite(value) && value >= 0 && value <= 100 ? value : null;
    var timestamp = (value) => Number.isFinite(value) && value > 0 && value < 864e13 ? value : null;
    var isoTimestamp = (value) => typeof value === "string" && /T.*(?:Z|[+-]\d{2}:\d{2})$/i.test(value) ? timestamp(Date.parse(value)) : null;
    var isAntigravityId2 = (id) => typeof id === "string" && /^[a-f0-9]{24}$/.test(id);
    var savedSize = (value) => Number.isFinite(value) && value > 0 ? value : null;
    var antigravityProfileName = (value) => {
      const name = text2(value, 60).replace(/\s+/g, " ");
      return name.includes("@") ? "" : name;
    };
    var dateLabel = new Intl.DateTimeFormat("zh-CN", { month: "numeric", day: "numeric" });
    var timeLabel = new Intl.DateTimeFormat("zh-CN", { hour: "2-digit", minute: "2-digit", hourCycle: "h23" });
    function resetLabel(time, now = Date.now()) {
      if (time === null) return "\u91CD\u7F6E\u65F6\u95F4\u672A\u77E5";
      const day = dateLabel.format(time) === dateLabel.format(now) ? "\u4ECA\u5929" : dateLabel.format(time);
      return day + " " + timeLabel.format(time) + " \u91CD\u7F6E";
    }
    function freshness(time, now = Date.now()) {
      return dateLabel.format(time) === dateLabel.format(now) ? timeLabel.format(time) : dateLabel.format(time) + " " + timeLabel.format(time);
    }
    function settings2(raw) {
      const data = isObject(raw) ? raw : {};
      const names = isObject(data.antigravityNames) ? Object.entries(data.antigravityNames) : [];
      return {
        interval: INTERVALS2.includes(data.interval) ? data.interval : 5,
        pinned: data.pinned === true,
        collapsed: typeof data.collapsed === "boolean" ? data.collapsed : false,
        left: typeof data.left === "number" && Number.isFinite(data.left) ? data.left : null,
        top: typeof data.top === "number" && Number.isFinite(data.top) ? data.top : null,
        width: savedSize(data.width),
        height: savedSize(data.height),
        antigravityNames: Object.fromEntries(names.flatMap(([id, rawName]) => {
          const name = text2(rawName, 60);
          return isAntigravityId2(id) && name ? [[id, name]] : [];
        })),
        enabled: Object.fromEntries(KEYS2.map((id) => [id, data.enabled?.[id] !== false]))
      };
    }
    function accountName2(provider, account, preferences) {
      if (provider !== "antigravity") return account.label;
      return preferences.antigravityNames[account.id] ?? (account.profileName || account.label);
    }
    function geminiWeekly2(row) {
      return row.windows.find((quota) => quota.id === "gemini-weekly");
    }
    function retainAntigravitySnapshots2(current, previous) {
      const saved = new Map(previous.filter((row) => isAntigravityId2(row.id) && row.windows.length).map((row) => [row.id, row]));
      if (!saved.size) return current;
      const stale = (row) => ({
        ...row,
        issue: { status: "offline", message: "\u6B64\u8D26\u53F7\u7684\u989D\u5EA6\u5C1A\u672A\u66F4\u65B0\uFF0C\u663E\u793A\u4E0A\u6B21\u91C7\u96C6\u7684\u5FEB\u7167\u3002" }
      });
      const rows = current.map((row) => {
        const old = saved.get(row.id);
        saved.delete(row.id);
        if (!old) return row;
        const missingWeekly = row.source === "Antigravity Tools \u5FEB\u7167" && geminiWeekly2(old) && !geminiWeekly2(row);
        const latest = missingWeekly || old.fetchedAt > (row.fetchedAt ?? 0) ? stale(old) : row;
        const profileName = row.profileName || old.profileName;
        return profileName && !latest.profileName ? { ...latest, profileName } : latest;
      });
      const remembered = [...rows, ...[...saved.values()].map(stale)];
      return remembered.some((row) => isAntigravityId2(row.id)) ? remembered.filter((row) => row.id !== "antigravity") : remembered;
    }
    function normalizeWindow(raw) {
      if (!isObject(raw)) return [];
      const name = text2(raw.name);
      const id = text2(raw.id);
      const remaining = percent(raw.remaining);
      const resetAt = timestamp(raw.resetAt);
      return id && name && (remaining !== null || resetAt !== null) ? [{ id, name, remaining, resetAt }] : [];
    }
    function cacheFrom2(raw) {
      const stored = isObject(raw?.cache) ? raw.cache : {};
      return Object.fromEntries(KEYS2.map((id) => {
        const accounts = Array.isArray(stored[id]) ? stored[id] : [];
        return [id, accounts.flatMap((row) => {
          if (!isObject(row) || !/^[a-z0-9-]{1,64}$/.test(row.id) || !AVAILABLE_SOURCES.has(row.source) || !Array.isArray(row.windows) || !timestamp(row.fetchedAt)) return [];
          const windows = row.windows.flatMap(normalizeWindow);
          if (!windows.length) return [];
          const profileName = id === "antigravity" ? antigravityProfileName(row.profileName) : "";
          return [{
            id: row.id,
            label: text2(row.label),
            source: row.source,
            plan: text2(row.plan),
            fetchedAt: row.fetchedAt,
            windows,
            ...profileName ? { profileName } : {}
          }];
        })];
      }));
    }
    function accountStatus(row, now, interval) {
      if (row.issue && !row.windows.length) return row.issue.status;
      if (row.issue || row.fetchedAt === null || row.fetchedAt > now + MINUTE2 || now - row.fetchedAt > Math.max(15, interval * 2) * MINUTE2) return "stale";
      return null;
    }
    function usableWindows(row, now, interval) {
      if (accountStatus(row, now, interval)) return [];
      return row.windows.filter((quota) => quota.resetAt === null || quota.resetAt > now);
    }
    function quotaText(value) {
      if (value === null) return "\u2014";
      if (value > 0 && value < 1) return "<1%";
      if (value > 99 && value < 100) return ">99%";
      return Math.round(value) + "%";
    }
    module2.exports = {
      MINUTE: MINUTE2,
      HOUR,
      PROVIDERS: PROVIDERS2,
      KEYS: KEYS2,
      INTERVALS: INTERVALS2,
      STATUSES,
      isObject,
      text: text2,
      percent,
      timestamp,
      isoTimestamp,
      resetLabel,
      freshness,
      settings: settings2,
      cacheFrom: cacheFrom2,
      normalizeWindow,
      accountStatus,
      usableWindows,
      quotaText,
      isAntigravityId: isAntigravityId2,
      antigravityProfileName,
      accountName: accountName2,
      geminiWeekly: geminiWeekly2,
      retainAntigravitySnapshots: retainAntigravitySnapshots2
    };
  }
});

// src/collectors.js
var require_collectors = __commonJS({
  "src/collectors.js"(exports2, module2) {
    var { spawn, execFile } = require("node:child_process");
    var { createHash } = require("node:crypto");
    var { constants, promises: fs } = require("node:fs");
    var http = require("node:http");
    var { homedir, tmpdir } = require("node:os");
    var { join, isAbsolute } = require("node:path");
    var {
      HOUR,
      PROVIDERS: PROVIDERS2,
      text: text2,
      percent,
      timestamp,
      isoTimestamp,
      normalizeWindow,
      antigravityProfileName
    } = require_model();
    var MAX_OUTPUT = 1024 * 1024;
    var ANTI_CACHE = join(homedir(), ".antigravity_tools");
    var ANTI_DAEMON = join(homedir(), ".gemini", "antigravity", "daemon");
    var TOKEN_PATTERN = /^[A-Za-z0-9_-]{6,256}$/;
    var ANTI_APPS = /* @__PURE__ */ new Set([
      "/Applications/Antigravity.app/Contents/Resources/bin/language_server",
      join(homedir(), "Applications/Antigravity.app/Contents/Resources/bin/language_server")
    ]);
    var LIMIT_METHOD = "account/rateLimits/read";
    var SourceError = class extends Error {
      constructor(status, message) {
        super(message);
        this.status = status;
      }
    };
    function issue2(error) {
      return error instanceof SourceError ? { status: error.status, message: error.message } : { status: "offline", message: "\u91C7\u96C6\u5931\u8D25\uFF0C\u8BF7\u7A0D\u540E\u91CD\u8BD5\u3002" };
    }
    function rpcError(provider, content) {
      const message = text2(content?.message, 400).toLowerCase();
      if (content?.code === -32601) return new SourceError("unsupported", "\u5F53\u524D\u5BA2\u6237\u7AEF\u7F3A\u5C11\u989D\u5EA6\u67E5\u8BE2\u63A5\u53E3\u3002");
      if (content?.code === 401 || /authenticat|unauthoriz|log(?:ged)? in|sign in|login/.test(message)) {
        return new SourceError("auth", "\u8BF7\u5728 " + PROVIDERS2[provider].source + " \u4E2D\u767B\u5F55\u8BA2\u9605\u8D26\u53F7\u3002");
      }
      return new SourceError("offline", PROVIDERS2[provider].source + " \u672A\u80FD\u8FD4\u56DE\u8BA2\u9605\u989D\u5EA6\u3002");
    }
    function cliDirectories() {
      const base = homedir();
      return [.../* @__PURE__ */ new Set([
        ...(process.env.PATH ?? "").split(":").filter(isAbsolute),
        join(base, ".local/bin"),
        join(base, ".grok/bin"),
        "/opt/homebrew/bin",
        "/usr/local/bin",
        "/usr/bin"
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
        } catch {
        }
      }
      throw new SourceError("offline", "\u627E\u4E0D\u5230 " + PROVIDERS2[provider].source + "\u3002");
    }
    function command(path, args, signal, options = {}) {
      return new Promise((resolve, reject) => {
        execFile(path, args, {
          cwd: tmpdir(),
          signal,
          timeout: 5e3,
          maxBuffer: MAX_OUTPUT,
          ...options
        }, (error, stdout) => error ? reject(error) : resolve(stdout));
      });
    }
    function rpc(provider, path, args, initialize, method, signal) {
      return new Promise((resolve, reject) => {
        signal.throwIfAborted();
        const child = spawn(path, args, {
          cwd: tmpdir(),
          stdio: ["pipe", "pipe", "ignore"],
          // GUI launches can omit the runtime needed by an executable's env shebang.
          env: { ...process.env, PATH: cliDirectories().join(":") }
        });
        const timer = setTimeout(() => finish(new SourceError("offline", "\u989D\u5EA6\u67E5\u8BE2\u8D85\u65F6\u3002")), 14e3);
        let pending = "";
        let total = 0;
        let settled = false;
        const onAbort = () => finish(new SourceError("offline", "\u989D\u5EA6\u67E5\u8BE2\u5DF2\u53D6\u6D88\u3002"));
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
        child.on("close", () => finish(new SourceError("offline", "\u989D\u5EA6\u67E5\u8BE2\u63D0\u524D\u7ED3\u675F\u3002")));
        child.stdin.on("error", finish);
        child.stdout.setEncoding("utf8");
        child.stdout.on("data", (chunk) => {
          total += Buffer.byteLength(chunk);
          if (total > MAX_OUTPUT) return finish(new SourceError("offline", "\u5BA2\u6237\u7AEF\u8FD4\u56DE\u7684\u989D\u5EA6\u6570\u636E\u8FC7\u5927\u3002"));
          pending += chunk;
          const lines = pending.split("\n");
          pending = lines.pop();
          for (const line of lines) {
            let data;
            try {
              data = JSON.parse(line);
            } catch {
              continue;
            }
            if (!data || data.id !== 1 && data.id !== 2) continue;
            if (data.error) return finish(rpcError(provider, data.error));
            if (data.id === 2) return finish(null, data.result);
            if (provider === "codex") send(void 0, "initialized");
            send(2, method, {});
          }
        });
        send(1, "initialize", initialize);
      });
    }
    function row(provider, windows, {
      id = provider,
      label = "",
      plan = "",
      profileName,
      source = PROVIDERS2[provider].source,
      fetchedAt = Date.now(),
      error
    } = {}) {
      const clean = windows.flatMap(normalizeWindow);
      return {
        id,
        label,
        plan,
        source,
        fetchedAt: clean.length ? fetchedAt : null,
        windows: clean,
        ...profileName ? { profileName } : {},
        ...error ? { issue: error } : {}
      };
    }
    function defaultFailure2(provider, error) {
      return row(provider, [], { error: issue2(error) });
    }
    function requireReading(windows) {
      if (windows.some((window2) => window2.remaining !== null)) return windows;
      throw new SourceError("unsupported", "\u5BA2\u6237\u7AEF\u6CA1\u6709\u53D1\u5E03\u53EF\u7528\u7684\u5269\u4F59\u989D\u5EA6\u3002");
    }
    function minutesLabel(minutes, fallback) {
      if (!Number.isInteger(minutes) || minutes < 1) return fallback;
      if (minutes === 10080) return "\u6BCF\u5468";
      if (minutes % 1440 === 0) return minutes / 1440 + " \u5929";
      if (minutes % 60 === 0) return minutes / 60 + " \u5C0F\u65F6";
      return minutes + " \u5206\u949F";
    }
    function codexWindows(result) {
      const limits = result?.rateLimitsByLimitId?.codex ?? result?.rateLimits;
      if (!limits || limits.limitId && limits.limitId !== "codex") {
        throw new SourceError("unsupported", "Codex CLI \u6CA1\u6709\u63D0\u4F9B Codex \u8BA2\u9605\u7A97\u53E3\u3002");
      }
      return ["primary", "secondary"].flatMap((id, index) => {
        const quota = limits[id];
        if (!quota) return [];
        const used = percent(quota.usedPercent);
        return [{
          id,
          name: minutesLabel(quota.windowDurationMins, ["\u4E3B\u8981\u7A97\u53E3", "\u6B21\u8981\u7A97\u53E3"][index]),
          remaining: used === null ? null : 100 - used,
          resetAt: timestamp(typeof quota.resetsAt === "number" ? quota.resetsAt * 1e3 : null)
        }];
      });
    }
    async function codex(signal) {
      const path = await executable("codex", "codex");
      const result = await rpc("codex", path, ["app-server", "--listen", "stdio://"], {
        clientInfo: { name: "obsidian-ai-usage", version: "1.0.0" }
      }, LIMIT_METHOD, signal);
      return [row("codex", requireReading(codexWindows(result)))];
    }
    function grokWindows(result) {
      const plan = text2(result?.subscription_tier);
      if (!/^supergrok(?: heavy)?$/i.test(plan)) {
        throw new SourceError("unsupported", "\u672C\u5730 Grok \u672A\u786E\u8BA4 SuperGrok \u8BA2\u9605\u79EF\u5206\u3002");
      }
      const config = result.config;
      const used = percent(config?.creditUsagePercent);
      const period = config?.currentPeriod;
      const label = {
        USAGE_PERIOD_TYPE_WEEKLY: "\u6BCF\u5468\u79EF\u5206",
        USAGE_PERIOD_TYPE_MONTHLY: "\u6BCF\u6708\u79EF\u5206"
      }[period?.type] ?? "\u5F53\u524D\u5468\u671F\u79EF\u5206";
      return { plan, windows: [{
        id: "credits",
        name: label,
        remaining: used === null ? null : 100 - used,
        resetAt: isoTimestamp(period?.end) ?? isoTimestamp(config?.billingPeriodEnd)
      }] };
    }
    async function grok(signal) {
      const path = await executable("grok", "grok");
      const result = await rpc("grok", path, ["agent", "stdio"], {
        protocolVersion: "1",
        clientCapabilities: { fs: { readTextFile: false, writeTextFile: false }, terminal: false }
      }, "_x.ai/billing", signal);
      const { plan, windows } = grokWindows(result);
      const missing = windows[0].remaining === null ? { status: "unsupported", message: "Grok \u516C\u5E03\u4E86\u79EF\u5206\u5468\u671F\uFF0C\u5269\u4F59\u79EF\u5206\u672A\u77E5\u3002" } : void 0;
      return [row("grok", windows, { plan, error: missing })];
    }
    function accountId(email) {
      return createHash("sha256").update(email.toLowerCase().trim()).digest("hex").slice(0, 24);
    }
    function loopback(port, csrf, method, signal) {
      const body = JSON.stringify({
        metadata: { ideName: "antigravity", extensionName: "antigravity", ideVersion: "unknown", locale: "en" }
      });
      return new Promise((resolve, reject) => {
        const req = http.request({
          hostname: "127.0.0.1",
          port,
          agent: false,
          method: "POST",
          signal,
          path: "/exa.language_server_pb.LanguageServerService/" + method,
          headers: {
            "Content-Type": "application/json",
            "Content-Length": Buffer.byteLength(body),
            "Connect-Protocol-Version": "1",
            "X-Codeium-Csrf-Token": csrf
          }
        }, (response) => {
          if (response.statusCode !== 200) {
            response.resume();
            reject(new SourceError(response.statusCode === 401 ? "auth" : "offline", "Antigravity \u684C\u9762\u989D\u5EA6\u63A5\u53E3\u6682\u4E0D\u53EF\u7528\u3002"));
            return;
          }
          let size = 0;
          response.on("error", reject);
          const chunks = [];
          response.on("data", (chunk) => {
            size += chunk.length;
            if (size > MAX_OUTPUT) req.destroy(new Error("Response too large"));
            else chunks.push(chunk);
          });
          response.on("end", () => {
            try {
              resolve(JSON.parse(Buffer.concat(chunks).toString("utf8")));
            } catch (error) {
              reject(error);
            }
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
        return output.trim().split(/\s+/).filter((pid) => /^\d+$/.test(pid)).slice(0, 12);
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
        if (!info.isFile() || info.uid !== process.getuid() || (info.mode & 63) !== 0 || info.size > 4096) return null;
        const buffer = Buffer.alloc(4097);
        const { bytesRead } = await file.read(buffer, 0, buffer.length, 0);
        if (bytesRead >= buffer.length) return null;
        const descriptor = JSON.parse(buffer.toString("utf8", 0, bytesRead));
        if (descriptor?.pid !== Number(pid) || descriptor.httpPort !== port) return null;
        return typeof descriptor.csrfToken === "string" && TOKEN_PATTERN.test(descriptor.csrfToken) ? descriptor.csrfToken : null;
      } catch {
        return null;
      } finally {
        if (file) await file.close().catch(() => {
        });
      }
    }
    async function localAntigravity(pid, signal) {
      const args = await command("/bin/ps", ["-ww", "-p", pid, "-o", "uid=,args="], signal);
      const [uid, invocation] = args.trim().split(/\s+(.*)/s, 2);
      if (uid !== String(process.getuid()) || ![...ANTI_APPS].some((path) => invocation?.startsWith(path + " "))) return null;
      const legacyToken = /(?:^|\s)--csrf_token(?:=|\s+)([A-Za-z0-9_-]{6,256})(?=\s|$)/.exec(invocation)?.[1];
      const sockets = await command(
        "/usr/sbin/lsof",
        ["-a", "-nP", "-p", pid, "-iTCP", "-sTCP:LISTEN", "-Fn"],
        signal
      );
      const ports = [...sockets.matchAll(/^n127\.0\.0\.1:(\d{1,5})$/gm)].map((match) => Number(match[1])).slice(0, 6);
      const listeners = await Promise.all(ports.map(async (port) => ({ port, csrf: legacyToken ?? await desktopDaemonToken(pid, port) })));
      const targets = listeners.filter((listener) => listener.csrf);
      if (!targets.length) {
        throw new SourceError("unsupported", "\u5F53\u524D Antigravity \u684C\u9762\u7AEF\u672A\u63D0\u4F9B\u53EF\u8BFB\u53D6\u7684\u672C\u5730\u989D\u5EA6\u63A5\u53E3\u3002\u8BF7\u5728\u684C\u9762\u7AEF\u7684 Models & Usage \u67E5\u770B\u3002");
      }
      const answers = await Promise.allSettled(targets.map(async ({ port, csrf }) => {
        const first = (await loopback(port, csrf, "GetUserStatus", signal))?.userStatus;
        const email = text2(first?.email);
        if (!email) throw new SourceError("auth", "\u8BF7\u5728 Antigravity \u684C\u9762\u7AEF\u767B\u5F55\u3002");
        let windows = [];
        let error;
        try {
          const payload = await loopback(port, csrf, "RetrieveUserQuotaSummary", signal);
          windows = requireReading(antiWindows(payload));
        } catch (failure) {
          signal.throwIfAborted();
          error = issue2(failure);
        }
        const current = (await loopback(port, csrf, "GetUserStatus", signal))?.userStatus;
        if (text2(current?.email).toLowerCase() !== email.toLowerCase()) {
          throw new SourceError("offline", "\u68C0\u6D4B\u5230\u8D26\u53F7\u5207\u6362\uFF0C\u8BF7\u91CD\u65B0\u5237\u65B0\u3002");
        }
        const profileName = [
          current.displayName,
          current.name,
          current.userName,
          [text2(current.firstName), text2(current.lastName)].filter(Boolean).join(" ")
        ].map(antigravityProfileName).find(Boolean);
        return row("antigravity", windows, {
          id: accountId(email),
          label: "\u684C\u9762\u8D26\u53F7",
          profileName,
          plan: text2(current.userTier?.name),
          error
        });
      }));
      const verified = answers.flatMap((answer) => answer.status === "fulfilled" ? [answer.value] : []);
      if (verified.length) return verified.find((account) => !account.issue) ?? verified[0];
      const fault = answers.find((answer) => answer.status === "rejected" && answer.reason instanceof SourceError);
      throw fault?.reason ?? new SourceError("offline", "\u65E0\u6CD5\u8BFB\u53D6 Antigravity \u684C\u9762\u7AEF\u989D\u5EA6\u3002");
    }
    function antiWindows(raw) {
      const payload = raw?.response ?? raw?.summary ?? raw;
      if (!Array.isArray(payload?.groups)) return [];
      return payload.groups.flatMap((group) => {
        if (!Array.isArray(group?.buckets)) return [];
        const label = text2(group.displayName ?? group.name) || "\u989D\u5EA6\u7EC4";
        return group.buckets.flatMap((bucket) => {
          const id = text2(bucket?.bucketId ?? bucket?.id);
          if (!id || bucket.disabled) return [];
          const value = bucket.remainingFraction ?? bucket.remaining?.remainingFraction ?? (bucket.remaining?.case === "remainingFraction" ? bucket.remaining.value : null);
          const remaining = typeof value === "number" ? percent(100 * value) : null;
          const scope = { weekly: "\u6BCF\u5468", "5h": "5 \u5C0F\u65F6" }[bucket.window] ?? (text2(bucket.displayName ?? bucket.name) || id);
          return [{ id, name: label + " \xB7 " + scope, remaining, resetAt: isoTimestamp(bucket.resetTime) }];
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
          const email = text2(account?.email);
          const fileId = text2(account?.id);
          if (!email || !/^[a-f0-9-]{36}$/i.test(fileId)) return [];
          return [{ id: accountId(email), fileId, label: "\u8D26\u53F7 " + (index + 1), profileName: antigravityProfileName(account.name) }];
        });
      } catch (error) {
        if (error.code === "ENOENT") return [];
        throw error;
      }
    }
    async function managerSnapshot(account) {
      const provider = "antigravity";
      const options = { id: account.id, label: account.label, profileName: account.profileName, source: "Antigravity Tools \u5FEB\u7167" };
      try {
        const data = await readJSON(join(ANTI_CACHE, "accounts", account.fileId + ".json"));
        if (!data?.email || accountId(data.email) !== account.id) throw new Error("Account mismatch");
        const quota = data.quota;
        if (quota?.is_forbidden) {
          return row(provider, [], { ...options, error: { status: "offline", message: "Antigravity Tools \u62A5\u544A\u65E0\u6CD5\u8BFB\u53D6\u6B64\u8D26\u53F7\u7684\u989D\u5EA6\u3002" } });
        }
        const fetchedAt = timestamp(typeof quota?.last_updated === "number" ? quota.last_updated * 1e3 : null);
        const windows = fetchedAt && Array.isArray(quota?.models) ? quota.models.flatMap((model) => [{
          id: text2(model?.name),
          name: text2(model?.display_name) || text2(model?.name),
          remaining: percent(model?.percentage),
          resetAt: isoTimestamp(model?.reset_time)
        }]) : [];
        return row(provider, windows, {
          ...options,
          fetchedAt,
          plan: text2(quota?.subscription_tier),
          error: windows.length ? void 0 : { status: "offline", message: "\u8BF7\u5728 Antigravity Tools \u4E2D\u5237\u65B0\u6B64\u8D26\u53F7\u7684\u989D\u5EA6\u3002" }
        });
      } catch {
        return row(provider, [], { ...options, error: { status: "offline", message: "\u6B64\u8D26\u53F7\u7684 Antigravity Tools \u5FEB\u7167\u65E0\u6CD5\u8BFB\u53D6\u3002" } });
      }
    }
    async function antigravity(signal, previous, onlyId) {
      const registered = await managerAccounts().catch(() => null);
      const live = [];
      let problem;
      try {
        const pids = await antigravityProcessIds(signal);
        const patients = await Promise.allSettled(pids.map((pid) => localAntigravity(pid, signal)));
        for (const answer of patients) {
          if (answer.status === "fulfilled" && answer.value) live.push(answer.value);
          if (answer.status === "rejected") problem = issue2(answer.reason);
        }
      } catch (error) {
        problem = issue2(error);
      }
      signal.throwIfAborted();
      const byId = /* @__PURE__ */ new Map();
      for (const account of live) {
        if (!byId.has(account.id) || !account.issue) byId.set(account.id, account);
      }
      const currentId = byId.size === 1 ? live[0].id : null;
      if (!live.length) {
        for (const saved of previous.filter((account) => account.source === PROVIDERS2.antigravity.source && account.windows.length)) {
          byId.set(saved.id, {
            ...saved,
            issue: problem ?? { status: "offline", message: "\u6253\u5F00 Antigravity \u684C\u9762\u7AEF\u4EE5\u5237\u65B0\u5F53\u524D\u8D26\u53F7\u3002" }
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
        for (const saved of previous.filter((account) => account.source === "Antigravity Tools \u5FEB\u7167")) {
          if (!byId.has(saved.id)) byId.set(saved.id, {
            ...saved,
            issue: { status: "offline", message: "Antigravity Tools \u8D26\u53F7\u7D22\u5F15\u65E0\u6CD5\u8BFB\u53D6\u3002" }
          });
        }
      }
      if (onlyId) {
        const selected = byId.get(onlyId) ?? {
          ...previous.find((account) => account.id === onlyId) ?? row("antigravity", [], { id: onlyId }),
          issue: { status: "offline", message: "\u65E0\u6CD5\u5237\u65B0\u6B64\u8D26\u53F7\uFF0C\u5F53\u524D\u767B\u5F55\u53EF\u80FD\u5DF2\u5207\u6362\u3002" }
        };
        return { rows: [selected], currentId };
      }
      const rows = [...byId.values()];
      if (!rows.length) {
        rows.push(row("antigravity", [], { error: problem ?? {
          status: "offline",
          message: "\u6253\u5F00\u5E76\u767B\u5F55 Antigravity \u684C\u9762\u7AEF\uFF0C\u6216\u5728 Antigravity Tools \u4E2D\u5237\u65B0\u5DF2\u767B\u8BB0\u8D26\u53F7\u3002"
        } }));
      }
      return { rows, currentId };
    }
    async function claude(signal) {
      const path = await executable("claude", "claude");
      const env = Object.fromEntries(Object.entries(process.env).filter(([key]) => !key.startsWith("ANTHROPIC_") && !key.startsWith("CLAUDE_CODE_")));
      const auth = JSON.parse(await command(path, ["auth", "status", "--json"], signal, { env }));
      if (!auth.loggedIn || auth.authMethod !== "claude.ai") {
        throw new SourceError("auth", "\u8BF7\u5728 Claude Code \u4E2D\u767B\u5F55 claude.ai \u8BA2\u9605\u8D26\u53F7\u3002");
      }
      throw new SourceError("offline", "Claude Code \u5DF2\u767B\u5F55\uFF0C\u5F53\u524D\u6CA1\u6709\u53EF\u663E\u793A\u7684\u8BA2\u9605\u989D\u5EA6\u3002");
    }
    var collectors2 = { codex, claude, antigravity, grok };
    module2.exports = { collectors: collectors2, issue: issue2, defaultFailure: defaultFailure2, codexWindows, grokWindows, antiWindows };
  }
});

// src/view.js
var require_view = __commonJS({
  "src/view.js"(exports2, module2) {
    var { Modal, setIcon } = require("obsidian");
    var {
      HOUR,
      KEYS: KEYS2,
      PROVIDERS: PROVIDERS2,
      STATUSES,
      resetLabel,
      freshness,
      accountStatus,
      usableWindows,
      quotaText,
      accountName: accountName2,
      isAntigravityId: isAntigravityId2,
      geminiWeekly: geminiWeekly2
    } = require_model();
    var MARGIN = 10;
    var MIN_WIDTH = 240;
    var MIN_HEIGHT = 150;
    var PREVIEW_GAP = 6;
    var LEAVE_DELAY = 160;
    function clamp(value, min, max) {
      return Math.max(min, Math.min(max, value));
    }
    function add(parent, tag, name, value) {
      const node = parent.ownerDocument.createElement(tag);
      if (name) node.className = "auf-" + name;
      if (value !== void 0) node.textContent = value;
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
      const label = busy ? "\u5237\u65B0\u4E2D" : compact ? "\u5237\u65B0\u5F53\u524D Antigravity \u8D26\u53F7" : "\u5237\u65B0\u5F53\u524D\u8D26\u53F7";
      control(parent, label, () => actions.refresh("antigravity"), {
        icon: "refresh-cw",
        iconOnly: compact,
        name: compact ? "icon-button" : "button auf-quiet auf-refresh-current",
        id: "refresh-antigravity",
        disabled: busy
      });
    }
    function track(parent, value, old) {
      if (value === null) return;
      const bar = add(parent, "div", old ? "track auf-track-old" : "track");
      bar.setAttribute("aria-hidden", "true");
      add(bar, "span").style.width = value + "%";
    }
    function rowStatus(row, now, interval) {
      return accountStatus(row, now, interval) ?? (row.windows.length && !usableWindows(row, now, interval).length ? "stale" : null);
    }
    function sourceLine(parent, row, now) {
      const stamp = row.fetchedAt === null ? "" : " \xB7 " + freshness(row.fetchedAt, now) + " \u91C7\u96C6";
      add(parent, "small", "muted", row.source + stamp);
    }
    function quotaWindow(parent, quota, status, now) {
      const cell = add(parent, "div", "quota");
      const heading = add(cell, "div", "quota-line");
      add(heading, "span", "", quota.name);
      const value = add(heading, "strong", "num", quotaText(quota.remaining));
      value.setAttribute("aria-label", quota.remaining === null ? "\u5269\u4F59\u989D\u5EA6\u672A\u77E5" : "\u5269\u4F59 " + quotaText(quota.remaining));
      const expired = quota.resetAt !== null && quota.resetAt <= now;
      track(cell, quota.remaining, status || expired);
      add(cell, "small", "muted", expired ? "\u5DF2\u8FC7\u91CD\u7F6E\u65F6\u95F4 \xB7 " + freshness(quota.resetAt, now) : resetLabel(quota.resetAt, now));
    }
    function allWindows(state) {
      const { rows, settings: settings2, now } = state;
      return KEYS2.filter((id) => settings2.enabled[id]).flatMap(
        (id) => rows[id].flatMap((row) => usableWindows(row, now, settings2.interval).map((quota) => ({ id, row, quota })))
      );
    }
    function minimum(windows) {
      return windows.filter((item) => item.quota.remaining !== null).sort((a, b) => a.quota.remaining - b.quota.remaining)[0];
    }
    function displayAccount(parent, id, account, state, actions) {
      const box = add(parent, "div", "account");
      const head = add(box, "div", "account-head");
      const labels = add(head, "div", "account-label");
      const status = rowStatus(account, state.now, state.settings.interval);
      const name = accountName2(id, account, state.settings);
      if (name) {
        add(labels, "strong", "", [name, account.plan].filter(Boolean).join(" \xB7 "));
      }
      if (status) add(labels, "span", "status", STATUSES[status]);
      sourceLine(labels, account, state.now);
      if (id === "antigravity" && account.id !== id) {
        control(head, account.source === "Antigravity Tools \u5FEB\u7167" ? "\u540C\u6B65\u5FEB\u7167" : "\u5237\u65B0", () => actions.refresh(id, account.id), {
          icon: "refresh-cw",
          name: "button auf-quiet",
          id: account.id,
          disabled: state.busy.has(id)
        });
      }
      if (account.issue) add(box, "p", "muted auf-account-note", account.issue.message);
      if (account.windows.length) {
        const grid = add(box, "div", "quota-grid");
        account.windows.forEach((quota) => quotaWindow(grid, quota, status, state.now));
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
      const title = id === "codex" ? "Codex" : PROVIDERS2[id].title;
      const { section, heading } = compactService(parent, id, title, id === "codex" ? "terminal" : "orbit", subscription?.plan);
      const busy = state.busy.has(id);
      control(heading, busy ? title + " \u5237\u65B0\u4E2D" : "\u5237\u65B0 " + title, () => actions.refresh(id), {
        icon: "refresh-cw",
        iconOnly: true,
        name: "icon-button",
        id: "refresh-" + id,
        disabled: busy
      });
      if (!subscription?.windows.length) {
        add(section, "p", "muted auf-account-note", subscription?.issue?.message || "\u6682\u65E0\u989D\u5EA6\u3002");
        return;
      }
      const status = rowStatus(subscription, state.now, state.settings.interval);
      if (status) {
        add(section, "p", "status auf-account-note", [STATUSES[status], freshness(subscription.fetchedAt, state.now)].join(" \xB7 "));
      }
      const grid = add(section, "div", "quota-grid");
      subscription.windows.forEach((quota) => quotaWindow(grid, quota, status, state.now));
    }
    function displayGeminiWindows(parent, row, state, snapshot = false) {
      const windows = row.windows.filter((quota) => /^gemini(?:$|[-_])/i.test(quota.id));
      if (!windows.length) {
        add(parent, "p", "muted", row.issue?.message || "\u6682\u65E0 Gemini \u989D\u5EA6\u3002");
        return;
      }
      const status = snapshot ? "stale" : rowStatus({ ...row, windows }, state.now, state.settings.interval);
      if (status && !snapshot) {
        add(parent, "p", "status auf-account-note", [STATUSES[status], freshness(row.fetchedAt, state.now)].join(" \xB7 "));
      }
      const grid = add(parent, "div", "quota-grid");
      for (const quota of windows) {
        quotaWindow(grid, { ...quota, name: quota.name.replace(/^Gemini Models · /i, "") }, status, state.now);
      }
    }
    function displayGemini(parent, state, actions, openSnapshots) {
      const { section, heading } = compactService(parent, "antigravity", "Gemini", "sparkles", "Antigravity");
      refreshAntigravity(heading, state, actions, true);
      const accounts = state.rows.antigravity.filter((row) => isAntigravityId2(row.id));
      const current = accounts.find((row) => row.id === state.currentAntigravityId);
      if (current) {
        const account = add(section, "div", "gemini-current");
        const title = add(account, "div", "gemini-account-head");
        add(title, "strong", "", accountName2("antigravity", current, state.settings));
        add(title, "small", "muted", "\u5F53\u524D\u8D26\u53F7");
        displayGeminiWindows(account, current, state);
      } else if (accounts.length) {
        add(section, "p", "muted auf-account-note", "\u5C1A\u672A\u786E\u8BA4\u5F53\u524D\u767B\u5F55\u8D26\u53F7\u3002");
      } else {
        add(section, "p", "empty", state.rows.antigravity[0]?.issue?.message || "\u6682\u65E0 Gemini \u989D\u5EA6\u3002");
      }
      const snapshots = accounts.filter((row) => row !== current);
      if (!snapshots.length) return;
      const snapshotHeading = add(section, "h4", "gemini-snapshot-title");
      add(snapshotHeading, "span", "", "\u8D26\u53F7\u5FEB\u7167");
      add(snapshotHeading, "span", "", "\u6BCF\u5468\u5269\u4F59 \xB7 \u91CD\u7F6E\u65F6\u95F4");
      for (const row of snapshots) {
        const entry = add(section, "details", "gemini-snapshot");
        entry.dataset.aufAccount = row.id;
        entry.open = openSnapshots.has(row.id);
        const summary = add(entry, "summary", "gemini-snapshot-summary");
        summary.dataset.aufFocus = "snapshot-" + row.id;
        const arrow = add(summary, "span", "icon auf-snapshot-arrow");
        arrow.setAttribute("aria-hidden", "true");
        setIcon(arrow, "chevron-right");
        add(summary, "span", "snapshot-name", accountName2("antigravity", row, state.settings));
        const weekly = geminiWeekly2(row);
        const metrics = add(summary, "span", "snapshot-metrics");
        const remaining = weekly?.remaining ?? null;
        const resetAt = weekly?.resetAt ?? null;
        const expired = resetAt !== null && resetAt <= state.now;
        const badge = add(metrics, "strong", "num auf-snapshot-quota", quotaText(remaining));
        if (!expired && remaining !== null) {
          badge.dataset.aufLevel = remaining >= 60 ? "high" : remaining >= 20 ? "medium" : "low";
        }
        const quotaLabel = expired ? "\u4E0A\u6B21\u8BB0\u5F55\u7684\u6BCF\u5468\u5269\u4F59 " : "\u6BCF\u5468\u5269\u4F59 ";
        badge.setAttribute("aria-label", quotaLabel + (remaining === null ? "\u672A\u77E5" : quotaText(remaining)));
        if (resetAt === null) {
          add(metrics, "small", "muted", "\u65F6\u95F4\u672A\u77E5");
        } else {
          const reset = add(metrics, "time", "muted", freshness(resetAt, state.now) + (expired ? " \u5F85\u540C\u6B65" : ""));
          reset.dateTime = new Date(resetAt).toISOString();
          reset.title = expired ? "\u91CD\u7F6E\u65F6\u95F4\u5DF2\u8FC7\uFF0C\u7B49\u5F85\u65B0\u7684\u5468\u989D\u5EA6" : resetLabel(resetAt, state.now);
        }
        const details = add(entry, "div", "snapshot-windows");
        displayGeminiWindows(details, row, state, true);
        if (row.fetchedAt !== null) add(details, "small", "muted auf-snapshot-captured", "\u91C7\u96C6\u4E8E " + freshness(row.fetchedAt, state.now));
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
        const next = [...root.querySelectorAll("[data-auf-focus]")].find((node) => node.dataset.aufFocus === key);
        next?.focus({ preventScroll: true });
      }
    }
    var Dashboard2 = class extends Modal {
      constructor(app, actions) {
        super(app);
        this.actions = actions;
        this.modalEl.addClass("auf-modal");
        this.setTitle("\u989D\u5EA6\u7528\u91CF");
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
          const clock = state.lastRefresh ? "\u6700\u8FD1\u67E5\u8BE2 " + freshness(state.lastRefresh, state.now) : "\u7B49\u5F85\u91C7\u96C6";
          add(toolbar, "span", "muted", clock + " \xB7 \u672C\u5730\u65F6\u95F4");
          control(toolbar, state.busy.size ? "\u5237\u65B0\u4E2D" : "\u5237\u65B0\u5168\u90E8", () => this.actions.refresh(), {
            icon: "refresh-cw",
            name: "button auf-primary",
            disabled: Boolean(state.busy.size),
            id: "refresh-all"
          });
          const layout = add(root, "div", "dashboard-grid");
          const services = card(layout, "\u670D\u52A1\u989D\u5EA6", "\u767E\u5206\u6BD4\u4E3A\u5269\u4F59\u91CF");
          const ids = KEYS2.filter((id) => state.settings.enabled[id]);
          for (const id of ids) {
            const provider = PROVIDERS2[id];
            const section = add(services, "section", "service");
            const head = add(section, "header", "service-head");
            add(head, "h4", "", provider.title);
            const registered = state.rows[id].filter((row) => row.id !== id);
            const plan = id === "antigravity" && registered.length ? registered.length + " \u4E2A\u8D26\u53F7" : id === "grok" && state.rows[id][0]?.plan ? state.rows[id][0].plan + " \u79EF\u5206" : provider.scope;
            if (plan) add(head, "small", "muted", plan);
            if (id === "antigravity") refreshAntigravity(head, state, this.actions);
            state.rows[id].forEach((row) => displayAccount(section, id, row, state, this.actions));
          }
          if (!ids.length) add(services, "p", "empty", "\u8BF7\u5728\u8BBE\u7F6E\u4E2D\u542F\u7528\u8981\u67E5\u770B\u7684\u670D\u52A1\u3002");
          const right = add(layout, "div", "right");
          const windows = allWindows(state);
          const low = minimum(windows);
          const priority = card(right, "\u5F53\u524D\u6700\u4F4E\u989D\u5EA6");
          const readout = add(priority, "div", "readout");
          if (low) {
            add(readout, "div", "priority-value", quotaText(low.quota.remaining));
            add(
              readout,
              "div",
              "context",
              [PROVIDERS2[low.id].title, accountName2(low.id, low.row, state.settings), low.quota.name].filter(Boolean).join(" \xB7 ")
            );
            add(readout, "small", "muted", resetLabel(low.quota.resetAt, state.now));
            track(readout, low.quota.remaining, false);
          } else {
            add(readout, "p", "muted", "\u6682\u65E0\u53EF\u6BD4\u8F83\u7684\u989D\u5EA6\u3002");
          }
          const resets = card(right, "\u5373\u5C06\u91CD\u7F6E", "\u672A\u6765 24 \u5C0F\u65F6");
          const soon = windows.filter(({ quota }) => quota.resetAt !== null && quota.resetAt <= state.now + 24 * HOUR).sort((a, b) => a.quota.resetAt - b.quota.resetAt);
          if (soon.length) {
            const list = add(resets, "ol", "resets");
            for (const { id, row, quota } of soon) {
              const item = add(list, "li");
              const label = add(item, "div");
              add(label, "div", "", PROVIDERS2[id].title);
              add(label, "small", "muted", [accountName2(id, row, state.settings), quota.name].filter(Boolean).join(" \xB7 "));
              add(item, "time", "num", freshness(quota.resetAt, state.now)).dateTime = new Date(quota.resetAt).toISOString();
            }
          } else {
            add(resets, "p", "empty", "\u6682\u65E0\u5DF2\u77E5\u91CD\u7F6E\u3002");
          }
        });
      }
      onClose() {
        this.contentEl.replaceChildren();
      }
    };
    var FloatingPanel2 = class {
      constructor(win, actions) {
        this.win = win;
        this.actions = actions;
        this.events = new AbortController();
        this.root = add(win.document.body, "aside", "float");
        this.root.id = "auf-floating-panel";
        this.root.hidden = true;
        this.root.setAttribute("aria-label", "\u989D\u5EA6\u7528\u91CF");
        this.launcher = control(win.document.body, "\u989D\u5EA6", actions.toggle, { name: "launcher", icon: "chart-no-axes-column" });
        this.launcher.setAttribute("aria-controls", this.root.id);
        this.header = add(this.root, "header", "float-head");
        this.handle = add(this.header, "div", "handle", "\u989D\u5EA6\u7528\u91CF");
        this.buttons = add(this.header, "div", "head-buttons");
        this.body = add(this.root, "div", "float-body");
        this.footer = add(this.root, "footer", "float-foot");
        this.footer.setAttribute("role", "status");
        this.footer.setAttribute("aria-live", "polite");
        this.grips = [this.resizeGrip("left"), this.resizeGrip("right")];
        this.place = this.place.bind(this);
        this.bindPointer(this.handle, (bounds) => (dx, dy) => this.move(bounds.left + dx, bounds.top + dy));
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
        this.handle.title = pinned ? "\u62D6\u52A8\u6D6E\u7A97" : "";
        this.body.hidden = this.footer.hidden = collapsed;
        this.grips.forEach((grip) => {
          grip.hidden = !pinned || collapsed;
        });
        const scroll = this.body.scrollTop;
        preserveFocus(this.root, () => {
          this.buttons.replaceChildren();
          control(this.buttons, "\u6253\u5F00\u989D\u5EA6\u603B\u89C8", this.actions.dashboard, {
            icon: "panel-top",
            iconOnly: true,
            name: "icon-button",
            id: "dashboard"
          });
          if (pinned) {
            control(this.buttons, collapsed ? "\u5C55\u5F00\u6D6E\u7A97" : "\u6298\u53E0\u6D6E\u7A97", this.actions.collapse, {
              icon: collapsed ? "chevron-down" : "minus",
              iconOnly: true,
              name: "icon-button",
              id: "collapse"
            }).setAttribute("aria-expanded", String(!collapsed));
            control(this.buttons, "\u9690\u85CF\u6D6E\u7A97", () => this.dismiss(), { icon: "x", iconOnly: true, name: "icon-button", id: "hide" });
          }
          if (collapsed) return;
          const openSnapshots = /* @__PURE__ */ new Set();
          if (this.currentAntigravityId === state.currentAntigravityId) {
            for (const entry of this.body.querySelectorAll(".auf-gemini-snapshot[open]")) openSnapshots.add(entry.dataset.aufAccount);
          }
          this.currentAntigravityId = state.currentAntigravityId;
          this.body.replaceChildren();
          const ids = ["codex", "grok", "antigravity"].filter((id) => state.settings.enabled[id]);
          for (const id of ids) {
            if (id === "antigravity") displayGemini(this.body, state, this.actions, openSnapshots);
            else displayCompactSubscription(this.body, id, state, this.actions);
          }
          if (!ids.length) add(this.body, "p", "empty", "\u8BF7\u5728\u8BBE\u7F6E\u4E2D\u542F\u7528\u8981\u67E5\u770B\u7684\u670D\u52A1\u3002");
          this.body.scrollTop = scroll;
          this.footer.textContent = ids.some((id) => state.busy.has(id)) ? "\u6B63\u5728\u67E5\u8BE2\u989D\u5EA6\u2026" : "\u767E\u5206\u6BD4\u4E3A\u5269\u4F59\u989D\u5EA6";
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
        this.launcher.title = pinned ? "\u53D6\u6D88\u56FA\u5B9A\u989D\u5EA6\u6D6E\u7A97" : "\u60AC\u505C\u67E5\u770B\u989D\u5EA6\uFF0C\u70B9\u51FB\u56FA\u5B9A";
        if (restoreFocus) this.launcher.focus({ preventScroll: true });
      }
      clearPreviewTimer() {
        this.win.clearTimeout(this.leaveTimer);
        this.leaveTimer = void 0;
      }
      dismiss() {
        this.clearPreviewTimer();
        this.preview = false;
        if (this.actions.state().settings.pinned) this.actions.hide();
        else this.updateVisibility();
      }
      listenForPreview() {
        const { signal } = this.events;
        this.launcher.addEventListener("pointerenter", (event) => {
          if (event.pointerType !== "mouse") return;
          this.clearPreviewTimer();
          this.preview = true;
          this.updateVisibility();
          this.place();
        }, { signal });
        this.root.addEventListener("pointerenter", (event) => {
          if (event.pointerType === "mouse") this.clearPreviewTimer();
        }, { signal });
        for (const region of [this.launcher, this.root]) {
          region.addEventListener("pointerleave", (event) => {
            if (event.pointerType !== "mouse") return;
            this.clearPreviewTimer();
            this.leaveTimer = this.win.setTimeout(() => {
              this.preview = false;
              this.updateVisibility();
            }, LEAVE_DELAY);
          }, { signal });
          region.addEventListener("keydown", (event) => {
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
        const corner = side === "left" ? "\u5DE6\u4E0B\u89D2" : "\u53F3\u4E0B\u89D2";
        grip.type = "button";
        grip.setAttribute("aria-label", "\u4ECE" + corner + "\u8C03\u6574\u6D6E\u7A97\u5927\u5C0F");
        grip.title = "\u62D6\u52A8\u6216\u6309\u65B9\u5411\u952E\u8C03\u6574\u6D6E\u7A97\u5927\u5C0F";
        this.bindPointer(grip, (bounds) => (dx, dy) => this.resizeFrom(side, bounds, dx, dy));
        grip.addEventListener("keydown", (event) => {
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
        handle.addEventListener("pointerdown", (event) => {
          if (event.button !== 0 || this.gesture || !this.actions.state().settings.pinned) return;
          this.gesture = {
            id: event.pointerId,
            x: event.clientX,
            y: event.clientY,
            patch: null,
            update: begin(this.root.getBoundingClientRect())
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
        this.win.addEventListener("pointermove", (event) => {
          const drag = this.gesture;
          if (drag?.id !== event.pointerId) return;
          if (!event.buttons) {
            finish();
            return;
          }
          drag.patch = drag.update(event.clientX - drag.x, event.clientY - drag.y);
        }, options);
        for (const name of ["pointerup", "pointercancel"]) {
          this.win.addEventListener(name, (event) => {
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
    };
    module2.exports = { Dashboard: Dashboard2, FloatingPanel: FloatingPanel2 };
  }
});

// src/main.js
var { Notice, Plugin, PluginSettingTab, Setting } = require("obsidian");
var {
  KEYS,
  PROVIDERS,
  MINUTE,
  INTERVALS,
  cacheFrom,
  settings,
  text,
  isAntigravityId,
  accountName,
  retainAntigravitySnapshots,
  geminiWeekly
} = require_model();
var { collectors, issue, defaultFailure } = require_collectors();
var { Dashboard, FloatingPanel } = require_view();
var UsageSettings = class extends PluginSettingTab {
  constructor(app, plugin) {
    super(app, plugin);
    this.plugin = plugin;
  }
  display() {
    const { containerEl, plugin } = this;
    containerEl.empty();
    new Setting(containerEl).setName("\u56FA\u5B9A\u989D\u5EA6\u6D6E\u7A97").setDesc("\u56FA\u5B9A\u540E\uFF0C\u9F20\u6807\u79FB\u5F00\u65F6\u4ECD\u53EF\u67E5\u770B\u548C\u8C03\u6574\u6D6E\u7A97\u3002").addToggle((control) => control.setValue(plugin.preferences.pinned).onChange((value) => plugin.configure({ pinned: value })));
    new Setting(containerEl).setName("\u81EA\u52A8\u5237\u65B0").setDesc("\u9047\u5230\u91C7\u96C6\u5931\u8D25\u65F6\u5EF6\u957F\u81EA\u52A8\u91CD\u8BD5\u95F4\u9694\u3002\u624B\u52A8\u5237\u65B0\u53EF\u968F\u65F6\u91CD\u8BD5\u3002").addDropdown((control) => {
      for (const interval of INTERVALS) control.addOption(String(interval), interval ? interval + " \u5206\u949F" : "\u4EC5\u624B\u52A8");
      control.setValue(String(plugin.preferences.interval)).onChange((value) => plugin.configure({ interval: Number(value) }));
    });
    new Setting(containerEl).setName("\u76D1\u63A7\u670D\u52A1").setHeading();
    for (const provider of KEYS) {
      const { title, scope } = PROVIDERS[provider];
      new Setting(containerEl).setName(title).setDesc(scope || "\u663E\u793A\u5DF2\u9A8C\u8BC1\u7684\u684C\u9762\u8D26\u53F7\u53CA Antigravity Tools \u6CE8\u518C\u8D26\u53F7\u7684\u672C\u5730\u5FEB\u7167\u3002").addToggle((control) => control.setValue(plugin.preferences.enabled[provider]).onChange((value) => plugin.enableProvider(provider, value)));
    }
    new Setting(containerEl).setName("\u91CD\u7F6E\u6D6E\u7A97\u4F4D\u7F6E").addButton((button) => button.setButtonText("\u91CD\u7F6E\u4F4D\u7F6E").onClick(() => plugin.configure({ left: null, top: null })));
    new Setting(containerEl).setName("\u91CD\u7F6E\u6D6E\u7A97\u5927\u5C0F").addButton((button) => button.setButtonText("\u6062\u590D\u9ED8\u8BA4\u5927\u5C0F").onClick(() => plugin.configure({ width: null, height: null })));
    const accounts = plugin.rows.antigravity.filter((row) => isAntigravityId(row.id));
    if (accounts.length) {
      new Setting(containerEl).setName("Antigravity \u8D26\u53F7\u540D\u79F0").setHeading();
      for (const row of accounts) {
        new Setting(containerEl).setName(accountName("antigravity", row, plugin.preferences)).setDesc(row.source).addText((input) => input.setPlaceholder(row.profileName || row.label).setValue(plugin.preferences.antigravityNames[row.id] ?? "").onChange((value) => plugin.nameAntigravityAccount(row.id, value)));
      }
    }
  }
};
var UsageFloatPlugin = class extends Plugin {
  async onload() {
    const saved = await this.loadData();
    this.preferences = settings(saved?.preferences);
    const cache = cacheFrom(saved);
    this.rows = Object.fromEntries(KEYS.map((id) => [
      id,
      cache[id].length ? cache[id].map((row) => ({ ...row, issue: { status: "offline", message: "\u7B49\u5F85\u672C\u6B21\u91C7\u96C6\u3002" } })) : [defaultFailure(id, new Error())]
    ]));
    for (const id of KEYS) {
      if (!cache[id].length) this.rows[id][0].issue.message = "\u7B49\u5F85\u9996\u6B21\u91C7\u96C6\u3002";
    }
    this.lifetime = new AbortController();
    this.busy = /* @__PURE__ */ new Map();
    this.due = /* @__PURE__ */ new Map();
    this.writes = Promise.resolve();
    this.lastRefresh = null;
    this.currentAntigravityId = null;
    this.actions = {
      state: () => this.state(),
      dashboard: () => this.openDashboard(),
      toggle: () => this.toggle(),
      refresh: (id, account) => void this.refreshFromControl(id, account),
      collapse: () => this.configure({ collapsed: !this.preferences.collapsed }),
      hide: () => this.configure({ pinned: false }),
      geometry: (patch) => this.configure(patch)
    };
    this.addSettingTab(new UsageSettings(this.app, this));
    this.addRibbonIcon("chart-no-axes-column", "\u663E\u793A\u6216\u9690\u85CF\u989D\u5EA6\u6D6E\u7A97", () => this.toggle());
    this.addCommand({ id: "toggle", name: "\u663E\u793A\u6216\u9690\u85CF\u989D\u5EA6\u6D6E\u7A97", callback: () => this.toggle() });
    this.addCommand({ id: "dashboard", name: "\u6253\u5F00\u989D\u5EA6\u603B\u89C8", callback: this.actions.dashboard });
    this.addCommand({ id: "refresh", name: "\u5237\u65B0\u8BA2\u9605\u989D\u5EA6", callback: () => void this.refreshFromControl() });
    this.app.workspace.onLayoutReady(() => {
      if (this.lifetime.signal.aborted) return;
      this.panel = new FloatingPanel(window, this.actions);
      this.render();
      if (this.preferences.interval) void this.refresh();
      this.registerInterval(window.setInterval(() => this.tick(), 3e4));
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
      settings: this.preferences,
      rows: this.rows,
      busy: this.busy,
      lastRefresh: this.lastRefresh,
      currentAntigravityId: this.currentAntigravityId,
      now: Date.now()
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
    const now = Date.now();
    for (const id of KEYS) {
      const due = this.due.get(id);
      const weekReset = id === "antigravity" && due && this.rows[id].some((row) => {
        const resetAt = geminiWeekly(row)?.resetAt;
        return resetAt > due.checkedAt && resetAt <= now;
      });
      if (now >= (due?.at ?? 0) || weekReset) void this.refresh(id);
    }
  }
  async refresh(onlyProvider, accountId) {
    const selected = onlyProvider ? [onlyProvider] : KEYS;
    await Promise.all(selected.filter((id) => this.preferences.enabled[id]).map((id) => this.refreshProvider(id, accountId)));
  }
  async refreshFromControl(onlyProvider, accountId) {
    const id = onlyProvider ?? "antigravity";
    if (!this.preferences.enabled[id]) return this.refresh(onlyProvider, accountId);
    const title = id === "codex" ? "Codex" : PROVIDERS[id].title;
    if (this.busy.has(id)) {
      new Notice(title + " \u6B63\u5728\u67E5\u8BE2\u989D\u5EA6\u3002");
      return;
    }
    const previous = new Map(this.rows[id].map((row) => [row.id, row.fetchedAt]));
    await this.refresh(onlyProvider, accountId);
    if (this.lifetime.signal.aborted || !this.preferences.enabled[id]) return;
    const rows = this.rows[id].filter((row) => !accountId || row.id === accountId);
    if (rows.some((row) => !row.issue && row.fetchedAt > (previous.get(row.id) ?? 0))) {
      new Notice(title + " \u989D\u5EA6\u5DF2\u66F4\u65B0\u3002");
      return;
    }
    const reason = rows.find((row) => row.issue)?.issue?.message;
    const summary = title + (rows.some((row) => row.windows.length) ? " \u4FDD\u7559\u4E86\u4E0A\u6B21\u5FEB\u7167\u3002" : " \u672A\u53D6\u5F97\u989D\u5EA6\u3002");
    new Notice([summary, reason].filter(Boolean).join("\n"), 7e3);
  }
  async refreshProvider(id, accountId) {
    if (this.busy.has(id) || this.lifetime.signal.aborted) return;
    const controller = new AbortController();
    const { signal } = controller;
    const checkedAt = Date.now();
    this.busy.set(id, controller);
    this.render();
    const prior = this.rows[id];
    let failed = false;
    try {
      const reading = await collectors[id](signal, prior, accountId);
      if (signal.aborted) return;
      const fresh = id === "antigravity" ? reading.rows : reading;
      const byId = new Map(prior.map((row) => [row.id, row]));
      const merged = fresh.map((row) => {
        const last = byId.get(row.id);
        if (last?.windows.some((window2) => window2.remaining !== null) && row.issue && !row.windows.some((window2) => window2.remaining !== null)) {
          return { ...last, issue: row.issue };
        }
        return row;
      });
      const resolved = id === "antigravity" ? retainAntigravitySnapshots(merged, accountId ? prior.filter((row) => row.id === accountId) : prior) : merged;
      failed = resolved.every((row) => row.issue || !row.windows.length);
      this.rows[id] = accountId ? prior.map((row) => row.id === accountId ? resolved[0] ?? row : row) : resolved;
      if (id === "antigravity") this.currentAntigravityId = reading.currentId;
    } catch (error) {
      if (signal.aborted) return;
      if (id === "antigravity") this.currentAntigravityId = null;
      failed = true;
      this.rows[id] = prior.map((row) => !accountId || row.id === accountId ? { ...row, issue: issue(error) } : row);
    } finally {
      this.busy.delete(id);
      if (!this.lifetime.signal.aborted) {
        if (!signal.aborted) {
          const previous = this.due.get(id);
          const misses = failed ? Math.min((previous?.misses ?? 0) + 1, 3) : 0;
          this.due.set(id, {
            misses,
            at: Date.now() + Math.max(1, this.preferences.interval) * 2 ** misses * MINUTE,
            checkedAt: accountId ? previous?.checkedAt ?? 0 : checkedAt
          });
          this.lastRefresh = Date.now();
          this.persist();
        }
        this.render();
      }
    }
  }
  persist() {
    const cache = Object.fromEntries(KEYS.map((id) => [id, this.rows[id].filter((row) => row.windows.length && row.fetchedAt !== null).map(({ issue: _issue, ...row }) => row)]));
    const data = { preferences: this.preferences, cache };
    this.writes = this.writes.then(() => this.saveData(data)).catch(() => {
      console.warn("AI Usage Float: could not save local preferences and quota snapshots");
    });
  }
};
module.exports = UsageFloatPlugin;
