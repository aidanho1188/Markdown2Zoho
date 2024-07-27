import re
import mistune
from bs4 import BeautifulSoup


# TODO: Add classes to html tags
# Check README.md for guidance on what classes to add
def convert_markdown_to_html(markdown_content):
  renderer = CustomRender()
  markdowner = mistune.create_markdown(renderer=renderer, plugins=[
    'strikethrough', 'footnotes', 'table', 'url', 'task_lists',
  ])
  # markdowner = Markdown()
  html = markdowner(markdown_content)
  tag_class_dict = {
    'a': 'zn-link editor-note-link',
    'table': 'ze_tableView',
    'blockquote': 'zn-qoute'
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

    # Add classes to ul and li tags. Remove input tags from beautiful soup object
    for ul in soup.find_all('ul'):
      if any('task-list-item' in li.get('class', []) for li in ul.find_all('li')):
        ul['class'] = ul.get('class', []) + ['checklist']
        for li in ul.find_all('li'):
          li['class'] = ['checkbox']
          input_tag = li.find('input', class_='task-list-item-checkbox')
          input_tag.decompose()


    return str(soup)

class CustomRender(mistune.HTMLRenderer):
    def text(self, text):
        # Detect ==text== and replace with a <span>
        text = re.sub(r'==(.+?)==', r'<span class="highlight" style="background-color:#FFD921">\1</span>', text)
        return text
    
    def image(self, alt, url, title=None):
        # Add a div and class to the image tag
        return f'<div class="imageWrapper"><img class="notecardImageClass" src="{url}" alt="{alt}"></div>'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)