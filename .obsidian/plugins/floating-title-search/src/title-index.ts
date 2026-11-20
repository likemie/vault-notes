export interface TitleEntry {
  path: string;
  title: string;
  foldedTitle: string;
  aliases: ReadonlyMap<string, string>;
  mtime: number;
}

export class TitleIndex {
  private readonly byPath = new Map<string, TitleEntry>();

  entries(): Iterable<TitleEntry> {
    return this.byPath.values();
  }

  set(path: string, mtime: number, properties: Record<string, unknown> | undefined): boolean {
    const title = typeof properties?.title === "string" ? properties.title.trim() : "";
    if (!title) return this.byPath.delete(path);
    const raw = properties?.aliases;
    const aliases = new Map<string, string>();
    for (const item of Array.isArray(raw) ? raw : [raw]) {
      if (typeof item !== "string" || !item.trim()) continue;
      const alias = item.trim();
      if (!aliases.has(alias.toLowerCase())) aliases.set(alias.toLowerCase(), alias);
    }
    const old = this.byPath.get(path);
    if (old?.title === title && old.mtime === mtime && old.aliases.size === aliases.size &&
        [...aliases].every(([key, val]) => old.aliases.get(key) === val)) return false;
    this.byPath.set(path, { path, title, foldedTitle: title.toLowerCase(), aliases, mtime });
    return true;
  }

  updateTime(path: string, mtime: number): boolean {
    const entry = this.byPath.get(path);
    if (!entry || entry.mtime === mtime) return false;
    entry.mtime = mtime;
    return true;
  }

  move(oldPath: string, path: string, mtime: number): boolean {
    const cached = this.byPath.get(oldPath);
    if (!cached || oldPath === path) return false;
    this.byPath.delete(oldPath);
    this.byPath.set(path, { ...cached, path, mtime });
    return true;
  }

  remove(path: string, folder = false): boolean {
    if (!folder) return this.byPath.delete(path);
    const prefix = path + "/";
    let changed = false;
    for (const key of this.byPath.keys()) {
      if (key.startsWith(prefix)) changed = this.byPath.delete(key) || changed;
    }
    return changed;
  }
}
