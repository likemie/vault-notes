#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
eef_sync.py

Maintain EEF Teaching and Learning Toolkit data and the generated EEF module
([!eef] callouts) in wiki entries. Mirrors scripts/metax_sync.py.

Data (outside wiki/, never linked or indexed):
  eef/eef.json     strands: toolkit ratings (impact months, cost, evidence),
                   pooled estimate, and the studies behind each strand
  eef/errata.json  sourced corrections (same schema as metax/errata.json)

Subcommands:
  import --raw RAW.json     normalise a browser export (overview + details + api topics)
  template                  regenerate wiki/templates/template-eef.md from real data
  sync [--check]            link studies to Arguments (DOI, or title + year) and render modules
  render [--check]          write [!eef] modules into mapped entries (MetaX blocks untouched)
  apply-mapping             attach strands to entries per MAPPING, creating stubs for NEW_ENTRY
  register-external [--dry-run]
                            register EEF and MetaX studies outside the vault in
                            citation/external_identities.json (doi or title, dataset tag)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "eef"
DATA_JSON = DATA_DIR / "eef.json"
ERRATA_JSON = DATA_DIR / "errata.json"
TEMPLATE = ROOT / "wiki/templates/template-eef.md"
CITATION_FULL = ROOT / "citation/citation_full.json"
WIKI_INDEX = ROOT / "wiki/index.json"
EXTERNAL_IDS = ROOT / "citation/external_identities.json"
METAX_JSON = ROOT / "metax/metax.json"
TAG = "eef"
FLAG = "⚑"
CIRCLED = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳"
# strand -> entry title (existing entry, or a stub created by apply-mapping)
MAPPING = {
    "arts-participation": "Arts Programs", "aspiration-interventions": "Aspiration Interventions",
    "behaviour-interventions": "Decreasing Disruptive Behavior", "collaborative-learning-approaches": "Collaborative Learning",
    "extending-school-time": "Extending School Time", "feedback": "Feedback", "homework": "Homework",
    "individualised-instruction": "Individualised Instruction", "learning-styles": "Learning Styles",
    "mastery-learning": "Mastery Learning", "mentoring": "Student Mentoring Programs",
    "metacognition-and-self-regulation": "Metacognition", "one-to-one-tuition": "Tutoring Interventions",
    "oral-language-interventions": "Oral Language Interventions", "outdoor-adventure-learning": "Outdoor Adventure Education",
    "parental-engagement": "Parental Involvement in Education", "peer-tutoring": "Peer-Supported Learning",
    "performance-pay": "Performance Pay", "phonics": "Phonics Instruction", "physical-activity": "Exercise Interventions",
    "reading-comprehension-strategies": "Reading Strategies", "reducing-class-size": "Class Size",
    "repeating-a-year": "Grade Retention", "school-uniform": "School Uniform", "setting-and-streaming": "Tracking",
    "small-group-tuition": "Small Group Tuition", "social-and-emotional-learning": "Social-Emotional Learning",
    "summer-schools": "Summer School", "teaching-assistant-interventions": "Teaching Assistant",
    "within-class-attainment-grouping": "Within-Class Grouping",
}
NEW_ENTRY = {  # title -> (folder, Chinese alias)
    "Aspiration Interventions": ("educational-psychology", "抱负干预"),
    "Extending School Time": ("educational-leadership-administration", "延长在校时间"),
    "Oral Language Interventions": ("curriculum", "口语干预"),
    "School Uniform": ("educational-leadership-administration", "学校校服政策"),
    "Small Group Tuition": ("instruction-pedagogy", "小组辅导"),
}
OVERVIEW_FIELDS = ["imp", "cost", "evi", "n", "smd", "ci", "i2"]
FIELD_ZH = {"imp": "影响（月）", "cost": "成本", "evi": "证据强度", "n": "研究数", "smd": "合并效应量", "ci": "95% 置信区间",
            "i2": "异质性", "ref": "研究信息", "type": "类型", "w": "权重", "year": "年份", "title": "篇名", "doi": "DOI"}
TOOLKIT_URL = "https://educationendowmentfoundation.org.uk/education-evidence/teaching-learning-toolkit"
AUTO = "∑"

ZH_NAMES = {
    "arts-participation": "艺术参与", "aspiration-interventions": "抱负干预", "behaviour-interventions": "行为干预",
    "collaborative-learning-approaches": "协作学习方法", "extending-school-time": "延长在校时间", "feedback": "反馈",
    "homework": "家庭作业", "individualised-instruction": "个别化教学", "learning-styles": "学习风格",
    "mastery-learning": "掌握学习", "mentoring": "导师指导", "metacognition-and-self-regulation": "元认知与自我调节",
    "one-to-one-tuition": "一对一辅导", "oral-language-interventions": "口语干预", "outdoor-adventure-learning": "户外探险学习",
    "parental-engagement": "家长参与", "peer-tutoring": "同伴辅导", "performance-pay": "绩效工资", "phonics": "自然拼读",
    "physical-activity": "体育活动", "reading-comprehension-strategies": "阅读理解策略", "reducing-class-size": "缩小班额",
    "repeating-a-year": "留级", "school-uniform": "校服", "setting-and-streaming": "分层与分流",
    "small-group-tuition": "小组辅导", "social-and-emotional-learning": "社会情感学习", "summer-schools": "暑期学校",
    "teaching-assistant-interventions": "助教干预", "within-class-attainment-grouping": "班内按成绩分组",
}
IMPACT_ZH = {"High": "高影响", "Moderate": "中等影响", "Low": "低影响", "Unclear": "影响不明", "Negative": "负向影响", "No": "无影响"}
COST_ZH = {"very low": "极低", "low": "低", "moderate": "中等", "high": "高", "very high": "极高"}
EVIDENCE_ZH = {"insufficient": "不足", "very limited": "极有限", "limited": "有限", "moderate": "中等", "extensive": "充分"}
TYPE_ZH = {"Journal, Article": "期刊论文", "Dissertation": "学位论文", "Report": "报告", "Conference Proceedings": "会议论文",
           "Book, Chapter": "图书章节", "Book, Whole": "专著", "Generic": "其他", "Research project": "研究项目"}
PHASE_ZH = [("nursery", "学前"), ("primary", "小学"), ("secondary", "中学"), ("home", "家庭")]
SUBJECT_ZH = [("reading", "阅读"), ("maths", "数学"), ("science", "科学")]


def load_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8-sig"))


def dump_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def na(v):
    return None if v in (None, "", "NA") else v


def fix_url(v):
    v = na(v)
    return v.replace("https //", "https://").replace("http //", "http://") if v else None


def icon_counts(card_html: str) -> dict:
    parts = re.split(r">\s*(Cost|Evidence|Impact \(months\))\s*<", card_html)
    out = {}
    for i in range(1, len(parts) - 1, 2):
        out[parts[i]] = len(re.findall(r"text-gray-blue-800 border-gray-blue-800", parts[i + 1]))
    return out


def cmd_import(args) -> int:
    raw = load_json(Path(args.raw), None)
    topics = {t["slug"]: t for t in raw.get("topics", [])}
    strands = {}
    for slug, ov in raw["overview"].items():
        det = raw["details"].get(slug, {})
        rd = (((topics.get(slug) or {}).get("data") or {}).get("strand") or {}).get("reference_data") or {}
        text = ov.get("card_text", "")
        m = re.search(r"(High|Moderate|Low|Unclear|Negative|No) impact for ([\w ]+?) cost based on ([\w ]+?) evidence", text)
        months = re.search(r"Impact \(months\)\s*([+−-]?\s*\d+)", text)
        icons = icon_counts(ov.get("card_html", ""))
        body = det.get("body_text", "")
        n_page = re.search(r"Number of studies\s*(\d+)", body)
        modified = None
        for g in (det.get("structured_data") or [{}])[0].get("@graph", []):
            modified = modified or g.get("dateModified")
        name = (det.get("headings") or [{"text": slug}])[0]["text"]
        refs = []
        for r in rd.get("references", []):
            short = r.get("title_short") or ""
            mm = re.match(r"^(.*?\(\d{4}[a-z]?\))\s*(.*)$", short)
            pd = r.get("plotData") or {}
            refs.append({
                "id": r.get("id"), "cite": mm.group(1) if mm else short, "tag": (mm.group(2) if mm else "").strip(),
                "title": na(r.get("title_full")), "source": na(r.get("title_parent")), "authors": na(r.get("authors")),
                "year": r.get("year"), "type": r.get("type"), "doi": fix_url(r.get("doi")), "url": fix_url(r.get("url")),
                "smd": pd.get("smd"), "se": pd.get("se"), "lo": pd.get("ci_lower"), "hi": pd.get("ci_upper"), "w": pd.get("weight"),
                "argument": None,
            })
        pooled = rd.get("pooledData") or {}
        strands[slug] = {
            "name": name, "url": f"{TOOLKIT_URL}/{slug}",
            "impact": m.group(1) if m else None, "cost_label": m.group(2) if m else None, "evidence_label": m.group(3) if m else None,
            "months": int(months.group(1).replace("−", "-").replace(" ", "")) if months else None,
            "cost": icons.get("Cost"), "evidence": icons.get("Evidence"),
            "n_page": int(n_page.group(1)) if n_page else None, "n_api": rd.get("total"),
            "modified": (modified or "")[:10] or None,
            "phase": rd.get("phase") or {}, "subject": rd.get("subject") or {},
            "pooled": {"smd": pooled.get("smd"), "lo": pooled.get("ci_lower"), "hi": pooled.get("ci_upper"),
                       "tau2": pooled.get("tau2"), "i2": pooled.get("i2"), "q": pooled.get("q")} if pooled else None,
            "description": (det.get("meta") or {}).get("description"),
            "entries": [], "refs": refs,
        }
    old = load_json(DATA_JSON, {"strands": {}})
    for slug, s in strands.items():
        prev = old["strands"].get(slug, {})
        s["entries"] = prev.get("entries", [])
    data = {"_note": "Generated by scripts/eef_sync.py import; edit only entries.",
            "source": TOOLKIT_URL, "exported_at": raw.get("exported_at"), "strands": dict(sorted(strands.items()))}
    dump_json(DATA_JSON, data)
    if not ERRATA_JSON.exists():
        dump_json(ERRATA_JSON, [])
    print(f"strands {len(strands)}, studies {sum(len(s['refs']) for s in strands.values())}")
    return 0


# ----------------------------------------------------------------- matching
def norm_doi(v) -> str:
    v = str(v or "").strip()
    v = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", v, flags=re.I)
    return v.lower()


def norm_alnum(v) -> str:
    import unicodedata
    v = unicodedata.normalize("NFKD", str(v or ""))
    v = "".join(c for c in v if not unicodedata.combining(c)).casefold()
    return re.sub(r"[^0-9a-z\u4e00-\u9fff]", "", v)


def arguments_meta() -> dict:
    out = {}
    for key, item in load_json(CITATION_FULL, {"items": {}})["items"].items():
        a = out.setdefault(item["argument"], {**item, "narrative": None, "paren": None})
        for alias in item.get("aliases", []):
            if alias.endswith(")"):
                a["narrative"] = a["narrative"] or alias
            else:
                a["paren"] = a["paren"] or alias
    return out


def match_refs(data: dict) -> int:
    """Link a study to an Argument only by DOI, or by full title plus year."""
    args = arguments_meta()
    by_doi = {norm_doi(a.get("doi")): k for k, a in args.items() if a.get("doi")}
    by_year: dict[str, list] = {}
    for k, a in args.items():
        by_year.setdefault(str(a.get("year", ""))[:4], []).append((k, norm_alnum(a.get("citation", ""))))
    n = 0
    for s_ in data["strands"].values():
        for r in s_["refs"]:
            r["argument"] = None
            d = norm_doi(r.get("doi"))
            if d and d in by_doi:
                r["argument"] = by_doi[d]
            else:
                t = norm_alnum(r.get("title"))
                if len(t) >= 20:
                    for k, cit in by_year.get(str(r.get("year")), []):
                        if t in cit:
                            r["argument"] = k
                            break
            n += bool(r["argument"])
    return n


# ----------------------------------------------------------------- render
def esc(t) -> str:
    return str(t).replace("|", "\\|")


def d2(v) -> str:
    return "NA" if v is None else f"{v:.2f}".replace("-", "−")


def dots(n, total=5) -> str:
    return "NA" if n is None else "●" * n + "○" * (total - n)


def auto_checks(s: dict) -> list[str]:
    out = []
    refs = s["refs"]
    if s.get("n_page") is not None and refs and s["n_page"] not in (len(refs), len({r["cite"] for r in refs})):
        studies = len({r["cite"] for r in refs})
        out.append(f"**自动核算 · 研究数不一致** 页面“How secure is the evidence?”一节称纳入 {s['n_page']} 项研究；"
                   f"参考文献列表为 {len(refs)} 条效应量，来自 {studies} 项研究，合并效应量据后者计算。")
    if refs:
        wsum = sum(r["w"] or 0 for r in refs)
        if abs(wsum - 100) > 1:
            out.append(f"**自动核算 · 权重不闭合** 各研究权重合计 {wsum:.1f}%，应为 100%。")
    p = s.get("pooled") or {}
    if refs and len(refs) > 1 and p and not p.get("q") and not p.get("tau2"):
        out.append(f"**自动核算 · 合并结果异常** {len(refs)} 条效应量的异质性 Q 与 τ² 均为 0，置信区间 {d2(p.get('lo'))} ~ {d2(p.get('hi'))}，疑为占位数据。")
    return out


def source_link(arg: str, pages: str, meta: dict) -> str:
    m = meta.get(arg)
    if not m:
        return ""
    disp = m["paren"] or m["narrative"]
    return f"[[{arg}|{disp}{', ' + pages if pages else ''}]]"


def errata_line(mark: str, level: str, e: dict, who: str, meta: dict) -> str:
    parts = [f"{mark} **{level} · {e.get('type', '勘误')}**"]
    field = FIELD_ZH.get(e.get("field", ""), e.get("field", ""))
    seg = f"{who}{field}" if (who or field) else ""
    if e.get("eef") is not None or e.get("corrected") is not None:
        seg += f"：EEF 记为 {e.get('eef', 'NA')}" + (f"，应为 {e['corrected']}" if e.get("corrected") is not None else "")
    if seg:
        parts.append(seg + "。")
    if e.get("note"):
        parts.append(e["note"])
    link = source_link(e.get("source", ""), e.get("pages", ""), meta)
    if link:
        parts.append(f"（{link}）")
    return " ".join(parts)


def render_strand(slug: str, s: dict, errata: list, meta: dict | None = None) -> str:
    meta = meta if meta is not None else {}
    own = [e for e in errata if e.get("strand") == slug]
    flags = {e.get("field") for e in own if e.get("level") == "strand"}
    fl = lambda f, v: f"{v} {FLAG}" if f in flags else v
    zh = ZH_NAMES.get(slug, "")
    title = f"{zh} · {s['name']}" if zh else s["name"]
    chips = [f"{z} {s['phase'].get(k)}" for k, z in PHASE_ZH if s["phase"].get(k)]
    chips += [f"{z} {s['subject'].get(k)}" for k, z in SUBJECT_ZH if s["subject"].get(k)]
    info = "EEF 教与学工具包" + (f" · 更新于 {s['modified']}" if s.get("modified") else "")
    if chips:
        info += " · " + " · ".join(chips)
    p = s.get("pooled") or {}
    has = bool(s["refs"])
    months = "NA" if s.get("months") is None else (f"+{s['months']}" if s["months"] > 0 else str(s["months"]).replace("-", "−")) + " 个月"
    i2 = (p.get("i2") or "").replace("%", "")
    i2 = f"{float(i2):.0f}%" if has and i2 else "NA"
    cells = [
        fl("imp", f"{months} {IMPACT_ZH.get(s.get('impact'), '')}".strip()),
        fl("cost", f"{dots(s.get('cost'))} {COST_ZH.get(s.get('cost_label'), '')}"),
        fl("evi", f"{dots(s.get('evidence'))} {EVIDENCE_ZH.get(s.get('evidence_label'), '')}"),
        fl("n", str(s.get("n_page") if s.get("n_page") is not None else len(s["refs"]))),
        fl("smd", d2(p.get("smd")) if has else "NA"),
        fl("ci", f"{d2(p.get('lo'))} ~ {d2(p.get('hi'))}" if has else "NA"),
        fl("i2", i2),
    ]
    lines = [f"> [!eef] [{esc(title)}]({s['url']})", f"> {info}", ">",
             "> | imp | cost | evi | n | smd | ci | i2 |", "> | --- | --- | --- | --- | --- | --- | --- |",
             "> | " + " | ".join(cells) + " |"]
    study_err = [e for e in own if e.get("level") == "study"]
    marks: dict[str, str] = {}
    numbered = []
    for i, e in enumerate(study_err):
        mark = CIRCLED[i] if i < len(CIRCLED) else f"({i + 1})"
        marks[str(e.get("study"))] = marks.get(str(e.get("study")), "") + mark
        numbered.append((mark, e))
    if has:
        lines += [">", f"> > [!eef-studies]- {len(s['refs'])} 条效应量 · {len({r['cite'] for r in s['refs']})} 项研究",
                  "> > | ref | type | smd | ci | w | e |", "> > | --- | --- | --- | --- | --- | --- |"]
        for r in s["refs"]:
            arg = r.get("argument")
            cite = f"[[{arg}\\|{meta[arg]['narrative']}]]" if arg in meta and meta[arg].get("narrative") else esc(r["cite"])
            if r["tag"]:
                cite += f" <span class=\"eef-tag\">{esc(r['tag'])}</span>"
            e = marks.get(str(r["id"]), "")
            lines.append(f"> > | {cite} | {TYPE_ZH.get(r['type'], r['type'] or '')} | {d2(r['smd'])} | {d2(r['lo'])} ~ {d2(r['hi'])} | {(r['w'] or 0):.1f}% | {e} |")
    auto = auto_checks(s)
    if auto or own:
        lines += [">", f"> > [!eef-errata] {len(auto) + len(own)} 条"]
        lines += [f"> > - {AUTO} {a}" for a in auto]
        lines += ["> > - " + errata_line(FLAG, "整合", e, "", meta) for e in own if e.get("level") == "strand"]
        for mark, e in numbered:
            r = next((x for x in s["refs"] if str(x["id"]) == str(e.get("study"))), None)
            who = f"{r['cite']}{(' ' + r['tag']) if r and r['tag'] else ''} 的" if r else ""
            lines.append("> > - " + errata_line(mark, "单项", e, who, meta))
    return "\n".join(lines)


def cmd_template(args) -> int:
    data = load_json(DATA_JSON, None)
    slug = args.slug
    s = data["strands"][slug]
    head = f"""---
title: template-eef
aliases: []
summary: "EEF 教与学工具包卡片样式样板，以 {ZH_NAMES.get(slug, slug)}的真实数据演示"
type: template
tags: []
status: active
created: 2026-10-25
updated: 2026-10-25
---

%% 样板。正式模块由 EEF 同步脚本生成并插入条目，条目中不设标题，放在 ## 实证数据 一节末尾，不手写。
   表头代号由 CSS 显示为中文：imp 影响（月）｜cost 成本｜evi 证据强度｜n 研究数｜smd 合并效应量｜ci 95% 置信区间｜i2 异质性 I²｜ref 研究｜type 类型｜w 权重｜e 勘误。\n   勘误写入 eef/errata.json：level 为 strand（整合，总览对应数值旁标 ⚑，field 取 imp/cost/evi/n/smd/ci/i2）或 study（单项，study 填该效应量的 id，列表 e 列标 ①②）；字段 type、eef、corrected、source（Argument 文件名）、pages、note，须附来源。
   成本与证据强度沿用 EEF 五级评分（●○），研究列表默认折叠；勘误框只在自动核算或 eef/errata.json 有内容时出现。 %%

"""
    TEMPLATE.write_text(head + render_strand(slug, s, load_json(ERRATA_JSON, []), arguments_meta()) + "\n", encoding="utf-8")
    print(f"wrote {TEMPLATE.relative_to(ROOT)}")
    return 0



# ----------------------------------------------------------------- entries
EEF_TOP_RE = re.compile(r"^> \[!eef\][^\n]*\n(?:>[^\n]*(?:\n|\Z))*\n*", re.M)
METAX_TOP_RE = re.compile(r"^> \[!metax\][^\n]*\n(?:>[^\n]*(?:\n|\Z))*", re.M)


def remove_module(body: str) -> str:
    """Remove only [!eef] blocks; MetaX blocks and all other content are untouched."""
    return re.sub(r"\n{3,}", "\n\n", EEF_TOP_RE.sub("", body))


def insert_module(body: str, module: str) -> str:
    """EEF follows MetaX inside the empirical-data group: right after the last [!metax]
    block; else directly before the first empirical table callout; else after the last
    effect/ma/ref table callout; else before the 相关研究 evidence callout; else at the end.
    Only [!eef] blocks are ever removed."""
    body = remove_module(body)
    lines = body.splitlines(keepends=True)

    def end_of_block(i: int) -> int:
        while i < len(lines) and lines[i].startswith(">"):
            i += 1
        return i

    def put_at(i: int) -> str:
        head = "".join(lines[:i]).rstrip("\n")
        tail = "".join(lines[i:]).lstrip("\n")
        return head + "\n\n" + module.rstrip("\n") + ("\n\n" + tail if tail.strip() else "\n")

    mx = [i for i, l in enumerate(lines) if l.startswith("> [!metax]")]
    if mx:
        return put_at(end_of_block(mx[-1]))
    emp = re.compile(r"concept-(effect|meta-analysis|second-order-meta|subgroup|other-empirical)-table-marker")
    for i, l in enumerate(lines):
        if l.startswith("> [!") and emp.search("".join(lines[i:i + 4])):
            return put_at(i)
    starts = [i for i, l in enumerate(lines) if re.match(r"^> \[!(effect-table|ma-table|ref-table)\b", l)]
    if starts:
        return put_at(end_of_block(starts[-1]))
    rel = [i for i, l in enumerate(lines) if re.match(r"^> \[!(evidence-grid-a|evidence-grid)\b[^\]]*\][+-]? *相关研究", l)]
    if rel:
        return put_at(rel[0])
    return body.rstrip("\n") + "\n\n" + module.rstrip("\n") + "\n"


def set_tag(text: str, present: bool) -> str:
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return text
    fm = m.group(1)
    has = re.search(rf"^  - {TAG}$", fm, re.M)
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
    data = data or load_json(DATA_JSON, None)
    if data is None:
        return 0
    errata = load_json(ERRATA_JSON, [])
    meta = arguments_meta()
    by_entry: dict[str, list[str]] = {}
    for slug, st in data["strands"].items():
        for e in st.get("entries", []):
            by_entry.setdefault(e, []).append(slug)
    for path in (ROOT / "wiki").rglob("*.md"):
        rel = path.relative_to(ROOT).as_posix()
        if rel not in by_entry and "templates" not in path.parts and "\n> [!eef] " in path.read_text(encoding="utf-8"):
            by_entry[rel] = []
    stale = []
    for rel, slugs in sorted(by_entry.items()):
        path = ROOT / rel
        if not path.exists():
            print(f"missing entry: {rel}", file=sys.stderr)
            continue
        text = path.read_text(encoding="utf-8")
        if slugs:
            module = "\n\n".join(render_strand(s_, data["strands"][s_], errata, meta) for s_ in sorted(slugs)) + "\n"
            new = insert_module(text, module)
        else:
            new = remove_module(text)
        new = set_tag(new, bool(slugs))
        if new != text:
            stale.append(rel)
            if not args.check:
                path.write_text(new, encoding="utf-8")
    for rel in stale:
        print(f"{'stale' if args.check else 'updated'}: {rel}")
    return 1 if (args.check and stale) else 0


def cmd_sync(args) -> int:
    data = load_json(DATA_JSON, None)
    if data is None:
        return 0
    before = json.dumps(data, sort_keys=True)
    linked = match_refs(data)
    if args.check:
        code = cmd_render(args, data)
        if json.dumps(data, sort_keys=True) != before:
            print("stale: eef/eef.json (study matches changed)")
            code = 1
        return code
    dump_json(DATA_JSON, data)
    print(f"studies linked to Arguments: {linked}")
    return cmd_render(args, data)


def cmd_apply_mapping(args) -> int:
    import datetime
    data = load_json(DATA_JSON, None)
    index = {e["title"]: e for e in load_json(WIKI_INDEX, [])}
    today = datetime.date.today().isoformat()
    created = 0
    for slug, title in MAPPING.items():
        if title in index:
            rel = index[title]["path"]
        elif title in NEW_ENTRY:
            folder, alias = NEW_ENTRY[title]
            rel = f"wiki/concepts/{folder}/{title}.md"
            path = ROOT / rel
            if not path.exists():
                zh = ZH_NAMES.get(slug, title)
                summary = f"EEF 教与学工具包策略{zh}的条目；目前只收录 EEF 证据汇总数据，概念界定待补充。"
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(
                    f"---\ntitle: {title}\naliases:\n  - {alias}\nsummary: \"{summary}\"\ntype: concept\ntags:\n  - {TAG}\n"
                    "related_concepts: []\nrelated_theories: []\nrelated_methods: []\nrelated_instruments: []\n"
                    "related_persons: []\nrelated_facts: []\nrelated_arguments: []\nconfidence: medium\nstatus: draft\n"
                    f"created: {today}\nupdated: {today}\n---\n\n# {title}\n", encoding="utf-8")
                created += 1
        else:
            print(f"mapping target missing: {slug} -> {title}", file=sys.stderr)
            continue
        if rel not in data["strands"][slug]["entries"]:
            data["strands"][slug]["entries"].append(rel)
    dump_json(DATA_JSON, data)
    print(f"stub entries created: {created}")
    return cmd_sync(argparse.Namespace(check=False))


# ----------------------------------------------------------------- external literature
def _apa_base(name: str, year) -> str:
    return f"{name}, {year}"


def cmd_register_external(args) -> int:
    """Register EEF and MetaX studies that are not vault Arguments in
    citation/external_identities.json (doi when known, otherwise title).
    Existing rows are never overwritten; a different work with the same
    author-year gets the next free year letter; a body-text sighting with no
    identity is left alone and the dataset work gets its own lettered key."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import citation_external as ce
    store = load_json(EXTERNAL_IDS, {"items": {}})
    items = store.setdefault("items", {})
    works = []
    eef = load_json(DATA_JSON, {"strands": {}})
    seen_eef = set()
    for slug, st in eef["strands"].items():
        for r in st["refs"]:
            if r.get("argument") or not (r.get("title") or r.get("doi")):
                continue
            key = (norm_doi(r.get("doi")) or norm_alnum(r.get("title")))
            if key in seen_eef:
                continue
            seen_eef.add(key)
            base = ce.comma_key(r["cite"])
            if base:
                works.append((base, {"doi": norm_doi(r.get("doi")) and r["doi"] or "", "title": r.get("title") or "", "dataset": f"eef:{slug}"}))
    mx = load_json(METAX_JSON, {"studies": {}})
    for sid, st in mx.get("studies", {}).items():
        if st.get("argument") or not st.get("title") or not st.get("authors"):
            continue
        names = st["authors"]
        author = names[0] if len(names) == 1 else (f"{names[0]} & {names[1]}" if len(names) == 2 else f"{names[0]} et al.")
        base = ce.comma_key(f"{author} ({st['year']})")
        if base:
            works.append((base, {"doi": "", "title": st["title"], "dataset": f"metax:{sid}"}))
    added = merged = 0
    # An author-year that is already a vault Argument's alias belongs to that Argument;
    # a different dataset work with the same author-year gets a year letter instead.
    vault_aliases = {ce.comma_key(a) for it in load_json(CITATION_FULL, {"items": {}})["items"].values() for a in it.get("aliases", [])}
    by_base: dict[str, list[str]] = {}
    for k in items:
        by_base.setdefault(ce.base_of(ce.comma_key(k) or k), []).append(k)
    for base, w in works:
        same_base = by_base.get(base, [])
        hit = None
        for k in same_base:
            row = ce.clean_row(items[k])
            if ce.has_identity(row) and ce.positive_match(row, w):
                hit = k
                break
        if hit:
            ds = items[hit].setdefault("datasets", [])
            if w["dataset"] not in ds:
                ds.append(w["dataset"])
                merged += 1
            continue
        key = base
        if key in items or same_base or key in vault_aliases:
            used = set(same_base)
            i = 0
            while f"{base}{ce.year_suffix(i)}" in used or f"{base}{ce.year_suffix(i)}" in items or f"{base}{ce.year_suffix(i)}" in vault_aliases:
                i += 1
            key = f"{base}{ce.year_suffix(i)}"
        items[key] = {"doi": w["doi"], "isbn": "", "title": w["title"], "seen_in": [], "datasets": [w["dataset"]]}
        by_base.setdefault(base, []).append(key)
        added += 1
    if not args.dry_run:
        EXTERNAL_IDS.write_text(json.dumps(store, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"external literature: {added} new rows, {merged} dataset tags added to existing rows ({len(works)} candidates)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("import"); p.add_argument("--raw", required=True); p.set_defaults(func=cmd_import)
    p = sub.add_parser("template"); p.add_argument("--slug", default="feedback"); p.set_defaults(func=cmd_template)
    for name, fn in (("render", cmd_render), ("sync", cmd_sync)):
        p = sub.add_parser(name); p.add_argument("--check", action="store_true"); p.set_defaults(func=fn)
    sub.add_parser("apply-mapping").set_defaults(func=cmd_apply_mapping)
    p = sub.add_parser("register-external"); p.add_argument("--dry-run", action="store_true"); p.set_defaults(func=cmd_register_external)
    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
