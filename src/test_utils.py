import unittest

from textnode import TextNode
from utils import extract_markdown_images, extract_markdown_links, split_nodes_delimiter


class TestUtils(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(new_nodes, [
        TextNode("This is text with a ", "text"),
        TextNode("code block", "code"),
        TextNode(" word", "text"),
        ])

    def test_split_nodes_delimiter_not_closed(self):
        node = TextNode("This is text with a `code block word", "text")
        with self.assertRaises(Exception):
             split_nodes_delimiter([node], "`", "code")
            
    def test_extract_markdown_images(self):
        text = "![image](https://www.google.com)"
        self.assertEqual(extract_markdown_images(text), [("image", "https://www.google.com")])
    
    def test_extract_markdown_links(self):
        text = "[Google](https://www.google.com)"
        self.assertEqual(extract_markdown_links(text), [("Google", "https://www.google.com")])
        
if __name__ == "__main__":
    unittest.main()