import unittest

from markdown_to_html import(
    markdown_to_html,
    heading_to_html_node,
    paragraph_to_html_node,
    )

class TestMarkdownToHTML(unittest.TestCase):
    def test_head_and_paragraph(self):
        markdown = """
        # This is a heading

        This is a paragraph
        """
        self.assertEqual("<h1>This is a heading</h1><p>This is a paragraph</p>", markdown_to_html(markdown))

    def test_block_quote(self):
        markdown = """
        My favorite Miss Manners quotes:

> Allowing an unimportant mistake to pass without comment is a wonderful social grace.
> Ideological differences are no excuse for rudeness.
        """
        html = "<p>My favorite Miss Manners quotes:</p><blockquote><p>Allowing an unimportant mistake to pass without comment is a wonderful social grace.Ideological differences are no excuse for rudeness.</p></blockquote>"
        result = markdown_to_html(markdown)
        print(result)
        self.assertEqual(html, result)

    def test_block_quote_with_empty_line(self):
        markdown = """
        My favorite Miss Manners quotes:

> Allowing an unimportant mistake to pass without comment is a wonderful social grace.
>
> Ideological differences are no excuse for rudeness.
        """
        html = "<p>My favorite Miss Manners quotes:</p><blockquote><p>Allowing an unimportant mistake to pass without comment is a wonderful social grace.</p><p>Ideological differences are no excuse for rudeness.</p></blockquote>"

        self.assertEqual(html, markdown_to_html(markdown))

    def test_ulist(self):
        markdown="""My favorite Miss Manners quotes:

* Allowing an unimportant mistake to pass without comment is a wonderful social grace.
* Ideological differences are no excuse for rudeness.
        """
        html = "<p>My favorite Miss Manners quotes:</p><ul><li>Allowing an unimportant mistake to pass without comment is a wonderful social grace.</li><li>Ideological differences are no excuse for rudeness.</li></ul>"
        self.assertEqual(html, markdown_to_html(markdown))

    def test_olist(self):
        markdown="""My favorite Miss Manners quotes:

* Allowing an unimportant mistake to pass without comment is a wonderful social grace.
* Ideological differences are no excuse for rudeness.
        """
        html = "<p>My favorite Miss Manners quotes:</p><ul><li>Allowing an unimportant mistake to pass without comment is a wonderful social grace.</li><li>Ideological differences are no excuse for rudeness.</li></ul>"
        self.assertEqual(html, markdown_to_html(markdown)) 