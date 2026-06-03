import re
import hashlib
from pathlib import Path
from pypdf import PdfReader

pdf_path = 'books/Cheng_2026_KeJiChuangXin/Cheng_2026_KeJiChuangXin.pdf'
output_dir = Path('books/Cheng_2026_KeJiChuangXin/')
reader = PdfReader(pdf_path)

full_text = ""
for page in reader.pages:
    full_text += page.extract_text() + "\n"

def normalize(t):
    # More comprehensive normalization for common variants seen in PDFs
    replacements = {
        '⼀': '一', '⼆': '二', '三': '三', '四': '四', '五': '五',
        '⼔': '五', '⼄': '乙', '六': '六', '七': '七', '⼋': '八',
        '九': '九', '⼗': '十', '⼫': '尸', '⼅': '亅', '⼐': '凵',
        # Handle some combined ones if they exist as single chars
    }
    for k, v in replacements.items():
        t = t.replace(k, v)
    return t

full_text = normalize(full_text)

# Split by Chapter or Part
pattern = r'\n(?=第[一二三四五六七八九十]+[篇章])'
sections = re.split(pattern, full_text)

def get_title(text):
    lines = [l.strip() for t in text.strip().split('\n') for l in [t] if l.strip()]
    if not lines: return "Empty"
    # Filter out potential page numbers or noise from first line
    title = " ".join(lines[:2])
    title = re.sub(r'[^\w\u4e00-\u9fa5]', '_', title) # Keep CJK characters
    title = re.sub(r'_+', '_', title).strip('_')
    return title[:100]

seen_hashes = set()
file_idx = 0

for content in sections:
    content_stripped = content.strip()
    if not content_stripped: continue
    
    # De-duplicate by content hash
    h = hashlib.md5(content_stripped.encode('utf-8')).hexdigest()
    if h in seen_hashes: continue
    seen_hashes.add(h)
    
    title = get_title(content_stripped)
    if file_idx == 0:
        filename = "00_Front_Matter.txt"
    else:
        filename = f"{file_idx:02d}_{title}.txt"
    
    with open(output_dir / filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {filename}")
    file_idx += 1

