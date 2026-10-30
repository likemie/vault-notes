/* Floating TOC 2.7.1 local adapter. Installed by patch_floating_toc.py.
 * This module never writes note content or changes Obsidian's metadata cache.
 */
const __ftocNotes = new WeakMap();
const __ftocNames = {
  question: '研究问题', def: '定义', claim: '主张', 'sub-claim': '子论点',
  'concept-proposition': '概念命题', 'concept-lens': '概念透镜',
  'citation-card': '关键表述', 'evidence-grid-a': '相关研究索引',
};
function __ftocParse(text, nativeHeadings = []) {
  const result = nativeHeadings.map(h => ({...h, position: {
    ...h.position, start: {...h.position.start}, end: {...h.position.end},
  }}));
  const lines = text.split('\n');
  let frontmatter = lines[0]?.trim() === '---', comment = false, fence = null, offset = 0;
  for (let line = 0; line < lines.length; line++) {
    const raw = lines[line], start = offset;
    offset += raw.length + 1;
    if (frontmatter) {
      if (line > 0 && /^(---|\.\.\.)\s*$/.test(raw)) frontmatter = false;
      continue;
    }
    const quote = raw.match(/^ {0,3}((?:>[ \t]*)+)/);
    const depth = quote ? (quote[1].match(/>/g) || []).length : 0;
    const body = quote ? raw.slice(quote[0].length) : raw;
    if (fence && depth < fence.depth && raw.trim()) fence = null;
    if (fence) {
      const close = body.match(/^ {0,3}(`{3,}|~{3,})\s*$/);
      if (close && close[1][0] === fence.char && close[1].length >= fence.size) fence = null;
      continue;
    }
    // Remove Obsidian comments before matching callouts, including inline comments.
    let visible = '', cursor = 0;
    while (cursor < body.length) {
      const mark = body.indexOf('%%', cursor);
      if (mark < 0) { if (!comment) visible += body.slice(cursor); break; }
      if (!comment) visible += body.slice(cursor, mark);
      comment = !comment;
      cursor = mark + 2;
    }
    const open = visible.match(/^ {0,3}(`{3,}|~{3,})/);
    if (open) { fence = {char: open[1][0], size: open[1].length, depth}; continue; }
    if (depth !== 1) continue;
    const match = visible.match(/^\[!([\w-]+)(?:\|[^\]]*)?\][+-]?(?:[ \t]+(.*?))?\s*$/);
    if (!match) continue;
    const type = match[1].toLowerCase();
    if (type.endsWith('-divider') || /^line-[ab]$/.test(type)) continue;
    const title = match[2]?.trim() || __ftocNames[type] || type;
    const previous = nativeHeadings.filter(h => h.position.start.line < line).at(-1);
    result.push({heading: title, level: Math.min(6, previous ? previous.level + 1 : 2),
      position: {start: {line, col: 0, offset: start},
        end: {line, col: raw.length, offset: start + raw.length}},
      __ftocCallout: type});
  }
  // Escape angle brackets so MarkdownRenderer and Floating TOC's HTML cleanup
  // preserve literal template placeholders, instead of interpreting them as HTML.
  return result.sort((a, b) => a.position.start.line - b.position.start.line)
    .map(h => h.__ftocCallout ? ({...h, heading: h.heading.replace(/</g, '&lt;').replace(/>/g, '&gt;')}) : h);
}
function __ftocCache(app, file) {
  const cache = file && app.metadataCache.getFileCache(file);
  const text = file && __ftocNotes.get(app)?.get(file.path);
  return {...cache, headings: text === undefined ? (cache?.headings || []) :
    __ftocParse(text, cache?.headings || [])};
}
function __ftocLabel(text) { return text.replace(/&lt;/g, '<').replace(/&gt;/g, '>'); }
function __ftocNavigate(view, line) {
  if (view.getMode() === 'preview') view.leaf.openFile(view.file, {eState: {line, focus: false}});
  else {
    const pos = {line, ch: 0};
    view.editor.setCursor(pos);
    view.editor.scrollIntoView({from: pos, to: pos}, true);
  }
}
// The parser is also exercised by Node tests without loading the Obsidian plugin.
if (typeof X === 'undefined') module.exports = {parse: __ftocParse};
else {
  const originalLoad = X.prototype.onload;
  X.prototype.onload = async function () {
    const app = this.app, texts = new Map();
    __ftocNotes.set(app, texts);
    const active = app.workspace.getActiveFile();
    if (active?.extension === 'md') texts.set(active.path, await app.vault.cachedRead(active));
    await originalLoad.call(this);
    let disposed = false, revision = 0;
    this.register(() => { disposed = true; revision++; __ftocNotes.delete(app); });
    const refresh = async (file, data) => {
      if (!file || file.extension !== 'md') return;
      const request = ++revision;
      try {
        const content = typeof data === 'string' ? data : await app.vault.cachedRead(file);
        if (disposed || request !== revision) return;
        texts.set(file.path, content);
        const view = app.workspace.getActiveViewOfType(T.MarkdownView);
        if (!view || view.file?.path !== file.path) return;
        this.currentFile = file.path;
        const ignored = new Set((this.settings.ignoreHeaders || '').split('\n'));
        this.headingdata = __ftocCache(app, file).headings.filter(h => !ignored.has(String(h.level)));
        if (!this.headingdata.length) { F(); return; }
        if (!N(this, view)) V(app, this);
      } catch (error) { console.error('Floating TOC callout refresh failed', error); }
    };
    this.registerEvent(app.workspace.on('active-leaf-change', () => {
      const view = app.workspace.getActiveViewOfType(T.MarkdownView);
      if (view?.file) void refresh(view.file);
    }));
    this.registerEvent(app.metadataCache.on('changed', (file, data) => {
      if (file.path === app.workspace.getActiveFile()?.path) void refresh(file, data);
      else texts.delete(file.path);
    }));
    this.registerEvent(app.vault.on('delete', file => texts.delete(file.path)));
    this.registerEvent(app.vault.on('rename', (file, old) => {
      texts.delete(old);
      if (file.path === app.workspace.getActiveFile()?.path) void refresh(file);
    }));
    await refresh(app.workspace.getActiveFile());
  };
  // Rebuild by stable source line, so duplicate author labels remain distinct
  // when edits insert or remove lines above them.
  X.prototype.updateOutlineLineNumbers = function (view, headings) {
    this.headingdata = headings;
    if (!N(this, view)) V(this.app, this);
  };
}
