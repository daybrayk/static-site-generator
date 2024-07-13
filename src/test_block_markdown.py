import unittest

from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list
)
from markdown_to_html import (
    paragraph_to_html_node,
    heading_to_html_node,
    code_to_html_node,
    )

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        blocks = markdown_to_blocks("This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items")
        self.assertListEqual([
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items",
            ],
            blocks
        )

    def test_multiple_line_feed(self):
        blocks = markdown_to_blocks("This is **bolded** paragraph\n\n\n\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n\n* This is a list\n* with items")
        self.assertListEqual([
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items",
            ],
            blocks
        )

    def test_no_text(self):
        blocks = markdown_to_blocks("")
        self.assertListEqual([], blocks)

    def test_end_whitespace(self):
        blocks = markdown_to_blocks("  This is **bolded** paragraph  \n\n    This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line \n\n * This is a list\n* with items")
        self.assertListEqual([
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items",
            ],
            blocks
        )

    def test_code_block(self):
        self.assertEqual(block_to_block_type("```This is a code block```"), block_type_code)

    def test_unclosed_code_block(self):
        self.assertRaises(ValueError, block_to_block_type, "```This is an unclosed code block")

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
