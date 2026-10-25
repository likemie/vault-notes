#!/usr/bin/env python3
"""效应量表格：指标白名单 + 数值解析 + 统一换算到 d + 生成效应条。

只处理"新结构"的实证数据表（表头含"效应值"列）：
  concept-effect-table-marker            原始研究结果
  concept-meta-analysis-table-marker     一阶元分析
  concept-second-order-meta-table-marker 二阶元分析
  concept-subgroup-table-marker          亚组与调节分析（指标沿用主表中同一研究的指标）

填表规则（给人和 AI）：
  - "效应指标"列只写指标名（Cohen's $d$、Hedges' $g$、$r$、OR、$\\eta^2$ 等），可在括号里注明"均值/中位数"。
  - "效应值"列只写原文报告的原始数值：0.40 / −0.12 / 0.62–0.66 / > 0.80 / —。
    不要写 d = …，不要写文字，不要自己换算，不要手写效应条。
  - 效应条由本脚本生成：python3 scripts/effect_table.py --write <文件…>
  - 换算只用于效应条长度（统一到 d 尺度）；单元格里显示的永远是原始数值。

用法：
  python3 scripts/effect_table.py --check [文件…]     # 校验（默认全库新结构表格）
  python3 scripts/effect_table.py --write [文件…]     # 重新生成效应条
  python3 scripts/effect_table.py --convert r 0.30    # 单次换算，打印公式
"""
from __future__ import annotations

import argparse
import html
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"

MARKERS = {
    "concept-effect-table-marker": "effect",
    "concept-meta-analysis-table-marker": "ma",
    "concept-second-order-meta-table-marker": "so",
    "concept-subgroup-table-marker": "subgroup",
}
BAR_STEPS, BAR_SCALE = 28, 20  # 与 MetaX 一致：b = round(|d| × 20)，28 格 = d 1.4

# ---------------------------------------------------------------- 指标白名单
# family: d   标准化均值差族，直接作为 d
#         r   相关系数          d = 2r / √(1 − r²)
#         z   Fisher z          r = tanh z，再按 r
#         or  比值比            d = ln(OR) · √3 / π
#         var 解释方差比例      d = 2 √(v / (1 − v))（两组、单因素近似）
#         beta 标准化回归系数（SD 单位）≈ d（近似）
#         none 不可换算（显示数值，不画条）
METRICS: List[Tuple[str, str, str]] = [
    # (正则, family, 规范名)
    (r"glass", "d", "Glass' Δ"),
    (r"\\delta|δ|Δ", "d", "δ / Δ"),
    (r"hedges|\bg\s*\+|\bg\b|g_", "d", "Hedges' g"),
    (r"cohen|\bd\b|d_", "d", "Cohen's d"),
    (r"\bsmd\b|标准化均差|标准化均值差|标准化平均差|标准化均数差", "d", "SMD"),
    (r"\bes\b|效应量差|es 差", "d", "ES"),
    (r"fisher|\bz_?r\b", "z", "Fisher z"),
    (r"\bor\b|比值比|优势比|odds", "or", "OR"),
    (r"partial|偏\s*\$?\\?eta|偏 η", "var", "partial η²"),
    (r"\\eta|η", "var", "η²"),
    (r"\\omega|ω", "var", "ω²"),
    (r"\br\^2\b|\bR\^2\b|R²|决定系数", "var", "R²"),
    (r"\\beta|β", "beta", "β"),
    (r"\br\b|pearson|相关系数|r_\{?pb", "r", "r"),
    (r"\brr\b|\bhr\b|风险比|危险比|百分位|成功率|%|率", "none", "不可换算"),
]
APPROX = {"var": "两组单因素近似", "beta": "仅当结果变量已标准化时近似", "or": "Logistic 潜变量假设"}

def clean(s: str) -> str:
    s = re.sub(r'<span class="[^"]*\bmx-bar\b[^"]*"(?: title="[^"]*")?><span class="b\d+"></span></span>', "", s)
    s = s.replace("$", "").replace("\\text", "").replace("\\mathrm", "").replace("{", "").replace("}", "")
    return s.strip()

def metric_family(cell: str) -> Tuple[Optional[str], str]:
    c = clean(cell)
    c = re.sub(r"[（(][^）)]*[）)]", lambda m: m.group(0) if re.search(r"\b[dgr]\b|η|ω|β", m.group(0)) else "", c)
    c = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", c)
    best = None
    for k, (pat, fam, name) in enumerate(METRICS):
        m = re.search(pat, c, re.I if fam not in ("var",) else 0)
        if m and (best is None or (m.start(), k) < best[0]):
            best = ((m.start(), k), fam, name)
    if best:
        return best[1], best[2]
    if c in ("—", "-", ""):
        return None, "—"
    return "unknown", c

# ---------------------------------------------------------------- 数值解析
NUM = r"[+\-−–]?\s*\d*\.?\d+"

@dataclass
class Value:
    kind: str            # point / range / bound / missing / ref / bad
    x: Optional[float]   # 用于画条的代表值
    text: str

def to_float(s: str) -> float:
    return float(s.replace("−", "-").replace("–", "-").replace(" ", "").replace(",", ""))

def parse_value(cell: str) -> Value:
    raw = html.unescape(clean(cell))
    v = raw.replace("\\approx", "≈").replace("\\ge", "≥").replace("\\le", "≤").replace("&gt;", ">").replace("&lt;", "<")
    v = v.strip()
    if v in ("—", "-", "–", "", "NA", "N/A"):
        return Value("missing", None, raw)
    if re.fullmatch(r"见亚组表", v):
        return Value("ref", None, raw)
    m = re.fullmatch(rf"[≈~]?\s*({NUM})", v)
    if m:
        return Value("point", to_float(m.group(1)), raw)
    m = re.fullmatch(rf"({NUM})\s*(?:–|—|~|to|-|\\?text–)\s*({NUM})", v)
    if m:
        a, b = to_float(m.group(1)), to_float(m.group(2))
        return Value("range", (a + b) / 2, raw)
    m = re.fullmatch(rf"([><≥≤])\s*({NUM})", v)
    if m:
        return Value("bound", to_float(m.group(2)), raw)
    return Value("bad", None, raw)

# ---------------------------------------------------------------- 换算
def to_d(fam: str, x: float) -> Tuple[Optional[float], str]:
    if fam in ("d", "beta"):
        return x, "d = x" if fam == "d" else "d ≈ β（结果变量已标准化）"
    if fam == "r":
        if abs(x) >= 1:
            return None, "|r| ≥ 1，无法换算"
        return 2 * x / math.sqrt(1 - x * x), "d = 2r / √(1 − r²)"
    if fam == "z":
        r = math.tanh(x)
        return 2 * r / math.sqrt(1 - r * r), "r = tanh z；d = 2r / √(1 − r²)"
    if fam == "or":
        if x <= 0:
            return None, "OR ≤ 0，无法换算"
        return math.log(x) * math.sqrt(3) / math.pi, "d = ln(OR) · √3 / π"
    if fam == "var":
        if not 0 <= x < 1:
            return None, "解释方差比例须在 [0, 1)"
        return 2 * math.sqrt(x / (1 - x)), "d = 2√(v / (1 − v))"
    return None, "不可换算"

def bar_html(d: float, fam: str, name: str, raw: str, formula: str, kind: str) -> str:
    n = min(BAR_STEPS, round(abs(d) * BAR_SCALE))
    cls = ["mx-bar", "ef-bar"]
    if d < 0: cls.append("neg")
    if fam not in ("d",): cls.append("conv")
    if kind == "bound": cls.append("bound")
    if kind == "range": cls.append("range")
    tip = f"{name} {raw}"
    if fam != "d":
        tip += f" → d ≈ {d:.2f}（{formula}"
        tip += f"；{APPROX[fam]}）" if fam in APPROX else "）"
    if kind == "range": tip += "；取区间中点"
    if kind == "bound": tip += "；下界/上界值"
    tip = tip.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")
    return f'<span class="{" ".join(cls)}" title="{tip}"><span class="b{n}"></span></span>'

# ---------------------------------------------------------------- 表格处理
def split_cells(line: str) -> List[str]:
    body = line[1:].strip() if line.startswith(">") else line.strip()
    return [c.strip() for c in re.split(r"(?<!\\)\|", body)[1:-1]]

def join_cells(cells: List[str]) -> str:
    return "> | " + " | ".join(cells) + " |"

def header_index(H: List[str], kind: str) -> Tuple[Optional[int], Optional[int]]:
    vi = next((i for i, h in enumerate(H) if h.strip() == "效应值"), None)
    mi = next((i for i, h in enumerate(H) if "效应指标" in h), None)
    return vi, mi

@dataclass
class Problem:
    sev: str
    line: int
    code: str
    msg: str

def process(text: str, write: bool) -> Tuple[str, List[Problem]]:
    lines = text.split("\n")
    probs: List[Problem] = []
    study_metric = {}
    blocks = []  # (kind, header_line_idx, row idxs)
    i = 0
    while i < len(lines):
        if lines[i].startswith("> [!"):
            j = i + 1
            while j < len(lines) and lines[j].startswith(">"):
                j += 1
            blk = "\n".join(lines[i:j])
            kind = next((v for k, v in MARKERS.items() if k in blk), None)
            if kind:
                rows = [k for k in range(i, j) if lines[k].startswith("> |")]
                if len(rows) >= 2:
                    blocks.append((kind, rows))
            i = j
        else:
            i += 1
    # 主表优先，亚组表最后（需要主表里的研究指标）
    blocks.sort(key=lambda b: b[0] == "subgroup")
    for kind, rows in blocks:
        H = split_cells(lines[rows[0]])
        vi, mi = header_index(H, kind)
        if vi is None:
            continue  # 旧结构表格，暂不处理
        if kind != "subgroup" and mi is None:
            probs.append(Problem("ERROR", rows[0] + 1, "EFFECT_METRIC_COL", "表头有“效应值”但缺少“效应指标”列"))
            continue
        current_study = ""
        last_sub = ("d", "Cohen's d")
        for r in rows[2:]:
            c = split_cells(lines[r])
            if len(c) != len(H):
                probs.append(Problem("ERROR", r + 1, "EFFECT_COLS", f"列数 {len(c)} 与表头 {len(H)} 不一致"))
                continue
            if c[0]:
                current_study = clean(c[0])
            if kind == "subgroup":
                if c[0]:
                    last_sub = study_metric.get(current_study, ("d", "Cohen's d"))
                if mi is not None and c[mi] and c[mi] not in ("—",):
                    last_sub = metric_family(c[mi])
                fam, name = last_sub
            else:
                fam, name = metric_family(c[mi])
                study_metric[current_study] = (fam, name) if fam not in (None, "unknown") else ("d", "Cohen's d")
            val = parse_value(c[vi])
            had_bar = "mx-bar" in c[vi]
            if val.kind == "bad":
                probs.append(Problem("ERROR", r + 1, "EFFECT_VALUE_FORMAT",
                    f"效应值只能是数字、区间、> / < 界值或 —：{val.text[:40]!r}（文字说明移到其他列）"))
                continue
            if fam == "unknown" and val.kind not in ("missing", "ref"):
                probs.append(Problem("ERROR", r + 1, "EFFECT_METRIC_UNKNOWN",
                    f"未登记的效应指标：{name[:40]!r}（在 scripts/effect_table.py METRICS 中登记或改用规范名）"))
                continue
            new = val.text
            if val.x is not None and fam not in (None, "none", "unknown"):
                d, formula = to_d(fam, val.x)
                if d is None:
                    probs.append(Problem("ERROR", r + 1, "EFFECT_CONVERT", f"{name} {val.text}：{formula}"))
                    continue
                if abs(d) > 3:
                    probs.append(Problem("WARN", r + 1, "EFFECT_EXTREME", f"换算后 |d| = {abs(d):.2f} > 3，请核对原文（是否把 SE 当成 SD？）"))
                new = bar_html(d, fam, name, val.text, formula, val.kind) + val.text
            if new != c[vi]:
                if write:
                    c[vi] = new
                    lines[r] = join_cells(c)
                else:
                    probs.append(Problem("ERROR" if had_bar else "WARN", r + 1, "EFFECT_BAR_STALE",
                        "效应条缺失或与数值不符；运行 python3 scripts/effect_table.py --write <文件>（不要手写效应条）"))
    return "\n".join(lines), probs

# ---------------------------------------------------------------- 无数据行
ALL_MARKERS = dict(MARKERS, **{"concept-other-empirical-table-marker": "other"})
RES_COL = re.compile(r"组别统计|效应值|效应量|汇总效应|原始统计|统计结果|显著|不确定|检验|关键结果|结果|发现|CI")
DATA = re.compile(r"\d|[一二两三四五六七八九十百千万几]+\s*(倍|成(?![为功果立员本绩就熟形型长])|个百分点|分之)|翻倍|翻番|半数|过半|一半")

def _strip_refs(s: str) -> str:
    s = re.sub(r'<span class="[^"]*"[^>]*>(?:<span[^>]*></span>)?</span>', "", s)
    s = re.sub(r"\[\[[^\]|]*\\?\|([^\]]*)\]\]", r"\1", s)
    s = re.sub(r"\[\[[^\]]*\]\]", "", s)
    s = re.sub(r"\bpp?\.\s*\d+(?:\s*[–—-]\s*\d+)?(?:\s*[,，、;；]\s*\d+(?:\s*[–—-]\s*\d+)?)*", "", s)
    s = re.sub(r"\b(1[89]|20)\d\d[a-z]?\b", "", s)
    return s

def nodata_rows(text: str) -> List[Tuple[int, str]]:
    """实证表格中结果栏没有任何数据的行：(行号, 行文本)。"""
    lines = text.split("\n"); out = []; i = 0
    while i < len(lines):
        if lines[i].startswith("> [!"):
            j = i + 1
            while j < len(lines) and lines[j].startswith(">"):
                j += 1
            blk = "\n".join(lines[i:j]); kind = next((v for k, v in ALL_MARKERS.items() if k in blk), None)
            rows = [k for k in range(i, j) if lines[k].startswith("> |")]
            if kind and len(rows) >= 3:
                H = split_cells(lines[rows[0]])
                first = _strip_refs(H[0])
                if kind != "other" or re.search(r"研究|文献|来源|调研|项目|监测", first):
                    rc = [n for n, h in enumerate(H) if n > 0 and RES_COL.search(h)] or list(range(1, len(H)))
                    for r in rows[2:]:
                        c = split_cells(lines[r])
                        if len(c) != len(H): continue
                        res = " ".join(_strip_refs(c[n]) for n in rc if n < len(c))
                        if "见亚组表" in res: continue
                        if not DATA.search(res): out.append((r + 1, lines[r]))
            i = j
        else:
            i += 1
    return out

_NSW = re.compile(r"未达显著|不显著|无显著|\bn\.?\s?s\.?(?![a-z])|\bns\b", re.I)
_PV = re.compile(r"p\s*([<>=≤≥])\s*(0?\.\d+|1(?:\.0+)?)", re.I)
_TEST = re.compile(r"Q|W\s*=|F\s*[(=]|χ|\\chi|组间|between", re.I)

def not_significant(sig: str) -> bool:
    """显著性栏是否表明不显著：有 p ≥ .05 或“不显著/n.s.”字样，且没有任何 p < .05。"""
    s = sig.replace("$", "")
    ps = _PV.findall(s)
    if any((op in "<≤" and float(v) <= .05) or (op == "=" and float(v) < .05) for op, v in ps):
        return False
    if "显著" in s and not _NSW.search(s) and "边缘" not in s:
        return False
    return any(op in ">≥=" and float(v) >= .05 for op, v in ps) or bool(_NSW.search(s))

def ns_subgroup_rows(text: str) -> List[Tuple[int, str]]:
    """亚组表中不显著的行：该水平不显著，或所在调节变量组的组间检验不显著（整组）。"""
    lines = text.split("\n"); out = []; i = 0
    while i < len(lines):
        if lines[i].startswith("> [!") and "concept-subgroup-table-marker" in "\n".join(lines[i:i + 3]):
            j = i + 1
            while j < len(lines) and lines[j].startswith(">"):
                j += 1
            rows = [k for k in range(i, j) if lines[k].startswith("> |")]
            if len(rows) >= 3:
                H = split_cells(lines[rows[0]])
                cG = H.index("显著性或组间检验") if "显著性或组间检验" in H else None
                cS = H.index("研究") if "研究" in H else None
                cM = H.index("调节变量") if "调节变量" in H else None
                group_ns = False
                for r in rows[2:]:
                    c = split_cells(lines[r])
                    if cG is None or len(c) != len(H): continue
                    if (cS is not None and c[cS]) or (cM is not None and c[cM]):
                        group_ns = bool(_TEST.search(c[cG]) and not_significant(c[cG]))
                    if group_ns or (not _TEST.search(c[cG]) and not_significant(c[cG])):
                        out.append((r + 1, lines[r]))
            i = j
        else:
            i += 1
    return out

def lint_file(path: Path, text: str, head_text: str = None) -> List[Problem]:
    """供 vault_lint.py 调用。head_text 为 HEAD 版本；已存在于 HEAD 的无数据行不报。"""
    p = str(path).replace("\\", "/")
    if "/templates/" in p or "table-marker" not in text:
        return []
    probs = process(text, write=False)[1] if "效应值" in text else []
    if "/arguments/" not in p and "Argument_" not in p.split("/")[-1]:
        old = set(head_text.split("\n")) if head_text else set()
        for ln, row in nodata_rows(text):
            if row in old: continue
            probs.append(Problem("ERROR", ln, "EMPIRICAL_NO_DATA",
                "实证表格只写有数据的结果：这一行的结果栏没有数值、比例、计数或统计量。"
                "质性结论、政策文本归纳、仅有样本量的文字结论改写进正文或“相关研究”，或回原文补上数据"))
        for ln, row in enumerate(text.split("\n"), 1):
            if row.startswith("> |") and "见亚组表" in row:
                probs.append(Problem("ERROR", ln, "EFFECT_SEE_SUBGROUP",
                    "主表效应值不能写“见亚组表”：填原文的总体效应；原文没有总体效应时，独立亚组可按逆方差合并计算并注明，否则删除该行"))
        for ln, row in ns_subgroup_rows(text):
            probs.append(Problem("ERROR", ln, "SUBGROUP_NOT_SIGNIFICANT",
                "亚组表只写显著的结果：该水平不显著，或所在调节变量的组间检验不显著（整组删除），不写入表格"))
    return probs

def iter_targets(args: List[str]) -> List[Path]:
    if args:
        return [Path(a) for a in args]
    return [p for p in WIKI.rglob("*.md") if "templates" not in p.parts and "效应值" in p.read_text(encoding="utf-8", errors="ignore")]

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--write", action="store_true")
    g.add_argument("--convert", nargs=2, metavar=("METRIC", "VALUE"))
    ap.add_argument("files", nargs="*")
    a = ap.parse_args()
    if a.convert:
        fam, name = metric_family(a.convert[0])
        val = parse_value(a.convert[1])
        if fam in (None, "unknown", "none") or val.x is None:
            print(f"{a.convert[0]} {a.convert[1]}：不可换算（family={fam}）"); return 1
        d, f = to_d(fam, val.x)
        print(f"{name} = {val.text}  →  d ≈ {d:.3f}   [{f}]" + (f"  ({APPROX[fam]})" if fam in APPROX else ""))
        return 0
    bad = 0
    for p in iter_targets(a.files):
        t = p.read_text(encoding="utf-8")
        new, probs = process(t, write=a.write)
        if a.write and new != t:
            p.write_text(new, encoding="utf-8"); print(f"updated {p}")
        for q in probs:
            if a.write and q.code == "EFFECT_BAR_STALE":
                continue
            print(f"{q.sev:<5} {p}:{q.line} [{q.code}] - {q.msg}")
            bad += q.sev == "ERROR"
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
