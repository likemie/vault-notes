import os
import re

def fix_authors_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return False
        
    if not content.startswith('---'):
        return False
        
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
        
    frontmatter = parts[1]
    
    # Match authors: "some name" or authors: 'some name' or authors: some name
    # But only if it's on a single line and not already a list
    match = re.search(r'^authors:\s*(.+)$', frontmatter, re.MULTILINE)
    
    if match:
        val = match.group(1).strip()
        # If it's already a list (starts with [ or is empty), skip
        if val.startswith('[') or val == '':
            return False
            
        # If it's a string, format it as a list item
        new_authors = f"authors:\n  - {val}"
        new_frontmatter = frontmatter[:match.start()] + new_authors + frontmatter[match.end():]
        
        new_content = f"---{new_frontmatter}---{parts[2]}"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    count = 0
    directories = ['wiki/arguments', 'templater']
    for directory in directories:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.md'):
                    filepath = os.path.join(root, file)
                    if fix_authors_in_file(filepath):
                        count += 1
    print(f"Fixed authors format in {count} files.")

if __name__ == '__main__':
    main()
