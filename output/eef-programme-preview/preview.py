"""Preview the saved note against the vault stylesheet, with Obsidian callout DOM."""
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
import html
import re
from markdown_it import MarkdownIt
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[2]
NOTE = ROOT / 'wiki/facts/uk/1stClass@Number 1.md'
CSS = ROOT / '.obsidian/snippets/argument-callouts.css'

def render(theme, expanded):
    text = NOTE.read_text()
    text = re.sub(r'\A---\n.*?\n---\n', '', text, count=1, flags=re.S)
    text = re.sub(r'\[\[([^\]|]+)(?:\\?\|([^\]]+))?\]\]', lambda m: f'[{m[2] or m[1]}](#{m[1].replace(" ", "-")})', text)
    soup = BeautifulSoup(MarkdownIt('commonmark').enable('table').render(text), 'html.parser')
    for block in reversed(soup.find_all('blockquote')):
        first = block.find('p', recursive=False)
        if first is None:
            continue
        marker = first.contents[0] if first.contents else ''
        match = re.match(r'\[!([\w-]+)(?:\|([^\]]*))?\]([-+]?)\s*', str(marker))
        if not match:
            continue
        title_html, _, body_start = first.decode_contents()[match.end():].partition('\n')
        first.extract()
        block.name = 'div'
        collapsed = match[3] == '-' and not expanded
        block['class'] = ['callout'] + (['is-collapsible'] if match[3] else []) + (['is-collapsed'] if collapsed else [])
        block['data-callout'] = match[1]
        if match[2]: block['data-callout-metadata'] = match[2]
        content = soup.new_tag('div', attrs={'class': 'callout-content'})
        if body_start.strip():
            intro = soup.new_tag('p'); intro.append(BeautifulSoup(body_start, 'html.parser')); content.append(intro)
        for child in list(block.contents): content.append(child.extract())
        title = soup.new_tag('div', attrs={'class': 'callout-title', 'tabindex': '0', 'role': 'button', 'aria-expanded': str(not collapsed).lower()})
        if match[3]:
            fold = soup.new_tag('span', attrs={'class': 'callout-fold'}); fold.string = '▸' if collapsed else '▾'; title.append(fold)
        inner = soup.new_tag('div', attrs={'class': 'callout-title-inner'})
        inner.append(BeautifulSoup(title_html, 'html.parser'))
        title.append(inner); block.append(title); block.append(content)
    return f'''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>1stClass@Number 1</title>
<style>
:root{{--font-text:-apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif;--background-primary:#fff;--background-secondary:#f5f5f3;--text-normal:#242521;--text-muted:#62645f;--background-modifier-border:#dcded8;--ac-paper:#fafaf7;--ac-raised:#fff;--ac-hair:#dcded8;--ac-hair-soft:#e9eae5;--ac-muted:#62645f;--ac-sans:var(--font-text);--ac-serif:Georgia,"Songti SC",serif}}
body.theme-dark{{--background-primary:#202020;--background-secondary:#292929;--text-normal:#e2e2df;--text-muted:#aaa9a4;--background-modifier-border:#454641;--ac-paper:#252622;--ac-raised:#2b2c27;--ac-hair:#454641;--ac-hair-soft:#383a34;--ac-muted:#aaa9a4}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--background-primary);color:var(--text-normal);font:16px/1.8 var(--font-text)}}article{{max-width:1060px;margin:auto;padding:32px 24px}}h1{{font-size:28px}}h2{{font-size:22px;margin-top:2em}}h3{{font-size:17px}}a{{color:inherit}}.callout-title{{display:flex;align-items:center}}.callout-title-inner{{flex:1}}.callout.is-collapsed>.callout-content{{display:none}}.callout.is-collapsible>.callout-title{{cursor:pointer}}table{{border-collapse:collapse;width:100%}}th,td{{padding:8px;text-align:left}}p{{margin:1em 0}}@media(max-width:600px){{article{{padding:20px 12px}}}}
</style><link rel="stylesheet" href="/argument-callouts.css"><body class="theme-{theme}"><article class="markdown-preview-view markdown-rendered"><h1>1stClass@Number 1</h1>{soup}</article>
<script>document.querySelectorAll('.callout.is-collapsible>.callout-title').forEach(t=>{{function toggle(){{const b=t.parentElement;b.classList.toggle('is-collapsed');t.setAttribute('aria-expanded',!b.classList.contains('is-collapsed'));t.querySelector('.callout-fold').textContent=b.classList.contains('is-collapsed')?'▸':'▾'}}t.onclick=toggle;t.onkeydown=e=>{{if(e.key==='Enter'||e.key===' '){{e.preventDefault();toggle()}}}}}});window.onload=()=>document.querySelector('[data-callout="eef-programme"]').scrollIntoView({{block:'start'}});</script></body></html>'''

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed=urlsplit(self.path); q=parse_qs(parsed.query)
        if parsed.path == '/argument-callouts.css':
            content=CSS.read_bytes(); kind='text/css'
        elif parsed.path == '/content':
            content=render(q.get('theme',['light'])[0],q.get('expanded',['0'])[0]=='1').encode(); kind='text/html'
        else:
            width=int(q.get('width',['1060'])[0]); theme=q.get('theme',['light'])[0]; expanded=q.get('expanded',['0'])[0]
            source=f'/content?theme={theme}&expanded={expanded}'
            content=f'''<!doctype html><meta charset="utf-8"><title>EEF 项目条目预览</title><style>body{{margin:0;background:#80817e;display:grid;justify-content:center}}iframe{{border:0;width:{width}px;max-width:100vw;height:1450px}}</style><iframe title="1stClass@Number 1 条目" src="{html.escape(source)}"></iframe>'''.encode();kind='text/html'
        self.send_response(200);self.send_header('Content-Type',kind+'; charset=utf-8');self.end_headers();self.wfile.write(content)

if __name__=='__main__':HTTPServer(('127.0.0.1',8767),Handler).serve_forever()
