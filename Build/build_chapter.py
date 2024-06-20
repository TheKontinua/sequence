import os
import util
import json

chap_file = "student.tex"
chap_dir = os.getcwd()
workdir = "../../../Build/Intermediate" 
if not os.path.exists(workdir):
    os.mkdir(workdir)
os.chdir(workdir)

with open("../user.cfg", "r") as config_fd:
    config = json.load(config_fd)

print(f"Building {chap_file} (in {chap_dir})")
final_pdf_path = os.path.join(chap_dir, "student.pdf")
util.build_chapter(chap_file, chap_dir, config, final_pdf_path)
