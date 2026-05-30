import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---'):
        return False

    parts = content.split('---', 2)
    if len(parts) < 3:
        return False

    frontmatter = parts[1]

    # Extract citation
    citation_match = re.search(r'^citation:\s*(.*?)$', frontmatter, re.MULTILINE)
    if not citation_match:
        return False

    citation = citation_match.group(1).strip()
    if (citation.startswith("'") and citation.endswith("'")) or (citation.startswith('"') and citation.endswith('"')):
        citation = citation[1:-1]

    # Extract author from citation
    author_match = re.match(r"^(.*?)\s*(?:\(Eds?\.\)\s*)?\(\d{4}[a-z]?\)", citation)
    
    if author_match:
        author = author_match.group(1).strip().rstrip('.,')
    else:
        fallback_match = re.match(r"^(.*?)\s*\(", citation)
        if fallback_match:
            author = fallback_match.group(1).strip().rstrip('.,')
        else:
            author = citation  # very rare case, but fallback to citation

    author = author.replace('"', '\\"')

    # Check if author exists
    has_author = re.search(r'^author:\s*(.*?)$', frontmatter, re.MULTILINE)
    new_frontmatter = frontmatter

    if has_author:
        existing_author = has_author.group(1).strip()
        # If empty ('' or "" or nothing)
        if not existing_author or existing_author in ("''", '""'):
            new_frontmatter = re.sub(r'^author:\s*.*?$', f'author: "{author}"', frontmatter, count=1, flags=re.MULTILINE)
        else:
            return False # already has a valid author
    else:
        # Insert author after title
        new_frontmatter = re.sub(r'^(title:.*?)$', rf'\1\nauthor: "{author}"', frontmatter, count=1, flags=re.MULTILINE)

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
                if process_file(filepath):
                    count += 1
                    print(f"Updated {filepath}")
    print(f"Total updated: {count}")

if __name__ == '__main__':
    main()
