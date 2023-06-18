import os
import re
import json

title_pattern = re.compile("chapter\{([^\}]+)\}")

def dir_list_for_book(mod_dir, book_str, langlist):
    # FIXME: should search from fav to least fave
    locale_str = langlist[0]
    modlist_filename = f"book_{book_str}.txt"
    modlist_path = os.path.join(mod_dir, modlist_filename)
    if not os.path.exists(modlist_path):
        print(f"Error: Chapter file {modlist_path} doesn't exist")
        return []
    modlist = open(modlist_path, "r")
    chapters = modlist.readlines()
    modlist.close()

    result_paths = []
    result_ids = []
    for chapter in chapters:
        trimmed_chapter = chapter.strip()
        if len(trimmed_chapter) > 0:
            result_ids.append(trimmed_chapter)
            fullpath = os.path.join(mod_dir,trimmed_chapter,locale_str)
            result_paths.append(fullpath)
    return (result_ids, result_paths)

def title_for_dir(dir):
    fullpath = os.path.join(dir, "student.tex")
    for i, line in enumerate(open(fullpath)):
        for match in re.finditer(title_pattern, line):
            return match.group(1)
        
def metadata_for_dir(dir):
    rpath = os.path.join(dir, "digital_resources.json")
    if not os.path.exists(rpath):
        print(f"Error: Resources file file {rpath} doesn't exist")
        result = {}
    else:
        with open(rpath, 'r') as f:
            data = f.read().strip()
        if len(data) < 2:
            result = {} 
        else:
            result = json.loads(data)
    title = title_for_dir(dir)
    result["title"] = title
    return result

def gather_data(mod_dir, book_str, config):
    (ids, dirs) = dir_list_for_book(mod_dir, book_str, config["Languages"])
    metadatas = []
    topics = {}
    for (i, dir) in enumerate(dirs):
        md = metadata_for_dir(dir)
        # Get the title from the tex file
        title = title_for_dir(dir)

        # Fill in some useful info
        md["book"] = book_str
        md["id"] = ids[i]
        md["title"] = title
        md["chap_num"] = i + 1

        # Make URLs for the files
        if "files" in md:
            filelist = md["files"]
            for j in range(len(filelist)):
                filename = filelist[j]["path"]
                filelist[j]["link"] = f"https://raw.githubusercontent.com/TheKontinua/sequence/master/Chapters/{ids[i]}/en_US/{filename}"
        # Add it to the array 
        metadatas.append(md)

        # Also put the data in the topics dictionary
        if "covers" in md:
            for c in md["covers"]:
                cd = c.copy()
                cd["book"] = book_str
                cd["chap_title"] = title
                cd["chap_num"] = i + 1
                cd["chap_id"] = ids[i] 
                topics[cd["id"]] = cd

    return (metadatas, topics)        