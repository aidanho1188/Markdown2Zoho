import sys
import os
import glob
sys.path.append('src')
from markdown_converter import convert_markdown_to_html
from zoho_sender import send_zoho_request
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('ZOHO_WEBHOOK_URL')

import os

def read_all_md_file(directory):
    md_contents = []
    for md_file in os.listdir(directory):
        if md_file.endswith('.md'):
            with open(os.path.join(directory, md_file), 'r', encoding='utf-8') as file:
                file_content = {
                    "name": os.path.basename(md_file),
                    "content": convert_markdown_to_html(file.read())
                }
                md_contents.append(file_content)
    return md_contents

def write_html_files(directory, contents):
    for content in contents:
        base_name = content['name']
        html_file_path = os.path.join(directory, f'{base_name}.html')
        with open(html_file_path, 'w', encoding='utf-8') as file:
            file.write(content['content'])


if __name__ == '__main__':
    print('Hello, World!')
    contents = read_all_md_file('test/')
    write_html_files('test/', contents)
    for content in contents:
        send_zoho_request(url, content)
    # testing the content
    for content in contents:
        print(f'File: {content["name"]}')
        print(content["content"])
        print('---')