import sys
import os
import glob
sys.path.append('src')
from markdown_converter import convert_markdown_to_html
from zoho_sender import send_zoho_request
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('ZOHO_WEBHOOK_URL')

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
            md_contents["name"] = os.path.basename(md_file) 
            md_contents["content"] = convert_markdown_to_html( file.read())
    return md_contents

def write_html_files(directory, content):
    for file_name, html_content in content.items():
        base_name = content['name'].split('.')[0]
        html_file_path = os.path.join(directory, f'{base_name}.html')
        with open(html_file_path, 'w', encoding='utf-8') as file:
            file.write(html_content)


if __name__ == '__main__':
    print('Hello, World!')
    content = read_all_md_file('test/')
    write_html_files('test/', content)
    # send_zoho_request(url, content)
    # testing the content
    for file_name, md_content in content.items():
        print(f'File: {file_name}')
        print(content)
        print('---')