"""Apply the local callout adapter to Floating TOC 2.7.1; safe to run again."""
from pathlib import Path
import hashlib

root = Path(__file__).resolve().parents[1]
plugin = root / '.obsidian/plugins/floating-toc/main.js'
adapter = (root / 'scripts/floating_toc_callouts.js').read_text()
source = plugin.read_text()
marker = '\n/* LOCAL FLOATING TOC CALLOUT ADAPTER */\n'
installed = source.split(marker, 1)[0] if marker in source else None
prefix_record = root / 'tmp/floating-toc-callouts/patched-prefix.sha256'
if installed is not None and prefix_record.exists():
    if hashlib.sha256(installed.encode()).hexdigest() != prefix_record.read_text().strip():
        raise SystemExit('Installed plugin has other local changes; inspect before updating.')
backup = root / 'tmp/floating-toc-callouts/main.original-2.7.1.js'
backup.parent.mkdir(parents=True, exist_ok=True)
if installed is not None:
    source = backup.read_text()
if backup.exists() and backup.read_text() != source:
    raise SystemExit('Backup differs from installed plugin; inspect before patching.')
backup.write_text(source)
replacements = {
    'i.app.metadataCache.getFileCache(y)': '__ftocCache(i.app,y)',
    'i.metadataCache.getFileCache(l)': '__ftocCache(i,l)',
    'this.app.metadataCache.getFileCache(a)': '__ftocCache(this.app,a)',
    'this.app.metadataCache.getFileCache(o)': '__ftocCache(this.app,o)',
    '_e=(i,e)=>{i.leaf.openFile(i.file,{eState:{line:e}})}': '_e=(i,e)=>{__ftocNavigate(i,e)}',
    'a.addClass("heading-list-item"),a.setAttribute("data-level"':
        'a.addClass("heading-list-item"),n.__ftocCallout&&a.setAttribute("data-ftoc-callout",n.__ftocCallout),a.setAttribute("data-level"',
    'function ke(i,e,t,n,o){!i.settings.enableDragReorder':
        'function ke(i,e,t,n,o){if(i.headingdata?.some(h=>h.__ftocCallout))return;!i.settings.enableDragReorder',
    'requestAnimationFrame(()=>{w.scrollIntoView({block:"nearest",behavior:"smooth"})})':
        'requestAnimationFrame(()=>{if(!c.some(h=>h.__ftocCallout))w.scrollIntoView({block:"nearest",behavior:"smooth"})})',
    'p.setAttribute("aria-label",t)': 'p.setAttribute("aria-label",__ftocLabel(t))',
    'if(m.ctrlKey||m.metaKey)Ue(e,L);else':
        'if((m.ctrlKey||m.metaKey)&&!i.headingdata?.some(h=>h.__ftocCallout))Ue(e,L);else',
}
expected = [1, 2, 2, 1, 1, 1, 1, 1, 1, 1]
for (old, new), count in zip(replacements.items(), expected):
    actual = source.count(old)
    if actual != count:
        raise SystemExit(f'Unsupported plugin build: expected {count} matches, got {actual}: {old}')
    source = source.replace(old, new)
plugin.write_text(source + marker + adapter)
prefix_record.write_text(hashlib.sha256(source.encode()).hexdigest() + '\n')
styles = plugin.with_name('styles.css')
css_marker = '\n/* LOCAL FLOATING TOC CALLOUT BADGES */\n'
css = styles.read_text().split(css_marker, 1)[0]
styles.write_text(css + css_marker + (root / 'scripts/floating_toc_callouts.css').read_text())
print('Installed Floating TOC callout adapter.')
print('Original SHA256:', hashlib.sha256(backup.read_bytes()).hexdigest())
print('Backup:', backup)
