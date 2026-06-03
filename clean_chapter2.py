import os
import re

# 1. Delete the files
files_to_delete = [
    'wiki/facts/china/Research and Development Super Deduction.md',
    'wiki/facts/china/STAR Market.md'
]
for f in files_to_delete:
    if os.path.exists(f):
        os.remove(f)
        print(f"Deleted {f}")

# 2. Remove links from Argument page
arg_file = 'wiki/arguments/books/Cheng_2026_KeJiChuangXin/Argument_Cheng_2026_KeJiChuangXin.md'
with open(arg_file, 'r', encoding='utf-8') as f:
    content = f.read()

# [[Research and Development Super Deduction|研发费用加计扣除]] -> 研发费用加计扣除
content = re.sub(r'\[\[Research and Development Super Deduction\|([^\]]+)\]\]', r'\1', content)
# [[STAR Market|科创板]] -> 科创板
content = re.sub(r'\[\[STAR Market\|([^\]]+)\]\]', r'\1', content)

with open(arg_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Removed links from Argument file.")

