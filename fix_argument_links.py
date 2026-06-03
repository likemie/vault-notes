import re

file_path = 'wiki/arguments/books/Cheng_2026_KeJiChuangXin/Argument_Cheng_2026_KeJiChuangXin.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace links with unlinked text since we deleted those concepts
content = content.replace('[[High-Quality Sci-Tech Supply|高质量科技供给]]', '高质量科技供给')
content = content.replace('[[Principal Status of Enterprises in Innovation|企业科技创新主体地位]]', '企业科技创新主体地位')
content = content.replace('[[Sci-Tech Achievement Transformation|科技成果转化应用]]', '科技成果转化应用')
content = content.replace('[[Deep Integration of Sci-Tech and Industrial Innovation|科技与产业融合]]', '科技与产业融合')
content = content.replace('[[Two Separate Skins Phenomenon]]', '“两张皮”现象')
content = content.replace('[[Two Separate Skins Phenomenon|两张皮现象]]', '“两张皮”现象')
content = content.replace('[[High-Quality Sci-Tech Supply|科技供给]]', '科技供给')
content = content.replace('[[Principal Status of Enterprises in Innovation|企业创新主体地位]]', '企业创新主体地位')
content = content.replace('[[Sci-Tech Achievement Transformation|成果转化]]', '成果转化')
content = content.replace('[[Deep Integration of Sci-Tech and Industrial Innovation|科技创新和产业创新深度融合]]', '科技创新和产业创新深度融合')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Unlinked deleted concepts in Argument.")
