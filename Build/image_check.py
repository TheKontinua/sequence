import os
import re

# Define the base directory relative to the location of the script in the Build folder
base_dir = os.path.join(os.path.dirname(__file__), '..', 'Chapters')

# Regular expression to match \includegraphics tags and extract the file path
include_graphics_regex = r'\\includegraphics(?:\[.*\])?\{(.+?)\}'

# Walk through the directory structure
for root, dirs, files in os.walk(base_dir):
    # Check if the current directory is an 'en_US' folder
    if os.path.basename(root) == 'en_US':
        # Collect all PNG files in the directory
        all_pngs = {file for file in files if file.endswith('.png')}
        
        # Set to store all PNGs referenced in .tex files within the same directory
        referenced_pngs = set()

        # Iterate through each .tex file in the current 'en_US' directory
        for file in files:
            if file.endswith('.tex'):
                # Construct the full file path
                tex_file_path = os.path.join(root, file)
                # Read the .tex file
                with open(tex_file_path, 'r') as tex_file:
                    tex_content = tex_file.read()
                    # Find all matches of \includegraphics
                    matches = re.findall(include_graphics_regex, tex_content)
                    for match in matches:
                        # Extract just the filename in case the path is included
                        referenced_png = os.path.basename(match)
                        referenced_pngs.add(referenced_png)

        # Find PNG files not mentioned in any .tex file in the same directory
        unreferenced_pngs = all_pngs - referenced_pngs

        if unreferenced_pngs:
            print(f"In {root}, the following PNGs are not referenced in any .tex file:")
            for png in unreferenced_pngs:
                print(png)
