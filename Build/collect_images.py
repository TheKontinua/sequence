import os
import shutil
import re

# Define the base directory relative to the location of the script in the Build folder
base_dir = os.path.join(os.path.dirname(__file__), '..', 'Chapters')
print(base_dir)

# Define the destination directory where all referenced PNGs will be collected
dest_dir = os.path.join(os.path.dirname(__file__), '..', 'Collected_PNGs')

# Path to the workbook_00.tex file which contains the list of chapters
workbook_tex_path = os.path.join(base_dir, 'book_00.txt')

# Create the destination directory if it doesn't exist
os.makedirs(dest_dir, exist_ok=True)

# Regular expression to match \includegraphics tags and extract the file path
include_graphics_regex = r'\\includegraphics(?:\[.*\])?\{(.+?)\}'

# Function to read chapter names from workbook_00.tex
def read_chapter_names(tex_path):
    with open(tex_path, 'r') as f:
        # Assuming each line in the file is a chapter name
        return [line.strip() for line in f if line.strip()]

# Read the list of chapter names from workbook_00.tex
chapter_names = read_chapter_names(workbook_tex_path)

# Iterate through the chapter names in the order they appear in workbook_00.tex
for chapter_number, chapter_name in enumerate(chapter_names, start=1):
    chapter_path = os.path.join(base_dir, chapter_name, 'en_US')
    if os.path.isdir(chapter_path):
        for file in os.listdir(chapter_path):
            if file.endswith('.tex'):
                tex_file_path = os.path.join(chapter_path, file)
                with open(tex_file_path, 'r') as tex_file:
                    tex_content = tex_file.read()
                    matches = re.findall(include_graphics_regex, tex_content)
                    for img_index, match in enumerate(matches, start=1):
                        img_filename = os.path.basename(match)
                        new_filename = f"{chapter_number:02d}-{chapter_name}-{img_index:02d} - {img_filename}"
                        img_file_path = os.path.join(chapter_path, match)
                        if os.path.exists(img_file_path):
                            dest_file_path = os.path.join(dest_dir, new_filename)
                            shutil.copy(img_file_path, dest_file_path)

print(f"All referenced images have been collected in: {dest_dir}")
