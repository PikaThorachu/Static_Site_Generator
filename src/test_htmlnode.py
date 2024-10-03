import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_parent_to_html(self):
        parent = ParentNode(
            "p", 
            [
                LeafNode("b", "This is bold text"),
                LeafNode("i", "This is italic text"),
                LeafNode("a", "This is a link", {"href": "http://www.link.com"})
            ])
        self.assertEqual(parent.to_html(), '<p><b>This is bold text</b><i>This is italic text</i><a href="http://www.link.com">This is a link</a></p>')

    def test_nested_parent_node(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "bold text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("i", "nested italic text")
                    ]
                ),
                LeafNode(None, "Normal text")
            ]
        )
        self.assertEqual(node.to_html(), f'<p><b>bold text</b><p><i>nested italic text</i></p>Normal text</p>')

if __name__ == "__main__":
    unittest.main()