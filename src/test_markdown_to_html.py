import unittest

from markdown_to_html import(
    markdown_to_html_node,
    heading_to_html_node,
    paragraph_to_html_node,
    extract_title,
    )

class TestMarkdownToHTML(unittest.TestCase):
    def test_head_and_paragraph(self):
        markdown = """
        # This is a heading

        This is a paragraph
        """
        self.assertEqual("<div><h1>This is a heading</h1><p>This is a paragraph</p></div>", markdown_to_html_node(markdown).to_html())

    def test_block_quote(self):
        markdown = """
        My favorite Miss Manners quotes:

> Allowing an unimportant mistake to pass without comment is a wonderful social grace.
> Ideological differences are no excuse for rudeness.
        """
        html = "<div><p>My favorite Miss Manners quotes:</p><blockquote><p>Allowing an unimportant mistake to pass without comment is a wonderful social grace. Ideological differences are no excuse for rudeness.</p></blockquote></div>"
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(html, result)

    def test_block_quote_with_empty_line(self):
        self.maxDiff = None
        markdown = """
        My favorite Miss Manners quotes:

> Allowing an unimportant mistake to pass without comment is a wonderful social grace.
>
> Ideological differences are no excuse for rudeness.
        """
        html = "<div><p>My favorite Miss Manners quotes:</p><blockquote><p>Allowing an unimportant mistake to pass without comment is a wonderful social grace.</p><p>Ideological differences are no excuse for rudeness.</p></blockquote></div>"

        self.assertEqual(html, markdown_to_html_node(markdown).to_html())

    def test_ulist(self):
        markdown="""My favorite Miss Manners quotes:

* Allowing an unimportant mistake to pass without comment is a wonderful social grace.
* Ideological differences are no excuse for rudeness.
        """
        html = "<div><p>My favorite Miss Manners quotes:</p><ul><li>Allowing an unimportant mistake to pass without comment is a wonderful social grace.</li><li>Ideological differences are no excuse for rudeness.</li></ul></div>"
        self.assertEqual(html, markdown_to_html_node(markdown).to_html())

    def test_olist(self):
        markdown="""My favorite Miss Manners quotes:

* Allowing an unimportant mistake to pass without comment is a wonderful social grace.
* Ideological differences are no excuse for rudeness.
        """
        html = "<div><p>My favorite Miss Manners quotes:</p><ul><li>Allowing an unimportant mistake to pass without comment is a wonderful social grace.</li><li>Ideological differences are no excuse for rudeness.</li></ul></div>"
        self.assertEqual(html, markdown_to_html_node(markdown).to_html())

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_quote_with_multiple_empty_lines_at_start(self):
        md = """> 
> 
>
> This is a
> blockquote block

this is paragraph text"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote><p>This is a blockquote block</p></blockquote><p>this is paragraph text</p></div>"
        )

    def test_extract_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_extract_title_no_title(self):
        self.assertRaises(ValueError, extract_title, "This is a paragraph with no title.")

    def test_codeblock(self):
        md = """
```
This is a code block
```

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is a code block\n</code></pre><p>this is paragraph text</p></div>",
        )