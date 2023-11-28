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

# Open the file
filename = f"globallist.txt"
fout = open(filename, "w")

# Gather all metadatas    
book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]

# What languages are we trying to localize for?
lang_list = ["en_US"]

# Walk the books
for book in book_nums:
    print(f"Gathering titles for book {book}...")
    print(book, file=fout)
    (ids, dirs) = util.dir_list_for_book("../Chapters", book, config["Languages"])
    for id in ids:
        print(f"\t{id}", file=fout)
        for lang in lang_list:
            loc_path = f"../Chapters/{id}/{lang}"
            if os.path.exists(loc_path):
                title = util.title_for_dir(loc_path)
                print(f"\t\t{lang}:{title}", file=fout)

fout.close()
print(f"Complete: {filename}")