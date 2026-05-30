import os

renames = {
    'Capability Approach in Education': 'Capability Approach',
    'Side Effects in Education': 'Side Effects',
    'Competitiveness in Higher Education': 'Competitiveness',
    'Cultural Barrier in Higher Education': 'Cultural Barrier',
    'Space-Making in Higher Education': 'Space-Making',
    'Transnational Research Collaboration in Higher Education': 'Transnational Research Collaboration',
    'Strategic Partnership in University-Industry Collaboration': 'Strategic Partnership',
    'Master Agreement in University-Industry Collaboration': 'Master Agreement',
    'Alumni Engagement in University-Industry Collaboration': 'Alumni Engagement',
    'Trade Mission in University-Industry Engagement': 'Trade Mission',
    'Product-Specific Research in University-Industry Consortia': 'Product-Specific Research',
    'Neo-Taylorism in Educational Administration': 'Neo-Taylorism'
}

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return False
        
    new_content = content
    for old_name, new_name in renames.items():
        # Replace title in frontmatter
        new_content = new_content.replace(f'title: {old_name}', f'title: {new_name}')
        # Replace wikilinks
        new_content = new_content.replace(f'[[{old_name}]]', f'[[{new_name}]]')
        new_content = new_content.replace(f'[[{old_name}|', f'[[{new_name}|')
        
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    count = 0
    directories = ['wiki', 'books', 'sources']
    for directory in directories:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.md') or file.endswith('.json'):
                    filepath = os.path.join(root, file)
                    if replace_in_file(filepath):
                        count += 1
                        print(f"Updated {filepath}")
    print(f"Total files updated: {count}")

if __name__ == '__main__':
    main()
