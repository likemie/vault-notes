import re
from pathlib import Path
from pypdf import PdfReader

pdf_path = 'books/Cheng_2026_KeJiChuangXin/Cheng_2026_KeJiChuangXin.pdf'
output_dir = Path('books/Cheng_2026_KeJiChuangXin/')
reader = PdfReader(pdf_path)

full_text = ""
for page in reader.pages:
    full_text += page.extract_text() + "\n"

# Define chapter patterns
# Note: The text might have spaces or newlines in headings.
# We look for "第...章" followed by the title.
chapters = re.split(r'\n(?=第[一二三四五六七八九十]+章)', full_text)

# The first part before "第[一]章" might be front matter, TOC, etc.
# Let's save each part.
for i, content in enumerate(chapters):
    if i == 0:
        filename = "00_Front_Matter.txt"
    else:
        # Extract title from the first line of content
        first_line = content.strip().split('\n')[0]
        # Clean title for filename
        clean_title = re.sub(r'[^\w\s-]', '', first_line).strip().replace(' ', '_')
        filename = f"{i:02d}_{clean_title}.txt"
    
    with open(output_dir / filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {filename}")

