import { Fragment, useEffect, useId, useState, type ReactNode } from 'react';

interface MarkdownViewProps {
  text: string;
  onWikilinkClick?: (target: string) => void;
}

interface MermaidGlobal {
  initialize: (cfg: Record<string, unknown>) => void;
  render: (id: string, text: string) => Promise<{ svg: string }>;
}

declare global {
  interface Window {
    mermaid?: MermaidGlobal;
  }
}

let mermaidLoaderPromise: Promise<MermaidGlobal> | null = null;
let mermaidInitialized = false;

const MERMAID_CDN_URLS = [
  'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js',
  'https://unpkg.com/mermaid@11/dist/mermaid.min.js',
];

function loadScript(src: string): Promise<void> {
  return new Promise((resolve, reject) => {
    const script = document.createElement('script');
    script.src = src;
    script.async = true;
    script.onload = () => resolve();
    script.onerror = () => reject(new Error(`无法加载脚本 ${src}`));
    document.head.appendChild(script);
  });
}

async function getMermaid(): Promise<MermaidGlobal> {
  if (window.mermaid) return window.mermaid;
  if (!mermaidLoaderPromise) {
    mermaidLoaderPromise = (async () => {
      let lastError: unknown;
      for (const url of MERMAID_CDN_URLS) {
        try {
          await loadScript(url);
          if (window.mermaid) return window.mermaid;
        } catch (err) {
          lastError = err;
        }
      }
      mermaidLoaderPromise = null;
      throw lastError ?? new Error('Mermaid 脚本加载失败');
    })();
  }
  return mermaidLoaderPromise;
}

function MermaidBlock({ code }: { code: string }) {
  const reactId = useId().replace(/:/g, '');
  const [svg, setSvg] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [showSource, setShowSource] = useState(false);

  useEffect(() => {
    let cancelled = false;
    setError(null);
    setSvg(null);

    (async () => {
      try {
        const mermaid = await getMermaid();
        if (!mermaidInitialized) {
          mermaid.initialize({
            startOnLoad: false,
            theme: 'neutral',
            securityLevel: 'strict',
            fontFamily: "-apple-system, BlinkMacSystemFont, 'PingFang SC', 'Noto Sans SC', sans-serif",
          });
          mermaidInitialized = true;
        }
        const renderId = `mmd-${reactId}-${Date.now()}`;
        const result = await mermaid.render(renderId, code.trim());
        if (!cancelled) {
          setSvg(result.svg);
        }
      } catch (err) {
        if (!cancelled) {
          setError(err instanceof Error ? err.message : 'Mermaid 语法解析失败');
        }
      }
    })();

    return () => {
      cancelled = true;
    };
  }, [code, reactId]);

  return (
    <div className="mermaid-card">
      <div className="mermaid-toolbar">
        <span className="mermaid-label">Mermaid 图表</span>
        <button
          type="button"
          className="mermaid-toggle-btn"
          onClick={() => setShowSource((prev) => !prev)}
        >
          {showSource ? '查看渲染图' : '查看源码'}
        </button>
      </div>
      {showSource || error ? (
        <>
          {error && <div className="mermaid-err">图表渲染失败，已回退源码：{error}</div>}
          <pre className="md-code-block" data-lang="mermaid">
            <code>{code}</code>
          </pre>
        </>
      ) : svg ? (
        <div className="mermaid-svg" dangerouslySetInnerHTML={{ __html: svg }} />
      ) : (
        <div className="mermaid-loading">正在渲染 Mermaid 图表…</div>
      )}
    </div>
  );
}

function splitTableRow(line: string): string[] {
  let trimmed = line.trim();
  if (trimmed.startsWith('|')) trimmed = trimmed.slice(1);
  if (trimmed.endsWith('|')) trimmed = trimmed.slice(0, -1);

  const cells: string[] = [];
  let current = '';
  for (let i = 0; i < trimmed.length; i++) {
    if (trimmed[i] === '\\' && trimmed[i + 1] === '|') {
      current += '|';
      i++;
    } else if (trimmed[i] === '|') {
      cells.push(current.trim());
      current = '';
    } else {
      current += trimmed[i];
    }
  }
  cells.push(current.trim());
  return cells;
}

function isTableSeparatorLine(line: string): boolean {
  const trimmed = line.trim();
  if (!trimmed.includes('|') && !trimmed.includes('-')) return false;
  const cells = splitTableRow(trimmed);
  return cells.length >= 1 && cells.every((c) => /^:?-{3,}:?$/.test(c));
}

function parseAlignments(line: string): Array<'left' | 'center' | 'right'> {
  return splitTableRow(line).map((cell) => {
    if (cell.startsWith(':') && cell.endsWith(':')) return 'center';
    if (cell.endsWith(':')) return 'right';
    return 'left';
  });
}

function isTableStart(lines: string[], idx: number): boolean {
  if (idx + 1 >= lines.length) return false;
  const header = lines[idx].trim();
  const sep = lines[idx + 1].trim();
  if (!header.includes('|')) return false;
  return isTableSeparatorLine(sep);
}

/**
 * Lightweight, XSS-safe Markdown + GFM Table + Mermaid + [[wikilink]] renderer.
 */
export function MarkdownView({ text, onWikilinkClick }: MarkdownViewProps) {
  const lines = text.replace(/\r\n/g, '\n').split('\n');
  const blocks: ReactNode[] = [];
  let i = 0;

  while (i < lines.length) {
    const line = lines[i];

    // Fenced code block (including mermaid)
    if (line.trim().startsWith('```')) {
      const lang = line.trim().slice(3).trim().toLowerCase();
      const codeLines: string[] = [];
      i++;
      while (i < lines.length && !lines[i].trim().startsWith('```')) {
        codeLines.push(lines[i]);
        i++;
      }
      i++;
      const codeText = codeLines.join('\n');
      if (lang === 'mermaid') {
        blocks.push(<MermaidBlock key={`mmd-${i}`} code={codeText} />);
      } else {
        blocks.push(
          <pre key={`code-${i}`} className="md-code-block" data-lang={lang || undefined}>
            <code>{codeText}</code>
          </pre>,
        );
      }
      continue;
    }

    // GFM pipe table
    if (isTableStart(lines, i)) {
      const headers = splitTableRow(lines[i]);
      const alignments = parseAlignments(lines[i + 1]);
      i += 2;
      const rows: string[][] = [];
      while (i < lines.length && lines[i].trim().includes('|') && !lines[i].trim().startsWith('```')) {
        if (isTableSeparatorLine(lines[i])) {
          i++;
          continue;
        }
        rows.push(splitTableRow(lines[i]));
        i++;
      }

      blocks.push(
        <div key={`tbl-${i}`} className="md-table-wrap">
          <table className="md-table">
            <thead>
              <tr>
                {headers.map((h, colIdx) => (
                  <th key={colIdx} style={{ textAlign: alignments[colIdx] || 'left' }}>
                    {renderInline(h, onWikilinkClick)}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {rows.map((row, rIdx) => (
                <tr key={rIdx}>
                  {headers.map((_, colIdx) => (
                    <td key={colIdx} style={{ textAlign: alignments[colIdx] || 'left' }}>
                      {renderInline(row[colIdx] ?? '', onWikilinkClick)}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>,
      );
      continue;
    }

    // Horizontal rule
    if (/^\s*([-*_])\1{2,}\s*$/.test(line)) {
      blocks.push(<hr key={`hr-${i}`} className="md-hr" />);
      i++;
      continue;
    }

    // Headings
    const headingMatch = line.match(/^(#{1,4})\s+(.+)$/);
    if (headingMatch) {
      const level = headingMatch[1].length;
      const content = renderInline(headingMatch[2], onWikilinkClick);
      if (level === 1) blocks.push(<h1 key={`h-${i}`} className="md-h1">{content}</h1>);
      else if (level === 2) blocks.push(<h2 key={`h-${i}`} className="md-h2">{content}</h2>);
      else if (level === 3) blocks.push(<h3 key={`h-${i}`} className="md-h3">{content}</h3>);
      else blocks.push(<h4 key={`h-${i}`} className="md-h4">{content}</h4>);
      i++;
      continue;
    }

    // Blockquote
    if (line.trim().startsWith('>')) {
      const quoteLines: string[] = [];
      while (i < lines.length && lines[i].trim().startsWith('>')) {
        quoteLines.push(lines[i].replace(/^\s*>\s?/, ''));
        i++;
      }
      blocks.push(
        <blockquote key={`bq-${i}`} className="md-quote">
          {renderInline(quoteLines.join(' '), onWikilinkClick)}
        </blockquote>,
      );
      continue;
    }

    // Unordered list
    if (/^\s*[-*•]\s+/.test(line)) {
      const items: string[] = [];
      while (i < lines.length && /^\s*[-*•]\s+/.test(lines[i])) {
        items.push(lines[i].replace(/^\s*[-*•]\s+/, ''));
        i++;
      }
      blocks.push(
        <ul key={`ul-${i}`} className="md-list">
          {items.map((item, idx) => (
            <li key={idx}>{renderInline(item, onWikilinkClick)}</li>
          ))}
        </ul>,
      );
      continue;
    }

    // Ordered list (preserves explicit starting index if indented/split across blocks)
    const ordFirst = line.match(/^\s*(\d+)\.\s+(.+)$/);
    if (ordFirst) {
      const startNum = Number(ordFirst[1]);
      const items: Array<{ text: string; subBullets: string[] }> = [];
      while (i < lines.length) {
        const m = lines[i].match(/^\s*(\d+)\.\s+(.+)$/);
        if (!m) break;
        const entry = { text: m[2], subBullets: [] as string[] };
        i++;
        while (i < lines.length && /^\s{2,}[-*•]\s+/.test(lines[i])) {
          entry.subBullets.push(lines[i].replace(/^\s*[-*•]\s+/, ''));
          i++;
        }
        items.push(entry);
      }
      blocks.push(
        <ol key={`ol-${i}`} start={startNum} className="md-list">
          {items.map((item, idx) => (
            <li key={idx}>
              {renderInline(item.text, onWikilinkClick)}
              {item.subBullets.length > 0 && (
                <ul className="md-sublist">
                  {item.subBullets.map((sb, sIdx) => (
                    <li key={sIdx}>{renderInline(sb, onWikilinkClick)}</li>
                  ))}
                </ul>
              )}
            </li>
          ))}
        </ol>,
      );
      continue;
    }

    // Blank line
    if (!line.trim()) {
      i++;
      continue;
    }

    // Paragraph
    const paraLines: string[] = [];
    while (
      i < lines.length &&
      lines[i].trim() &&
      !lines[i].trim().startsWith('```') &&
      !isTableStart(lines, i) &&
      !/^\s*([-*_])\1{2,}\s*$/.test(lines[i]) &&
      !/^#{1,4}\s+/.test(lines[i]) &&
      !lines[i].trim().startsWith('>') &&
      !/^\s*[-*•]\s+/.test(lines[i]) &&
      !/^\s*\d+\.\s+/.test(lines[i])
    ) {
      paraLines.push(lines[i]);
      i++;
    }
    blocks.push(
      <p key={`p-${i}`} className="md-p">
        {renderInline(paraLines.join('\n'), onWikilinkClick)}
      </p>,
    );
  }

  return <div className="md-root">{blocks}</div>;
}

const INLINE_TOKEN_RE =
  /(\[\[[^\]]+\]\]|`[^`]+`|\*\*[^*]+\*\*|\*[^*]+\*|\[[^\]]+\]\(https?:\/\/[^)]+\))/g;

function renderInline(text: string, onWikilinkClick?: (target: string) => void): ReactNode[] {
  const parts = text.split(INLINE_TOKEN_RE);
  return parts.map((part, idx) => {
    if (!part) return null;

    if (part.startsWith('[[') && part.endsWith(']]')) {
      const inner = part.slice(2, -2);
      const [target, alias] = inner.split('|');
      const label = (alias || target).trim();
      const cleanTarget = target.trim();
      return (
        <button
          key={idx}
          type="button"
          className="wikilink-pill"
          onClick={() => onWikilinkClick?.(cleanTarget)}
          title={`查看索引：${cleanTarget}`}
        >
          {label}
        </button>
      );
    }

    if (part.startsWith('`') && part.endsWith('`')) {
      return (
        <code key={idx} className="md-inline-code">
          {part.slice(1, -1)}
        </code>
      );
    }

    if (part.startsWith('**') && part.endsWith('**')) {
      return <strong key={idx}>{part.slice(2, -2)}</strong>;
    }

    if (part.startsWith('*') && part.endsWith('*')) {
      return <em key={idx}>{part.slice(1, -1)}</em>;
    }

    const linkMatch = part.match(/^\[([^\]]+)\]\((https?:\/\/[^)]+)\)$/);
    if (linkMatch) {
      return (
        <a key={idx} href={linkMatch[2]} target="_blank" rel="noreferrer" className="md-ext-link">
          {linkMatch[1]}
        </a>
      );
    }

    return <Fragment key={idx}>{part}</Fragment>;
  });
}
