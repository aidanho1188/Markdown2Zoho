# Markdown2Zoho
Markdown to Zoho HTML converter to migrate from Obsidian to Zoho Notebook

## Goals
- Select a Markdown file in a directory 
- Convert the Markdown file to Zoho HTML
- Send the HTML to the to Zoho API


## Usage
```bash 
python main.py <path>
```

## Requirements

To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```

## Zoho HTML
The Zoho HTML is a subset of HTML that is supported by Zoho Notebook. The following is a list of supported HTML tags:

<details>
<summary>Code tag</summary>

```html
<code>
  <pre>
    code...
  </pre>
</code>
```
</details>

<details>
<summary>Bold tag</summary>

```html
<b>bold text</b>
```
</details>

<details>
<summary>Italic tag</summary>

```html
<i>italic text</i>
```
</details>

<details>
<summary>Underline tag</summary>

```html
<u>underline text</u>
```
</details>

<details>
<summary>Strikethrough tag</summary>

```html
<strike>strikethrough text</strike>
```
</details>

<details>
<summary>Highlight tag</summary>

```html
<span class="highlight" style="background-color:#61D1FF">
  highlight text
</span>
```
</details>

<details>
<summary>Text color tag</summary>
Obsidian does not support text color, so this is a custom tag.
```html
<span class="colour" style="color:#61D1FF">
  text color
</span>
```
</details>

<details>
<summary>Font size tag</summary>
Obsidian does not support font size, so this is a custom tag.
```html
<span class="size" style="font-size: 32px;line-height: 32px">
  Summary
</span>
```
</details>

<details>
<summary>Unordered list tag</summary>

```html
<ul>
  <li>item 1</li>
  <li>item 2</li>
</ul>
```
</details>

<details>
<summary>Ordered list tag</summary>

```html
<ol>
  <li>item 1</li>
  <li>item 2</li>
</ol>
```
</details>

<details>
<summary>Checklist tag</summary>

```html
<ul class="checklist">
  <li class="checkbox">
    item 1
  </li>
  <li class="checkbox">
    item 2
  </li>S
</ul>
```
</details>

<details>
<summary>Link tag</summary>

```html
<!-- Need more research for all of the defaults attributes -->
<a href="https://www.zoho.com/notebook/" class="zn-link editor-note-link">
  Zoho Notebook
</a>
```
</details>

<details>
<summary>Image tag</summary>

```html
<!-- Need more research! -->
<!-- max width is editable-->
<div class="imgWrapperDiv">
  <img class="notecardImageClass" style="max-width: 100%" src="data:image/png;base64,...">
</div>
```
</details>

<details>
<summary>Horizontal line tag</summary>

```html
<hr>
```
</details>

<details>
<summary>Table tag</summary>

```html
<!-- Need research for default attributes -->
<table class="ze_tableView" cellpadding="4" cellspacing="2" border="1" style="border-collapse: collapse; overflow-x: auto; width: max-content; margin: 16px 0px;">
  <tbody>
    <tr>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
```
</details>

<details>
<summary>Blockquote tag</summary>

```html
<blockquote class="zn-quote">
  <div>quote</div>
</blockquote>
```
</details>