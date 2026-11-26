import { Fragment, type ReactNode } from 'react';

interface MarkdownViewProps {
  text: string;
  onWikilinkClick?: (target: string) => void;
}

/**
 * Lightweight, XSS-safe Markdown + [[wikilink]] renderer for academic answers.
 */
export function MarkdownView({ text, onWikilinkClick }: MarkdownViewProps) {
  const lines = text.replace(/\r\n/g, '\n').split('\n');
  const blocks: ReactNode[] = [];
  let i = 0;

  while (i < lines.length) {
    const line = lines[i];

    // Fenced code block
    if (line.trim().startsWith('```')) {
      const lang = line.trim().slice(3).trim();
      const codeLines: string[] = [];
      i++;
      while (i < lines.length && !lines[i].trim().startsWith('```')) {
        codeLines.push(lines[i]);
        i++;
      }
      i++;
      blocks.push(
        <pre key={`code-${i}`} className="md-code-block" data-lang={lang || undefined}>
          <code>{codeLines.join('\n')}</code>
        </pre>,
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

    // Ordered list
    if (/^\s*\d+\.\s+/.test(line)) {
      const items: string[] = [];
      while (i < lines.length && /^\s*\d+\.\s+/.test(lines[i])) {
        items.push(lines[i].replace(/^\s*\d+\.\s+/, ''));
        i++;
      }
      blocks.push(
        <ol key={`ol-${i}`} className="md-list">
          {items.map((item, idx) => (
            <li key={idx}>{renderInline(item, onWikilinkClick)}</li>
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

    // Paragraph (coalesce consecutive non-special lines)
    const paraLines: string[] = [];
    while (
      i < lines.length &&
      lines[i].trim() &&
      !lines[i].trim().startsWith('```') &&
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
