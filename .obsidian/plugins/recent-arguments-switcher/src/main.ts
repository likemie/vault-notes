import { MarkdownView, Plugin, TFile, TFolder, type TAbstractFile } from "obsidian";
import { linkedNotes, noteTitle } from "./linked-notes";
import { creationDay, RecentStore, type ArgumentNote } from "./recent-store";
import { ARGUMENT_ROOT, BATCH_MS, readSaved, type SaveState } from "./settings";
import { HoverDock, type HoverPanel } from "./panel";

export default class RecentArgumentsSwitcher extends Plugin {
  private model: RecentStore | null = null;
  private dock: HoverDock | null = null;
  private panel: HoverPanel | null = null;
  private links: HoverPanel | null = null;
  private currentLinkPaths = new Set<string>();
  private currentLinkPage: string | null = null;
  private state: SaveState = readSaved(null);
  private refreshTimer: number | null = null;
  private linksTimer: number | null = null;
  private midnightTimer: number | null = null;
  private writes = Promise.resolve();
  private disposed = false;

  async onload(): Promise<void> {
    this.state = readSaved(await this.loadData());
    this.addCommand({
      id: "toggle-recent-arguments",
      name: "展开或收起最近论证",
      callback: () => this.panel?.toggle(true),
    });
    this.addCommand({
      id: "toggle-current-note-links",
      name: "展开或收起本页链接",
      callback: () => this.links?.toggle(true),
    });
    this.app.workspace.onLayoutReady(() => {
      if (!this.disposed) this.mount();
    });
  }

  onunload(): void {
    this.disposed = true;
    if (this.refreshTimer !== null) window.clearTimeout(this.refreshTimer);
    if (this.linksTimer !== null) window.clearTimeout(this.linksTimer);
    if (this.midnightTimer !== null) window.clearTimeout(this.midnightTimer);
    if (this.model) this.persist(this.model.snapshot(Date.now()).checkpoint);
    this.dock?.destroy();
    this.dock = null;
    this.panel = null;
    this.links = null;
    this.model = null;
  }

  private mount(): void {
    const { vault, workspace, metadataCache } = this.app;
    const model = this.model = new RecentStore(this.state.checkpoint);
    const notes = vault.getMarkdownFiles().flatMap(file => {
      const candidate = this.note(file);
      return candidate ? [candidate] : [];
    });
    model.seed(notes, Date.now());
    const active = workspace.getActiveFile();
    if (active) model.read(active.path);
    this.dock = new HoverDock(window, this.state.panel, () => this.schedule());
    this.links = this.dock.add({
      id: "links", label: "链接", title: "本页链接", listLabel: "当前笔记链接的条目", badgeUnit: "条链接",
    }, path => this.open(path));
    this.panel = this.dock.add({
      id: "arguments", label: "论证", title: "最新论证", listLabel: "最近 100 条论证", badgeUnit: "条未读",
    }, path => this.open(path, true));

    this.registerEvent(vault.on("create", file => {
      this.update(file);
      if (file instanceof TFile && file.extension === "md") this.scheduleLinks();
    }));
    this.registerEvent(vault.on("modify", file => this.update(file)));
    this.registerEvent(vault.on("delete", file => {
      const now = Date.now();
      const changed = file instanceof TFolder ? model.removeFolder(file.path, now) : model.remove(file.path, now);
      if (changed) this.schedule();
      this.scheduleLinks();
    }));
    this.registerEvent(vault.on("rename", (file, oldPath) => {
      this.rename(file, oldPath);
      this.scheduleLinks();
    }));
    this.registerEvent(metadataCache.on("changed", file => {
      this.update(file);
      if (file.path === this.currentLinkPage || this.currentLinkPaths.has(file.path)) this.scheduleLinks();
    }));
    this.registerEvent(metadataCache.on("resolve", file => {
      if (file.path === this.currentLinkPage) this.scheduleLinks();
    }));
    this.registerEvent(workspace.on("file-open", file => {
      if (file) model.read(file.path);
      this.schedule();
      this.scheduleLinks();
    }));
    this.registerEvent(workspace.on("active-leaf-change", () => this.scheduleLinks()));
    this.flush();
    this.refreshLinks();
    this.untilMidnight();
  }

  private note(file: TAbstractFile): { note: ArgumentNote; hasMetadata: boolean } | null {
    if (!(file instanceof TFile) || file.extension.toLowerCase() !== "md" ||
        !file.path.startsWith(ARGUMENT_ROOT) || file.basename === "index") return null;
    const cache = this.app.metadataCache.getFileCache(file);
    const fields = cache?.frontmatter;
    if (typeof fields?.type === "string" && fields.type.trim().toLowerCase() !== "argument") return null;
    return {
      note: { path: file.path, title: noteTitle(file, cache), created: creationDay(fields?.created) },
      hasMetadata: Boolean(cache),
    };
  }

  private update(file: TAbstractFile): void {
    if (!this.model || !(file instanceof TFile) || !file.path.startsWith(ARGUMENT_ROOT)) return;
    const candidate = this.note(file);
    const now = Date.now();
    const changed = candidate ? this.model.upsert(candidate.note, now, candidate.hasMetadata) : this.model.remove(file.path, now);
    if (changed) this.schedule();
  }

  private rename(file: TAbstractFile, oldPath: string): void {
    const model = this.model;
    if (!model) return;
    if (file instanceof TFolder) {
      if (!file.path.startsWith(ARGUMENT_ROOT) && !oldPath.startsWith(ARGUMENT_ROOT) &&
          !ARGUMENT_ROOT.startsWith(file.path + "/") && !ARGUMENT_ROOT.startsWith(oldPath + "/")) return;
      for (const child of file.children) this.rename(child, oldPath + child.path.slice(file.path.length));
      return;
    }
    if (!oldPath.startsWith(ARGUMENT_ROOT) && !file.path.startsWith(ARGUMENT_ROOT)) return;
    const now = Date.now();
    const candidate = this.note(file);
    const changed = candidate
      ? model.rename(oldPath, candidate.note, now, candidate.hasMetadata)
      : model.remove(oldPath, now);
    if (changed) this.schedule();
  }

  private async open(path: string, argumentOnly = false): Promise<void> {
    const file = this.app.vault.getFileByPath(path);
    if (!file || file.extension.toLowerCase() !== "md" || (argumentOnly && !this.note(file))) {
      throw new Error("The note is no longer available");
    }
    const { workspace } = this.app;
    const current = workspace.getMostRecentLeaf();
    const leaf = current?.view.getViewType() === "markdown" ? current : workspace.getLeaf("tab");
    await leaf.openFile(file);
    if (this.model?.read(file.path)) this.schedule();
  }

  private schedule(): void {
    if (this.disposed || this.refreshTimer !== null) return;
    this.refreshTimer = window.setTimeout(() => {
      this.refreshTimer = null;
      this.flush();
    }, BATCH_MS);
  }

  private flush(): void {
    if (!this.model || !this.panel) return;
    const now = Date.now();
    const active = this.app.workspace.getActiveFile()?.path ?? null;
    const { checkpoint, rows, unread, today } = this.model.snapshot(now);
    this.panel.render({ rows, badge: unread, count: "今日 " + today, countDescription: "今天创建 " + today + " 条论证",
      empty: "暂无论证", active, now });
    this.persist(checkpoint);
  }

  private scheduleLinks(): void {
    if (this.disposed || this.linksTimer !== null) return;
    this.linksTimer = window.setTimeout(() => {
      this.linksTimer = null;
      this.refreshLinks();
    }, BATCH_MS);
  }

  private refreshLinks(): void {
    if (!this.links) return;
    const { workspace, metadataCache } = this.app;
    const file = workspace.getActiveViewOfType(MarkdownView)?.file ?? null;
    const rows = file ? linkedNotes(file, metadataCache) : [];
    this.currentLinkPage = file?.path ?? null;
    this.currentLinkPaths = new Set(rows.map(note => note.path));
    this.links.render({ rows, badge: rows.length, count: rows.length + " 条", active: null, context: this.currentLinkPage,
      empty: file ? "本页没有可打开的笔记链接" : "打开一篇笔记即可查看链接", now: Date.now() });
  }

  private persist(checkpoint: SaveState["checkpoint"]): void {
    const snapshot = { panel: { ...this.state.panel }, checkpoint };
    this.writes = this.writes.then(() => this.saveData(snapshot)).catch(error => {
      console.error("Recent Arguments Switcher could not save its state", error);
    });
  }

  private untilMidnight(): void {
    const midnight = new Date();
    midnight.setHours(24, 0, 0, 100);
    this.midnightTimer = window.setTimeout(() => {
      this.schedule();
      this.scheduleLinks();
      this.untilMidnight();
    }, midnight.getTime() - Date.now());
  }
}
