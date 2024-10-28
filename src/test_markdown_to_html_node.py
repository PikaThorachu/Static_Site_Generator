import unittest
from markdown_to_html_node import markdown_to_html_node 
from htmlnode import HTMLNode, LeafNode
from textnode import TextNode

class TestMarkdown_to_HTML_Node(unittest.TestCase):
    def test_markdown_to_html_headings(self):
        markdown = '''# This is a heading_1

## This is a heading_2

### This is a heading_3'''
        results = markdown_to_html_node(markdown)
        expected = HTMLNode('div', children=[HTMLNode('h1', 'This is a heading_1'), HTMLNode('h2', 'This is a heading_2'), HTMLNode('h3', 'This is a heading_3')])
        self.assertEqual(results, expected)

    def test_markdown_to_html_code_quote(self):
        markdown = '''``` This is a code block```

> This is a quote block.'''
        results = markdown_to_html_node(markdown)
        expected = HTMLNode('div', children=[HTMLNode('pre', children=[LeafNode('code', 'This is a code block')]), HTMLNode('blockquote', 'This is a quote block.'), ])
        self.assertEqual(results, expected)

    def test_markdown_to_html_ul(self):
        markdown = '''* This is the first list item in a unordered list block.
* This is a list item.
* This is another list item.
* This is the final list item.'''
        results = markdown_to_html_node(markdown)
        expected = HTMLNode('div', children=[HTMLNode('ul', children=[LeafNode('li', 'This is the first list item in a unordered list block.'), LeafNode('li', 'This is a list item.'), LeafNode('li', 'This is another list item.'), LeafNode('li', 'This is the final list item.')])])
        self.assertEqual(results, expected)

    def test_markdown_to_html_ol(self):
        markdown = '''1. This is the first item of an ordered list.
2. This is the second item of an ordered list.
3. This is the final item of this ordered list.'''
        results = markdown_to_html_node(markdown)
        expected = HTMLNode('div', children=[HTMLNode('ol', children=[LeafNode('li', 'This is the first item of an ordered list.'), LeafNode('li', 'This is the second item of an ordered list.'), LeafNode('li', 'This is the final item of this ordered list.')])])
        self.assertEqual(results, expected)

if __name__ == '__main__':
    unittest.main()