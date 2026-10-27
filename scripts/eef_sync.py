#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
eef_sync.py

Maintain EEF Teaching and Learning Toolkit data and the generated EEF module
([!eef] callouts) in wiki entries. Mirrors scripts/metax_sync.py.

Data (outside wiki/, never linked or indexed):
  datasets/eef/eef.json     strands: toolkit ratings (impact months, cost, evidence),
                   pooled estimate, and the studies behind each strand
  datasets/eef/errata.json  sourced corrections (same schema as datasets/metax/errata.json)

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
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vaultlib import dump_json, load_json, norm_doi  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "datasets/eef"
DATA_JSON = DATA_DIR / "eef.json"
ERRATA_JSON = DATA_DIR / "errata.json"
TEMPLATE = ROOT / "wiki/templates/template-eef.md"
CITATION_FULL = ROOT / "citation/citation_full.json"
WIKI_INDEX = ROOT / "wiki/index.json"
EXTERNAL_IDS = ROOT / "citation/external_identities.json"
METAX_JSON = ROOT / "datasets/metax/metax.json"
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
    "ey:communication-and-language-approaches": "Oral Language Interventions",
    "ey:earlier-starting-age": "Early Education Starting Age", "ey:extra-hours": "Extra Hours in Early Education",
    "ey:early-literacy-approaches": "Early Literacy Approaches", "ey:early-numeracy-approaches": "Early Numeracy Approaches",
    "ey:parental-engagement": "Parental Involvement in Education", "ey:physical-development-approaches": "Physical Development Approaches",
    "ey:play-based-learning": "Play Programs", "ey:self-regulation-strategies": "Self-Regulated Learning",
    "ey:social-and-emotional-learning-strategies": "Social-Emotional Learning",
}
NEW_ENTRY = {  # title -> (folder, Chinese alias)
    "Aspiration Interventions": ("educational-psychology", "抱负干预"),
    "Extending School Time": ("educational-leadership-administration", "延长在校时间"),
    "Oral Language Interventions": ("curriculum", "口语干预"),
    "School Uniform": ("educational-leadership-administration", "学校校服政策"),
    "Small Group Tuition": ("instruction-pedagogy", "小组辅导"),
    "Early Literacy Approaches": ("curriculum", "早期读写教学"),
    "Early Numeracy Approaches": ("curriculum", "早期数学教学"),
    "Early Education Starting Age": ("educational-leadership-administration", "早期教育起始年龄"),
    "Extra Hours in Early Education": ("educational-leadership-administration", "早期教育在园时长"),
    "Physical Development Approaches": ("curriculum", "早期身体发展教学"),
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
    # Early Years Toolkit (keys prefixed ey:)
    "ey:communication-and-language-approaches": "沟通与语言教学", "ey:earlier-starting-age": "提早入园年龄",
    "ey:early-literacy-approaches": "早期读写教学", "ey:early-numeracy-approaches": "早期数学教学", "ey:extra-hours": "增加在园时长",
    "ey:parental-engagement": "家长参与（早期）", "ey:physical-development-approaches": "身体发展教学",
    "ey:play-based-learning": "游戏化学习（早期）", "ey:self-regulation-strategies": "自我调节策略（早期）",
    "ey:social-and-emotional-learning-strategies": "社会情感学习策略（早期）",
}
TOOLKITS = {
    "tlt": {"prefix": "", "url": "https://educationendowmentfoundation.org.uk/education-evidence/teaching-learning-toolkit", "zh": "EEF 教与学工具包", "meta": ""},
    "ey": {"prefix": "ey:", "url": "https://educationendowmentfoundation.org.uk/early-years/toolkit", "zh": "EEF 早期教育工具包", "meta": "|ey"},
}
IMPACT_ZH = {"Very high": "极高影响", "High": "高影响", "Moderate": "中等影响", "Low": "低影响", "Unclear": "影响不明", "Negative": "负向影响", "No": "无影响"}
COST_ZH = {"very low": "极低", "low": "低", "moderate": "中等", "high": "高", "very high": "极高"}
EVIDENCE_ZH = {"insufficient": "不足", "very limited": "极有限", "limited": "有限", "moderate": "中等", "extensive": "充分"}
TYPE_ZH = {"Journal, Article": "期刊论文", "Dissertation": "学位论文", "Report": "报告", "Conference Proceedings": "会议论文",
           "Book, Chapter": "图书章节", "Book, Whole": "专著", "Generic": "其他", "Research project": "研究项目"}
PHASE_ZH = [("nursery", "学前"), ("primary", "小学"), ("secondary", "中学"), ("home", "家庭")]
SUBJECT_ZH = [("reading", "阅读"), ("maths", "数学"), ("science", "科学")]


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
    kit = TOOLKITS[args.toolkit]
    topics = {t["slug"]: t for t in raw.get("topics", [])}
    strands = {}
    for slug0, ov in raw["overview"].items():
        slug = kit["prefix"] + slug0
        det = raw["details"].get(slug0, {})
        rd = (((topics.get(slug0) or {}).get("data") or {}).get("strand") or {}).get("reference_data") or {}
        text = ov.get("card_text", "")
        m = re.search(r"(Very high|High|Moderate|Low|Unclear|Negative|No) impact for ([\w ]+?) cost based on ([\w ]+?) evidence", text)
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
            "name": name, "url": det.get("source_url") or f"{kit['url']}/{slug0}", "toolkit": args.toolkit, "slug": slug0,
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
    # Keep the other toolkit's strands; replace only this toolkit's.
    merged = {k: v for k, v in old.get("strands", {}).items() if (v.get("toolkit") or "tlt") != args.toolkit}
    merged.update(strands)
    exported = dict(old.get("exported", {}))
    exported[args.toolkit] = raw.get("exported_at")
    data = {"_note": "Generated by scripts/eef_sync.py import; edit only entries.",
            "sources": {k: v["url"] for k, v in TOOLKITS.items()}, "exported": exported, "strands": dict(sorted(merged.items()))}
    dump_json(DATA_JSON, data)
    if not ERRATA_JSON.exists():
        dump_json(ERRATA_JSON, [])
    print(f"strands {len(strands)}, studies {sum(len(s['refs']) for s in strands.values())}")
    return 0


# ----------------------------------------------------------------- matching


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
    kit = TOOLKITS[s.get("toolkit") or "tlt"]
    info = kit["zh"] + (f" · 更新于 {s['modified']}" if s.get("modified") else "")
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
    lines = [f"> [!eef{kit['meta']}] [{esc(title)}]({s['url']})", f"> {info}", ">",
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
   表头代号由 CSS 显示为中文：imp 影响（月）｜cost 成本｜evi 证据强度｜n 研究数｜smd 合并效应量｜ci 95% 置信区间｜i2 异质性 I²｜ref 研究｜type 类型｜w 权重｜e 勘误。\n   勘误写入 datasets/eef/errata.json：level 为 strand（整合，总览对应数值旁标 ⚑，field 取 imp/cost/evi/n/smd/ci/i2）或 study（单项，study 填该效应量的 id，列表 e 列标 ①②）；字段 type、eef、corrected、source（Argument 文件名）、pages、note，须附来源。
   成本与证据强度沿用 EEF 五级评分（●○），研究列表默认折叠；勘误框只在自动核算或 datasets/eef/errata.json 有内容时出现。 %%

"""
    TEMPLATE.write_text(head + DIVIDER + "\n\n" + render_strand(slug, s, load_json(ERRATA_JSON, []), arguments_meta()) + "\n", encoding="utf-8")
    print(f"wrote {TEMPLATE.relative_to(ROOT)}")
    return 0



# ----------------------------------------------------------------- entries
EEF_TOP_RE = re.compile(r"^> \[!eef(?:\|[^\]]*)?\][^\n]*\n(?:>[^\n]*(?:\n|\Z))*\n*", re.M)
DIVIDER = "> [!eef-divider]"
DIVIDER_RE = re.compile(r"^> \[!eef-divider\][^\n]*(?:\n>[^\n]*)*\n*", re.M)
METAX_TOP_RE = re.compile(r"^> \[!metax\][^\n]*\n(?:>[^\n]*(?:\n|\Z))*", re.M)


def remove_module(body: str) -> str:
    """Remove only [!eef] blocks; MetaX blocks and all other content are untouched."""
    return re.sub(r"\n{3,}", "\n\n", DIVIDER_RE.sub("", EEF_TOP_RE.sub("", body)))


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
        if l.startswith("> [!empirical-divider]") or (l.startswith("> [!") and emp.search("".join(lines[i:i + 4]))):
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
        if rel not in by_entry and "templates" not in path.parts and re.search(r"\n> \[!eef(?:\|[^\]]*)?\] ", path.read_text(encoding="utf-8")):
            by_entry[rel] = []
    stale = []
    for rel, slugs in sorted(by_entry.items()):
        path = ROOT / rel
        if not path.exists():
            print(f"missing entry: {rel}", file=sys.stderr)
            continue
        text = path.read_text(encoding="utf-8")
        if slugs:
            module = DIVIDER + "\n\n" + "\n\n".join(render_strand(s_, data["strands"][s_], errata, meta) for s_ in sorted(slugs, key=lambda k: (k.startswith("ey:"), k))) + "\n"
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
        return cmd_render_programmes(args)
    before = json.dumps(data, sort_keys=True)
    linked = match_refs(data)
    if args.check:
        code = cmd_render(args, data)
        if json.dumps(data, sort_keys=True) != before:
            print("stale: datasets/eef/eef.json (study matches changed)")
            code = 1
        return max(code, cmd_render_programmes(args))
    dump_json(DATA_JSON, data)
    print(f"studies linked to Arguments: {linked}")
    return max(cmd_render(args, data), cmd_render_programmes(args))


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
        data["strands"][slug]["entries"] = [rel]
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
    import citation_index as ce
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
                works.append((base, {"doi": norm_doi(r.get("doi")) and r["doi"] or "", "title": r.get("title") or "", "dataset": ("eef-ey:" + slug[3:]) if slug.startswith("ey:") else f"eef:{slug}"}))
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

# ----------------------------------------------------------------- promising programmes
PROG_JSON = DATA_DIR / "programmes.json"
PROG_TEMPLATE = ROOT / "wiki/templates/template-fact-eef-programme.md"
PROG_ZH = {
    "1stclass-number-1": "为二年级数学困难学生设计的 10 周小组数学干预。",
    "concept-cat": "面向全班的早期语言概念教学方法。",
    "counting-collections": "面向学前班全班的早期数感项目，练习点数、目测数量、比较与组合。",
    "dialogic-teaching": "提升课堂对话质量，以增强儿童的投入、学习与学业成绩。",
    "embedding-formative-assessment": "在全校推行形成性评价策略的教师专业发展项目。",
    "emotion-coaching": "帮助早期教育从业者支持儿童情绪调节。",
    "fft-reciprocal-reading": "定向、结构化、以讨论为基础的阅读理解教学。",
    "focus-for-teacher-assessment-in-primary-science-focus4taps": "支持小学教师改进科学教学与评价的项目。",
    "lexia-reading-core5": "以技术为主导、旨在提升阅读能力的整合学习系统。",
    "mathematical-reasoning": "帮助学生理解数学背后逻辑原理的全班项目。",
    "mathematics-mastery-primary": "全校推行的小学数学掌握教学。",
    "mathematics-mastery-secondary": "面向第三关键阶段的数学掌握教学。",
    "maths-champions": "提升幼儿园从业者知识，以支持儿童早期数学发展。",
    "maths-whizz-intelligent-tutoring": "面向全班的在线智能导学项目。",
    "neli-preschool": "面向 3 至 4 岁儿童的全班口语丰富项目，附加定向干预。",
    "nuffield-early-language-intervention": "通过脚本化的个别与小组语言课提升儿童语言能力。",
    "pals-uk": "全班结构化结对阅读，提升阅读流畅度与理解。",
    "power-of-pictures": "用图画书与插画提升第二关键阶段学生的读写能力。",
    "reception-jigsaw": "面向学前班教师的专业发展项目，提升儿童早期数学理解。",
    "stop-and-think": "以测验与游戏帮助学生掌握反直觉科学概念的软件项目。",
    "success-for-all": "全校推行的小学读写改进项目。",
    "talking-time": "面向 3 至 5 岁儿童口语能力的普及性干预。",
    "tutor-trust-primary": "低成本的一对一与小组数学辅导。",
}
EVIDENCE_TYPE_ZH = {"Efficacy level evidence": "效能试验", "Effectiveness level evidence": "成效试验",
                    "Pilot Study": "试点研究", "Scale-Up": "规模化评估", "Subsidised Programme": "资助推广"}
TAG_ZH = {"Maths": "数学", "Reading": "阅读", "Literacy": "读写", "Science": "科学", "Cross curriculum": "跨学科",
          "Communication and language": "沟通与语言", "Speech and language": "言语与语言", "Early Years": "早期教育",
          "Personal, social and emotional development": "个人、社会与情绪发展", "Whole class approach": "全班实施",
          "Whole school approach": "全校实施", "Whole setting approach": "全园实施", "Targeted approach": "定向干预"}
SECURITY_ZH = {"very high": "极高", "high": "高", "moderate-to-high": "中高", "moderate": "中", "low": "低", "very low": "极低"}
MONTH_NUM = {m: i for i, m in enumerate(["January", "February", "March", "April", "May", "June", "July", "August",
                                         "September", "October", "November", "December"], 1)}


def _int(v):
    v = re.sub(r"[^\d]", "", str(v or ""))
    return int(v) if v else None


def _trial_label(title: str, programme: str) -> str:
    tail = re.split(r"\s+[–-]\s+", title, maxsplit=1)
    tail = tail[1] if len(tail) > 1 else ""
    t = tail.lower().strip(" ()")
    for k, v in (("second effectiveness", "第二次成效试验"), ("first trial", "第一次试验"), ("second trial", "第二次试验"),
                 ("scale up evaluation", "规模化评估"), ("scale-up", "规模化评估"), ("scale up", "规模化评估"),
                 ("pilot", "试点"), ("re-grant", "追加资助试验"), ("trial", "试验")):
        if k in t:
            return v
    if "(first trial)" in title.lower():
        return "第一次试验"
    if "(second trial)" in title.lower():
        return "第二次试验"
    return title


def cmd_import_programmes(args) -> int:
    raw = load_json(Path(args.raw), None)
    selected = getattr(args, "slug", None)
    if selected and not any(p["url"].rstrip("/").rsplit("/", 1)[-1] == selected for p in raw["programmes"]):
        raise ValueError(f"programme not found: {selected}")
    trials_by_url = {t["url"]: t for t in raw["trials"]}
    progs = {}
    for p in raw["programmes"]:
        slug = p["url"].rstrip("/").rsplit("/", 1)[-1]
        if selected and slug != selected:
            continue
        urls = list(dict.fromkeys(list(p.get("trial_urls") or []) + [t["url"] for t in raw["trials"] if t.get("programme_url") == p["url"]]))
        cost = None
        for s_ in p.get("sections", []):
            if "cost" in s_.get("heading", "").lower():
                m = re.search(r"£\s?([\d,]+(?:\.\d+)?)\s*per pupil", s_.get("text", ""))
                cost = float(m.group(1).replace(",", "")) if m else None
        strands = []
        for l in p.get("detail_links", []):
            m = re.search(r"/(teaching-learning-toolkit|early-years/toolkit)/([\w-]+)", l.get("url", ""))
            if m:
                key = ("ey:" if m.group(1).startswith("early") else "") + m.group(2)
                if key not in strands:
                    strands.append(key)
        trials = []
        for u in urls:
            t = trials_by_url.get(u)
            if not t:
                continue
            pt, mt = t.get("page_text", ""), t.get("metrics", {})
            mm = re.search(r"Impact \(months\).*?([+−-]?\d+)months", pt, re.S)
            ev = re.search(r"Independent Evaluator(.+?)(?:" + re.escape((t.get("subtitle") or "")[:20] or "@@") + r"|\n)", pt)
            sec = re.search(r"(very high|moderate-to-high|high|moderate|very low|low) security rating", pt, re.I)
            done = re.search(r"Completed (\w+) (\d{4})", mt.get("completed", ""))
            reports = [d_ for d_ in t.get("documents", []) if re.search(r"report", d_.get("title", ""), re.I)]
            reports.sort(key=lambda d_: d_.get("uploaded_at", ""), reverse=True)
            trials.append({
                "url": u, "title": t["title"], "label": _trial_label(t["title"], p["title"]), "kind": t.get("project_kind"),
                "type": mt.get("type_of_trial") or None, "completed": f"{done.group(2)}-{MONTH_NUM.get(done.group(1), 0):02d}" if done else None,
                "pupils": _int(mt.get("pupils")), "schools": _int(mt.get("schools")), "grant": mt.get("grant"),
                "key_stage": mt.get("key_stage"), "months": int(mm.group(1).replace("−", "-")) if mm else None,
                "security": sec.group(1).lower() if sec else None,
                "not_significant": "not statistically significant" in pt,
                "evaluator": ev.group(1).strip() if ev else None,
                "report": reports[0]["url"] if reports else None,
                "completed_raw": mt.get("completed"),
                "security_rating": t.get("evidence_strength_rating"),
                "security_total": t.get("evidence_strength_total"),
                "cost_rating": t.get("implementation_cost_rating"),
                "cost_total": t.get("implementation_cost_total"),
                "cost_status": t.get("implementation_cost_status"),
                "outcomes": t.get("trial_outcomes", []),
                "documents": t.get("documents", []),
                "page_project_duration": mt.get("duration"),
                "source_digest": hashlib.sha256(json.dumps({
                    "metrics": mt, "organisation": t.get("organisation"),
                    "evaluator": ev.group(1).strip() if ev else None,
                    "documents": [(d_.get("title"), (d_.get("url") or "").split("?", 1)[0], d_.get("uploaded_at")) for d_ in t.get("documents", [])],
                    "sections": [(s.get("heading"), s.get("metadata"), s.get("text")) for s in t.get("sections", [])],
                    "programme_sections": [(s.get("heading"), s.get("text")) for s in p.get("sections", [])],
                    "outcomes": t.get("trial_outcomes", []),
                }, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
            })
        trials.sort(key=lambda t: t["completed"] or "9999")
        progs[slug] = {
            "name": p["title"], "url": p["url"], "description": p.get("description"),
            "months": int(p["months_progress"]) if re.fullmatch(r"[+-]?\d+", p.get("months_progress") or "") else None,
            "evidence_type": p.get("evidence_type"), "tags": p.get("tags", []), "cost_per_pupil": cost,
            "strands": strands, "trial_urls_listed": len(p.get("trial_urls") or []), "trials": trials, "entries": [],
            "card_version": 3,
            "security_rating": p.get("evidence_strength_rating"),
            "security_total": p.get("evidence_strength_total"),
            "cost_rating": p.get("implementation_cost_rating"),
            "cost_total": p.get("implementation_cost_total"),
            "cost_status": p.get("implementation_cost_status"),
            "impact_label": p.get("impact_label"),
            "cost_context": next((s["text"].removeprefix(s["heading"]).strip() for s in p.get("sections", []) if "cost" in s.get("heading", "").lower()), ""),
            "checked_at": raw.get("exported_at", "")[:10],
        }
    old = load_json(PROG_JSON, {"programmes": {}})
    for k, v in progs.items():
        v["entries"] = old.get("programmes", {}).get(k, {}).get("entries", [])
        # Human-reviewed translations and result-specific qualifications survive refreshes.
        for key in ("cost_note", "review_notes", "developer", "delivery_organisation"):
            if key in old.get("programmes", {}).get(k, {}):
                v[key] = old["programmes"][k][key]
        previous = {(t["url"], o.get("outcome_group")): o
                    for t in old.get("programmes", {}).get(k, {}).get("trials", []) for o in t.get("outcomes", [])}
        for trial in v["trials"]:
            previous_trial = next((t for t in old.get("programmes", {}).get(k, {}).get("trials", []) if t["url"] == trial["url"]), {})
            if previous_trial.get("source_digest") == trial["source_digest"] and "record" in previous_trial:
                trial["record"] = previous_trial["record"]
            for outcome in trial["outcomes"]:
                reviewed = previous.get((trial["url"], outcome.get("outcome_group")), {})
                # Invalidate annotations whenever the source result changes.
                if all(reviewed.get(key) == outcome.get(key) for key in outcome):
                    for key in ("label_zh", "group_zh", "significance"):
                        if key in reviewed:
                            outcome[key] = reviewed[key]
    if selected:
        progs = {**old.get("programmes", {}), **progs}
    dump_json(PROG_JSON, {"_note": "Generated by scripts/eef_sync.py import-programmes; edit only entries.",
                          "source": raw.get("source"), "exported_at": raw.get("exported_at"), "programmes": dict(sorted(progs.items()))})
    if selected:
        print(f"programme {selected}: refreshed {len(progs[selected]['trials'])} linked pages; other programmes preserved")
    else:
        print(f"programmes {len(progs)}, trials {sum(len(v['trials']) for v in progs.values())}")
    return 0


def programme_checks(p: dict) -> list[str]:
    out = []
    if p["trial_urls_listed"] and p["trial_urls_listed"] != len(p["trials"]):
        out.append(f"**自动核算 · 试验数不一致** 项目页列出 {p['trial_urls_listed']} 项试验，采集到的试验页为 {len(p['trials'])} 项。")
    months = [t["months"] for t in p["trials"] if t["months"] is not None]
    if p.get("months") is not None and months and p["months"] not in months:
        out.append(f"**自动核算 · 影响月数对不上** 项目标注 {p['months']:+d} 个月，各试验报告的是 {'、'.join(f'{m:+d}' for m in months)} 个月。")
    if p.get("months") is None:
        out.append("**自动核算 · 缺少影响月数** 项目页没有给出影响月数。")
    return out


def render_programme(slug: str, p: dict, errata: list, titles: dict) -> str:
    if p.get("card_version") in (2, 3):
        return render_programme_v3(slug, p, errata)
    tags = " · ".join(TAG_ZH.get(t, t) for t in p["tags"])
    links = []
    for k in p["strands"]:
        title = MAPPING.get(k)
        zh = ZH_NAMES.get(k, k)
        links.append(f"[[{title}|{zh}]]" if title and title in titles else zh)
    info = "EEF 有望项目 · " + EVIDENCE_TYPE_ZH.get(p.get("evidence_type"), p.get("evidence_type") or "") + (f" · {tags}" if tags else "")
    if links:
        info += " · 工具包策略 " + "、".join(dict.fromkeys(links))
    pupils = sum(t["pupils"] or 0 for t in p["trials"])
    schools = sum(t["schools"] or 0 for t in p["trials"])
    months = "NA" if p.get("months") is None else f"{p['months']:+d} 个月".replace("+0", "0")
    cost = "NA" if p.get("cost_per_pupil") is None else f"£{p['cost_per_pupil']:g}"
    lines = [f"> [!eef-programme] [{esc(p['name'])}]({p['url']})", f"> {PROG_ZH.get(slug, p.get('description') or '')}", ">",
             f"> {info}", ">",
             "> | imp | type | n | pupils | schools | cost |", "> | --- | --- | --- | --- | --- | --- |",
             f"> | {months} | {EVIDENCE_TYPE_ZH.get(p.get('evidence_type'), 'NA')} | {len(p['trials'])} | {pupils:,} | {schools:,} | {cost} |"]
    if p["trials"]:
        lines += [">", f"> > [!eef-trials]- {len(p['trials'])} 项试验",
                  "> > | trial | type | done | n | imp | sec | rep |", "> > | --- | --- | --- | --- | --- | --- | --- |"]
        for t in p["trials"]:
            imp = "NA" if t["months"] is None else f"{t['months']:+d}".replace("+0", "0")
            if t["not_significant"] and t["months"] is not None:
                imp += "（不显著）"
            n = f"{(t['pupils'] or 0):,} / {(t['schools'] or 0):,}" if (t["pupils"] or t["schools"]) else "NA"
            rep = f"[PDF]({t['report']})" if t.get("report") else ""
            lines.append(f"> > | [{esc(t['label'])}]({t['url']}) | {EVIDENCE_TYPE_ZH.get(t.get('type'), t.get('type') or '—')} | "
                         f"{t['completed'] or '—'} | {n} | {imp} | {SECURITY_ZH.get(t.get('security'), '—')} | {rep} |")
    auto = programme_checks(p)
    own = [e for e in errata if e.get("programme") == slug]
    if auto or own:
        lines += [">", f"> > [!eef-errata] {len(auto) + len(own)} 条"]
        lines += [f"> > - {AUTO} {a}" for a in auto]
        lines += [f"> > - {FLAG} **{e.get('type', '勘误')}** {e.get('note', '')}" for e in own]
    return "\n".join(lines)


PENDING = '<span class="eef-pending">待核实</span>'


def programme_rating(value, total=5, status="ok") -> str:
    if status == "not_applicable":
        return "不适用"
    return f"{value}/{total or 5}" if value is not None else "未评级"


def programme_months(value) -> str:
    return f"{value:+g}".replace("+0", "0") if value is not None else "未提供"


def programme_date_range(record: dict, prefix: str) -> str:
    start, end = record.get(prefix + "_start"), record.get(prefix + "_end")
    if start and end:
        return f"{start} 至 {end}"
    if start:
        return f"{start} 至 {PENDING}"
    if end:
        return f"{PENDING} 至 {end}"
    return PENDING


def programme_project_period(trial: dict) -> str | None:
    """Infer only the page project period; never populate observed study/teaching dates."""
    duration = trial.get("page_project_duration") or ""
    completed = trial.get("completed") or ""
    match = re.fullmatch(r"(\d+) year\(s\) (\d+) month\(s\)", duration)
    if not match or not re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])", completed):
        return None
    years, months = map(int, match.groups())
    year, month = map(int, completed.split("-"))
    start_year, start_month = divmod(year * 12 + month - 1 - years * 12 - months, 12)
    return (f"{start_year:04d}-{start_month + 1:02d} 至 {completed}"
            f"（{years} 年 {months} 个月；起点按周期倒推，{PENDING}）")


def _dots(value, total=5, status="ok") -> str:
    if status == "not_applicable":
        return "不适用"
    if value is None:
        return "未评级"
    total = total or 5
    return "●" * value + "○" * (total - value)


COST_LEVEL_ZH = {1: "极低", 2: "低", 3: "中等", 4: "高", 5: "极高"}


def _cost_rating(value, total=5, status="ok") -> str:
    """EEF 实施成本评级（1–5，越高越贵），与 Toolkit 卡片的成本圆点一致。"""
    if status == "not_provided" or (value is None and status != "not_rated"):
        return "未提供"
    if value is None:
        return "未评级"
    return f'<span class="eef-cost">{_dots(value, total)} {COST_LEVEL_ZH.get(value, "")}</span>'


def _doc_title(title: str) -> str:
    return {"Evaluation Protocol": "研究方案", "Evaluation protocol": "研究方案", "Evaluation protocol [v2]": "研究方案（修订版）",
            "Evaluation protocol (amended)": "研究方案（修订版）", "Statistical Analysis Plan": "统计分析计划",
            "Statistical Analysis Plan (SAP)": "统计分析计划", "Project Report": "评估报告", "Evaluation report": "评估报告",
            "Further Appendices": "补充附录", "Appendices": "附录"}.get(title, title)


def render_programme_v3(slug: str, p: dict, errata: list) -> str:
    """Compact programme card: four headline figures, a two-column fact table, one collapsible
    block per trial (facts table + one outcome table, subgroups as indented rows) and all
    verification notes gathered in a single box at the end."""
    pend = lambda s: esc(s).replace("待核实", PENDING)
    impact = f"{programme_months(p['months'])} 个月" if p.get("months") is not None else (p.get("impact_label") or "未提供")
    cost = _cost_rating(p.get("cost_rating"), p.get("cost_total"), p.get("cost_status") or "ok")
    if p.get("cost_per_pupil") is not None:
        cost += f"<br><small>£{p['cost_per_pupil']:g}/生/年</small>"
    stage = EVIDENCE_TYPE_ZH.get(p.get("evidence_type"), p.get("evidence_type") or "未提供")
    lines = [f"> [!eef-programme|v3] [{esc(p['name'])}]({p['url']})",
             f"> {PROG_ZH.get(slug, p.get('description') or '')}", ">",
             "> | imp | stage | sec | cost |", "> | --- | --- | --- | --- |",
             f"> | {esc(impact)} | {esc(stage)} | {_dots(p.get('security_rating'), p.get('security_total'))} | {cost} |"]
    facts = [("开发机构", p.get("developer")), ("实施主体", p.get("delivery_organisation")),
             ("成本口径", p.get("cost_note") or p.get("cost_context"))]
    facts = [(k, v) for k, v in facts if v]
    if facts:
        lines += [">", "> | k | v |", "> | --- | --- |"] + [f"> | {k} | {pend(v)} |" for k, v in facts]
    notes: list[str] = []
    for trial in p.get("trials", []):
        r = trial.get("record", {})
        label = esc(trial["label"])
        phase = "推广" if trial.get("kind") == "scale_up" else EVIDENCE_TYPE_ZH.get(trial.get("type"), trial.get("type") or "阶段未提供")
        summary = [phase]
        if trial.get("completed"):
            summary.append(f"完成 {trial['completed']}")
        if trial.get("pupils"):
            summary.append(f"{trial['pupils']:,} 名学生")
        if trial.get("months") is not None:
            summary.append(f"{programme_months(trial['months'])} 个月")
        rows = []
        # time
        period = programme_project_period(trial)
        when = []
        if period:
            when.append("项目周期 " + period)
        study = programme_date_range(r, "study")
        if study != PENDING or not period:
            when.append("试验 " + study)
        iv = programme_date_range(r, "intervention")
        when.append("干预 " + iv + (f"，共 {r['intervention_weeks']} 周" if r.get("intervention_weeks") is not None else ""))
        rows.append(("时间", "；".join(when)))
        evaluator = esc(r.get("evaluator_zh") or trial.get("evaluator") or "未提供")
        if r.get("evaluator_url"):
            evaluator = f"[{evaluator}]({r['evaluator_url']})"
        rows.append(("评估", evaluator + (f"；{pend(r['design_note'])}" if r.get("design_note") else "")))
        sample = []  # 学生数已在试验标题行，此处只列学校
        if trial.get("schools") is not None:
            sample.append(f"页面学校数 {trial['schools']:,} 所")
        if r.get("schools_randomised") is not None:
            sample.append(f"随机分配学校 {r['schools_randomised']} 所")
        text = "；".join(sample) or "未提供"
        if r.get("sample_context"):
            text += "<br>" + "<br>".join(esc(v) for v in r["sample_context"])
        rows.append(("样本", text))
        if all(r.get(k) is not None for k in ("sessions_per_week", "session_minutes", "group_size")):
            dose = f"每周 {r['sessions_per_week']} 次 × {r['session_minutes']} 分钟，每组 {r['group_size']} 人"
            if r.get("delivery_scope"):
                dose += "；" + pend(r["delivery_scope"])
            rows.append(("剂量", dose))
        if r.get("training"):
            rows.append(("培训", pend(r["training"])))
        money = []
        if trial.get("cost_rating") is not None or trial.get("cost_status") in ("not_rated", "not_provided"):
            money.append("成本评级 " + _cost_rating(trial.get("cost_rating"), trial.get("cost_total"), trial.get("cost_status") or "ok"))
        if trial.get("grant"):
            money.append(f"研究拨款 {esc(trial['grant'])}")
        if r.get("cost_per_pupil_year") is not None:
            c = f"交付 £{r['cost_per_pupil_year']:g}/生/年"
            if r.get("cost_amortisation_years") is not None:
                c += f"（{r['cost_amortisation_years']} 年摊销）"
            money.append(c)
        if r.get("school_cost_year_one") is not None:
            money.append(f"学校首年 £{r['school_cost_year_one']:,.0f}")
        if r.get("school_cost_annual_average") is not None:
            money.append(f"学校年均 £{r['school_cost_annual_average']:g}")
        if r.get("cost_exclusions"):
            money.append(esc(r["cost_exclusions"]))
        if money:
            rows.append(("经费", "；".join(money)))
        docs = []
        for d_ in trial.get("documents", []):
            if d_.get("url"):
                docs.append(f"[{esc(_doc_title(d_.get('title') or '文件'))}]({d_['url']})")
        if docs:
            rows.append(("资料", " · ".join(docs)))
        lines += [">", f"> > [!eef-trial]- [{label}]({trial['url']}) · " + " · ".join(summary),
                  "> > | k | v |", "> > | --- | --- |"] + [f"> > | {k} | {v} |" for k, v in rows]
        outcomes = sorted(trial.get("outcomes", []), key=lambda o: bool(o.get("is_subgroup")))
        if outcomes:
            lines += ["> >", "> > | out | grp | imp | es | sec | sig |", "> > | --- | --- | --- | --- | --- | --- |"]
            for o in outcomes:
                grp = esc(o.get("group_zh") or ("亚组" if o.get("is_subgroup") else "全体学生"))
                if o.get("is_subgroup"):
                    grp = "↳ " + grp
                es = f"{o['effect_size']:g}" if o.get("effect_size") is not None else "未提供"
                lines.append(f"> > | {esc(o.get('label_zh') or o.get('outcome_group') or '指标未提供')} | {grp} | "
                             f"{programme_months(o.get('impact_months'))} | {es} | "
                             f"{_dots(o.get('security_strength'), o.get('security_total'), o.get('security_status'))} | {esc(o.get('significance') or '未报告')} |")
        notes += [f"**{label}** {esc(n)}" for n in r.get("review_notes", [])]
    notes = [esc(n) for n in p.get("review_notes", [])] + notes
    notes += [esc(e.get("note", "")) for e in errata if e.get("programme") == slug]
    notes += programme_checks(p)
    if notes:
        lines += [">", f"> > [!eef-errata]- {len(notes)} 项待核实"] + [f"> > - {n}" for n in notes]
    return "\n".join(lines)


PROGRAMME_BLOCK_RE = re.compile(r"^> \[!eef-programme(?:\|[^\]]*)?\][^\n]*\n(?:>[^\n]*(?:\n|\Z))*", re.M)


def cmd_render_programmes(args) -> int:
    """Refresh only explicitly mapped programme entries, preserving surrounding text."""
    data = load_json(PROG_JSON, {"programmes": {}})
    by_entry: dict[str, list[str]] = {}
    for slug, programme in data["programmes"].items():
        for entry in programme.get("entries", []):
            by_entry.setdefault(entry, []).append(slug)
    stale = False
    for entry, slugs in sorted(by_entry.items()):
        path = ROOT / entry
        if not path.is_file():
            print(f"missing programme entry: {entry}", file=sys.stderr)
            return 1
        text = path.read_text(encoding="utf-8")
        blocks = "\n\n".join(render_programme(slug, data["programmes"][slug], load_json(ERRATA_JSON, []), {}) for slug in sorted(slugs))
        matches = list(PROGRAMME_BLOCK_RE.finditer(text))
        if matches:
            # Replace the first module and remove any older mapped modules as one update.
            first = True
            def replace(match):
                nonlocal first
                result = blocks + "\n" if first else ""
                first = False
                return result
            new = PROGRAMME_BLOCK_RE.sub(replace, text)
        elif "\n> [!finding-cards]" in text:
            # 与 template-fact-program 对齐：卡片位于成效段首，紧接 [!finding-cards]。
            new = text.replace("\n> [!finding-cards]", "\n" + blocks + "\n\n> [!finding-cards]", 1)
        elif "## 成效评估\n" in text:
            new = text.replace("## 成效评估\n", "## 成效评估\n\n" + blocks + "\n", 1)
        elif "\n> [!entry-map]" in text:
            new = text.replace("\n> [!entry-map]", "\n" + blocks + "\n\n---\n\n> [!entry-map]", 1)
        else:
            print(f"programme entry needs a module, [!finding-cards] or [!entry-map]: {entry}", file=sys.stderr)
            return 1
        if new != text:
            stale = True
            print(f"{'stale' if args.check else 'updated'}: {entry}")
            if not args.check:
                path.write_text(new, encoding="utf-8")
    return int(args.check and stale)


def cmd_template_programme(args) -> int:
    """把指定项目的真实卡片写进 EEF Program 模板的成效段，作为样板。"""
    data = load_json(PROG_JSON, None)
    titles = {e["title"] for e in load_json(WIKI_INDEX, [])}
    p = data["programmes"][args.slug]
    card = render_programme(args.slug, p, load_json(ERRATA_JSON, []), titles)
    text = PROG_TEMPLATE.read_text(encoding="utf-8")
    if not PROGRAMME_BLOCK_RE.search(text):
        print("模板中未找到 [!eef-programme] 卡片位置"); return 1
    PROG_TEMPLATE.write_text(PROGRAMME_BLOCK_RE.sub(lambda m: card.rstrip("\n") + "\n", text, count=1), encoding="utf-8")
    print(f"wrote {PROG_TEMPLATE.relative_to(ROOT)}")
    return 0



def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("import"); p.add_argument("--raw", required=True)
    p.add_argument("--toolkit", choices=sorted(TOOLKITS), default="tlt", help="tlt = Teaching and Learning Toolkit; ey = Early Years Toolkit")
    p.set_defaults(func=cmd_import)
    p = sub.add_parser("template"); p.add_argument("--slug", default="feedback"); p.set_defaults(func=cmd_template)
    for name, fn in (("render", cmd_render), ("sync", cmd_sync)):
        p = sub.add_parser(name); p.add_argument("--check", action="store_true"); p.set_defaults(func=fn)
    sub.add_parser("apply-mapping").set_defaults(func=cmd_apply_mapping)
    p = sub.add_parser("import-programmes"); p.add_argument("--raw", required=True); p.add_argument("--slug", help="Refresh only this programme; preserve the other records"); p.set_defaults(func=cmd_import_programmes)
    p = sub.add_parser("template-programme"); p.add_argument("--slug", default="1stclass-number-1"); p.set_defaults(func=cmd_template_programme)
    p = sub.add_parser("render-programmes"); p.add_argument("--check", action="store_true"); p.set_defaults(func=cmd_render_programmes)
    p = sub.add_parser("register-external"); p.add_argument("--dry-run", action="store_true"); p.set_defaults(func=cmd_register_external)
    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
