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

paragraphs = [p.strip() for p in old.split('\n\n') if p.strip()]

missing_paras = []
for p in paragraphs:
    if p.startswith('title:') or p.startswith('aliases:') or p.startswith('tags:') or p.startswith('summary:') or p.startswith('type:') or p.startswith('domain:') or p.startswith('related_'):
        continue
    # skip if it is just a frontmatter block or YAML
    if p.strip().startswith('---'):
        continue
    p_norm = normalize(p)
    if len(p_norm) < 15:
        continue
    # Let's search if the paragraph's normalized text is inside cur_normalized.
    # To handle small edits/additions within the paragraph, let's see if 80% of its sentences are in the current text
    sentences = re.split(r'[。！？.!?\n]', p)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
    if not sentences:
        continue
    
    found_count = 0
    for s in sentences:
        s_norm = normalize(s)
        if s_norm in cur_normalized:
            found_count += 1
            
    ratio = found_count / len(sentences)
    if ratio < 0.3: # less than 30% of sentences matched
        missing_paras.append((p, ratio))

print(f"Total paragraphs analyzed in old: {len(paragraphs)}")
print(f"Missing paragraphs count: {len(missing_paras)}")
print("\n--- MISSING PARAGRAPHS DETAIL ---")
for i, (p, ratio) in enumerate(missing_paras):
    print(f"--- Missing Paragraph {i+1} (Match Ratio: {ratio:.2f}, Length: {len(p)}) ---")
    print(p[:500] + ("..." if len(p) > 500 else ""))
    print()
