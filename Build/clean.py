import os
import shutil
import glob

build_dir = "."

files_in_dir = os.listdir(build_dir)
filtered_files = [file for file in files_in_dir if file.endswith(".pdf") or file.endswith(".tgz") or file.endswith("html")]

for file in filtered_files:
    full_path = os.path.join(build_dir, file)
    os.remove(full_path)

intermediate_dir = "./Intermediate"
if os.path.exists(intermediate_dir):
    shutil.rmtree(intermediate_dir)

files = glob.glob("../Chapters/*/*/draft.pdf")
for draft_file in files:
    os.remove(draft_file)

print('Cleaned.')
    
