import { FormEvent, useEffect, useState } from 'react';

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

interface ChatMessage {
  id: string;
  role: 'user' | 'model';
  text: string;
  mode?: 'file-search' | 'local-preview' | 'index-only';
  model?: string;
  usedIndexQueries?: Array<{ query: string; type?: string; hitCount: number }>;
  indexMatches?: IndexEntry[];
  citations?: CitationItem[];
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
  '“再情境化（Recontextualization）”在知识库中有哪些核心界定与代表文献？',
  '知识库里对 John Hattie《Visible Learning》元分析方法有哪些主要学术批评？',
  '对比新加坡、芬兰与新西兰在课程改革或教育评估方面的关键事实与研究发现。',
];

const MODEL_OPTIONS = [
  { value: 'gemini-3.8-flash', label: 'Gemini 3.8 Flash（快且省额度）' },
  { value: 'gemini-pro-latest', label: 'Gemini Pro Latest（复杂综合）' },
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

  const [indexQuery, setIndexQuery] = useState('');
  const [indexResults, setIndexResults] = useState<IndexEntry[]>([]);
  const [indexLoading, setIndexLoading] = useState(false);

  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState('');
  const [sending, setSending] = useState(false);

  const [previewEntry, setPreviewEntry] = useState<(IndexEntry & { content?: string | null }) | null>(
    null,
  );

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
          <h1>教育研究知识库 · AI 助手</h1>
          <p>该独立知识库应用已启用访问密码保护。</p>
          <input
            type="password"
            placeholder="请输入访问密码"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            autoFocus
          />
          {authError && <div className="error-text">{authError}</div>}
          <button type="submit">进入知识库</button>
        </form>
      </div>
    );
  }

  return (
    <div className="layout">
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-title">学术知识库问答助手</div>
          <div className="brand-sub">
            {health ? `已载入 ${health.indexCount.toLocaleString()} 条索引` : '正在连接服务…'}
          </div>
          {health && (
            <div className="status-badges">
              <span className={`badge ${health.storeConfigured ? 'ok' : 'warn'}`}>
                {health.storeConfigured ? 'File Search 已连接' : '本地预览 / 未绑 Store'}
              </span>
              {!health.apiKeyConfigured && (
                <span className="badge err">未配置 GEMINI_API_KEY</span>
              )}
            </div>
          )}
        </div>

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

        <div className="panel-section index-box">
          <label className="field-label">直查 wiki/index.json</label>
          <input
            type="search"
            placeholder="输入中英文术语、别名或人名…"
            value={indexQuery}
            onChange={(e) => setIndexQuery(e.target.value)}
          />
          <div className="index-list">
            {indexLoading && <div className="muted">检索索引中…</div>}
            {!indexLoading && indexResults.length === 0 && indexQuery.trim() && (
              <div className="muted">未找到匹配标题或别名</div>
            )}
            {indexResults.map((item) => (
              <div key={item.path} className="index-item">
                <div className="index-item-head">
                  <span className="type-pill">{item.type}</span>
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
        <div className="messages">
          {messages.length === 0 ? (
            <div className="empty-state">
              <h2>基于你的教育研究维基库提问</h2>
              <p>
                每次提问会先调用 <code>wiki/index.json</code> 解析中英文术语与别名，再通过 Gemini
                File Search 检索知识条目原文并返回出处。
              </p>
              <div className="starters">
                {STARTER_PROMPTS.map((q) => (
                  <button
                    key={q}
                    type="button"
                    className="starter-btn"
                    onClick={() => sendQuestion(q)}
                  >
                    {q}
                  </button>
                ))}
              </div>
            </div>
          ) : (
            messages.map((msg) => (
              <div key={msg.id} className={`msg ${msg.role} ${msg.error ? 'is-error' : ''}`}>
                <div className="msg-role">
                  <span>{msg.role === 'user' ? '提问' : '知识库回答'}</span>
                  {msg.mode && (
                    <span className="mode-tag">
                      {msg.mode === 'file-search'
                        ? 'File Search'
                        : msg.mode === 'local-preview'
                          ? '本地回退预览'
                          : '仅索引'}
                    </span>
                  )}
                </div>
                <div className="msg-body">{msg.text}</div>

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
                            [{m.type}] {m.title}
                          </button>
                        ))}
                      </div>
                    )}
                  </details>
                )}

                {msg.citations && msg.citations.length > 0 && (
                  <details className="meta-details" open>
                    <summary>引用来源（{msg.citations.length}）</summary>
                    <div className="citation-list">
                      {msg.citations.map((c, idx) => (
                        <div key={idx} className="citation-card">
                          <div className="citation-head">
                            {c.entryType && <span className="type-pill">{c.entryType}</span>}
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
              </div>
            ))
          )}
          {sending && (
            <div className="msg model loading">正在检索 wiki/index.json 与知识库条目…</div>
          )}
        </div>

        <form
          className="composer"
          onSubmit={(e) => {
            e.preventDefault();
            sendQuestion(input);
          }}
        >
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
            {sending ? '检索中…' : '提问'}
          </button>
        </form>
      </main>

      {previewEntry && (
        <div className="modal-backdrop" onClick={() => setPreviewEntry(null)}>
          <div className="modal-card" onClick={(e) => e.stopPropagation()}>
            <div className="modal-head">
              <div>
                <span className="type-pill">{previewEntry.type}</span>
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
              <div className="alias-box">别名：{previewEntry.aliases.join(' / ')}</div>
            )}
            <pre className="entry-content">
              {previewEntry.content ??
                '当前为纯云端独立容器模式（未挂载本地 wiki/ 原文件目录），请点击上方 Quartz 链接或结合 File Search 引文查看全文。'}
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
                让 AI 深度解读该条目
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
