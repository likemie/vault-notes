from pathlib import Path
import re

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph


SOURCE = Path("raw/香港国民教育调研（修订版）.docx")
OUTPUT = Path("raw/香港国民教育调研（修订版）.md")


def iter_blocks(document):
    for child in document.element.body.iterchildren():
        if child.tag == qn("w:p"):
            yield Paragraph(child, document)
        elif child.tag == qn("w:tbl"):
            yield Table(child, document)


def escape_text(text):
    return text.replace("\\", "\\\\").replace("*", "\\*").replace("_", "\\_")


def paragraph_markdown(paragraph):
    parts = []
    for child in paragraph._p:
        if child.tag == qn("w:r"):
            text = "".join(t.text or "" for t in child.iter(qn("w:t")))
            if not text:
                continue
            text = escape_text(text)
            rpr = child.find(qn("w:rPr"))
            is_sup = (
                rpr is not None
                and rpr.find(qn("w:vertAlign")) is not None
                and rpr.find(qn("w:vertAlign")).get(qn("w:val")) == "superscript"
            )
            parts.append(f"<sup>{text}</sup>" if is_sup else text)
        elif child.tag == qn("w:hyperlink"):
            text = "".join(t.text or "" for t in child.iter(qn("w:t")))
            rid = child.get(qn("r:id"))
            target = paragraph.part.rels[rid].target_ref if rid in paragraph.part.rels else text
            if text == target or text.startswith("http"):
                parts.append(f"<{target}>")
            else:
                parts.append(f"[{escape_text(text)}]({target})")
    return "".join(parts).strip()


def cell_text(cell):
    return "<br>".join(paragraph_markdown(p) for p in cell.paragraphs if paragraph_markdown(p))


def table_markdown(table):
    rows = [[cell_text(cell) for cell in row.cells] for row in table.rows]
    if not rows:
        return []
    width = len(rows[0])
    lines = [
        "| " + " | ".join(rows[0]) + " |",
        "| " + " | ".join(["---"] * width) + " |",
    ]
    for row in rows[1:]:
        lines.append("| " + " | ".join(row) + " |")
    return lines


def list_metadata(paragraph):
    ppr = paragraph._p.pPr
    if ppr is None or ppr.numPr is None:
        return None
    num_id = ppr.numPr.numId.val if ppr.numPr.numId is not None else 0
    ilvl = ppr.numPr.ilvl.val if ppr.numPr.ilvl is not None else 0
    return int(num_id), int(ilvl)


doc = Document(SOURCE)
lines = [
    "<!-- 修订主稿：截至2026年7月。由同名DOCX修订版转换，后续优先在本文件迭代。 -->",
    "",
]
list_counters = {}
in_policy_references = False

for block in iter_blocks(doc):
    if isinstance(block, Table):
        lines.extend(table_markdown(block))
        lines.append("")
        continue

    text = paragraph_markdown(block)
    if not text:
        continue
    style = block.style.name
    if style == "Heading 1":
        lines.extend([f"# {text}", ""])
        continue
    if style == "Heading 2":
        lines.extend([f"## {text}", ""])
        continue
    if style == "Heading 3":
        lines.extend([f"### {text}", ""])
        in_policy_references = text == "政策、统计、调研与媒体资料（沿用原稿编号）"
        if text == "补充学术文献与学位论文":
            in_policy_references = False
        continue
    if style == "Heading 4":
        lines.extend([f"#### {text}", ""])
        continue

    meta = list_metadata(block)
    if in_policy_references:
        key = ("policy", 0)
        list_counters[key] = list_counters.get(key, 0) + 1
        lines.extend([f"{list_counters[key]}. {text}", ""])
    elif meta is not None:
        num_id, level = meta
        key = (num_id, level)
        list_counters[key] = list_counters.get(key, 0) + 1
        indent = "    " * level
        lines.extend([f"{indent}{list_counters[key]}. {text}", ""])
    elif style == "List Bullet":
        lines.extend([f"- {text}", ""])
    elif any(text.startswith(prefix) for prefix in ("考察前：", "考察中：", "考察后：")):
        lines.extend([f"- {text}", ""])
    elif block._p.getparent() is not None:
        if lines and lines[-1] != "":
            lines.append("")
        lines.extend([text, ""])

content = "\n".join(lines).rstrip() + "\n"
OUTPUT.write_text(content, encoding="utf-8")
print(OUTPUT)
