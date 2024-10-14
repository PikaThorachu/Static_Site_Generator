from textnode import TextNode
from markdown_to_blocks import markdown_to_blocks


def main():
    markdown = """# This is a heading

    This is a paragraph of text. It has some **bold** and *italic* words inside of it.

    * This is the first list item in a list block
    * This is a list item
    * This is another list item"""
    results = markdown_to_blocks(markdown)
    print(results)

main()
