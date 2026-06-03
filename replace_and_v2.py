import re

file_path = 'wiki/arguments/books/Hall_Boccanfuso_2025_Springer/Argument_Ramming_2025_CorporateSupport.md'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # Skip citation lines and the specific Act link
    if line.strip().startswith('citation:') or '[[CHIPS and Science Act]]' in line:
        new_lines.append(line)
        continue
    
    # Skip lines that are purely English quotes (starting with > ")
    # Also handles potential leading whitespace
    if re.search(r'^\s*>\s*"[^"]+"', line) and not re.search(r'[\u4e00-\u9fff]', line):
        new_lines.append(line)
        continue

    # Replace " and " with " 和 "
    # We use \b to ensure word boundaries
    # We pad with spaces to keep the flow if it was "A and B"
    line = re.sub(r'(\s)and(\s)', r'\1和\2', line)
    
    new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Done")
