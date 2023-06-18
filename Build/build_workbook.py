import os
import sys
import shutil
import json

# Paths are from Intermediate
mod_dir = "../../Chapters"
vol_count = 36

def usage():
    print("Usage: python3 build_workbook.py <i>")
    print("   or  python3 build_workbook.py all")
    sys.exit(1)


def path_for_chapter_locale_list(chapter, locale_list):
    # Assumes mod has already been stripped of whitespace
    # FIXME: When we start localizing, this will need to be smarter
    return os.path.join(mod_dir, chapter, "en_US", "student.tex")


def build_book(book_id, config, draft):
    locale_list = config["Languages"]
    paper_size = config["Paper"]
    tool = config["LatexExecutable"]

    output_tex_path = "workbook-{}-{}.tex".format(book_id, locale_list[0])
    output_pdf_path = "workbook-{}-{}.pdf".format(book_id, locale_list[0])
    final_pdf_path = "../{}".format(output_pdf_path)
    if os.path.exists(final_pdf_path):
        os.remove(final_pdf_path)
    output_tex = open(output_tex_path, "w")

    # Write the header
    header_file = open("../Support/bookheader.tex", "r")
    header = header_file.read()
    header_file.close()
    output_tex.write(header)

    # Which modules go into the book?
    modlist_filename = "book_{}.txt".format(book)
    modlist_path = os.path.join(mod_dir, modlist_filename)
    if not os.path.exists(modlist_path):
        print(f"Chapter file {modlist_path} doesn't exist")
        return None

    modlist = open(modlist_path, "r")
    chapters = modlist.readlines()
    modlist.close()

    for chapter in chapters:
        trimmed_chapter = chapter.strip()
        if len(trimmed_chapter) > 0:
            # Look for the graphics in the module directory
            gpath_string =f"\\graphicspath{{{{../../Chapters/{trimmed_chapter}/{locale_list[0]}}}}}\n"
            output_tex.write(gpath_string)

            chapter_path = path_for_chapter_locale_list(trimmed_chapter, locale_list)
            include_string = "\\input{{{}}}\n".format(chapter_path)
            output_tex.write(include_string)

    # Write the footer
    footer_file = open("../Support/bookfooter.tex", "r")
    footer = footer_file.read()
    footer_file.close()
    output_tex.write(footer)
    output_tex.close()
    os.system(f"{tool} {output_tex_path}")

    if not draft:
        # If a pdf was made, run it again to get cross-references right
        if not draft and os.path.exists(output_pdf_path):
            os.system(f"{tool} {output_tex_path}")
            shutil.move(output_pdf_path, final_pdf_path)
        else:
            print(f"Build failed for {final_pdf_path}")
            return None

    return output_pdf_path


if not os.path.exists("Intermediate"):
    os.mkdir("Intermediate")

if not os.path.exists("user.cfg"):
    shutil.copyfile("Support/default.cfg", "user.cfg")

with open("user.cfg", "r") as config_fd:
    config = json.load(config_fd)

if len(sys.argv) < 2:
    usage()

arg1 = sys.argv[1]
if arg1 == "all":
    book_nums = [str(x).zfill(2) for x in range(1, vol_count + 1)]
else:
    book_nums = [arg1.zfill(2)]

os.chdir("Intermediate")

newfilenames = []
failednumbers = []
for book in book_nums:
    print(f"Building book {book}")
    newfile = build_book(book, config, False)
    if newfile is None:
        failednumbers.append(book)
    else:
        newfilenames.append(newfile)

if len(newfilenames) > 0:
    print("\n**** Created ****")
    for filename in newfilenames:
        print(filename)

if len(failednumbers) > 0:
    print(f"**** Failures: {failednumbers} *****")
