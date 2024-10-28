import unittest
from inline_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    extract_markdown_links,
    extract_markdown_images,
    text_to_text_node,
)

from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT.value)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD.value)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT.value),
                TextNode("bolded", TextType.BOLD.value),
                TextNode(" word", TextType.TEXT.value),
            ],
            new_nodes,
            print(new_nodes)
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT.value
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD.value)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT.value),
                TextNode("bolded", TextType.BOLD.value),
                TextNode(" word and ", TextType.TEXT.value),
                TextNode("another", TextType.BOLD.value),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT.value
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD.value)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT.value),
                TextNode("bolded word", TextType.BOLD.value),
                TextNode(" and ", TextType.TEXT.value),
                TextNode("another", TextType.BOLD.value),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT.value)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC.value)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT.value),
                TextNode("italic", TextType.ITALIC.value),
                TextNode(" word", TextType.TEXT.value),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT.value)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE.value)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT.value),
                TextNode("code block", TextType.CODE.value),
                TextNode(" word", TextType.TEXT.value),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT.value,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT.value),
                TextNode("image", TextType.IMAGE.value, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT.value,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE.value, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT.value,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT.value),
                TextNode("image", TextType.IMAGE.value, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT.value),
                TextNode(
                    "second image", TextType.IMAGE.value, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.TEXT.value,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT.value),
                TextNode("link", TextType.LINK.value, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT.value),
                TextNode("another link", TextType.LINK.value, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.TEXT.value),
            ],
            new_nodes,
        )

    def test_text_to_text_node(self):
        node = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        result = text_to_text_node(node)
        expected = [
                TextNode('This is ', TextType.TEXT.value), 
                TextNode('text', TextType.BOLD.value), 
                TextNode(' with an ', TextType.TEXT.value),
                TextNode('italic', TextType.ITALIC.value),
                TextNode(' word and a ', TextType.TEXT.value),
                TextNode('code block', TextType.CODE.value),
                TextNode(' and an ', TextType.TEXT.value),
                TextNode('obi wan image', TextType.IMAGE.value, 'https://i.imgur.com/fJRm4Vk.jpeg'),
                TextNode(' and a ', TextType.TEXT.value),
                TextNode('link', TextType.LINK.value, 'https://boot.dev')
            ]
        print(result)
        print(expected)
        self.assertEqual(result,expected)

if __name__ == "__main__":
    unittest.main()
