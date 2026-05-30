import os
import yaml

def check_duplicates(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return
        
    if not content.startswith('---'):
        return
        
    parts = content.split('---', 2)
    if len(parts) < 3:
        return
        
    frontmatter = parts[1]
    
    keys = []
    for line in frontmatter.split('\n'):
        if ':' in line and not line.strip().startswith('-') and not line.strip().startswith('#') and line.strip() and not line.startswith(' '):
            key = line.split(':')[0].strip()
            if key in keys:
                print(f"DUPLICATE KEY '{key}' in {filepath}")
            keys.append(key)

def main():
    for root, dirs, files in os.walk('wiki/arguments/'):
        for file in files:
            if file.endswith('.md'):
                check_duplicates(os.path.join(root, file))

if __name__ == '__main__':
    main()
