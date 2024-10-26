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
    def test_text_split_nodes_link(self): # Test 18
        text = [TextNode("This is a paragraph with a link [link_text](https://google.com).", "text")]
        results = TextNode.split_nodes_link(text)
        expected = [
            TextNode("This is a paragraph with a link ", "text"),
            TextNode("link_text", "link", url="https://google.com")
        ]
        self.assertEqual(results, expected)

    def text_split_nodes_link_multiple_links(self):
        text = [TextNode("This is a paragraph with multiple links [link_text](https://google.com), [other_link_text](https://www.getsome.com).", "text")]
        results = TextNode.split_nodes_link(text)
        expected = [
            TextNode("This is a paragraph with multiple links ", "text"),
            TextNode("link_text", "link", url="https://google.com"),
            TextNode(", ", "text"),
            TextNode("other_link_text", "link", url="https://www.getsome.com"),
            TextNode(".", "text")
        ]
        self.assertEqual(results, expected)

    def text_to_textnodes(self):
        text = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        results =  TextNode.text_node_to_html_node(text)
        expected = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]
        self.assertEqual(results, expected)

if __name__ == "__main__":
    unittest.main()