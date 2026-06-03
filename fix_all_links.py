import re

file_path = 'wiki/arguments/books/Cheng_2026_KeJiChuangXin/Argument_Cheng_2026_KeJiChuangXin.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove from YAML array
content = re.sub(r'\s*-\s*"\[\[High-Quality Sci-Tech Supply\]\]"', '', content)
content = re.sub(r'\s*-\s*"\[\[Principal Status of Enterprises in Innovation\]\]"', '', content)
content = re.sub(r'\s*-\s*"\[\[Sci-Tech Achievement Transformation\]\]"', '', content)
content = re.sub(r'\s*-\s*"\[\[Deep Integration of Sci-Tech and Industrial Innovation\]\]"', '', content)
content = re.sub(r'\s*-\s*"\[\[Two Separate Skins Phenomenon\]\]"', '', content)
content = re.sub(r'\s*-\s*"“两张皮”现象"', '', content)

# Remove from body
bad_links = [
    "High-Quality Sci-Tech Supply",
    "Principal Status of Enterprises in Innovation",
    "Sci-Tech Achievement Transformation",
    "Deep Integration of Sci-Tech and Industrial Innovation",
    "Two Separate Skins Phenomenon"
]

for link in bad_links:
    # Pattern for [[Link|Text]] -> Text
    content = re.sub(rf'\[\[{re.escape(link)}\|([^\]]+)\]\]', r'\1', content)
    # Pattern for [[Link]] -> Link
    content = re.sub(rf'\[\[{re.escape(link)}\]\]', link, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed all remaining broken links.")
