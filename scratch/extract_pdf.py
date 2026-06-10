import fitz  # PyMuPDF
import os

pdf_path = "/Users/shaoyangwu/Documents/MyNotes/sources/SpronkenSmith_2024_AEHE.pdf"
output_dir = "/Users/shaoyangwu/Documents/MyNotes/scratch"
output_path = os.path.join(output_dir, "SpronkenSmith_2024_AEHE_text.txt")

os.makedirs(output_dir, exist_ok=True)

print(f"Reading PDF from {pdf_path}...")
doc = fitz.open(pdf_path)
print(f"Total pages: {len(doc)}")

with open(output_path, "w", encoding="utf-8") as f:
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        f.write(f"--- PAGE {page_num + 1} ---\n")
        f.write(text)
        f.write("\n")

print(f"Text successfully extracted to {output_path}")
