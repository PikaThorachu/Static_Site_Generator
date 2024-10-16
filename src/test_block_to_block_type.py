import unittest
from block_to_block_type import block_to_block_type


class TestBlocktoBlockType(unittest.TestCase):
    def test_block_to_block_type_all_types(self):
        block = ["### ### This block is a heading block", "```This is a code block```", ">This is a quote block", "* This is an unordered list.\n* This is the second line of an unordered list.", "1. This is an ordered list.\n2. This is the second item of the ordered list.\n3. This is the final item in this ordered list."]
        result = block_to_block_type(block)
        expected = ["heading", "code", "quote", "unordered_list", "ordered_list"]
        self.assertEqual(result, expected)

    def test_block_to_block_type_ordered_skip_numbers(self):
        block = ["19. This is an ordered list.\n5. This is the second item of the ordered list.\n1042. This is the final item in this ordered list."]
        result = block_to_block_type(block)
        expected = ["ordered_list"]
        self.assertEqual(result, expected)        


if __name__ == '__main__':
    unittest.main()