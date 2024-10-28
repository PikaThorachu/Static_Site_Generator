from htmlnode import LeafNode
from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    LIST = "list_item"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == TextType.TEXT.value:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD.value:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC.value:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE.value:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK.value:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE.value:
        return LeafNode("image", "", {"src": text_node.url, "alt": text_node.text})
    elif text_node.text_type == TextType.LIST.value:
        return LeafNode("li", text_node.text)
    else:
        raise ValueError(f"Invalid text type: {text_node.text_type}")

