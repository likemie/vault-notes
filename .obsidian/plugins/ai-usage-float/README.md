# AI Usage Float

Obsidian 桌面版额度悬浮窗。MyNotes 已启用此插件。点击窗口右侧的「额度」按钮可打开或隐藏浮窗。拖动浮窗标题可移动位置，拖动任一底角可调整大小。点击某行可展开对应的额度窗口，点击标题栏的面板图标可打开额度总览。位置、大小、折叠状态和刷新间隔会保存。

安装到另一个 vault 时，将 `manifest.json`、`main.js` 和 `styles.css` 复制到该 vault 的 `.obsidian/plugins/ai-usage-float/`，然后在「设置 → 第三方插件」启用 AI Usage Float。当前采集器在 macOS 上核验。构建命令为 `npm ci && npm run build`。

## 本机核验记录

| 服务 | 本机结果 | 看板所用来源 |
| --- | --- | --- |
| Codex | Codex CLI 0.133.0 返回 5 小时与每周窗口，两者均含使用百分比和重置时间。 | `codex app-server --listen stdio://` 的 `account/rateLimits/read`。 |
| Claude Code | Claude Code 2.1.272 的原生 claude.ai 登录状态为 Pro。两次交互式 `/usage` 查询都返回限流。 | 通过 `claude auth status --json` 确认登录。订阅额度显示为暂不可用。 |
| Antigravity | 桌面版 2.33.0 和 2.34.0 均已读取到已登录账号的 Gemini 和 Claude/GPT 额度。 | 桌面端本地 `RetrieveUserQuotaSummary`，用 `GetUserStatus` 在查询前后确认账号。2.34.0 通过本机服务登记文件定位已运行的桌面服务。 |
| SuperGrok | Grok Build 1.0.88 的 ACP 返回 `SuperGrok` 计划、每周积分使用百分比和周期结束时间。 | `grok agent stdio` 的 `_x.ai/billing`。看板只展示明确归属 SuperGrok 的积分窗口。 |

已运行的 Antigravity 桌面端提供当前账号数据。其他已在 Antigravity Tools 注册的账号，可以在 Tools 中刷新各自的额度，再在看板点击「同步快照」。同一账号出现在两个来源时，看板使用桌面端的实时查询结果。刷新失败会保留上次可用快照并标明状态。旧快照与已到重置时间的窗口不计入当前最低额度和即将重置列表。

刷新时会读取当前登录账号的显示名，并按账号保存额度快照。在插件设置的「Antigravity 账号名称」里可设置优先显示的名称。

点击 Antigravity 旁的「刷新当前账号」，即可从正在运行的桌面端确认登录账号并更新对应的额度。定时刷新执行同样的检查。切换账号或刷新失败时，其他已有账号仍保留最近的快照。

插件在本机保留窗口数值、重置时间、来源、采集时间及设置。插件数据文件不保存原始账号邮箱、登录凭据或客户端响应正文。

采集协议参考 [CodexBar](https://github.com/steipete/CodexBar/tree/1f6da9b/docs) 和 [Antigravity Manager](https://github.com/lbjlaq/Antigravity-Manager/tree/9b82fb7/src-tauri/src/models)。
