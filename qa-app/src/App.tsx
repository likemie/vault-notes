import { FormEvent, useEffect, useRef, useState } from 'react';
import { MarkdownView } from './MarkdownView';

interface HealthInfo {
  ok: boolean;
  indexCount: number;
  typeCounts: Record<string, number>;
  storeConfigured: boolean;
  apiKeyConfigured: boolean;
  authRequired: boolean;
  quartzBaseUrl: string | null;
  defaultModel: string;
}

interface IndexEntry {
  title: string;
  type: string;
  path: string;
  aliases: string[];
  score?: number;
  quartzUrl?: string;
}

interface CitationItem {
  title: string;
  uri?: string;
  textSnippet?: string;
  entryPath?: string;
  entryType?: string;
  quartzUrl?: string;
}

interface WebSourceItem {
  title: string;
  uri: string;
}

interface ChatMessage {
  id: string;
  role: 'user' | 'model';
  text: string;
  mode?: 'file-search' | 'local-preview' | 'index-only';
  model?: string;
  usedIndexQueries?: Array<{ query: string; type?: string; hitCount: number }>;
  indexMatches?: IndexEntry[];
  citations?: CitationItem[];
  webSupplement?: string;
  webSources?: WebSourceItem[];
  webSearchQueries?: string[];
  error?: boolean;
}

const TYPE_OPTIONS = [
  { value: '', label: '全部类型' },
  { value: 'concept', label: '概念 Concept' },
  { value: 'theory', label: '理论 Theory' },
  { value: 'argument', label: '论证 Argument' },
  { value: 'fact', label: '事实 Fact' },
  { value: 'method', label: '方法 Method' },
  { value: 'instrument', label: '工具 Instrument' },
  { value: 'person', label: '人物 Person' },
];

const STARTER_PROMPTS = [
  {
    tag: '概念与论证',
    text: '“再情境化（Recontextualization）”在知识库中有哪些核心界定与代表文献？',
  },
  {
    tag: '方法论批评',
    text: '知识库里对 John Hattie《Visible Learning》元分析方法有哪些主要学术批评？',
  },
  {
    tag: '跨国比较',
    text: '对比新加坡、芬兰与新西兰在课程改革或教育评估方面的关键事实与研究发现。',
  },
];

const MODEL_OPTIONS = [
  { value: 'gemini-3.8-flash', label: 'Gemini 3.8 Flash（快速低耗）' },
  { value: 'gemini-pro-latest', label: 'Gemini Pro Latest（深度综合）' },
  { value: 'gemini-flash-latest', label: 'Gemini Flash Latest' },
  { value: 'gemini-3.1-pro-preview', label: 'Gemini 3.1 Pro Preview' },
];

const OUTPUT_MODE_OPTIONS = [
  { value: 'qa', label: '常规研究问答' },
  { value: 'synthesis', label: '文献综合 / 写作底稿' },
  { value: 'report', label: '主题 / 政策报告' },
  { value: 'ppt', label: 'PPT 叙事结构' },
];

export default function App() {
  const [health, setHealth] = useState<HealthInfo | null>(null);
  const [password, setPassword] = useState(() => localStorage.getItem('qa_password') || '');
  const [unlocked, setUnlocked] = useState(false);
  const [authError, setAuthError] = useState('');

  const [typeFilter, setTypeFilter] = useState('');
  const [model, setModel] = useState('gemini-3.8-flash');
  const [outputMode, setOutputMode] = useState('qa');
  const [allowWebSearch, setAllowWebSearch] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const [indexQuery, setIndexQuery] = useState('');
  const [indexResults, setIndexResults] = useState<IndexEntry[]>([]);
  const [indexLoading, setIndexLoading] = useState(false);

  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState('');
  const [sending, setSending] = useState(false);

  const [previewEntry, setPreviewEntry] = useState<(IndexEntry & { content?: string | null }) | null>(
    null,
  );
  const messagesEndRef = useRef<HTMLDivElement | null>(null);

  function authHeaders(): Record<string, string> {
    return password ? { 'x-access-password': password } : {};
  }

  useEffect(() => {
    fetch('/api/health')
      .then((r) => r.json())
      .then((data: HealthInfo) => {
        setHealth(data);
        if (data.defaultModel) setModel(data.defaultModel);
        if (!data.authRequired) {
          setUnlocked(true);
        } else if (password) {
          verifyStoredPassword(password);
        }
      })
      .catch(() => {
        setHealth(null);
      });
  }, []);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, sending]);

  async function verifyStoredPassword(pw: string) {
    const res = await fetch('/api/auth/verify', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ password: pw }),
    });
    if (res.ok) {
      localStorage.setItem('qa_password', pw);
      setUnlocked(true);
      setAuthError('');
    } else {
      setUnlocked(false);
      setAuthError('访问密码不正确');
    }
  }

  async function handleUnlock(e: FormEvent) {
    e.preventDefault();
    await verifyStoredPassword(password);
  }

  useEffect(() => {
    if (!unlocked) return;
    const trimmed = indexQuery.trim();
    if (!trimmed && !typeFilter) {
      setIndexResults([]);
      return;
    }
    const timer = setTimeout(async () => {
      setIndexLoading(true);
      try {
        const params = new URLSearchParams({ q: trimmed, limit: '20' });
        if (typeFilter) params.set('type', typeFilter);
        const res = await fetch(`/api/index/search?${params.toString()}`, {
          headers: authHeaders(),
        });
        if (res.ok) {
          const data = await res.json();
          setIndexResults(data.results || []);
        }
      } finally {
        setIndexLoading(false);
      }
    }, 180);
    return () => clearTimeout(timer);
  }, [indexQuery, typeFilter, unlocked]);

  async function openEntryPreview(entryPath: string) {
    const res = await fetch(`/api/entry?path=${encodeURIComponent(entryPath)}`, {
      headers: authHeaders(),
    });
    if (res.ok) {
      const data = await res.json();
      setPreviewEntry(data);
    }
  }

  async function handleWikilinkClick(target: string) {
    const params = new URLSearchParams({ q: target, limit: '5' });
    const res = await fetch(`/api/index/search?${params.toString()}`, {
      headers: authHeaders(),
    });
    if (res.ok) {
      const data = await res.json();
      const first = (data.results || [])[0] as IndexEntry | undefined;
      if (first) {
        await openEntryPreview(first.path);
        return;
      }
    }
    setIndexQuery(target);
    setSidebarOpen(true);
  }

  async function sendQuestion(questionText: string) {
    const trimmed = questionText.trim();
    if (!trimmed || sending) return;

    const userMsg: ChatMessage = {
      id: `${Date.now()}-u`,
      role: 'user',
      text: trimmed,
    };
    const nextHistory = messages
      .filter((m) => !m.error)
      .map((m) => ({ role: m.role, text: m.text }));

    setMessages((prev) => [...prev, userMsg]);
    setInput('');
    setSending(true);

    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...authHeaders(),
        },
        body: JSON.stringify({
          message: trimmed,
          history: nextHistory,
          typeFilter: typeFilter || undefined,
          model,
          outputMode,
          allowWebSearch,
        }),
      });

      const data = await res.json();
      if (!res.ok) {
        throw new Error(data.error || '请求失败');
      }

      const modelMsg: ChatMessage = {
        id: `${Date.now()}-m`,
        role: 'model',
        text: data.answer,
        mode: data.mode,
        model: data.model,
        usedIndexQueries: data.usedIndexQueries,
        indexMatches: data.indexMatches,
        citations: data.citations,
        webSupplement: data.webSupplement,
        webSources: data.webSources,
        webSearchQueries: data.webSearchQueries,
      };
      setMessages((prev) => [...prev, modelMsg]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          id: `${Date.now()}-e`,
          role: 'model',
          text: err instanceof Error ? err.message : '请求失败，请检查后端日志或 API Key 配置。',
          error: true,
        },
      ]);
    } finally {
      setSending(false);
    }
  }

  if (health?.authRequired && !unlocked) {
    return (
      <div className="auth-shell">
        <form className="auth-card" onSubmit={handleUnlock}>
          <div className="auth-badge">学术研究知识库</div>
          <h1>AI 问答与证据检索助手</h1>
          <p>当前独立应用已启用访问密码保护，请输入密码以进入检索界面。</p>
          <input
            type="password"
            placeholder="请输入访问密码"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            autoFocus
          />
          {authError && <div className="error-text">{authError}</div>}
          <button type="submit">验证并进入</button>
        </form>
      </div>
    );
  }

  const currentModeLabel =
    OUTPUT_MODE_OPTIONS.find((m) => m.value === outputMode)?.label ?? '常规研究问答';

  return (
    <div className="layout">
      {sidebarOpen && (
        <div className="sidebar-backdrop" onClick={() => setSidebarOpen(false)} />
      )}

      <aside className={`sidebar ${sidebarOpen ? 'is-open' : ''}`}>
        <div className="brand">
          <div className="brand-top">
            <span className="brand-mark">Wiki</span>
            <div>
              <div className="brand-title">教育研究知识库助手</div>
              <div className="brand-sub">
                {health ? `${health.indexCount.toLocaleString()} 条规范索引` : '正在连接后端…'}
              </div>
            </div>
          </div>

          {health && (
            <div className="status-badges">
              <span className={`badge ${health.storeConfigured ? 'ok' : 'warn'}`}>
                <span className="dot" />
                {health.storeConfigured ? 'File Search 已连接' : '本地预览 / 未绑 Store'}
              </span>
              {!health.apiKeyConfigured && (
                <span className="badge err">未配置 GEMINI_API_KEY</span>
              )}
            </div>
          )}
        </div>

        <div className="controls-grid">
          <div className="panel-section">
            <label className="field-label">推理模型</label>
            <select value={model} onChange={(e) => setModel(e.target.value)}>
              {MODEL_OPTIONS.map((opt) => (
                <option key={opt.value} value={opt.value}>
                  {opt.label}
                </option>
              ))}
            </select>
          </div>

          <div className="panel-section">
            <label className="field-label">回答组织模式（Vault Use）</label>
            <select value={outputMode} onChange={(e) => setOutputMode(e.target.value)}>
              {OUTPUT_MODE_OPTIONS.map((opt) => (
                <option key={opt.value} value={opt.value}>
                  {opt.label}
                </option>
              ))}
            </select>
          </div>

          <div className="panel-section">
            <label className="field-label">限定条目类型</label>
            <select value={typeFilter} onChange={(e) => setTypeFilter(e.target.value)}>
              {TYPE_OPTIONS.map((opt) => (
                <option key={opt.value} value={opt.value}>
                  {opt.label}
                  {opt.value && health?.typeCounts[opt.value]
                    ? ` (${health.typeCounts[opt.value]})`
                    : ''}
                </option>
              ))}
            </select>
          </div>
        </div>

        <div className="panel-section index-box">
          <div className="field-header">
            <label className="field-label">直查 wiki/index.json</label>
            {indexResults.length > 0 && (
              <span className="count-pill">{indexResults.length} 项</span>
            )}
          </div>
          <input
            type="search"
            placeholder="搜中英文术语、别名或人名…"
            value={indexQuery}
            onChange={(e) => setIndexQuery(e.target.value)}
          />
          <div className="index-list">
            {indexLoading && <div className="muted">正在检索索引…</div>}
            {!indexLoading && !indexQuery.trim() && !typeFilter && (
              <div className="muted tip-box">
                输入中文术语（如“再情境化”）、英文缩写或学者姓名，可实时定位条目并预览详情。
              </div>
            )}
            {!indexLoading && indexResults.length === 0 && (indexQuery.trim() || typeFilter) && (
              <div className="muted">未找到匹配标题或别名</div>
            )}
            {indexResults.map((item) => (
              <div key={item.path} className="index-item">
                <div className="index-item-head">
                  <span className={`type-pill type-${item.type}`}>{item.type}</span>
                  <button
                    type="button"
                    className="link-btn"
                    onClick={() => openEntryPreview(item.path)}
                    title={item.path}
                  >
                    {item.title}
                  </button>
                </div>
                {item.aliases.length > 0 && (
                  <div className="alias-line">{item.aliases.slice(0, 3).join(' · ')}</div>
                )}
              </div>
            ))}
          </div>
        </div>
      </aside>

      <main className="main">
        <header className="topbar">
          <div className="topbar-left">
            <button
              type="button"
              className="menu-btn"
              onClick={() => setSidebarOpen(true)}
              aria-label="打开索引侧栏"
            >
              ☰ 索引与设置
            </button>
            <div className="topbar-chips">
              <span className="topbar-chip">模式：{currentModeLabel}</span>
              {typeFilter && <span className="topbar-chip accent">类型：{typeFilter}</span>}
              {allowWebSearch && <span className="topbar-chip web">已启用联网补充</span>}
            </div>
          </div>
          <div className="topbar-right">
            {health?.quartzBaseUrl && (
              <a
                href={health.quartzBaseUrl}
                target="_blank"
                rel="noreferrer"
                className="ghost-link"
              >
                知识库主页 ↗
              </a>
            )}
            {messages.length > 0 && (
              <button
                type="button"
                className="ghost-btn"
                onClick={() => setMessages([])}
                disabled={sending}
              >
                清空对话
              </button>
            )}
          </div>
        </header>

        <div className="messages">
          {messages.length === 0 ? (
            <div className="empty-state">
              <div className="empty-eyebrow">Vault Use 规范驱动 · 证据可溯源</div>
              <h2>教育研究维基知识库问答台</h2>
              <p>
                系统默认严格限定在你的 <strong>{health?.indexCount.toLocaleString() ?? '5,600+'}</strong>{' '}
                条知识条目内检索作答，自动调用 <code>wiki/index.json</code> 解析双语术语，并遵循《Vault
                Use》的论证综合与 APA 引用规范。如需补充外部最新动态，可在下方开启“允许联网补充”。
              </p>
              <div className="starters">
                {STARTER_PROMPTS.map((q) => (
                  <button
                    key={q.text}
                    type="button"
                    className="starter-btn"
                    onClick={() => sendQuestion(q.text)}
                  >
                    <span className="starter-tag">{q.tag}</span>
                    <span className="starter-text">{q.text}</span>
                  </button>
                ))}
              </div>
            </div>
          ) : (
            messages.map((msg) => (
              <article key={msg.id} className={`msg ${msg.role} ${msg.error ? 'is-error' : ''}`}>
                <div className="msg-role">
                  <span className="msg-author">
                    {msg.role === 'user' ? '研究提问' : '知识库综合回答'}
                  </span>
                  <div className="msg-tags">
                    {msg.model && <span className="mode-tag">{msg.model}</span>}
                    {msg.mode && (
                      <span className="mode-tag">
                        {msg.mode === 'file-search'
                          ? 'File Search'
                          : msg.mode === 'local-preview'
                            ? '本地预览'
                            : '仅索引'}
                      </span>
                    )}
                  </div>
                </div>

                <div className="msg-body">
                  {msg.role === 'user' || msg.error ? (
                    <div className="plain-text">{msg.text}</div>
                  ) : (
                    <MarkdownView text={msg.text} onWikilinkClick={handleWikilinkClick} />
                  )}
                </div>

                {msg.webSupplement && (
                  <section className="web-supplement-box">
                    <div className="web-supplement-header">
                      <span className="web-badge">外部联网补充 · 非知识库来源</span>
                      {msg.webSearchQueries && msg.webSearchQueries.length > 0 && (
                        <span className="web-queries">
                          搜索词：{msg.webSearchQueries.join(' / ')}
                        </span>
                      )}
                    </div>
                    <div className="web-supplement-body">
                      <MarkdownView text={msg.webSupplement} />
                    </div>
                    {msg.webSources && msg.webSources.length > 0 && (
                      <div className="web-sources-list">
                        {msg.webSources.map((ws, idx) => (
                          <a
                            key={idx}
                            href={ws.uri}
                            target="_blank"
                            rel="noreferrer"
                            className="web-source-chip"
                          >
                            {ws.title} ↗
                          </a>
                        ))}
                      </div>
                    )}
                  </section>
                )}

                {msg.usedIndexQueries && msg.usedIndexQueries.length > 0 && (
                  <details className="meta-details">
                    <summary>
                      索引工具检索记录（{msg.usedIndexQueries.length} 次查询，命中{' '}
                      {msg.indexMatches?.length ?? 0} 个候选条目）
                    </summary>
                    <ul className="meta-list">
                      {msg.usedIndexQueries.map((q, idx) => (
                        <li key={idx}>
                          <code>{q.query}</code>
                          {q.type ? ` [${q.type}]` : ''} → {q.hitCount} 条
                        </li>
                      ))}
                    </ul>
                    {msg.indexMatches && msg.indexMatches.length > 0 && (
                      <div className="chip-row">
                        {msg.indexMatches.map((m) => (
                          <button
                            key={m.path}
                            type="button"
                            className="ref-chip"
                            onClick={() => openEntryPreview(m.path)}
                          >
                            <span className={`type-pill type-${m.type}`}>{m.type}</span>
                            {m.title}
                          </button>
                        ))}
                      </div>
                    )}
                  </details>
                )}

                {msg.citations && msg.citations.length > 0 && (
                  <details className="meta-details" open>
                    <summary>知识库引用来源（{msg.citations.length}）</summary>
                    <div className="citation-list">
                      {msg.citations.map((c, idx) => (
                        <div key={idx} className="citation-card">
                          <div className="citation-head">
                            {c.entryType && (
                              <span className={`type-pill type-${c.entryType}`}>{c.entryType}</span>
                            )}
                            {c.entryPath ? (
                              <button
                                type="button"
                                className="link-btn"
                                onClick={() => openEntryPreview(c.entryPath!)}
                              >
                                {c.title}
                              </button>
                            ) : (
                              <strong>{c.title}</strong>
                            )}
                            {c.quartzUrl && (
                              <a
                                href={c.quartzUrl}
                                target="_blank"
                                rel="noreferrer"
                                className="quartz-link"
                              >
                                打开站点页面 ↗
                              </a>
                            )}
                          </div>
                          {c.entryPath && <div className="path-line">{c.entryPath}</div>}
                          {c.textSnippet && <div className="snippet-line">{c.textSnippet}</div>}
                        </div>
                      ))}
                    </div>
                  </details>
                )}
              </article>
            ))
          )}
          {sending && (
            <div className="msg model loading">
              <span className="spinner" />
              <span>
                正在依次检索 <code>wiki/index.json</code> 与知识库条目
                {allowWebSearch ? '，并补充外部联网搜索…' : '…'}
              </span>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        <form
          className="composer-wrap"
          onSubmit={(e) => {
            e.preventDefault();
            sendQuestion(input);
          }}
        >
          <div className="composer-toolbar">
            <label className={`web-toggle ${allowWebSearch ? 'active' : ''}`}>
              <input
                type="checkbox"
                checked={allowWebSearch}
                onChange={(e) => setAllowWebSearch(e.target.checked)}
              />
              <span className="toggle-track">
                <span className="toggle-thumb" />
              </span>
              <span>允许联网补充外部信息（Google Search）</span>
            </label>
            <span className="composer-hint">
              {allowWebSearch
                ? '已开启：外部网页结果将单独标注，不混入库内引用'
                : '默认关闭：仅依据自有知识库作答'}
            </span>
          </div>

          <div className="composer">
            <textarea
              rows={2}
              placeholder="输入研究问题（支持中英文术语，Enter 发送，Shift+Enter 换行）…"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === 'Enter' && !e.shiftKey) {
                  e.preventDefault();
                  sendQuestion(input);
                }
              }}
            />
            <button type="submit" disabled={sending || !input.trim()}>
              {sending ? '检索中…' : '发送提问'}
            </button>
          </div>
        </form>
      </main>

      {previewEntry && (
        <div className="modal-backdrop" onClick={() => setPreviewEntry(null)}>
          <div className="modal-card" onClick={(e) => e.stopPropagation()}>
            <div className="modal-head">
              <div>
                <span className={`type-pill type-${previewEntry.type}`}>{previewEntry.type}</span>
                <h3>{previewEntry.title}</h3>
                <div className="path-line">{previewEntry.path}</div>
              </div>
              <div className="modal-actions">
                {previewEntry.quartzUrl && (
                  <a
                    href={previewEntry.quartzUrl}
                    target="_blank"
                    rel="noreferrer"
                    className="quartz-link"
                  >
                    在 Quartz 打开 ↗
                  </a>
                )}
                <button type="button" onClick={() => setPreviewEntry(null)}>
                  关闭
                </button>
              </div>
            </div>
            {previewEntry.aliases?.length > 0 && (
              <div className="alias-box">别名：{previewEntry.aliases.join(' · ')}</div>
            )}
            <pre className="entry-content">
              {previewEntry.content ??
                '当前为云端容器模式（未挂载本地 wiki/ 原文件目录），请点击右上角“在 Quartz 打开 ↗”或直接让 AI 结合 File Search 检索解读该条目。'}
            </pre>
            <div className="modal-foot">
              <button
                type="button"
                onClick={() => {
                  const title = previewEntry.title;
                  setPreviewEntry(null);
                  sendQuestion(`请系统梳理知识库条目《${title}》的核心内容、相关文献论证与主要争议。`);
                }}
              >
                让 AI 解读该条目
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
