import os
import re

def get_frontmatter(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return ""
        
    if not content.startswith('---'):
        return ""
    
    parts = content.split('---', 2)
    if len(parts) >= 3:
        return parts[1]
    return ""

def extract_field(frontmatter, field):
    match = re.search(r'^' + field + r':\s*(.*?)$', frontmatter, re.MULTILINE)
    if match:
        val = match.group(1).strip()
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            return val[1:-1]
        return val
    return ""

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python analyze_concepts.py <directory>")
        return
        
    directory = sys.argv[1]
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                fm = get_frontmatter(filepath)
                title = extract_field(fm, 'title') or file.replace('.md', '')
                summary = extract_field(fm, 'summary')
                print(f"FILE: {file}")
                print(f"TITLE: {title}")
                print(f"SUMMARY: {summary}")
                print("-" * 40)

if __name__ == '__main__':
    main()
