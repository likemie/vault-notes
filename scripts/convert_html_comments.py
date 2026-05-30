import os
import re

def convert_comments(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False

    # Regex for HTML comments %% some comment %%
    # We use non-greedy matching .*?
    new_content = re.sub(r'%%(.*?)%%', r'%%\1%%', content, flags=re.DOTALL)

    if new_content != content:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        except Exception as e:
            print(f"Error writing {filepath}: {e}")
            return False
    return False

def main():
    count = 0
    # Scan wiki and templater (and any other relevant dirs)
    directories = ['wiki', 'templater', 'scripts']
    for directory in directories:
        if not os.path.exists(directory):
            continue
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.md') or file.endswith('.py'):
                    filepath = os.path.join(root, file)
                    if convert_comments(filepath):
                        count += 1
                        print(f"Converted comments in: {filepath}")
    
    # Also check GEMINI.md in root
    if os.path.exists('GEMINI.md'):
        if convert_comments('GEMINI.md'):
            count += 1
            print("Converted comments in: GEMINI.md")
            
    print(f"Total files updated: {count}")

if __name__ == '__main__':
    main()
