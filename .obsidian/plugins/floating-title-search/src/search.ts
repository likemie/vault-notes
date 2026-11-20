import type { TitleEntry } from "./title-index";

export const RESULT_LIMIT = 30;
const PATH_ORDER = new Intl.Collator("zh-CN", { numeric: true });

export interface TitleMatch {
  entry: TitleEntry;
  tier: 0 | 1 | 2;
  foldedStart: number;
  alias?: string;
}

export function searchTitles(entries: Iterable<TitleEntry>, input: string, exactAliases: boolean) {
  const query = input.trim().toLowerCase();
  const rows: TitleMatch[] = [];
  if (!query) return { rows, total: 0, query };

  for (const entry of entries) {
    if (entry.foldedTitle === query) {
      rows.push({ entry, tier: 0, foldedStart: 0 });
      continue;
    }
    const alias = exactAliases ? entry.aliases.get(query) : undefined;
    if (alias) {
      rows.push({ entry, tier: 1, foldedStart: -1, alias });
      continue;
    }
    const start = entry.foldedTitle.indexOf(query);
    if (start >= 0) rows.push({ entry, tier: 2, foldedStart: start });
  }

  rows.sort((a, b) => a.tier - b.tier || b.entry.mtime - a.entry.mtime ||
    PATH_ORDER.compare(a.entry.path, b.entry.path) || (a.entry.path < b.entry.path ? -1 : a.entry.path > b.entry.path ? 1 : 0));
  return { rows: rows.slice(0, RESULT_LIMIT), total: rows.length, query };
}

export function titleRange(title: string, foldedTitle: string, start: number, length: number): [number, number] {
  if (title.length === foldedTitle.length) return [start, start + length];

  // Some characters lower-case to multiple code points. Return character boundaries in the display title.
  let original = 0;
  let folded = 0;
  let from = 0;
  for (const character of title) {
    const next = folded + character.toLowerCase().length;
    if (folded <= start && start < next) from = original;
    original += character.length;
    if (next >= start + length) return [from, original];
    folded = next;
  }
  return [from, title.length];
}
