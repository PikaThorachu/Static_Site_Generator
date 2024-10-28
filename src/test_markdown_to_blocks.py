import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks_full(self):
        markdown = """# HEADER

        This is a (short) paragraph.

        * This is the first line of an unordered list.
        * This is a second line.
        * Final line.

        1. And this is an ordered list.
        2. Another line of the list.
        3. Final line in ordered list."""

        result = markdown_to_blocks(markdown)
        expected = [
            "# HEADER",
            "This is a (short) paragraph.",
            "* This is the first line of an unordered list.\n* This is a second line.\n* Final line.",
            "1. And this is an ordered list.\n2. Another line of the list.\n3. Final line in ordered list.",
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()