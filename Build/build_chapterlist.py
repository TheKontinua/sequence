import enum
import os
import sys
import json
import util
import shutil

vol_count = 36
# Does the user not have a config file?
if not os.path.exists("user.cfg"):
    # Give them the default
    shutil.copyfile("Support/default.cfg", "user.cfg")

# Read in the config 
with open("user.cfg", "r") as config_fd:
    config = json.load(config_fd)

# Name the directory after the user's favorite locale
main_locale = config["Languages"][0]
resources_dir = f"Resources-{main_locale}"

# Make the directory if necessary
if not os.path.exists(resources_dir):
    os.makedirs(resources_dir)

# Open the file
filename = f"{resources_dir}/chaplist.txt"
fout = open(filename, "w")

# Gather all metadatas    
book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]

# Walk the books
for book in book_nums:
    print(f"Gathering titles for book {book}...")
    print(book, file=fout)
    (ids, dirs) = util.dir_list_for_book("../Chapters", book, config["Languages"])
    for (i, dir) in enumerate(dirs):
        # Get the title from the tex file
        title = util.title_for_dir(dir)
        print(f"\t{title}", file=fout)
fout.close()
print(f"Complete: {filename}")