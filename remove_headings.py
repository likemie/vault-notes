import re

file_path = 'wiki/arguments/books/Cheng_2026_KeJiChuangXin/Argument_Cheng_2026_KeJiChuangXin.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace #### 章节问题 and #### 论证链条
# We will wrap the question in a > [!question] callout for better reading experience as requested previously, or just leave it as text. 
# The user specifically said "直接论述内容" (directly discuss the content), so removing the headers is the main goal.
content = re.sub(r'#### 章节问题\n+', '', content)
content = re.sub(r'#### 论证链条\n+', '', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Headers removed.")
