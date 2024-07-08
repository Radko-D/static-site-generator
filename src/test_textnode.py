import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", "italic")
        self.assertEqual(node.url, None)
    
    def test_eq_url(self):
        node = TextNode("This is a text node", "text", "https://www.google.com")
        node2 = TextNode("This is a text node", "text", "https://www.google.com")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()