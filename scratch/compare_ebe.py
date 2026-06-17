import re

with open('scratch/old_version.md') as f:
    old = f.read()
with open('wiki/concepts/educational-policy-reform/Evidence-Based Education.md') as f:
    cur = f.read()

def normalize(text):
    text = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', text)
    text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', text)
    text = re.sub(r'\s+', '', text)
    text = re.sub(r'[*#_`|>\-]', '', text)
    return text

cur_normalized = normalize(cur)

# Split old version into paragraphs, ignoring yaml frontmatter
sections = old.split('\n\n')
paragraphs = []
in_yaml = False
for s in sections:
    s = s.strip()
    if not s:
        continue
    if s == '---':
        in_yaml = not in_yaml
        continue
    if in_yaml:
        continue
    # Skip headings (lines starting with #)
    if s.startswith('#'):
        continue
    paragraphs.append(s)

missing = []
for p in paragraphs:
    p_norm = normalize(p)
    if len(p_norm) < 15:
        continue
    
    # Try splitting by sentence to see how many are present
    sentences = re.split(r'[。！？.!?\n]', p)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
    if not sentences:
        continue
    
    # Check if ANY sentence has a substantial match in the current file.
    # If not even a single sentence is matched, or the match ratio is 0.0, it is fully deleted.
    found_any = False
    for s in sentences:
        s_norm = normalize(s)
        # Check if this sentence's normalized text is contained in cur_normalized.
        # Let's check for fuzzy match: if a 20-character substring of s_norm is in cur_normalized
        if len(s_norm) > 20:
            for j in range(len(s_norm) - 20):
                if s_norm[j:j+20] in cur_normalized:
                    found_any = True
                    break
        else:
            if s_norm in cur_normalized:
                found_any = True
        if found_any:
            break
            
    if not found_any:
        missing.append(p)

with open('scratch/truly_deleted_paragraphs.txt', 'w') as f:
    f.write(f"Total paragraphs analyzed: {len(paragraphs)}\n")
    f.write(f"Truly deleted paragraphs count: {len(missing)}\n\n")
    for i, p in enumerate(missing):
        f.write(f"=== Paragraph {i+1} (Length: {len(p)}) ===\n")
        f.write(p)
        f.write("\n\n")

print(f"Analysis complete. Found {len(missing)} truly deleted paragraphs. Written to scratch/truly_deleted_paragraphs.txt")
