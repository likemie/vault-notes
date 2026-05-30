import os

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False
        
    new_content = content.replace('郑_2023_上海三联书店', 'Zheng_2023_ShanghaiSanlian')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    count = 0
    # Also include the scripts directory just in case, but definitely wiki and books
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
