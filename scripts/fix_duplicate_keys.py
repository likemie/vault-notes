import os
import re

def fix_file(filepath):
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
    lines = frontmatter.split('\n')
    
    seen_keys = set()
    new_lines = []
    skipping = False
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            new_lines.append(line)
            continue
            
        # Check if this is a new key at the root
        if ':' in line and not line.startswith(' ') and not line.startswith('-'):
            key = line.split(':')[0].strip()
            if key in seen_keys:
                print(f"Removing duplicate key '{key}' and its values in {filepath}")
                skipping = True
                continue
            else:
                seen_keys.add(key)
                skipping = False
        elif line.startswith(' ') or line.startswith('-'):
            # This is a continuation of the previous key
            if skipping:
                continue
        else:
            # Maybe a comment or something else at root
            skipping = False
            
        new_lines.append(line)
        
    new_frontmatter = '\n'.join(new_lines)
    if new_frontmatter != frontmatter:
        new_content = f"---{new_frontmatter}---{parts[2]}"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    count = 0
    for root, dirs, files in os.walk('wiki/arguments/'):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                if fix_file(filepath):
                    count += 1
    print(f"Fixed {count} files.")

if __name__ == '__main__':
    main()
