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
        out.append(f"**自动核算 · 合并结果异常** {len(refs)} 项研究的异质性 Q 与 τ² 均为 0，置信区间 {d2(p.get('lo'))} ~ {d2(p.get('hi'))}，疑为占位数据。")
    return out


def render_strand(slug: str, s: dict, errata: list, args_meta: dict | None = None) -> str:
    zh = ZH_NAMES.get(slug, "")
    title = f"{zh} · {s['name']}" if zh else s["name"]
    chips = [f"{z} {s['phase'].get(k)}" for k, z in PHASE_ZH if s["phase"].get(k)]
    chips += [f"{z} {s['subject'].get(k)}" for k, z in SUBJECT_ZH if s["subject"].get(k)]
    meta = "EEF 教与学工具包" + (f" · 更新于 {s['modified']}" if s.get("modified") else "")
    if chips:
        meta += " · " + " · ".join(chips)
    p = s.get("pooled") or {}
    months = "NA" if s.get("months") is None else (f"+{s['months']}" if s["months"] > 0 else str(s["months"]).replace("-", "−")) + " 个月"
    imp = f"{months} {IMPACT_ZH.get(s.get('impact'), '')}".strip()
    cost = f"{dots(s.get('cost'))} {COST_ZH.get(s.get('cost_label'), '')}"
    evi = f"{dots(s.get('evidence'))} {EVIDENCE_ZH.get(s.get('evidence_label'), '')}"
    i2 = (p.get("i2") or "NA").replace("%", "")
    i2 = f"{float(i2):.0f}%" if i2 not in ("NA", "") else "NA"
    lines = [f"> [!eef] [{esc(title)}]({s['url']})", f"> {meta}", ">",
             "> | imp | cost | evi | n | smd | ci | i2 |",
             "> | --- | --- | --- | --- | --- | --- | --- |",
             f"> | {imp} | {cost} | {evi} | {s.get('n_page') if s.get('n_page') is not None else len(s['refs'])} | "
             f"{d2(p.get('smd')) if s['refs'] else 'NA'} | {(d2(p.get('lo')) + ' ~ ' + d2(p.get('hi'))) if s['refs'] else 'NA'} | {i2 if s['refs'] else 'NA'} |"]
    if s["refs"]:
        lines += [">", f"> > [!eef-studies]- {len(s['refs'])} 条效应量 · {len({r['cite'] for r in s['refs']})} 项研究",
                  "> > | ref | type | smd | ci | w |", "> > | --- | --- | --- | --- | --- |"]
        for r in s["refs"]:
            cite = esc(r["cite"]) + (f" <span class=\"eef-tag\">{esc(r['tag'])}</span>" if r["tag"] else "")
            lines.append(f"> > | {cite} | {TYPE_ZH.get(r['type'], r['type'] or '')} | {d2(r['smd'])} | {d2(r['lo'])} ~ {d2(r['hi'])} | {(r['w'] or 0):.1f}% |")
    auto = auto_checks(s)
    own = [e for e in errata if e.get("strand") == slug]
    if auto or own:
        lines += [">", f"> > [!eef-errata] {len(auto) + len(own)} 条"]
        lines += [f"> > - {AUTO} {a}" for a in auto]
        lines += [f"> > - ⚑ **{e.get('type', '勘误')}** {e.get('note', '')}" for e in own]
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
   表头代号由 CSS 显示为中文：imp 影响（月）｜cost 成本｜evi 证据强度｜n 研究数｜smd 合并效应量｜ci 95% 置信区间｜i2 异质性 I²｜ref 研究｜type 类型｜w 权重。
   成本与证据强度沿用 EEF 五级评分（●○），研究列表默认折叠；勘误框只在自动核算或 eef/errata.json 有内容时出现。 %%

"""
    TEMPLATE.write_text(head + render_strand(slug, s, load_json(ERRATA_JSON, [])) + "\n", encoding="utf-8")
    print(f"wrote {TEMPLATE.relative_to(ROOT)}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("import"); p.add_argument("--raw", required=True); p.set_defaults(func=cmd_import)
    p = sub.add_parser("template"); p.add_argument("--slug", default="feedback"); p.set_defaults(func=cmd_template)
    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
