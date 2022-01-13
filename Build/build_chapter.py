import os
import sys
import shutil

def usage():
    print('Usage: python3 ../../Build/test_chapter.py <texfile>')
    sys.exit(1)

def build_chapter(chapter_file, chap_dir, paper_size):
    output_tex_path = 'chapter.tex'
    output_pdf_path = 'chapter.pdf'
    final_pdf_path = os.path.join(chap_dir,'chapter.pdf') 
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
    os.system('lualatex {}'.format(output_tex_path))
    if os.path.exists(output_pdf_path):
        shutil.move(output_pdf_path, final_pdf_path)
        print(f"{final_pdf_path} built.")
    else:
        print(f"Build of {final_pdf_path} Failed")


if len(sys.argv) < 2:
    usage()
chap_file = sys.argv[1]

chap_dir = os.getcwd()
os.chdir('../../Build/Intermediate')
print(f"Building {chap_file} (in {chap_dir})")
build_chapter(chap_file, chap_dir, 'Letter')
                        
