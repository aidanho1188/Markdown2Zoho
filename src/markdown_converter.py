from markdown2 import Markdown

def convert_markdown_to_html(markdown_content):
  markdowner = Markdown()
  html = markdowner.convert(markdown_content)
  return html

