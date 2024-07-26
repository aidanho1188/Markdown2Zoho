import mistune
# from markdown2 import Markdown
from bs4 import BeautifulSoup
from mistune.plugins import task_lists


# TODO: Add classes to html tags
# Check README.md for guidance on what classes to add
def convert_markdown_to_html(markdown_content):
  markdowner = mistune.create_markdown(plugins=['mistune.plugins.task_lists.task_lists'])
  # markdowner = Markdown()
  html = markdowner(markdown_content)
  tag_class_dict = {
    'h1': '',
    'h2': '',
    'p': ''
  }
  html = add_classes_to_tags(html, tag_class_dict)
  return html

# Add classes to tags
# For best time complexity, we should add classes while converting markdown to html or get all tags and add classes in one go
def add_classes_to_tags(html_content, tag_class_dict):
    soup = BeautifulSoup(html_content, 'html.parser')
    for tag, class_name in tag_class_dict.items():
        for element in soup.find_all(tag):
            element['class'] = element.get('class', []) + [class_name]
    return str(soup)