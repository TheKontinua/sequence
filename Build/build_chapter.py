import os
import sys
import shutil
import json

def usage():
    print('Usage: python3 ../../Build/test_chapter.py <texfile>')
    sys.exit(1)

def build_chapter(chapter_file, chap_dir, config):
    locale_list = config['Languages']
    paper_size = config['Paper']
    tool = config['LatexExecutable']

    output_tex_path = 'draft.tex'
    output_pdf_path = 'draft.pdf'
    final_pdf_path = os.path.join(chap_dir,'draft.pdf') 
    if os.path.exists(output_pdf_path):
        os.remove(output_pdf_path)
    output_tex = open(output_tex_path, 'w')

    # Write the header
    header_file = open('../Support/minibookheader.tex', 'r')
    header = header_file.read()
    header_file.close()
    output_tex.write(header)

    gpath_string = '\\graphicspath{{{{{}/}}}}\n'.format(chap_dir)
    output_tex.write(gpath_string)

    # Include file
    full_path = os.path.join(chap_dir, chapter_file)
    include_string = '\\input{{{}}}\n'.format(full_path)
    output_tex.write(include_string)

    # Write the footer
    footer_file = open('../Support/bookfooter.tex', 'r')
    footer = footer_file.read()
    footer_file.close()
    output_tex.write(footer)
    output_tex.close()
    os.system(f'{tool} {output_tex_path}')
    if os.path.exists(output_pdf_path):
        shutil.move(output_pdf_path, final_pdf_path)
        print(f"{final_pdf_path} built.")
    else:
        print(f"Build of {final_pdf_path} Failed")

    

chap_file = 'student.tex'
chap_dir = os.getcwd()
os.chdir('../../../Build/Intermediate')

with open('../user.cfg','r') as config_fd:
    config = json.load(config_fd)

print(f"Building {chap_file} (in {chap_dir})")
build_chapter(chap_file, chap_dir, config)
                        
