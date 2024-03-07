import os
import re
import csv

# Define the base directory relative to the location of the script in the Build folder
base_dir = os.path.join(os.path.dirname(__file__), '..', 'Chapters')

# Path to the book_00.txt file which contains the list of chapters
book_txt_path = os.path.join(base_dir, 'book_00.txt')

# CSV file to output the results
csv_file_path = os.path.join(os.path.dirname(__file__), 'PNG_Usage_Status.csv')

# Regular expression to match \includegraphics tags and extract the file path
include_graphics_regex = r'\\includegraphics(?:\[.*\])?\{(.+?)\}'

# Function to read chapter names from book_00.txt
def read_chapter_names(txt_path):
    with open(txt_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

# Read the list of chapter names from book_00.txt
chapter_names = read_chapter_names(book_txt_path)

# Prepare to write to the CSV file
with open(csv_file_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write the header row
    csv_writer.writerow(['#-chapter', 'filename', 'status'])

    # Iterate through the chapter names in the order they appear in book_00.txt
    for chapter_number, chapter_name in enumerate(chapter_names, start=1):
        chapter_path = os.path.join(base_dir, chapter_name, 'en_US')
        if os.path.isdir(chapter_path):
            all_pngs = {file: 0 for file in os.listdir(chapter_path) if file.endswith('.png')}  # Initialize all as not included (0)

            for file in os.listdir(chapter_path):
                if file.endswith('.tex'):
                    tex_file_path = os.path.join(chapter_path, file)
                    with open(tex_file_path, 'r') as tex_file:
                        tex_content = tex_file.read()
                        matches = re.findall(include_graphics_regex, tex_content)
                        for match in matches:
                            referenced_png = os.path.basename(match)
                            if referenced_png in all_pngs:
                                all_pngs[referenced_png] = 1  # Mark as included (1)

            # Write each PNG's status to the CSV
            for filename, status in all_pngs.items():
                csv_writer.writerow([f"{chapter_number}-{chapter_name}", filename, status])

print(f"PNG usage status has been written to: {csv_file_path}")
