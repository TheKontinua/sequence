import os
import datetime
import json
import util
import shutil

# How many volumes are there?
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


# Have the links been lookedup?
link_file = f"{resources_dir}/Links.json"
if not os.path.exists(link_file):
    print(f"Run url_check.py to create {link_file}")
    exit()

with open(link_file, 'r') as f:
    links = json.load(f)

# Gather all metadatas
book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]
all_topics = {}
for book in book_nums:
    print(f"Indexing book {book}...")
    (chapter_datas, topics) = util.gather_data("../Chapters", book, config)
    all_topics.update(topics)

    toc_dict = util.chapter_toc(book)

    for i, chapter_meta in enumerate(chapter_datas):

        chapter_str = str(i + 1)
        chapter_page = toc_dict[chapter_str]
        # Will recreate covers with url title
        if "covers" in chapter_meta:
            del chapter_meta["covers"]
        chapter_meta["covers"] = []
        chapter_meta["start_page"] = chapter_page
        # I don't think we need files in reader app
        if "files" in chapter_meta:
            del chapter_meta["files"]
        del chapter_meta["book"]

    # Walk through the topics, attaching to correct chapter
    for tid, t in topics.items():
        chap_idx = t["chap_num"] - 1
        topic_dict =  {"id":tid, "desc":t["desc"]}

        # Get titles for urls
        for key in ["videos", "references"]:
            if key in t:
                url_list = t[key]
                out_list = []
                for url in url_list:
                    if url in links:
                        title = links[url]["title"]
                    else:
                        title = "???"
                    out_list.append({"link":url, "title":title})
                    topic_dict[key] = out_list

        # print(f"Appending {topic_dict}")
        chapter_datas[chap_idx]["covers"].append(topic_dict)

    outpath = f"{resources_dir}/workbook-{book}.json"
    with open(outpath, 'w') as f:
        json.dump(chapter_datas, f, indent=2)
    print(f"Wrote {outpath}")

outpath = f"{resources_dir}/topic_index.json"
# Don't need this in the index
for topic_id in all_topics:
    if "videos" in all_topics[topic_id]:
        del all_topics[topic_id]["videos"]
    if "references" in all_topics[topic_id]:
        del all_topics[topic_id]["references"]

with open(outpath, 'w') as f:
    json.dump(all_topics, f, indent=2)
    print(f"Wrote {outpath}")
