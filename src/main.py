from textnode import TextNode
from markdown_to_blocks import markdown_to_blocks


def main():
    text = [TextNode("This is a paragraph with a link [link_text](https://google.com).", "text")]
    results = TextNode.split_nodes_link(text)
    expected = [
        TextNode("This is a paragraph with a link ", "text"),
        TextNode("link_text", "link", url="https://google.com")
    ]
    print(expected)
    print(results)


main()
