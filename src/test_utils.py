import unittest

from textnode import TextNode
from utils import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, split_nodes_image


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
    
    def test_extract_markdown_links_no_links(self):
        text = "This is a paragraph of text."
        self.assertEqual(extract_markdown_links(text), [])
        
    def test_extract_markdown_images_no_images(self):
        text = "This is a paragraph of text."
        self.assertEqual(extract_markdown_images(text), [])
        
    def test_extract_markdown_images_many_images(self):
        text = "![image](https://www.google.com) ![image](https://www.google.com)"
        self.assertEqual(extract_markdown_images(text), [("image", "https://www.google.com"), ("image", "https://www.google.com")])
    
    def test_extract_markdown_links_many_links(self):
        text = "[Google](https://www.google.com) [Google](https://www.google.com)"
        self.assertEqual(extract_markdown_links(text), [("Google", "https://www.google.com"), ("Google", "https://www.google.com")])
    
    def test_split_nodes_image(self):
        node = TextNode("This is an image ![image](https://www.google.com) and this is follow-up text", "text")
        new_nodes = split_nodes_image([node])
        print(new_nodes)
        self.assertEqual(new_nodes, [
        TextNode("This is an image ", "text"),
        TextNode("image", "image", "https://www.google.com"),
        TextNode(" and this is follow-up text", "text")
        ])
    
    def test_split_nodes_image_no_images(self):
        node = TextNode("This is a paragraph of text.", "text")
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [node])

    def test_split_nodes_image_many_images(self):
        node = TextNode("This is an image ![image](https://www.google.com) and this is another image ![image](https://www.google.com)", "text")
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [
        TextNode("This is an image ", "text"),
        TextNode("image", "image", "https://www.google.com"),
        TextNode(" and this is another image ", "text"),
        TextNode("image", "image", "https://www.google1.com")
        ])    
    
if __name__ == "__main__":
    unittest.main()