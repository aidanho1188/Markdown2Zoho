import sys
import os
import glob
sys.path.append('src')
from markdown_converter import convert_markdown_to_html

# TODO: extract this function to a new module
# get all the files in the directory
# read the contents of the files
# convert the contents of the files to HTML
# write the HTML to a new file for now
def read_all_md_file(directory):
    md_files = glob.glob(os.path.join(directory, '*.md'))
    md_contents = {} # temperary store the contents of the md files

    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as file:
            # convert the markdown to html and store it in the dictionary
            # this saves time but function name is not clear
            md_contents[os.path.basename(md_file)] = convert_markdown_to_html( file.read() )
    return md_contents



if __name__ == '__main__':
    print('Hello, World!')
    content = read_all_md_file('test/')
    
    # testing the content
    for file_name, md_content in content.items():
        print(f'File: {file_name}')
        print(content)
        print('---')