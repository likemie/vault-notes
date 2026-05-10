#!/usr/bin/env python3
"""Update frontmatter of wiki entries to match new templates.
Adds aliases: [] and missing related_* fields based on entry type."""

import os
import sys

BASE = "/Users/shaoyangwu/Documents/MyNotes/wiki"

# Expected related_* fields by entry type
EXPECTED_FIELDS = {
    "concept": ["aliases", "related_concepts", "related_theories", "related_methods",
                "related_persons", "related_facts", "related_arguments"],
    "theory": ["aliases", "related_concepts", "related_theories", "related_methods",
               "related_persons", "related_facts", "related_arguments"],
    "person": ["aliases", "related_concepts", "related_theories", "related_methods",
               "related_persons", "related_arguments"],
    "argument": ["aliases", "related_concepts", "related_theories", "related_methods",
                 "related_persons", "related_facts", "related_arguments"],
    "fact": ["aliases", "related_concepts", "related_theories", "related_methods",
             "related_persons", "related_facts", "related_arguments"],
    "method": ["aliases", "related_concepts", "related_theories", "related_methods",
               "related_persons", "related_arguments"],
}

# Order of fields in frontmatter (top to bottom)
FIELD_ORDER = [
    "title", "aliases", "type", "subtype", "citation", "tags",
    "related_concepts", "related_theories", "related_methods",
    "related_persons", "related_facts", "related_arguments",
    "sources", "part_of", "confidence", "status", "created", "updated"
]


def parse_frontmatter(lines):
    """Extract frontmatter lines between first two --- markers."""
    if not lines or lines[0].strip() != "---":
        return None, lines

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break

    if end_idx is None:
        return None, lines

    fm_lines = lines[1:end_idx]
    body_lines = lines[end_idx+1:]
    return fm_lines, body_lines


def get_field_order(field_name):
    """Return sort key for field ordering."""
    try:
        return FIELD_ORDER.index(field_name)
    except ValueError:
        return 999


def update_frontmatter(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    lines = content.split("\n")
    fm_lines, body_lines = parse_frontmatter(lines)

    if fm_lines is None:
        print(f"  SKIP: no frontmatter found")
        return False

    # Parse existing fields
    existing_fields = {}
    field_positions = {}  # field_name -> line index in fm_lines
    for i, line in enumerate(fm_lines):
        if ":" in line:
            key = line.split(":")[0].strip()
            existing_fields[key] = line
            field_positions[key] = i

    # Determine type
    entry_type = None
    if "type" in existing_fields:
        type_line = existing_fields["type"]
        entry_type = type_line.split(":", 1)[1].strip()

    if not entry_type:
        print(f"  SKIP: no type field")
        return False

    # For fact entries, check subtype
    if entry_type == "fact":
        pass  # same fields regardless of policy/event

    expected = EXPECTED_FIELDS.get(entry_type, [])
    if not expected:
        print(f"  SKIP: unknown type '{entry_type}'")
        return False

    modified = False

    # Check for missing aliases
    if "aliases" in expected and "aliases" not in existing_fields:
        # Insert after title line
        title_idx = field_positions.get("title", 0)
        fm_lines.insert(title_idx + 1, "aliases: []")
        # Update field_positions for shifted lines
        for key in field_positions:
            if field_positions[key] > title_idx:
                field_positions[key] += 1
        field_positions["aliases"] = title_idx + 1
        existing_fields["aliases"] = "aliases: []"
        modified = True
        print(f"  + aliases")

    # Check for missing related_* fields
    related_fields = [f for f in expected if f.startswith("related_")]
    # Find the position to insert (after the last existing related_* field or before sources/confidence)
    last_related_pos = -1
    for key in field_positions:
        if key.startswith("related_"):
            last_related_pos = max(last_related_pos, field_positions[key])
        elif key == "related_facts" or key == "related_arguments" or key == "related_methods":
            last_related_pos = max(last_related_pos, field_positions[key])

    # If no related_* fields exist, find where to put them (after tags or after type-dependent field)
    if last_related_pos < 0:
        # Find position after tags (or after citation for argument, or after title for others)
        if "tags" in field_positions:
            last_related_pos = field_positions["tags"]
        elif "citation" in field_positions:
            last_related_pos = field_positions["citation"]
        elif "subtype" in field_positions:
            last_related_pos = field_positions["subtype"]
        else:
            last_related_pos = field_positions.get("type", 0)

    # Add missing related_* fields in order
    missing_related = []
    for field in related_fields:
        if field not in existing_fields:
            missing_related.append(field)

    if missing_related:
        # Sort missing fields by FIELD_ORDER
        missing_related.sort(key=get_field_order)
        # Insert after last_related_pos
        insert_pos = last_related_pos + 1
        for field in missing_related:
            fm_lines.insert(insert_pos, f"{field}: []")
            insert_pos += 1
            modified = True
            print(f"  + {field}")

    if modified:
        # Reconstruct file
        new_content = "---\n" + "\n".join(fm_lines) + "\n---\n" + "\n".join(body_lines)
        # Make sure body starts on new line
        if not new_content.endswith("\n"):
            new_content += "\n"
        with open(filepath, "w") as f:
            f.write(new_content)

    return modified


def main():
    files = sys.argv[1:]
    if not files:
        print("Usage: python3 _update_frontmatter.py <file1> <file2> ...")
        sys.exit(1)

    updated = 0
    skipped = 0
    for filepath in files:
        fname = os.path.basename(filepath)
        print(f"{fname}:")
        try:
            if update_frontmatter(filepath):
                updated += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"  ERROR: {e}")
            skipped += 1

    print(f"\nDone. Updated: {updated}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
