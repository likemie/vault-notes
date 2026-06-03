import re
from pathlib import Path
from pypdf import PdfReader

pdf_path = 'books/Cheng_2026_KeJiChuangXin/Cheng_2026_KeJiChuangXin.pdf'
output_dir = Path('books/Cheng_2026_KeJiChuangXin/')
reader = PdfReader(pdf_path)

full_text = ""
for page in reader.pages:
    full_text += page.extract_text() + "\n"

# Match "第" followed by 1-4 characters (Kangxi or CJK) then "章"
# Use re.MULTILINE to ensure it's often at the start of a line or after a newline.
# Pattern: \n第.{1,4}章
pattern = r'\n(?=第.{1,4}章)'
chapters = re.split(pattern, full_text)

def clean_filename(text):
    # Take first two lines to get title
    lines = text.strip().split('\n')
    title = " ".join(lines[:2])
    # Remove forbidden chars
    title = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_')
    return title[:100]

for i, content in enumerate(chapters):
    if i == 0:
        filename = "00_Front_Matter.txt"
    else:
        title = clean_filename(content)
        filename = f"{i:02d}_{title}.txt"
    
    with open(output_dir / filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {filename}")

