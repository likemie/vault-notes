"""Exact sentence/target exclusions for ordinary wiki links; no semantic rules."""
from __future__ import annotations

import json
import contextlib
import fcntl
import re
import unicodedata
from collections import Counter
from pathlib import Path

LINK = re.compile(r'(?<!!)\[\[([^\]|#]+?)(?:#[^\]|]+)?(?:(?:\\\||\|)([^\]]+))?\]\]')


@contextlib.contextmanager
def registry_lock(root):
    path = root / 'output/link-exceptions.lock'
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a') as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        yield


def clean(root, registry, dry_run=False):
    with registry_lock(root):
        original = load(registry)
        active = prune(root, original)
        if active != original and not dry_run: save(registry, active)
    return original, active


def canonical(text):
    return unicodedata.normalize('NFC', re.sub(r'\s+', ' ', text).strip())


def visible_map(text):
    """Visible wiki labels with source offsets, so linking does not change identity."""
    chars, offsets = [], []
    cursor = 0
    for match in LINK.finditer(text):
        for pos in range(cursor, match.start()):
            chars.append(text[pos]); offsets.append((pos, pos + 1))
        label = match[2] if match[2] is not None else match[1]
        for char in label:
            chars.append(char); offsets.append((match.start(), match.end()))
        cursor = match.end()
    for pos in range(cursor, len(text)):
        chars.append(text[pos]); offsets.append((pos, pos + 1))
    return ''.join(chars), offsets


def sentences(body):
    """Sentence units never cross a line or table cell; preserve raw offsets."""
    visible, offsets = visible_map(body)
    # English full stops split only before whitespace/end, not within decimals/URLs.
    for match in re.finditer(r'[^\n|。！？!?]+(?:[。！？!?][”’」』\"\']*|(?=\n|\||$))', visible):
        start, end = match.span()
        unit = visible[start:end]
        prefix = re.match(r'^\s*(?:>\s*)*(?:(?:[-*+] |\d+[.)] )|#{1,6} )?', unit)
        start += prefix.end()
        while end > start and visible[end - 1].isspace(): end -= 1
        if start == end: continue
        for part in re.finditer(r'.+?(?:\.(?=\s|$)|$)', visible[start:end]):
            a, b = start + part.start(), start + part.end()
            while a < b and visible[a].isspace(): a += 1
            if a < b:
                yield canonical(visible[a:b]), offsets[a][0], offsets[b - 1][1]


def body_of(text):
    return re.sub(r'\A---\s*\n.*?\n---\s*\n', '', text, count=1, flags=re.S)


def valid_path(name):
    if not isinstance(name, str): return False
    path = Path(name)
    return (isinstance(name, str) and name.startswith('wiki/') and path.suffix == '.md'
            and not path.is_absolute() and '..' not in path.parts and '\\' not in name
            and path.as_posix() == name and unicodedata.normalize('NFC', name) == name
            and 'templates' not in path.parts and 'indexes' not in path.parts)


def load(path):
    if not path.exists(): return {}
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result: raise ValueError(f'重复例外路径: {key}')
            result[key] = value
        return result
    data = json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=pairs)
    if not isinstance(data, dict): raise ValueError('链接例外表必须是 JSON 对象')
    for name, records in data.items():
        if not valid_path(name) or not isinstance(records, list): raise ValueError(f'无效例外路径: {name}')
        seen = set()
        for record in records:
            if (not isinstance(record, dict) or set(record) != {'sentence', 'target'}
                    or not isinstance(record['sentence'], str) or not record['sentence']
                    or canonical(record['sentence']) != record['sentence']
                    or not isinstance(record['target'], str) or not valid_path(record['target'])):
                raise ValueError(f'无效链接例外: {name}')
            key = record['sentence'], record['target']
            if key in seen: raise ValueError(f'重复链接例外: {name}')
            seen.add(key)
    return data


def save(path, data):
    temp = path.with_suffix('.json.tmp')
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temp.replace(path)


def prune(root, data):
    """Only confirmed absence expires records; read errors propagate, never delete."""
    kept = {}
    for name, records in data.items():
        path = root / name
        try: text = path.read_text(encoding='utf-8')
        except FileNotFoundError: continue
        units = {sentence for sentence, _, _ in sentences(body_of(text))}
        active = []
        for record in records:
            try: (root / record['target']).stat()
            except FileNotFoundError: continue
            if record['sentence'] in units: active.append(record)
        if active: kept[name] = active
    return kept


def mask(body, records, entries, boundary):
    """Hide only excluded occurrences before the unchanged ordinary-link pipeline."""
    if not records: return body, {}
    entries = list(entries)
    by_path = {e.path: e for e in entries if e.type in {'concept', 'theory', 'method', 'instrument', 'person', 'fact'}}
    units = list(sentences(body))
    counts = Counter(sentence for sentence, _, _ in units)
    if any(counts[r['sentence']] > 1 for r in records):
        raise ValueError('链接例外句子重复，请先改写区分或移除该例外')
    names = {}
    all_terms = []
    for entry in entries:
        for name in (entry.path, entry.path.removesuffix('.md'), entry.title, *entry.aliases):
            names.setdefault(canonical(name).casefold(), set()).add(entry.path)
        if entry.path in by_path:
            all_terms.extend((term, entry.path) for term in {entry.title, *entry.aliases} if term)
    protected = []
    # Preserve code, embeds, Markdown links and HTML; exclusions never edit these.
    for rx in (r'(?ms)^\s*(?:>\s*)?(`{3,}|~{3,})[^\n]*\n.*?^\s*(?:>\s*)?\1[^\n]*',
               r'`+[^`\n]*`+', r'!\[\[[^\]]*\]\]', r'!?\[[^\]]*\]\([^)]*\)', r'<[^>]*>'):
        protected.extend(m.span() for m in re.finditer(rx, body))
    spans = []
    for sentence, start, end in units:
        blocked = {r['target'] for r in records if r['sentence'] == sentence and r['target'] in by_path}
        if not blocked: continue
        raw = body[start:end]
        links = list(LINK.finditer(raw))
        for match in links:
            targets = names.get(canonical(match[1]).casefold(), set())
            if len(targets) == 1 and targets <= blocked:
                label = match[2] if match[2] is not None else match[1]
                spans.append((start + match.start(), start + match.end(), label))
        for target in blocked:
            entry = by_path.get(target)
            if entry is None: continue
            terms = sorted({entry.title, *entry.aliases}, key=len, reverse=True)
            for term in terms:
                for match in re.finditer(re.escape(term), raw, re.I):
                    if any(a.start() < match.end() and a.end() > match.start() for a in links): continue
                    if boundary(raw, match.start(), match.end(), term):
                        # Do not mask a short alias inside another target's longer term.
                        longer = False
                        for other, other_target in all_terms:
                            if other_target == target or len(other) <= len(term): continue
                            for candidate in re.finditer(re.escape(other), raw, re.I):
                                if (candidate.start() <= match.start() and candidate.end() >= match.end()
                                        and boundary(raw, candidate.start(), candidate.end(), other)):
                                    longer = True
                                    break
                            if longer: break
                        if longer: continue
                        spans.append((start + match.start(), start + match.end(), match[0]))
    selected = []
    for a, b, label in sorted(set(spans), key=lambda s: (s[0], -s[1])):
        if any(p < b and q > a for p, q in protected): continue
        if selected and a < selected[-1][1]: continue
        selected.append((a, b, label))
    prefix = '\ue100'
    while prefix in body: prefix += '\ue100'
    out, replacements, cursor = [], {}, 0
    for number, (a, b, label) in enumerate(selected):
        token = prefix + '\ue102' * (number + 1) + '\ue101'
        replacements[token] = label
        out.extend((body[cursor:a], token)); cursor = b
    out.append(body[cursor:])
    return ''.join(out), replacements


def restore(body, replacements):
    if not replacements: return body
    pattern = '|'.join(re.escape(t) for t in sorted(replacements, key=len, reverse=True))
    return re.sub(pattern, lambda m: replacements[m[0]], body)
