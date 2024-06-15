import unittest

from htmlnode import HTMLNode, LeafNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("h1", "This is a text node", None, {"class": "bold", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' class="bold" target="_blank"')

    def test_props_to_html_none(self):
        node = HTMLNode("h1", "This is a text node", None, None)
        self.assertEqual(node.props_to_html(), None)
    
    def test_to_html_no_tag(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>')
        
    def test_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
        
    def should_raise_value_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
            
    def should_return_value(self):
        node = LeafNode(None, "This is a paragraph of text.")
        self.assertEqual(node.to_html(), 'This is a paragraph of text.')
        
if __name__ == "__main__":
    unittest.main()