from textnode import TextNode


def main():
    text = [TextNode("This is a paragraph with a [link_text](https://www.google.com), and this is a test of the nested loop.", "text")]
    matches = TextNode.split_nodes_link(text)
    print(matches)

main()
