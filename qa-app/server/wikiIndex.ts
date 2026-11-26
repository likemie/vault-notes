import fs from 'node:fs';
import path from 'node:path';

export interface WikiEntry {
  title: string;
  type: string;
  path: string;
  aliases: string[];
}

export interface SearchMatch extends WikiEntry {
  score: number;
  matchedIn: string[];
}

export interface SearchOptions {
  query: string;
  type?: string;
  limit?: number;
}

/**
 * Resolve wiki-index.json from bundled data/ first, then parent vault ../wiki/index.json.
 */
export function resolveIndexPath(appDir: string): string {
  const bundled = path.join(appDir, 'data', 'wiki-index.json');
  if (fs.existsSync(bundled)) {
    return bundled;
  }
  const vaultIndex = path.resolve(appDir, '..', 'wiki', 'index.json');
  if (fs.existsSync(vaultIndex)) {
    return vaultIndex;
  }
  throw new Error('Could not locate data/wiki-index.json or ../wiki/index.json');
}

export function loadWikiIndex(indexPath: string): WikiEntry[] {
  const raw = fs.readFileSync(indexPath, 'utf-8');
  const parsed = JSON.parse(raw);
  if (!Array.isArray(parsed)) {
    throw new Error(`Invalid wiki index format at ${indexPath}: expected array`);
  }
  return parsed.map((item) => ({
    title: String(item.title ?? ''),
    type: String(item.type ?? 'unknown'),
    path: String(item.path ?? ''),
    aliases: Array.isArray(item.aliases) ? item.aliases.map(String) : [],
  }));
}

function normalize(value: string): string {
  return value.trim().toLowerCase().replace(/\s+/g, ' ');
}

/**
 * Split query into meaningful search tokens while preserving the full normalized query.
 */
function tokenize(query: string): string[] {
  const norm = normalize(query);
  if (!norm) return [];
  const parts = norm
    .split(/[\s,，、;；/()（）[\]【】]+/)
    .map((p) => p.trim())
    .filter((p) => p.length >= 2 || /[\u4e00-\u9fff]/.test(p));
  return Array.from(new Set([norm, ...parts]));
}

/**
 * Search wiki/index.json entries by title, aliases, path, and optional type.
 */
export function searchWikiIndex(
  entries: WikiEntry[],
  options: SearchOptions,
): SearchMatch[] {
  const normQuery = normalize(options.query);
  const typeFilter = options.type ? normalize(options.type) : '';
  const limit = Math.min(Math.max(options.limit ?? 15, 1), 50);

  if (!normQuery && !typeFilter) {
    return [];
  }

  const tokens = tokenize(normQuery);
  const results: SearchMatch[] = [];

  for (const entry of entries) {
    if (typeFilter && normalize(entry.type) !== typeFilter) {
      continue;
    }

    if (!normQuery) {
      results.push({ ...entry, score: 1, matchedIn: ['type'] });
      if (results.length >= limit) break;
      continue;
    }

    const normTitle = normalize(entry.title);
    const normPath = normalize(entry.path);
    const normAliases = entry.aliases.map(normalize);

    let score = 0;
    const matchedIn = new Set<string>();

    if (normTitle === normQuery) {
      score += 120;
      matchedIn.add('title:exact');
    } else if (normTitle.includes(normQuery)) {
      score += 75;
      matchedIn.add('title');
    }

    for (const alias of normAliases) {
      if (alias === normQuery) {
        score += 110;
        matchedIn.add('alias:exact');
        break;
      }
      if (alias.includes(normQuery) || (alias.length >= 2 && normQuery.includes(alias))) {
        score += 65;
        matchedIn.add('alias');
        break;
      }
    }

    if (normPath.includes(normQuery)) {
      score += 30;
      matchedIn.add('path');
    }

    for (const token of tokens) {
      if (token === normQuery) continue;
      if (normTitle.includes(token)) {
        score += 22;
        matchedIn.add('title:token');
      }
      if (normAliases.some((a) => a.includes(token))) {
        score += 18;
        matchedIn.add('alias:token');
      }
      if (normPath.includes(token)) {
        score += 8;
        matchedIn.add('path:token');
      }
    }

    if (score > 0) {
      results.push({
        ...entry,
        score,
        matchedIn: Array.from(matchedIn),
      });
    }
  }

  results.sort((a, b) => b.score - a.score || a.title.localeCompare(b.title));
  return results.slice(0, limit);
}

export function getIndexStats(entries: WikiEntry[]): Record<string, number> {
  const counts: Record<string, number> = {};
  for (const entry of entries) {
    counts[entry.type] = (counts[entry.type] ?? 0) + 1;
  }
  return counts;
}

export function buildQuartzUrl(entryPath: string, quartzBaseUrl?: string): string | undefined {
  if (!quartzBaseUrl) return undefined;
  const base = quartzBaseUrl.replace(/\/+$/, '');
  const clean = entryPath.replace(/^\/+/, '').replace(/\.md$/i, '');
  const encoded = clean
    .split('/')
    .map((seg) => encodeURIComponent(seg.replace(/\s+/g, '-')))
    .join('/');
  return `${base}/${encoded}`;
}
