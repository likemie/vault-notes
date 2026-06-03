import os
import glob

files_to_delete = [
    'wiki/concepts/technology-innovation/High-Quality Sci-Tech Supply.md',
    'wiki/concepts/technology-innovation/Principal Status of Enterprises in Innovation.md',
    'wiki/concepts/technology-innovation/Sci-Tech Achievement Transformation.md',
    'wiki/concepts/technology-innovation/Deep Integration of Sci-Tech and Industrial Innovation.md',
    'wiki/concepts/technology-innovation/Two Separate Skins Phenomenon.md'
]

for file_path in files_to_delete:
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted {file_path}")

