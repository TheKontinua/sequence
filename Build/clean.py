import os
import shutil

build_dir = "."

files_in_dir = os.listdir(build_dir)
filtered_files = [file for file in files_in_dir if file.endswith(".pdf") or file.endswith(".tgz")]

for file in filtered_files:
    full_path = os.path.join(build_dir, file)
    os.remove(full_path)

intermediate_dir = "./Intermediate"
shutil.rmtree(intermediate_dir)
    
print('Cleaned.')
    
