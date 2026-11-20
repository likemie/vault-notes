import { parseLinktext, type CachedMetadata, type MetadataCache, type TFile } from "obsidian";
import { compareCreationDays, creationDay, type ArgumentNote } from "./recent-store";

const PATH_ORDER = new Intl.Collator("zh-CN", { numeric: true });

export function noteTitle(file: TFile, cache: CachedMetadata | null): string {
  const fields = cache?.frontmatter;
  for (const value of [fields?.argument_display_title, fields?.title]) {
    if (typeof value === "string" && value.trim()) return value.trim();
  }
  return file.basename;
}

export function linkedNotes(file: TFile, metadata: MetadataCache): ArgumentNote[] {
  const source = metadata.getFileCache(file);
  if (!source) return [];

  const linkpaths = new Set<string>();
  const destinations = new Map<string, ArgumentNote>();
  for (const reference of [...(source.links ?? []), ...(source.embeds ?? [])]) {
    const { path } = parseLinktext(reference.link);
    if (!path || /^(?:[a-z][a-z\d+.-]*:|\/\/)/i.test(path) || linkpaths.has(path)) continue;
    linkpaths.add(path);
    const target = metadata.getFirstLinkpathDest(path, file.path);
    if (!target || target.path === file.path || target.extension.toLowerCase() !== "md" ||
        destinations.has(target.path)) continue;

    const cache = metadata.getFileCache(target);
    const fields = cache?.frontmatter;
    const isSource = target.path.startsWith("sources/") || target.path.startsWith("books/");
    const created = creationDay(fields?.created) ?? (isSource ? creationDay(fields?.processed_date) : null);
    destinations.set(target.path, { path: target.path, title: noteTitle(target, cache), created });
  }

  return [...destinations.values()].sort((a, b) =>
    compareCreationDays(a.created, b.created) || PATH_ORDER.compare(a.path, b.path));
}
