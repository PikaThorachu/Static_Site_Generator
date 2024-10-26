import unittest
from block_to_block_type import block_to_block_type
from markdown_to_blocks import markdown_to_blocks


class TestBlocktoBlockType(unittest.TestCase):
    def test_block_to_block_type_all_types(self):
        block = "### This block is a heading block"
        result = block_to_block_type(block)
        expected = 'heading_3'
        self.assertEqual(result, expected)

    def test_block_to_block_type_ordered_skip_numbers(self):
        block = "19. This is an ordered list.\n5. This is the second item of the ordered list.\n1042. This is the final item in this ordered list."
        result = block_to_block_type(block)
        expected = "ordered_list"
        self.assertEqual(result, expected)  
    
    def test_markdown_to_block_to_block_type(self):
        markdown = '''# This is a heading_1

## This is a heading_2

### This is a heading_3

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item'''
        blocks = markdown_to_blocks(markdown)
        blocks_types = []
        for block in blocks:
            blocks_types.append(block_to_block_type(block))
        result = blocks_types
        expected = ['heading_1', 'heading_2', 'heading_3', 'paragraph', 'unordered_list']
        self.assertEqual(result, expected)  



if __name__ == '__main__':
    unittest.main()