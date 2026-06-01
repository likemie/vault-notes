import sys
import re
import os

def fix_author_name(name):
    name = name.strip().strip('"').strip("'").strip(",").strip(";")
    # Remove (Eds.) or (Ed.)
    name = re.sub(r"\s*\(Eds?\.?\)", "", name)
    # Ensure initials have periods (e.g., "S" -> "S.")
    # Match a single capital letter at the end or followed by a space
    name = re.sub(r"(^|\s)([A-Z])(?=\s|$)", r"\1\2.", name)
    # Clean up any double periods
    name = name.replace("..", ".")
    return name.strip()

def split_authors(authors_text):
    # Remove surrounding quotes
    authors_text = authors_text.strip().strip('"').strip("'")
    
    # Common separators
    # Use a unique separator to avoid breaking "Last, F."
    # We replace " & ", " and ", " with ", ", & ", ", and "
    temp = re.sub(r"\s*(?:,|;)?\s*(?:&|and|with)\s+", "|SEP|", authors_text)
    
    # Split by the unique separator
    parts = temp.split("|SEP|")
    
    final_authors = []
    for p in parts:
        # Check if this part contains multiple authors separated by commas
        # Example: "Cowen, N., Cartwright, N., Virk, B."
        # We split by ", " only if followed by another name (Word or Initial)
        # and NOT just an initial for the current name.
        
        # A name usually has "Last, F." or "Last, F. I."
        # If we see "Word, Initial, Word, Initial", we should split between Initial and Word.
        
        # Split by comma followed by space and a Word (at least 2 letters or a capital letter that is not a single initial followed by period)
        # Actually, let's look for ", [A-Z]" where the [A-Z] is the start of a new Last Name.
        # This is tricky. Let's try splitting by ", " and then merging if it looks like "Last, F."
        
        sub_parts = re.split(r",\s+", p)
        i = 0
        while i < len(sub_parts):
            current = sub_parts[i].strip()
            if not current:
                i += 1
                continue
            
            # If current looks like a Last Name (no period, >1 char) 
            # and next looks like initials (1-2 chars with period)
            # or if next exists and current doesn't have a period, they might belong together.
            
            if i + 1 < len(sub_parts):
                next_part = sub_parts[i+1].strip()
                # If next_part is just initials like "J." or "J. B."
                if re.match(r"^[A-Z]\.?(\s+[A-Z]\.?)*$", next_part):
                    final_authors.append(fix_author_name(current + ", " + next_part))
                    i += 2
                else:
                    # Current might be a full name already or "Last, F." was not caught.
                    final_authors.append(fix_author_name(current))
                    i += 1
            else:
                final_authors.append(fix_author_name(current))
                i += 1
    
    return [a for a in final_authors if a]

def process_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    in_authors = False
    authors_content = []
    processed = False

    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("authors:"):
            # Check if it's already a list or a single string in a list
            # The user said they look like:
            # authors:
            #   - "Name1, & Name2"
            
            new_lines.append(line)
            i += 1
            # Look for the list item
            if i < len(lines) and lines[i].strip().startswith("-"):
                authors_text = lines[i].strip()[1:].strip()
                # Split it
                split_list = split_authors(authors_text)
                for author in split_list:
                    new_lines.append(f"  - \"{author}\"\n")
                i += 1
                processed = True
            else:
                # Maybe authors: "Name1 & Name2" (not a list yet)
                # Not expected based on examples, but let's handle it
                match = re.match(r"authors:\s*(.*)", line)
                if match and match.group(1).strip():
                    authors_text = match.group(1).strip()
                    split_list = split_authors(authors_text)
                    # Replace the "authors: ..." line with "authors:\n"
                    new_lines[-1] = "authors:\n"
                    for author in split_list:
                        new_lines.append(f"  - \"{author}\"\n")
                    processed = True
        else:
            new_lines.append(line)
            i += 1

    if processed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Processed: {file_path}")
    else:
        print(f"No authors field found or already processed: {file_path}")

if __name__ == "__main__":
    with open('files_to_fix.txt', 'r') as f:
        files = [line.strip() for line in f if line.strip()]
    
    for f in files:
        process_file(f)
