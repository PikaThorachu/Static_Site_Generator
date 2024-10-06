import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node2", text_type_text)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_italic, "https://www.boot.dev")
        node2 = TextNode(
            "This is a text node", text_type_italic, "https://www.boot.dev"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

    def test_to_html_text(self):
        node = TextNode("This is normal text", "text")
        self.assertEqual(node.text_node_to_html_node(), 'LeafNode("This is normal text")')

    def test_to_html_bold(self):
        node = TextNode("bold", "bold")
        self.assertEqual(node.text_node_to_html_node(), 'LeafNode("b", "bold")')

    def test_to_html_italic(self):
        node = TextNode("italic", "italic")
        self.assertEqual(node.text_node_to_html_node(), 'LeafNode("i", "italic")')

    def test_to_html_code(self):
        node = TextNode("string of code", "code")
        self.assertEqual(node.text_node_to_html_node(), 'LeafNode("code", "string of code")')
    
    def test_to_html_link(self):
        node = TextNode("this is anchor text", "link", "https://www.image_link.com")
        self.assertEqual(node.text_node_to_html_node(), 'LeafNode("a", "this is anchor text", {"href", "https://www.image_link.com"})')

def test_delimiter_bold(self):
    node = TextNode("This is a string with **bold** text.", "text")
    result = split_nodes_delimiter([node], "**", "bold")
    expected = [
        TextNode("This is a string with ", "text"),
        TextNode("bold", "bold"),
        TextNode(" text.", "text")
    ]
    self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
