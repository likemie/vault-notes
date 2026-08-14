import re

filepath = "/Users/shaoyangwu/Documents/MyNotes/wiki/arguments/journal-articles/Review of Educational Research/Argument_Hofer_1997_RER.md"

with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

replacements = {
    "接收知识": "Received Knowledge",
    "主观知识": "Subjective Knowledge",
    "程序知识": "Procedural Knowledge",
    "建构知识": "Constructed Knowledge",
    "绝对认知": "Absolute Knowing",
    "过渡认知": "Transitional Knowing",
    "独立认知": "Independent Knowing",
    "语境认知": "Contextual Knowing",
    "绝对论者": "Absolutist",
    "多元论者": "Multiplist",
    "评价论者": "Evaluatist",
}

for zh_term, en_term in replacements.items():
    # Replace ONLY if not already enclosed in [[ ]] or followed by |
    # Using negative lookbehind (?<!\[\[) and negative lookahead (?![^\[]*\]\]) is tricky.
    # A safer approach is to replace all occurrences not already linked.
    pattern = r'(?<!\[\[)(%s)(?!\||\]\])' % zh_term
    replacement = r'[[%s|\1]]' % en_term
    text = re.sub(pattern, replacement, text)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)

print("Linked concepts in Argument_Hofer_1997_RER.md")
