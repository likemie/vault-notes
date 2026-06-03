import re
from pathlib import Path

files_to_check = [
    Path('wiki/facts/china/1999 Reform of Research Institutes.md'),
    Path('wiki/facts/china/Jiebang Guashuai.md'),
    Path('wiki/facts/us/DARPA.md'),
    Path('wiki/concepts/education/STEM Education.md'),
    Path('wiki/concepts/industrial-innovation/Hidden Champions.md'),
    Path('wiki/concepts/technology-innovation/Society 5.0.md'),
    Path('wiki/facts/japan/Tsukuba Science City.md'),
    Path('wiki/facts/china/Shenzhen Four 90 Percent Innovation Pattern.md'),
    Path('wiki/facts/china/Xi\'an Three Reforms on Sci-Tech Achievements.md'),
    Path('wiki/facts/us/SBIR and STTR Programs.md')
]

for file_path in files_to_check:
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = re.sub(r'Cheng_2026_KeJiChuangXin,\s*p\.', '程楠 等, 2026, p.', content)
        new_content = re.sub(r'Cheng_2026_KeJiChuangXin,\s*pp\.', '程楠 等, 2026, pp.', new_content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
                print(f"Fixed citations in {file_path}")

print("Done fixing citations.")
