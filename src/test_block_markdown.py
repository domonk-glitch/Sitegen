import unittest

from block_markdown import markdown_to_blocks, block_to_block_type

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks1(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks2(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks3(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

     

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )



    def test_block_to_block_type1(self):
        md = "###### Heading test"
        blocktype = block_to_block_type(md)
        self.assertEqual(
            blocktype,
            blocktype.HEADING
        )

    def test_block_to_block_type2(self):
        md = "```\nThis should be a code block.\nMultiple lines for the test of course.\n```"
        blocktype = block_to_block_type(md)
        self.assertEqual(
            blocktype,
            blocktype.CODE
        )

    def test_block_to_block_type3(self):
        md = """> Quote testing.
> Gotta make sure all the lines are contained within.
oops! missed one!
> another quote.
"""
        blocktype = block_to_block_type(md)
        self.assertEqual(
            blocktype,
            blocktype.PARAGRAPH
        )

    def test_block_to_block_type4(self):
        md = "- Unordered lists are fun.\n- No. No they are not.\n- Maybe"
        blocktype = block_to_block_type(md)
        self.assertEqual(
            blocktype,
            blocktype.UNORDERED_LIST
        )

    def test_block_to_block_type5(self):
        md = """
1. Something wrong with me.
2. Something wrong with me.
3. Something wrong with me.
5. What happened to 4?
"""
        blocktype = block_to_block_type(md)
        self.assertEqual(
            blocktype,
            blocktype.PARAGRAPH
        )

    def test_block_to_block_type6(self):
        md = "Paragraph test"
        blocktype = block_to_block_type(md)
        self.assertEqual(
            blocktype,
            blocktype.PARAGRAPH
        )
