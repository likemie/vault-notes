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
  apply-mapping [--dry-run]             create stub entries and attach influences per metax/mapping.json
  report                                matched / collision / review summary
  domains                               VL-style domain summary + per-domain sub-domain callouts (Markdown)
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
ZH_JSON = DATA_DIR / "zh.json"
MAPPING_JSON = DATA_DIR / "mapping.json"
CITATION_FULL = ROOT / "citation/citation_full.json"
WIKI_INDEX = ROOT / "wiki/index.json"

SECTION = "## Visible Learning MetaX"
TAG = "metax"
CIRCLED = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳"
FLAG = "⚑"
OVERVIEW_FIELDS = ["impact", "ma", "k", "n", "m", "d", "du", "rob"]
ROW_FIELDS = ["var", "k", "n", "m", "d"]
FIELD_LABELS = {
    "domain": "领域", "sub_domain": "子领域", "impact": "影响判定", "ma": "元分析数",
    "k": "研究数", "n": "学生数", "m": "效应数", "d": "效应量", "rob": "稳健性",
    "du": "未加权平均效应量", "var": "变量", "author": "作者", "year": "年份", "title": "篇名", "classification": "归类",
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


def zh_table() -> dict:
    return load_json(ZH_JSON, {})


def impact_cell(impact: str, zh: dict) -> str:
    info = (zh.get("impact") or {}).get(impact)
    if not info:
        return esc(impact)
    n = info.get("stars", 0)
    if n < 0:
        return f"▼ {info['label']}"
    return "★" * n + "☆" * (4 - n) + f" {info['label']}"


def rob_cell(rob) -> str:
    if rob is None:
        return "NA"
    return "●" * rob + "○" * (5 - rob)


AUTO = "∑"


def weighted_d(rows: list[dict]):
    """MetaX overview d = mean of row d weighted by k (verified on all 440 influences)."""
    pairs = [(r["d"], r["k"]) for r in rows if r["d"] is not None and r["k"]]
    total = sum(k for _, k in pairs)
    return round(sum(d * k for d, k in pairs) / total, 2) if total else None


def simple_d(rows: list[dict]):
    """MetaX TOTAL/AVERAGE row d = unweighted mean of row d (verified on all 440 influences)."""
    ds = [r["d"] for r in rows if r["d"] is not None]
    return round(sum(ds) / len(ds), 2) if ds else None


def auto_checks(inf: dict, studies: dict, marked: set | None = None) -> list[str]:
    """Recompute the overview from the rows; return errata lines for real mismatches only.

    Checks: meta-analysis count; k / n / m sums against the overview and the MetaX
    TOTAL row; k-weighted mean d against the overview; unweighted mean d against
    the TOTAL row; suspected duplicate rows. Known properties of MetaX totals that
    hold for every influence (plain summing, NA excluded, overlap not removed) are
    explained once in the Visible Learning Meta-X fact entry, not per card."""
    rows = inf["rows"]
    out = []
    if inf.get("ma") is not None and inf["ma"] != len(rows):
        out.append(f"**自动核算 · 计数不符** 元分析数：总览 {inf['ma']}，列表实有 {len(rows)} 项。")
    src_total = inf.get("source_total") or {}
    for f in ("k", "n", "m"):
        if not any(r[f] is not None for r in rows):
            continue
        total = sum(r[f] or 0 for r in rows)
        if inf.get(f) is not None and inf[f] != total:
            out.append(f"**自动核算 · 加总不符** {FIELD_LABELS[f]}：总览 {fmt_int(inf[f])}，各项相加为 {fmt_int(total)}。")
        if src_total.get(f) is not None and src_total[f] != total:
            out.append(f"**自动核算 · 加总不符** {FIELD_LABELS[f]}：MetaX 合计行 {fmt_int(src_total[f])}，各项相加为 {fmt_int(total)}。")
    wd = weighted_d(rows)
    if wd is not None and inf.get("d") is not None and abs(wd - inf["d"]) > 0.011:
        out.append(f"**自动核算 · 效应量不符** 加权平均效应量：总览 {fmt_d(inf['d'])}，按研究数加权重算为 {fmt_d(wd)}。")
    sd = simple_d(rows)
    du = (inf.get("source_total") or {}).get("d")
    if sd is not None and du is not None and abs(sd - du) > 0.011:
        out.append(f"**自动核算 · 效应量不符** 未加权平均效应量：MetaX 合计行 {fmt_d(du)}，按列表重算为 {fmt_d(sd)}。")
    seen: dict[tuple, dict] = {}
    dup_rows = []
    for r in rows:
        if r["k"] is None or r["d"] is None:
            continue
        key = (r["k"], r["m"], r["d"])
        first = seen.get(key)
        if first is None:
            seen[key] = r
            continue
        same = first["study"] == r["study"]
        a, b = studies[first["study"]]["apa"], studies[r["study"]]["apa"]
        what = f"{a} 在列表中重复出现" if same else f"{a} 与 {b} 的研究数、效应数与效应量完全相同，疑为同一项元分析重复收录"
        dup_rows.append(r)
        if marked is not None:
            marked.update({id(first), id(r)})
        out.append(f"**自动核算 · 疑似重复** {what}。")
    if dup_rows:
        keep = [r for r in rows if r not in dup_rows]
        k = sum(r["k"] or 0 for r in keep)
        out.append(f"**自动核算 · 剔除重复后** 元分析 {len(keep)} 项，研究数 {fmt_int(k)}，加权平均效应量 {fmt_d(weighted_d(keep))}，未加权平均效应量 {fmt_d(simple_d(keep))}（仅供参考，尚未经文献核实）。")
    return out


def render_influence(iid: str, inf: dict, studies: dict, errata: list, args_meta: dict) -> str:
    zh = zh_table()
    own = [e for e in errata if e.get("influence") == iid]
    inf_err = [e for e in own if e.get("level") == "influence"]
    study_err = [e for e in own if e.get("level") == "study"]
    flags = {e.get("field") for e in inf_err}
    flag = lambda f, v: f"{v} {FLAG}" if f in flags else v

    name_zh = (zh.get("influences") or {}).get(iid, "")
    title = f"{name_zh} · {inf['name']}" if name_zh else inf["name"]
    domain = (zh.get("domain") or {}).get(inf["domain"], inf["domain"])
    sub = (zh.get("sub_domain") or {}).get(inf["sub_domain"], inf["sub_domain"])

    lines = [f"> [!metax] [{esc(title)}]({inf['url']})"]
    lines.append(f"> {flag('domain', esc(domain))} › {flag('sub_domain', esc(sub))}")
    lines.append(">")
    lines.append("> | rate | ma | k | n | m | d | du | rob |")
    lines.append("> | --- | --- | --- | --- | --- | --- | --- | --- |")
    cells = [
        flag("impact", impact_cell(inf.get("impact", ""), zh)),
        flag("ma", fmt_int(inf.get("ma"))),
        flag("k", fmt_int(inf.get("k"))),
        flag("n", fmt_int(inf.get("n"))),
        flag("m", fmt_int(inf.get("m"))),
        flag("d", fmt_d(inf.get("d"))),
        flag("du", fmt_d((inf.get("source_total") or {}).get("d") if (inf.get("source_total") or {}).get("d") is not None else simple_d(inf["rows"]))),
        flag("rob", rob_cell(inf.get("rob"))),
    ]
    lines.append("> | " + " | ".join(cells) + " |")

    marks: dict[str, list[str]] = {}
    numbered = []
    for i, e in enumerate(study_err):
        mark = CIRCLED[i] if i < len(CIRCLED) else f"({i + 1})"
        marks.setdefault(e.get("study", ""), []).append(mark)
        numbered.append((mark, e))

    marked: set = set()
    auto = auto_checks(inf, studies, marked)

    lines.append(">")
    lines.append(f"> > [!metax-ma]- {len(inf['rows'])} 项")
    lines.append("> > | ref | var | k | n | m | d | e |")
    lines.append("> > | --- | --- | --- | --- | --- | --- | --- |")
    for r in inf["rows"]:
        st = studies[r["study"]]
        e = "".join(marks.get(r["study"], []) + marks.get(st["apa"], []) + ([AUTO] if id(r) in marked else []))
        lines.append(
            "> > | " + " | ".join([
                cite_cell(st, args_meta), esc(r["var"]), fmt_int(r["k"]), fmt_int(r["n"]),
                fmt_int(r["m"]), fmt_d(r["d"]), e,
            ]) + " |"
        )

    # Errata appear only when there is something to report: sourced entries from
    # metax/errata.json, or mismatches found by recomputing the overview.
    if own or auto:
        lines.append(">")
        lines.append(f"> > [!metax-errata] {len(own) + len(auto)} 条")
        for a in auto:
            lines.append(f"> > - {AUTO} {a}")
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
    """The module is only the stacked [!metax] callouts: no heading of its own, so the
    vault does not fill up with identical "Visible Learning MetaX" sections."""
    blocks = [render_influence(i, data["influences"][i], data["studies"], errata, args_meta) for i in iids]
    return "\n\n".join(blocks) + "\n"


LEGACY_SECTION_RE = re.compile(r"^## Visible Learning MetaX\n.*?(?=^---\n\n## |^## (?!Visible Learning MetaX)|\Z)", re.M | re.S)
METAX_TOP_RE = re.compile(r"^> \[!metax\][^\n]*\n(?:>[^\n]*(?:\n|\Z))*\n*", re.M)


def remove_module(body: str) -> str:
    m = LEGACY_SECTION_RE.search(body)
    if m:  # modules written before 2026-10-22 had their own H2
        rest = body[m.end():]
        if rest.startswith("---\n\n"):
            rest = rest[5:]
        prefix = body[: m.start()]
        if not rest.strip():
            prefix = re.sub(r"(?:\n*---[ \t]*)+\s*\Z", "", prefix.rstrip()) + "\n"
        body = prefix + rest
    body = METAX_TOP_RE.sub("", body)
    return re.sub(r"\n{3,}", "\n\n", body)


def insert_module(body: str, module: str) -> str:
    """Place the callouts directly before the first empirical table callout (MetaX leads the
    empirical-data group); otherwise after the last empirical callout, before the 相关研究索引
    callout, or at the end of the note. Section headings are not used."""
    body = remove_module(body)
    lines = body.splitlines(keepends=True)
    # EEF blocks ([!eef], scripts/eef_sync.py) follow MetaX: if present, MetaX goes right before them.
    for i, l in enumerate(lines):
        if l.startswith("> [!eef]"):
            head = "".join(lines[:i]).rstrip("\n")
            return head + "\n\n" + module.rstrip("\n") + "\n\n" + "".join(lines[i:])
    # 实证数据组内 MetaX 排在最前：有实证表格时插在第一张实证表正前方
    emp_marker = re.compile(r"concept-(effect|meta-analysis|second-order-meta|subgroup|other-empirical)-table-marker")
    for i, l in enumerate(lines):
        if l.startswith("> [!") and emp_marker.search("".join(lines[i:i + 4])):
            head = "".join(lines[:i]).rstrip("\n")
            tail = "".join(lines[i:])
            return head + "\n\n" + module.rstrip("\n") + "\n\n" + tail
    target = None
    if target is None:
        # Callout-only layout: after the last top-level empirical table callout,
        # else before the related-studies evidence callout, else at the end.
        starts = [i for i, l in enumerate(lines) if re.match(r"^> \[!(effect-table|ma-table|ref-table)\b", l)]
        if starts:
            j = starts[-1] + 1
            while j < len(lines) and lines[j].startswith(">"):
                j += 1
            head = "".join(lines[:j]).rstrip("\n")
            tail = "".join(lines[j:]).lstrip("\n")
            return head + "\n\n" + module.rstrip("\n") + ("\n\n" + tail if tail else "\n")
        rel = [i for i, l in enumerate(lines) if re.match(r"^> \[!(evidence-grid-a|evidence-grid)\b[^\]]*\][+-]? *相关研究", l)]
        if rel:
            target = rel[0]
        else:
            return body.rstrip("\n") + "\n\n" + module
    cut = target
    while cut > 0 and lines[cut - 1].strip() in {"", "---"}:
        cut -= 1
    head = "".join(lines[:cut]).rstrip("\n")
    tail = "".join(lines[cut:]).lstrip("\n")
    return head + "\n\n" + module.rstrip("\n") + "\n\n" + tail


def set_tag(text: str, present: bool) -> str:
    """Update only tags, accepting both YAML block-list indentation styles."""
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return text
    lines = m.group(1).splitlines()
    start = next((i for i, line in enumerate(lines) if re.match(r"^tags:", line)), None)
    if start is None:
        if present:
            lines.extend(["tags:", f"  - {TAG}"])
    else:
        value = lines[start].split(":", 1)[1].strip()
        flow = re.fullmatch(r"\[(.*)\]([ \t]*(?:#.*)?)", value)
        if flow:
            # Keep quoted scalars intact, including commas within tag strings.
            tokens = re.findall(r"""(?:"(?:\\.|[^"\\])*"|'(?:''|[^'])*'|[^,])+""", flow[1])
            tags = [token.strip() for token in tokens if token.strip()]
            if not present:
                tags = [tag for tag in tags if tag.strip("\"'") != TAG]
            elif not any(tag.strip("\"'") == TAG for tag in tags):
                tags.append(TAG)
            lines[start] = "tags: [" + ", ".join(tags) + "]" + flow[2]
        elif value and not value.startswith("#"):
            if value.strip("\"'") == TAG:
                lines[start] = f"tags: {TAG}" if present else "tags: []"
            elif present:
                lines[start:start + 1] = ["tags:", f"  - {value}", f"  - {TAG}"]
        else:
            end = start + 1
            while end < len(lines) and re.match(r"^[ \t]*(?:- |#|$)", lines[end]):
                end += 1
            items = []
            has_tag = False
            for line in lines[start + 1:end]:
                item = re.match(r"^[ \t]*- (.*)$", line)
                if item:
                    if re.fullmatch(r"(?:metax|'metax'|\"metax\")(?:[ \t]+#.*)?", item[1].strip()):
                        if not present or has_tag:
                            continue
                        has_tag = True
                    items.append("  - " + item[1])
                else:
                    items.append(line)
            if present and not has_tag:
                items.append(f"  - {TAG}")
            header = lines[start] if any(re.match(r"^  - ", line) for line in items) else "tags: []"
            lines[start:end] = [header, *items]
    return "---\n" + "\n".join(lines) + "\n---\n" + text[m.end():]


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
            if "\n> [!metax] " in t or "\n" + SECTION + "\n" in t:
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



# ----------------------------------------------------------------- mapping -> entries
DOMAIN_FOLDER = {
    "Student": "educational-psychology",
    "Student Learning Strategies": "learning-science-cognitive-science",
    "Teaching Strategies": "instruction-pedagogy",
    "Classroom": "instruction-pedagogy",
    "Curricula": "curriculum",
    "Teacher": "teacher-education",
    "School": "educational-leadership-administration",
    "Home": "sociology-of-education",
    "Technology, School, and Out-of-School Strategies": "educational-technology",
}
FAMILY_ZH = {
    "Academic Emotions": "学业情绪", "Academic Anxiety": "学业焦虑", "Game-Based Learning": "基于游戏的学习",
    "Student Personality Traits": "学生人格特质", "Technology in Subject Teaching": "学科教学技术",
    "Educational Technology Across Learner Groups": "不同学习者群体的教育技术", "Virtual Reality in Education": "教育虚拟现实",
    "Mathematics Intervention Programs": "数学干预项目", "Teacher Professional Development Programs": "教师专业发展项目",
    "Achievement Goal Orientations": "成就目标定向", "Student Approaches to Learning": "学生学习方式",
    "Parental Involvement in Education": "家长教育参与", "Parenting Styles and Support": "父母教养方式",
    "Student Motivation": "学生学习动机", "Tutoring Interventions": "辅导干预", "Mindfulness Interventions in Schools": "学校正念干预",
    "Cooperative, Competitive and Individualistic Learning": "合作、竞争与个体式学习", "Preschool Education Programs": "学前教育项目",
    "Teacher Expectations": "教师期望", "Whole-School Improvement": "全校改进", "Practice Testing and Retrieval": "练习测验与提取练习",
    "Reading Programs": "阅读项目", "Family Structure and Achievement": "家庭结构与学业成就",
}


def stub_text(title: str, aliases: list[str], members: list[dict], zh: dict, today: str) -> str:
    first = members[0]
    dom = (zh.get("domain") or {}).get(first["domain"], first["domain"])
    sub = (zh.get("sub_domain") or {}).get(first["sub_domain"], first["sub_domain"])
    names = "、".join((zh.get("influences") or {}).get(m["_id"], m["name"]) for m in members)
    summary = (f"Visible Learning MetaX 因素{names}的条目，归属{dom} › {sub}；"
               f"目前只收录 MetaX 元分析汇总数据，概念界定待补充。")
    if len(summary) > 240:
        summary = f"Visible Learning MetaX {len(members)} 个相关因素的合并条目，归属{dom} › {sub}；目前只收录 MetaX 元分析汇总数据，概念界定待补充。"
    alias_block = "aliases: []" if not aliases else "aliases:\n" + "\n".join(f"  - {a}" for a in aliases)
    return (f"---\ntitle: {title}\n{alias_block}\nsummary: \"{summary}\"\ntype: concept\ntags:\n  - {TAG}\n"
            "related_concepts: []\nrelated_theories: []\nrelated_methods: []\nrelated_instruments: []\n"
            "related_persons: []\nrelated_facts: []\nrelated_arguments: []\nconfidence: medium\nstatus: draft\n"
            f"created: {today}\nupdated: {today}\n---\n\n# {title}\n")


def cmd_apply_mapping(args) -> int:
    """Create stub entries for new influences and attach every influence to its entry,
    following metax/mapping.json (reviewed in metax/MetaX 映射审核.md)."""
    import datetime
    data = load_json(DATA_JSON, None)
    zh = zh_table()
    mapping = load_json(MAPPING_JSON, [])
    index = {e["title"]: e for e in load_json(WIKI_INDEX, [])}
    today = datetime.date.today().isoformat()
    groups: dict[str, list[dict]] = {}
    for row in mapping:
        groups.setdefault(row["target"], []).append(row)
    created = 0
    for title, rows in groups.items():
        if rows[0]["action"] == "挂载":
            if title not in index:
                print(f"mount target missing: {title}", file=sys.stderr)
                continue
            rel = index[title]["path"]
        else:
            existing = index.get(title)
            if existing:
                rel = existing["path"]
            else:
                inf0 = data["influences"][rows[0]["id"]]
                rel = f"wiki/concepts/{DOMAIN_FOLDER[inf0['domain']]}/{title}.md"
                path = ROOT / rel
                if not path.exists():
                    aliases = [FAMILY_ZH[title]] if title in FAMILY_ZH else [a for a in {r["alias"] for r in rows} if a]
                    members = [{**data["influences"][r["id"]], "_id": r["id"]} for r in rows]
                    if not args.dry_run:
                        path.parent.mkdir(parents=True, exist_ok=True)
                        path.write_text(stub_text(title, aliases, members, zh, today), encoding="utf-8")
                    created += 1
        for r in rows:
            entries = data["influences"][r["id"]].setdefault("entries", [])
            if rel not in entries:
                entries.append(rel)
    print(f"stub entries {'to create' if args.dry_run else 'created'}: {created}")
    if args.dry_run:
        return 0
    dump_json(DATA_JSON, data)
    return cmd_render(argparse.Namespace(check=False))


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


def bar(value: float) -> str:
    """Inline bar for a mean effect size; width bucket in 0.05 steps (fixed track .mx-bar, fill .b0-b28, so numbers line up)."""
    if value < 0:
        return f'<span class="mx-bar neg"><span class="b{min(28, round(-value * 20))}"></span></span>'
    return f'<span class="mx-bar"><span class="b{min(28, round(value * 20))}"></span></span>'


def cmd_domains(args) -> int:
    """Print the VL-style domain summary and per-domain sub-domain callouts for the
    Visible Learning Meta-X fact entry. Header cells are codes; CSS shows labels."""
    import statistics as stats
    data = load_json(DATA_JSON, None)
    zh = zh_table()
    inf = data["influences"]

    def agg(ids):
        ds = [inf[i]["d"] for i in ids if inf[i]["d"] is not None]
        rows = [r for i in ids for r in inf[i]["rows"] if r["d"] is not None and r["k"]]
        return {
            "n": len(ids),
            "ma": sum(inf[i]["ma"] or 0 for i in ids),
            "uniq": len({r["study"] for i in ids for r in inf[i]["rows"]}),
            "mean": stats.mean(ds), "kw": sum(r["d"] * r["k"] for r in rows) / sum(r["k"] for r in rows),
            "med": stats.median(ds), "sd": stats.pstdev(ds) if len(ds) > 1 else 0.0,
            "lo": min(ds), "hi": max(ds), "neg": sum(1 for x in ds if x < 0),
        }

    D = lambda x: f"{x:.2f}".replace("-", "−")
    dom: dict[str, list[str]] = {}
    sub: dict[tuple, list[str]] = {}
    for iid, v in inf.items():
        dom.setdefault(v["domain"], []).append(iid)
        sub.setdefault((v["domain"], v["sub_domain"]), []).append(iid)
    res = {k: agg(v) for k, v in dom.items()}
    order = sorted(res, key=lambda k: -res[k]["mean"])
    neg = lambda n: str(n) if n else "—"

    out = ["> [!metax-domain] 九个领域（按因素等权平均降序）",
           "> | dom | n | ma | dm | dw | med | sd | rng | neg |",
           "> | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for k in order:
        r = res[k]
        out.append(f"> | {zh['domain'].get(k, k)} | {r['n']} | {r['ma']:,} / {r['uniq']:,} | {bar(r['mean'])}{D(r['mean'])} | {D(r['kw'])} | {D(r['med'])} | {D(r['sd'])} | {D(r['lo'])} ~ {D(r['hi'])} | {neg(r['neg'])} |")
    a = agg(list(inf))
    out.append(f"> | 全部 | {a['n']} | {a['ma']:,} / {a['uniq']:,} | {bar(a['mean'])}{D(a['mean'])} | {D(a['kw'])} | {D(a['med'])} | {D(a['sd'])} | {D(a['lo'])} ~ {D(a['hi'])} | {neg(a['neg'])} |")
    print("\n".join(out))
    for k in order:
        subs = sorted([sk for (dk, sk) in sub if dk == k], key=lambda sk: -agg(sub[(k, sk)])["mean"])
        r = res[k]
        print()
        lines = [f"> [!metax-subdomain]- {zh['domain'].get(k, k)} · {len(subs)} 个子领域 · {r['n']} 个因素",
                 "> | sub | n | dm | dw | rng | neg |",
                 "> | --- | --- | --- | --- | --- | --- |"]
        for sk in subs:
            x = agg(sub[(k, sk)])
            lines.append(f"> | {zh['sub_domain'].get(sk, sk)} | {x['n']} | {bar(x['mean'])}{D(x['mean'])} | {D(x['kw'])} | {D(x['lo'])} ~ {D(x['hi'])} | {neg(x['neg'])} |")
        print("\n".join(lines))
    if getattr(args, "factors", False):
        titles = {e["path"]: e["title"] for e in load_json(WIKI_INDEX, [])}
        print("\n<!-- factors -->")
        for k in order:
            subs = sorted([sk for (dk, sk) in sub if dk == k], key=lambda sk: -agg(sub[(k, sk)])["mean"])
            print(f"\n#### {zh['domain'].get(k, k)}")
            for sk in subs:
                ids = sorted(sub[(k, sk)], key=lambda i: -(inf[i]["d"] or -9))
                lines = [f"> [!metax-factors]- {zh['sub_domain'].get(sk, sk)} · {len(ids)} 个因素",
                         "> | fac | rate | ma | k | dw | rob |",
                         "> | --- | --- | --- | --- | --- | --- |"]
                for i in ids:
                    v = inf[i]
                    name = (zh.get("influences") or {}).get(i, v["name"])
                    ent = (v.get("entries") or [None])[0]
                    cell = f"[[{titles[ent]}\\|{name}]]" if ent in titles else name
                    lines.append(f"> | {cell} | {impact_cell(v.get('impact', ''), zh)} | {fmt_int(v.get('ma'))} | {fmt_int(v.get('k'))} | "
                                 f"{bar(v['d']) if v['d'] is not None else ''}{fmt_d(v.get('d')).replace('-', '−')} | {rob_cell(v.get('rob'))} |")
                print()
                print("\n".join(lines))
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
    p = sub.add_parser("apply-mapping")
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(func=cmd_apply_mapping)
    sub.add_parser("audit").set_defaults(func=cmd_audit)
    p = sub.add_parser("domains")
    p.add_argument("--factors", action="store_true", help="also print the per-sub-domain influence index (links to entries)")
    p.set_defaults(func=cmd_domains)
    p = sub.add_parser("report")
    p.add_argument("--verbose", action="store_true")
    p.set_defaults(func=cmd_report)
    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
