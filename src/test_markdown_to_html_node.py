import unittest
from markdown_to_html_node import markdown_to_html_node, split_html_nodes_into_text_nodes
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestMarkdown_to_HTML_Node(unittest.TestCase):
    def test_markdown_to_html_headings(self):
        markdown = '''# This is a heading_1

## This is a heading_2

### This is a heading_3

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

``` This is a code block```

> This is a quote block.

* This is the first list item in a unordered list block.
* This is a list item.
* This is another list item.
* This is the final list item.

1. This is the first item of an ordered list.
2. This is the second item of an ordered list.
3. This is the final item of this ordered list.'''
        HTML_nodes = markdown_to_html_node(markdown)
        test_child_text_nodes = split_html_nodes_into_text_nodes(HTML_nodes)
        print(test_child_text_nodes)
        
        

if __name__ == '__main__':
    unittest.main()