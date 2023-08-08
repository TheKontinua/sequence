import os
import shutil
import glob
import pathlib

# Delete the generated directories
dirs = ["Intermediate"]
dirs.extend(glob.glob("Resources-*"))
dirs.extend(glob.glob("Workbooks-*"))
print(f"Deleting {dirs}")
for dir in dirs:
    if os.path.exists(dir):
        shutil.rmtree(dir)

# Delete any old chapter drafts
files = glob.glob("../Chapters/*/*/draft.pdf")
for draft_file in files:
    os.remove(draft_file)

# Delete any pycache directories
for p in pathlib.Path('../Chapters').rglob('__pycache__'):
    shutil.rmtree(p)

print('Cleaned.')
    
