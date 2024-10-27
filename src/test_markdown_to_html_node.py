import unittest
from markdown_to_html_node import markdown_to_html_node 
from htmlnode import HTMLNode
from textnode import TextNode

class TestMarkdown_to_HTML_Node(unittest.TestCase):
    def test_markdown_to_html_headings(self):
        markdown = '''# This is a heading_1

## This is a heading_2

### This is a heading_3

This is a paragraph of text. It has some **bold text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)

``` This is a code block```

> This is a quote block.

* This is the first list item in a unordered list block.
* This is a list item.
* This is another list item.
* This is the final list item.

1. This is the first item of an ordered list.
2. This is the second item of an ordered list.
3. This is the final item of this ordered list.'''
        results = markdown_to_html_node(markdown)
        expected = HTMLNode('div', children=[HTMLNode('h1', 'This is a heading_1'), HTMLNode('h2', 'This is a heading_2'), HTMLNode('h3', 'This is a heading_3'), HTMLNode('p', children=[TextNode('This is a paragraph of text. It has some ', 'text'), TextNode('bold text', 'bold'), TextNode(' with an ', 'text'), TextNode('italic', 'italic'), TextNode(' word and a ', 'text'), 
TextNode('code block', 'code'), TextNode(' and an ', 'text'), TextNode('obi wan image', 'image', 'https://i.imgur.com/fJRm4Vk.jpeg'), TextNode(' and a ', 'text'), TextNode('link', 'link', 'https://boot.dev')]), HTMLNode('code', 'This is a code block'), HTMLNode('quote', 'This is a quote block.'), HTMLNode('unordered_list', children=[TextNode('This is the first list item in a unordered list block.', 'list_item'), TextNode('This is a list item.', 'list_item'), TextNode('This is another list item.', 'list_item'), TextNode('This is the final list item.', 'list_item')]), HTMLNode('ordered_list', children=[TextNode("1. This is the first item of an ordered list.", 'list_item'), TextNode('2. This is the second item of an ordered list.', 'list_item'), TextNode('3. This is the final item of this ordered list.', 'list_item')])])
        print(results)

        

if __name__ == '__main__':
    unittest.main()