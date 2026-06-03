import os
import re
from pathlib import Path

# 1. Rename the file
old_file = Path('wiki/facts/china/1999 Reform of 242 Research Institutes.md')
new_file = Path('wiki/facts/china/1999 Reform of Research Institutes.md')

if old_file.exists():
    os.rename(old_file, new_file)

# 2. Update content in the new file
if new_file.exists():
    with open(new_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update title in YAML and header
    content = content.replace('1999 Reform of 242 Research Institutes', '1999 Reform of Research Institutes')
    
    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. Update links in Argument file
arg_file = Path('wiki/arguments/books/Cheng_2026_KeJiChuangXin/Argument_Cheng_2026_KeJiChuangXin.md')
if arg_file.exists():
    with open(arg_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('1999 Reform of 242 Research Institutes', '1999 Reform of Research Institutes')
    
    with open(arg_file, 'w', encoding='utf-8') as f:
        f.write(content)

# 4. Fix APA citations in all created concept/fact files
files_to_check = [
    new_file,
    arg_file,
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
            
        # Replace Cheng_2026_KeJiChuangXin with 程楠 等, 2026
        # Matches: Cheng_2026_KeJiChuangXin, p.
        # Matches: Cheng_2026_KeJiChuangXin, pp.
        new_content = re.sub(r'Cheng_2026_KeJiChuangXin,\s*p\.', '程楠 等, 2026, p.', content)
        new_content = re.sub(r'Cheng_2026_KeJiChuangXin,\s*pp\.', '程楠 等, 2026, pp.', content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
                print(f"Fixed citations in {file_path}")

print("Done fixing names and citations.")
