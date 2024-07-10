import unittest

from block_markdown import block_to_block_type, block_type_heading, block_type_code, block_type_quote, block_type_unordered_list, block_type_ordered_list, block_type_paragraph, markdown_to_blocks


class TestUtils(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = "This is a paragraph of text.\n\nThis is another paragraph of text."
        self.assertEqual(markdown_to_blocks(markdown), ["This is a paragraph of text.", "This is another paragraph of text."])
    
    def test_markdown_to_blocks_no_blocks(self):
        markdown = ""
        self.assertEqual(markdown_to_blocks(markdown), [])
    
    def test_markdown_to_blocks_one_block(self):
        markdown = "This is a paragraph of text."
        self.assertEqual(markdown_to_blocks(markdown), ["This is a paragraph of text."])
    
    def test_markdown_to_blocks_many_blocks(self):
        markdown = "This is a paragraph of text.\n\nThis is another paragraph of text.\n\nThis is a third paragraph of text."
        self.assertEqual(markdown_to_blocks(markdown), ["This is a paragraph of text.", "This is another paragraph of text.", "This is a third paragraph of text."])
    
    def test_markdown_to_blocks_no_newline(self):
        markdown = "This is a paragraph of text."
        self.assertEqual(markdown_to_blocks(markdown), ["This is a paragraph of text."])
    
    def test_markdown_to_blocks_no_newline_many_blocks(self):
        markdown = "This is a paragraph of text. This is another paragraph of text. This is a third paragraph of text."
        self.assertEqual(markdown_to_blocks(markdown), ["This is a paragraph of text. This is another paragraph of text. This is a third paragraph of text."])
    
    def test_markdown_blocks_empty_block(self):
        markdown = "This is a paragraph of text.\n\n\n\nThis is another paragraph of text."
        self.assertEqual(markdown_to_blocks(markdown), ["This is a paragraph of text.", "This is another paragraph of text."])
        
    def test_heading_blocks(self):
        for i in range(1, 7):
            with self.subTest(i=i):
                block = "#" * i + " Heading"
                self.assertEqual(block_to_block_type(block), block_type_heading)

    def test_code_block(self):
        block = "```code block```"
        self.assertEqual(block_to_block_type(block), block_type_code)

    def test_quote_block(self):
        block = "> quote\n> quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)

    def test_unordered_list_blocks(self):
        blocks = ["- item\n- item", "* item\n* item"]
        for block in blocks:
            with self.subTest(block=block):
                self.assertEqual(block_to_block_type(block), block_type_unordered_list)

    def test_ordered_list_block(self):
        block = "1. item\n2. item"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)

    def test_paragraph_block(self):
        block = "This is a paragraph."
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_empty_string(self):
        block = ""
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_mixed_content(self):
        block = "#1. Mixed content\n- Not a list"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_incorrect_format(self):
        block = "##Not a heading"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

if __name__ == '__main__':
    unittest.main()