import { Plugin, TFile, TFolder, type TAbstractFile } from "obsidian";
import { creationDay, RecentStore, type ArgumentNote } from "./recent-store";
import { ARGUMENT_ROOT, BATCH_MS, readSaved, type SaveState } from "./settings";
import { RecentPanel } from "./panel";

export default class RecentArgumentsSwitcher extends Plugin {
  private model: RecentStore | null = null;
  private panel: RecentPanel | null = null;
  private state: SaveState = readSaved(null);
  private refreshTimer: number | null = null;
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
    this.app.workspace.onLayoutReady(() => {
      if (!this.disposed) this.mount();
    });
  }

  onunload(): void {
    this.disposed = true;
    if (this.refreshTimer !== null) window.clearTimeout(this.refreshTimer);
    if (this.midnightTimer !== null) window.clearTimeout(this.midnightTimer);
    if (this.model) this.persist(this.model.snapshot(Date.now()).checkpoint);
    this.panel?.destroy();
    this.panel = null;
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
    this.panel = new RecentPanel(window, this.state.panel, path => this.open(path), () => this.schedule());

    this.registerEvent(vault.on("create", file => this.update(file)));
    this.registerEvent(vault.on("modify", file => this.update(file)));
    this.registerEvent(vault.on("delete", file => {
      const now = Date.now();
      const changed = file instanceof TFolder ? model.removeFolder(file.path, now) : model.remove(file.path, now);
      if (changed) this.schedule();
    }));
    this.registerEvent(vault.on("rename", (file, oldPath) => this.rename(file, oldPath)));
    this.registerEvent(metadataCache.on("changed", file => this.update(file)));
    this.registerEvent(workspace.on("file-open", file => {
      if (file) model.read(file.path);
      this.schedule();
    }));
    this.flush();
    this.untilMidnight();
  }

  private note(file: TAbstractFile): { note: ArgumentNote; hasMetadata: boolean } | null {
    if (!(file instanceof TFile) || file.extension.toLowerCase() !== "md" ||
        !file.path.startsWith(ARGUMENT_ROOT) || file.basename === "index") return null;
    const cache = this.app.metadataCache.getFileCache(file);
    const fields = cache?.frontmatter;
    if (typeof fields?.type === "string" && fields.type.trim().toLowerCase() !== "argument") return null;
    const title = [fields?.argument_display_title, fields?.title]
      .find(value => typeof value === "string" && value.trim());
    return {
      note: { path: file.path, title: title?.trim() ?? file.basename, created: creationDay(fields?.created) },
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

  private async open(path: string): Promise<void> {
    const file = this.app.vault.getFileByPath(path);
    if (!file || !this.note(file)) throw new Error("The argument is no longer available");
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
    const { checkpoint, ...view } = this.model.snapshot(now);
    this.panel.render({ ...view, active, now });
    this.persist(checkpoint);
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
      this.untilMidnight();
    }, midnight.getTime() - Date.now());
  }
}
