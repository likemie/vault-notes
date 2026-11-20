import { Plugin, TFile, TFolder, type TAbstractFile } from "obsidian";
import { FloatingSearch } from "./floating-panel";
import { readSettings, type SearchState } from "./settings";
import { TitleIndex } from "./title-index";

export default class FloatingTitleSearch extends Plugin {
  private readonly index = new TitleIndex();
  private panel: FloatingSearch | null = null;
  private state: SearchState = readSettings(null);
  private saving = Promise.resolve();
  private disposed = false;
  private focusWhenReady = false;

  async onload(): Promise<void> {
    this.state = readSettings(await this.loadData());
    this.addCommand({
      id: "open-title-search",
      name: "打开标题搜索",
      hotkeys: [{ modifiers: ["Mod", "Shift"], key: "K" }],
      callback: () => {
        if (this.panel) this.panel.show(true);
        else this.focusWhenReady = true;
      },
    });
    this.app.workspace.onLayoutReady(() => {
      if (!this.disposed) this.mount();
    });
  }

  onunload(): void {
    this.disposed = true;
    this.panel?.destroy();
    this.panel = null;
  }

  private mount(): void {
    const { metadataCache, vault } = this.app;
    for (const file of vault.getMarkdownFiles()) this.update(file);
    this.panel = new FloatingSearch(window, this.state, () => this.index.entries(),
      path => this.openFile(path), () => this.persist());
    this.registerEvent(metadataCache.on("changed", (file, _, cache) => {
      if (this.isMarkdown(file) && this.index.set(file.path, file.stat.mtime, cache.frontmatter)) this.panel?.refresh();
    }));
    this.registerEvent(vault.on("create", file => {
      if (this.update(file)) this.panel?.refresh();
    }));
    this.registerEvent(vault.on("modify", file => {
      if (this.isMarkdown(file) && this.index.updateTime(file.path, file.stat.mtime)) this.panel?.refresh();
    }));
    this.registerEvent(vault.on("rename", (file, oldPath) => {
      if (this.rename(file, oldPath)) this.panel?.refresh();
    }));
    this.registerEvent(vault.on("delete", file => {
      if (this.index.remove(file.path, file instanceof TFolder)) this.panel?.refresh();
    }));
    if (this.focusWhenReady) this.panel.show(true);
  }

  private isMarkdown(file: TAbstractFile): file is TFile {
    return file instanceof TFile && file.extension.toLowerCase() === "md";
  }

  private update(file: TAbstractFile): boolean {
    if (!this.isMarkdown(file)) return false;
    const cache = this.app.metadataCache.getFileCache(file);
    return cache ? this.index.set(file.path, file.stat.mtime, cache.frontmatter) : false;
  }

  private rename(file: TAbstractFile, oldPath: string): boolean {
    if (file instanceof TFolder) {
      let changed = false;
      for (const child of file.children) {
        changed = this.rename(child, oldPath + child.path.slice(file.path.length)) || changed;
      }
      return changed;
    }
    if (!this.isMarkdown(file)) return this.index.remove(oldPath);

    const moved = this.index.move(oldPath, file.path, file.stat.mtime);
    return this.update(file) || moved;
  }

  private async openFile(path: string): Promise<void> {
    const file = this.app.vault.getFileByPath(path);
    if (!file || !this.isMarkdown(file)) throw new Error("Invalid Markdown note");
    const workspace = this.app.workspace;
    const current = workspace.getMostRecentLeaf();
    const leaf = current?.view.getViewType() === "markdown" ? current : workspace.getLeaf("tab");
    await leaf.openFile(file);
  }

  private persist(): void {
    const state = { ...this.state };
    this.saving = this.saving.then(() => this.saveData(state)).catch(error => {
      console.error("Floating Title Search could not save preferences", error);
    });
  }
}
