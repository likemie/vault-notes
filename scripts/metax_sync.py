#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
metax_sync.py

Maintain Visible Learning MetaX data and the generated `## Visible Learning MetaX`
module in wiki entries.

Data (outside wiki/, never linked or indexed):
  metax/metax.json   studies (bibliographic data, match state) + influences
                     (overview figures, per-influence rows, mapped entries)
  metax/errata.json  study-level and influence-level corrections with sources

Cards show only APA short citations and figures. Titles, journals and full author
lists stay in metax.json. A study is linked to an Argument only when year, first
author and title agree with citation/citation_full.json; author-year matches with
a different title are recorded as collisions and never linked.

Subcommands:
  import   --overview MD --factors MD   build metax.json from the scraped tables
  match                                 match studies against citation_full.json
  render   [--check]                    write modules into mapped entries
  sync     [--check]                    match + render (called by vault_index.py)
  map      INFLUENCE_ID ENTRY_PATH...   attach an influence to entries
  unmap    INFLUENCE_ID [ENTRY_PATH...] detach
  suggest                               influences whose name equals an entry title/alias
  report                                matched / collision / review summary
  audit                                 suspected data errors -> metax/audit.json (leads, not errata)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "metax"
DATA_JSON = DATA_DIR / "metax.json"
ERRATA_JSON = DATA_DIR / "errata.json"
CITATION_FULL = ROOT / "citation/citation_full.json"
WIKI_INDEX = ROOT / "wiki/index.json"

SECTION = "## Visible Learning MetaX"
TAG = "metax"
CIRCLED = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳"
FLAG = "⚑"
OVERVIEW_FIELDS = ["domain", "sub_domain", "impact", "ma", "k", "n", "m", "d", "rob"]
ROW_FIELDS = ["var", "k", "n", "m", "d"]
FIELD_LABELS = {
    "domain": "领域", "sub_domain": "子领域", "impact": "影响判定", "ma": "元分析数",
    "k": "研究数", "n": "学生数", "m": "效应数", "d": "效应量", "rob": "稳健性",
    "var": "变量", "author": "作者", "year": "年份", "title": "篇名", "classification": "归类",
}

WIKILINK_RE = re.compile(r"\[\[([^\]|\\]+)(?:\\?\|([^\]]+))?\]\]")


# ----------------------------------------------------------------- helpers
def load_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def strip_links(text: str) -> str:
    return WIKILINK_RE.sub(lambda m: m.group(2) or m.group(1), text)


def fold(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    return "".join(c for c in text if not unicodedata.combining(c)).casefold()


def norm_alnum(text: str) -> str:
    return re.sub(r"[^0-9a-z一-鿿]", "", fold(text))


def words(text: str) -> list[str]:
    return [w for w in re.findall(r"[0-9a-z一-鿿]+", fold(text)) if len(w) > 3]


def to_int(value: str):
    value = value.strip().replace(",", "")
    if not value or value.upper() == "NA":
        return None
    try:
        return int(float(value))
    except ValueError:
        return None


def to_float(value: str):
    value = value.strip().replace(",", "")
    if not value or value.upper() == "NA":
        return None
    try:
        return float(value)
    except ValueError:
        return None


def fmt_int(v) -> str:
    return "NA" if v is None else f"{v:,}"


def fmt_d(v) -> str:
    return "NA" if v is None else f"{v:.2f}"


def table_cells(line: str) -> list[str]:
    return [c.strip() for c in strip_links(line).strip().strip("|").split("|")]


# ----------------------------------------------------------------- authors / APA
INITIALS_RE = re.compile(r"^(?:[A-Z]\.?\s*-?)+$")


def parse_authors(raw: str) -> tuple[list[str], bool]:
    s = raw.strip()
    etal = bool(re.search(r"\bet al\.?", s))
    s = re.sub(r"\bet al\.?", "", s)
    s = re.sub(r"\s+and\s+", ",", s)
    s = s.replace("&", ",").replace(";", ",")
    s = re.sub(r"(?<=[a-z]{2})\.\s+(?=[A-Z])", ",", s)  # "Ogletree. Benson"
    names = []
    for tok in s.split(","):
        tok = tok.strip().strip(".").strip()
        if not tok or INITIALS_RE.match(tok + "."):
            continue
        names.append(tok)
    return names, etal


def apa_names(names: list[str], etal: bool, shown: int) -> str:
    if not names:
        return "Anonymous"
    if len(names) == 1 and not etal:
        return names[0]
    if len(names) == 2 and not etal:
        return f"{names[0]} & {names[1]}"
    if shown >= len(names) and not etal:
        return ", ".join(names[:-1]) + ", & " + names[-1]
    return ", ".join(names[:shown]) + (", et al." if shown > 1 else " et al.")


def vault_cites(full: dict) -> dict[str, str]:
    """narrative cite (folded) -> argument, for every Argument in the vault."""
    out = {}
    for key, item in full.items():
        for alias in item.get("aliases", []):
            if alias.endswith(")"):
                out[fold(alias)] = item["argument"]
    return out


def assign_apa(studies: dict, full: dict) -> None:
    """APA 7 short cites, unique across MetaX and the vault.

    Different works whose cites collide list more authors (APA 7, 8.18); identical
    author lists get a/b suffixes ordered by title. Studies matched to an Argument
    reuse that Argument's narrative cite.
    """
    taken = vault_cites(full)
    meta = arguments_from_full(full)
    pending = {}
    for sid, st in studies.items():
        if st.get("argument"):
            st["apa"] = (meta.get(st["argument"]) or {}).get("narrative") or st.get("apa", "")
            continue
        pending[sid] = 1
    for _ in range(8):
        groups: dict[str, list[str]] = {}
        for sid, shown in pending.items():
            st = studies[sid]
            cite = f"{apa_names(st['authors'], st['etal'], shown)} ({st['year']})"
            groups.setdefault(fold(cite), []).append(sid)
        changed = False
        for key, sids in groups.items():
            clash_vault = key in taken
            if len(sids) == 1 and not clash_vault:
                continue
            for sid in sids:
                st = studies[sid]
                limit = len(st["authors"])
                if pending[sid] < limit:
                    pending[sid] += 1
                    changed = True
        if not changed:
            break
    final: dict[str, list[str]] = {}
    for sid, shown in pending.items():
        st = studies[sid]
        name = apa_names(st["authors"], st["etal"], shown)
        final.setdefault(fold(f"{name} ({st['year']})"), []).append(sid)
        st["_name"] = name
    for key, sids in final.items():
        if len(sids) == 1 and key not in taken:
            st = studies[sids[0]]
            st["apa"] = f"{st['_name']} ({st['year']})"
        else:
            sids.sort(key=lambda s: fold(studies[s]["title"]))
            for i, sid in enumerate(sids):
                st = studies[sid]
                st["apa"] = f"{st['_name']} ({st['year']}{chr(97 + i)})"
    for st in studies.values():
        st.pop("_name", None)


# ----------------------------------------------------------------- import
def slug_from_url(url: str) -> str:
    return url.rstrip("/").rsplit("/", 1)[-1]


def parse_overview(path: Path) -> dict:
    out = {}
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if not line.startswith("| ") or line.startswith("| Influence") or line.startswith("| ---"):
            continue
        c = table_cells(line)
        if len(c) < 11:
            continue
        iid = slug_from_url(c[10])
        out[iid] = {
            "name": c[0], "domain": c[1], "sub_domain": c[2], "impact": c[3],
            "ma": to_int(c[4]), "k": to_int(c[5]), "n": to_int(c[6]), "m": to_int(c[7]),
            "d": to_float(c[8]), "rob": to_int(c[9]), "url": c[10],
        }
    return out


def parse_factors(path: Path):
    blocks = {}
    cur = None
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if line.startswith("### "):
            cur = {"name": line[4:].strip(), "rows": [], "total": None, "url": None}
            continue
        if cur is None:
            continue
        if line.startswith("- Detail page:"):
            cur["url"] = line.split(":", 1)[1].strip()
            blocks[slug_from_url(cur["url"])] = cur
        elif line.startswith("- Source TOTAL/AVERAGE row:"):
            c = [x.strip() for x in line.split(":", 1)[1].split("|")]
            if len(c) >= 5:
                cur["total"] = {"k": to_int(c[1]), "n": to_int(c[2]), "m": to_int(c[3]), "d": to_float(c[4])}
        elif line.startswith("| ") and not line.startswith("| Journal Title") and not line.startswith("| ---"):
            c = table_cells(line)
            if len(c) != 9:
                print(f"skip malformed row in {cur['name']}: {line[:80]}", file=sys.stderr)
                continue
            cur["rows"].append(c)
    return blocks


def cmd_import(args) -> int:
    old = load_json(DATA_JSON, {"studies": {}, "influences": {}})
    old_by_key = {(norm_alnum(s["title"]), s["year"]): (sid, s) for sid, s in old["studies"].items()}
    overview = parse_overview(Path(args.overview))
    factors = parse_factors(Path(args.factors))

    studies: dict[str, dict] = {}
    key_to_sid: dict[tuple, str] = {}
    next_no = 1 + max([int(s[1:]) for s in old["studies"]] or [0])
    influences = {}
    for iid, ov in overview.items():
        fb = factors.get(iid, {"rows": [], "total": None})
        rows = []
        for c in fb["rows"]:
            journal, author_raw, title, year, var, k, n, m, d = c
            year = year.strip()
            key = (norm_alnum(title), year)
            sid = key_to_sid.get(key)
            if sid is None:
                if key in old_by_key:
                    sid, prev = old_by_key[key]
                else:
                    sid, prev = f"S{next_no:04d}", {}
                    next_no += 1
                names, etal = parse_authors(author_raw)
                studies[sid] = {
                    "authors": names, "etal": etal, "authors_raw": author_raw, "year": year,
                    "title": title, "journal": journal, "doi": prev.get("doi", ""),
                    "apa": prev.get("apa", ""), "argument": prev.get("argument"),
                    "match": prev.get("match"),
                }
                if prev.get("match") in {"manual", "reject"}:
                    studies[sid]["match"] = prev["match"]
                key_to_sid[key] = sid
            rows.append({"study": sid, "var": var, "k": to_int(k), "n": to_int(n), "m": to_int(m), "d": to_float(d)})
        prev_inf = old["influences"].get(iid, {})
        influences[iid] = {**ov, "source_total": fb["total"], "entries": prev_inf.get("entries", []), "rows": rows}

    data = {
        "_note": "Generated by scripts/metax_sync.py import; edit only entries, doi, argument and match (manual/reject).",
        "source": "https://www.visiblelearningmetax.com/influences",
        "collected": args.collected,
        "studies": dict(sorted(studies.items())),
        "influences": dict(sorted(influences.items())),
    }
    full = load_json(CITATION_FULL, {"items": {}})["items"]
    match_studies(data["studies"], full)
    assign_apa(data["studies"], full)
    dump_json(DATA_JSON, data)
    if not ERRATA_JSON.exists():
        dump_json(ERRATA_JSON, [])
    print(f"influences {len(influences)}, studies {len(studies)}, rows {sum(len(i['rows']) for i in influences.values())}")
    return 0


# ----------------------------------------------------------------- matching
def arguments_from_full(full: dict) -> dict[str, dict]:
    args = {}
    for key, item in full.items():
        a = args.setdefault(item["argument"], {**item, "narrative": None, "paren": None})
        for alias in item.get("aliases", []):
            if alias.endswith(")"):
                a["narrative"] = a["narrative"] or alias
            else:
                a["paren"] = a["paren"] or alias
    return args


def first_surname(arg: dict) -> str:
    authors = arg.get("authors") or []
    if not authors:
        return ""
    name = strip_links(str(authors[0]))
    return norm_alnum(name.split(",")[0])


def match_studies(studies: dict, full: dict) -> dict:
    args = arguments_from_full(full)
    by_year: dict[str, list[dict]] = {}
    for a in args.values():
        by_year.setdefault(str(a.get("year", "")), []).append(a)
    stats = {"matched": 0, "collision": 0, "review": 0}
    for sid, st in studies.items():
        if st.get("match") in {"manual", "reject"}:
            if st.get("argument") and st["argument"] not in args:
                st["argument"] = None
            continue
        st["argument"], st["match"] = None, None
        st.pop("collides_with", None)
        first = norm_alnum(st["authors"][0]) if st["authors"] else ""
        if not first:
            continue
        twords = set(words(st["title"]))
        tnorm = norm_alnum(st["title"])
        best = None
        for a in by_year.get(str(st["year"]), []):
            if first_surname(a) != first:
                continue
            cit = a.get("citation", "")
            if st.get("doi") and a.get("doi") and fold(st["doi"]) == fold(a["doi"]):
                best = ("doi", a, 1.0)
                break
            cnorm = norm_alnum(cit)
            cwords = set(words(cit))
            contain = len(twords & cwords) / len(twords) if twords else 0.0
            if len(tnorm) >= 12 and tnorm in cnorm:
                contain = 1.0
            if best is None or contain > best[2]:
                best = ("title", a, contain)
        if best is None:
            continue
        kind, a, score = best
        if kind == "doi" or score >= 0.9:
            st["argument"], st["match"] = a["argument"], kind
            stats["matched"] += 1
        elif score < 0.6:
            st["match"] = "collision"
            st["collides_with"] = a["argument"]
            stats["collision"] += 1
        else:
            st["match"] = "review"
            st["collides_with"] = a["argument"]
            stats["review"] += 1
    return stats


def cmd_match(args) -> int:
    data = load_json(DATA_JSON, None)
    full = load_json(CITATION_FULL, {"items": {}})["items"]
    stats = match_studies(data["studies"], full)
    assign_apa(data["studies"], full)
    dump_json(DATA_JSON, data)
    print(stats)
    return 0


# ----------------------------------------------------------------- render
def esc(text: str) -> str:
    return str(text).replace("|", "\\|")


def cite_cell(st: dict, args_meta: dict) -> str:
    arg = st.get("argument")
    if arg and arg in args_meta and args_meta[arg]["narrative"]:
        return f"[[{arg}\\|{args_meta[arg]['narrative']}]]"
    return st["apa"]


def source_link(arg: str, pages: str, args_meta: dict) -> str:
    meta = args_meta.get(arg)
    if not meta:
        return ""
    disp = meta["paren"] or meta["narrative"]
    if pages:
        disp = f"{disp}, {pages}"
    return f"[[{arg}|{disp}]]"


def fmt_value(field: str, value) -> str:
    if field == "d":
        return fmt_d(value)
    if field in {"ma", "k", "n", "m"}:
        return fmt_int(value)
    if field == "rob":
        return "NA" if value is None else f"{value}/5"
    return esc(value if value is not None else "NA")


def render_influence(iid: str, inf: dict, studies: dict, errata: list, args_meta: dict) -> str:
    own = [e for e in errata if e.get("influence") == iid]
    inf_err = [e for e in own if e.get("level") == "influence"]
    study_err = [e for e in own if e.get("level") == "study"]
    flags = {e.get("field") for e in inf_err}

    lines = [f"> [!metax] [{esc(inf['name'])}]({inf['url']})"]
    lines.append("> | dom | sub | impact | ma | k | n | m | d | rob |")
    lines.append("> | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    cells = []
    for f in OVERVIEW_FIELDS:
        v = fmt_value(f, inf.get(f))
        cells.append(f"{v} {FLAG}" if f in flags else v)
    lines.append("> | " + " | ".join(cells) + " |")

    marks: dict[str, list[str]] = {}
    numbered = []
    for i, e in enumerate(study_err):
        mark = CIRCLED[i] if i < len(CIRCLED) else f"({i + 1})"
        marks.setdefault(e.get("study", ""), []).append(mark)
        numbered.append((mark, e))

    lines.append(">")
    lines.append(f"> > [!metax-ma]- {len(inf['rows'])}")
    lines.append("> > | ref | var | k | n | m | d | e |")
    lines.append("> > | --- | --- | --- | --- | --- | --- | --- |")
    for r in inf["rows"]:
        st = studies[r["study"]]
        e = "".join(marks.get(r["study"], []) + marks.get(st["apa"], []))
        lines.append(
            "> > | " + " | ".join([
                cite_cell(st, args_meta), esc(r["var"]), fmt_int(r["k"]), fmt_int(r["n"]),
                fmt_int(r["m"]), fmt_d(r["d"]), e,
            ]) + " |"
        )

    if own:
        lines.append(">")
        lines.append(f"> > [!metax-errata] {len(own)}")
        for e in inf_err:
            lines.append("> > - " + errata_line(FLAG, "整合", e, None, args_meta))
        for mark, e in numbered:
            sid = e.get("study", "")
            st = studies.get(sid) or next((s for s in studies.values() if s["apa"] == sid), None)
            lines.append("> > - " + errata_line(mark, "单篇", e, st, args_meta))
    return "\n".join(lines)


def errata_line(mark: str, level: str, e: dict, st, args_meta: dict) -> str:
    parts = [f"{mark} **{level} · {e.get('type', '')}**"]
    field = FIELD_LABELS.get(e.get("field", ""), e.get("field", ""))
    who = f"{st['apa']} 的" if st else ""
    if e.get("metax") is not None or e.get("corrected") is not None:
        seg = f"{who}{field}：MetaX 记为 {e.get('metax', 'NA')}"
        if e.get("corrected") is not None:
            seg += f"，应为 {e['corrected']}"
        parts.append(seg + "。")
    elif who or field:
        parts.append(f"{who}{field}。")
    if e.get("note"):
        parts.append(e["note"])
    link = source_link(e.get("source", ""), e.get("pages", ""), args_meta)
    if link:
        parts.append(f"（{link}）")
    return " ".join(parts)


def render_module(iids: list[str], data: dict, errata: list, args_meta: dict) -> str:
    blocks = [render_influence(i, data["influences"][i], data["studies"], errata, args_meta) for i in iids]
    return SECTION + "\n\n" + "\n\n".join(blocks) + "\n"


SECTION_RE = re.compile(r"^## Visible Learning MetaX\n.*?(?=^---\n\n## |^## (?!Visible Learning MetaX)|\Z)", re.M | re.S)


def remove_module(body: str) -> str:
    m = SECTION_RE.search(body)
    if not m:
        return body
    end = m.end()
    rest = body[end:]
    if rest.startswith("---\n\n"):
        rest = rest[5:]
    return body[: m.start()] + rest


def insert_module(body: str, module: str) -> str:
    body = remove_module(body)
    block = module.rstrip("\n") + "\n\n---\n\n"
    lines = body.splitlines(keepends=True)
    h2 = [i for i, l in enumerate(lines) if l.startswith("## ")]
    target = None
    for n, i in enumerate(h2):
        if lines[i].strip() == "## 实证数据":
            target = h2[n + 1] if n + 1 < len(h2) else None
            break
    if target is None:
        for i in h2:
            if lines[i].strip() in {"## 相关研究", "## 领域应用"}:
                target = i
                break
    if target is None:
        return body.rstrip("\n") + "\n\n---\n\n" + module
    # Keep the separator that precedes the next section in front of the module.
    return "".join(lines[:target]) + block + "".join(lines[target:])


def set_tag(text: str, present: bool) -> str:
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return text
    fm = m.group(1)
    has = re.search(rf"^  - {TAG}$", fm, re.M) or re.search(rf"^tags: \[.*\b{TAG}\b.*\]$", fm, re.M)
    if present and not has:
        if re.search(r"^tags: \[\]$", fm, re.M):
            fm = re.sub(r"^tags: \[\]$", f"tags:\n  - {TAG}", fm, flags=re.M)
        elif re.search(r"^tags:\s*$", fm, re.M):
            fm = re.sub(r"^(tags:\s*\n(?:  - .*\n?)*)", lambda x: x.group(1).rstrip("\n") + f"\n  - {TAG}\n", fm + "\n", count=1, flags=re.M).rstrip("\n")
        else:
            fm += f"\ntags:\n  - {TAG}"
    elif not present and has:
        fm = re.sub(rf"^  - {TAG}\n?", "", fm + "\n", flags=re.M).rstrip("\n")
        fm = re.sub(r"^tags:\s*$(?!\n  - )", "tags: []", fm, flags=re.M)
    return f"---\n{fm}\n---\n" + text[m.end():]


def cmd_render(args, data=None) -> int:
    if data is None:
        data = load_json(DATA_JSON, None)
    if data is None:
        return 0
    errata = load_json(ERRATA_JSON, [])
    args_meta = arguments_from_full(load_json(CITATION_FULL, {"items": {}})["items"])
    by_entry: dict[str, list[str]] = {}
    for iid, inf in data["influences"].items():
        for p in inf.get("entries", []):
            by_entry.setdefault(p, []).append(iid)
    # Entries that still carry a module but are no longer mapped.
    for path in (ROOT / "wiki").rglob("*.md"):
        rel = path.relative_to(ROOT).as_posix()
        if rel not in by_entry and "templates" not in path.parts:
            t = path.read_text(encoding="utf-8")
            if "\n" + SECTION + "\n" in t:
                by_entry[rel] = []
    stale = []
    for rel, iids in sorted(by_entry.items()):
        path = ROOT / rel
        if not path.exists():
            print(f"missing entry: {rel}", file=sys.stderr)
            continue
        text = path.read_text(encoding="utf-8")
        iids.sort(key=lambda i: fold(data["influences"][i]["name"]))
        if iids:
            new = insert_module(text, render_module(iids, data, errata, args_meta))
        else:
            new = remove_module(text)
        new = set_tag(new, bool(iids))
        if new != text:
            stale.append(rel)
            if not args.check:
                path.write_text(new, encoding="utf-8")
    verb = "stale" if args.check else "updated"
    for rel in stale:
        print(f"{verb}: {rel}")
    return 1 if (args.check and stale) else 0


def cmd_sync(args) -> int:
    if not DATA_JSON.exists():
        return 0
    if not args.check:
        cmd_match(args)
        return cmd_render(args)
    # Check mode: re-match in memory so a newly added Argument that MetaX cites
    # is reported as stale until vault_index.py regenerates the modules.
    data = load_json(DATA_JSON, None)
    full = load_json(CITATION_FULL, {"items": {}})["items"]
    before = json.dumps(data["studies"], sort_keys=True)
    match_studies(data["studies"], full)
    assign_apa(data["studies"], full)
    code = cmd_render(args, data)
    if json.dumps(data["studies"], sort_keys=True) != before:
        print("stale: metax/metax.json (study matches changed)")
        code = 1
    return code


# ----------------------------------------------------------------- mapping
def resolve_entry(p: str) -> str:
    path = Path(p)
    if not path.is_absolute():
        path = ROOT / p
    return path.resolve().relative_to(ROOT).as_posix()


def cmd_map(args) -> int:
    data = load_json(DATA_JSON, None)
    inf = data["influences"].get(args.influence)
    if inf is None:
        print(f"unknown influence id: {args.influence}", file=sys.stderr)
        return 2
    for p in args.entries:
        rel = resolve_entry(p)
        if rel not in inf["entries"]:
            inf["entries"].append(rel)
    dump_json(DATA_JSON, data)
    return cmd_render(argparse.Namespace(check=False))


def cmd_unmap(args) -> int:
    data = load_json(DATA_JSON, None)
    inf = data["influences"][args.influence]
    drop = {resolve_entry(p) for p in args.entries} if args.entries else set(inf["entries"])
    inf["entries"] = [e for e in inf["entries"] if e not in drop]
    dump_json(DATA_JSON, data)
    return cmd_render(argparse.Namespace(check=False))


def cmd_suggest(args) -> int:
    data = load_json(DATA_JSON, None)
    index = load_json(WIKI_INDEX, [])
    names = {}
    for e in index:
        if e.get("type") in {"concept", "theory", "method", "instrument"}:
            for n in [e["title"], *e.get("aliases", [])]:
                names.setdefault(fold(n), e["path"])
    for iid, inf in data["influences"].items():
        hit = names.get(fold(inf["name"]))
        if hit and hit not in inf["entries"]:
            print(f"{iid}\t{inf['name']}\t{hit}")
    return 0


def cmd_audit(args) -> int:
    """Flag suspected MetaX data errors. Findings are leads, not errata: move a
    finding into metax/errata.json only after checking it against a source."""
    data = load_json(DATA_JSON, None)
    st, inf = data["studies"], data["influences"]
    out = []
    by_title: dict[str, list[str]] = {}
    for sid, s_ in st.items():
        by_title.setdefault(norm_alnum(s_["title"]), []).append(sid)
    for sids in by_title.values():
        if len(sids) > 1:
            desc = "; ".join(f"{i} {st[i]['authors_raw']} {st[i]['year']}" for i in sids)
            out.append({"check": "same_title_diff_author_or_year", "studies": sids, "detail": desc})
    for iid, i in inf.items():
        seen: dict[tuple, str] = {}
        for r in i["rows"]:
            if r["k"] is None or r["d"] is None:
                continue
            key = (r["k"], r["m"], r["d"])
            if key in seen and seen[key] != r["study"]:
                a, b = st[seen[key]]["apa"], st[r["study"]]["apa"]
                out.append({"check": "duplicate_row_values", "influence": iid, "studies": [seen[key], r["study"]],
                            "detail": f"{a} / {b}: k={r['k']} m={r['m']} d={r['d']}"})
            seen.setdefault(key, r["study"])
        if i["ma"] is not None and i["ma"] != len(i["rows"]):
            out.append({"check": "ma_count_vs_rows", "influence": iid, "detail": f"ma={i['ma']} rows={len(i['rows'])}"})
        tot = i.get("source_total") or {}
        for f in ("k", "n", "m"):
            rows_sum = sum(r[f] or 0 for r in i["rows"])
            if i.get(f) is not None and rows_sum and i[f] != rows_sum:
                out.append({"check": f"overview_{f}_vs_row_sum", "influence": iid, "detail": f"overview={i[f]} rows={rows_sum}"})
        if tot.get("d") is not None and i.get("d") is not None and abs(tot["d"] - i["d"]) > 0.015:
            out.append({"check": "overview_d_vs_source_total", "influence": iid, "detail": f"overview={i['d']} total={tot['d']}"})
    dump_json(DATA_DIR / "audit.json", out)
    counts: dict[str, int] = {}
    for f in out:
        counts[f["check"]] = counts.get(f["check"], 0) + 1
    print(counts, "-> metax/audit.json")
    return 0


def cmd_report(args) -> int:
    data = load_json(DATA_JSON, None)
    counts: dict[str, int] = {}
    for sid, st in data["studies"].items():
        counts[st.get("match") or "none"] = counts.get(st.get("match") or "none", 0) + 1
        if st.get("match") in {"collision", "review"} or (st.get("argument") and args.verbose):
            print(f"{st.get('match')}\t{sid}\t{st['apa']}\t{st['title'][:70]}\t-> {st.get('argument') or st.get('collides_with')}")
    mapped = sum(1 for i in data["influences"].values() if i["entries"])
    print(counts, f"mapped influences: {mapped}/{len(data['influences'])}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("import")
    p.add_argument("--overview", required=True)
    p.add_argument("--factors", required=True)
    p.add_argument("--collected", default="")
    p.set_defaults(func=cmd_import)
    sub.add_parser("match").set_defaults(func=cmd_match)
    for name, fn in (("render", cmd_render), ("sync", cmd_sync)):
        p = sub.add_parser(name)
        p.add_argument("--check", action="store_true")
        p.set_defaults(func=fn)
    p = sub.add_parser("map")
    p.add_argument("influence")
    p.add_argument("entries", nargs="+")
    p.set_defaults(func=cmd_map)
    p = sub.add_parser("unmap")
    p.add_argument("influence")
    p.add_argument("entries", nargs="*")
    p.set_defaults(func=cmd_unmap)
    sub.add_parser("suggest").set_defaults(func=cmd_suggest)
    sub.add_parser("audit").set_defaults(func=cmd_audit)
    p = sub.add_parser("report")
    p.add_argument("--verbose", action="store_true")
    p.set_defaults(func=cmd_report)
    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
