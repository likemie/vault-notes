import re
from pathlib import Path
from pypdf import PdfReader

pdf_path = 'books/Cheng_2026_KeJiChuangXin/Cheng_2026_KeJiChuangXin.pdf'
output_dir = Path('books/Cheng_2026_KeJiChuangXin/')
reader = PdfReader(pdf_path)

full_text = ""
for page in reader.pages:
    full_text += page.extract_text() + "\n"

# Normalize Kangxi Radicals to standard CJK
kangxi_to_cjk = {
    '\u2f00': '\u4e00', # ⼀ -> 一
    '\u2f06': '\u4e8c', # ⼆ -> 二
    '\u2f0b': '\u516b', # ⼋ -> 八
    '\u2f17': '\u5341', # ⼗ -> 十
    '\u2f04': '\u4e94', # ⼔ -> 五 (Wait, check 5)
}
# Actually \u2f04 is \u4e59 (Radical SECOND). 
# Let's just do a broad replacement for common ones seen.
def normalize(t):
    t = t.replace('⼀', '一').replace('⼆', '二').replace('⼋', '八').replace('⼗', '十').replace('⼔', '五').replace('⼄', '乙')
    return t

full_text = normalize(full_text)

# Split by Part or Chapter
# Use a pattern that matches "第...篇" or "第...章" at the start of a line.
# We skip the TOC by checking if there are dots or page numbers immediately after.
pattern = r'\n(?=第[一二三四五六七八九十]+[篇章])'
sections = re.split(pattern, full_text)

def clean_filename(text):
    lines = [l.strip() for t in text.strip().split('\n') for l in [t] if l.strip()]
    if not lines: return "empty"
    # Take up to 2 lines for the title
    title = " ".join(lines[:2])
    title = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_')
    return title[:80]

# Detect and skip duplicates (headers appearing on every page)
seen_titles = set()

file_idx = 0
for content in sections:
    title = clean_filename(content)
    if title in seen_titles and len(content) < 500: # Heuristic for page headers
        continue
    
    if file_idx == 0:
        filename = "00_Front_Matter.txt"
    else:
        filename = f"{file_idx:02d}_{title}.txt"
    
    with open(output_dir / filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {filename}")
    seen_titles.add(title)
    file_idx += 1

