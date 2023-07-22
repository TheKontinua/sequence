import enum
import os
import sys
import json
import util
import shutil

vol_count = 36

if not os.path.exists("Resources"):
    os.makedirs("Resources")

if not os.path.exists("user.cfg"):
    shutil.copyfile("Support/default.cfg", "user.cfg")

with open("user.cfg", "r") as config_fd:
    config = json.load(config_fd)

filename = "Resources/chaplist.txt"
fout = open("Resources/chaplist.txt", "w")

# Gather all metadatas    
book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]

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