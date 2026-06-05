from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(block: str):
    
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if block.startswith('```\n') and block.endswith('```'):
        return BlockType.CODE

    lines = block.split('\n')
    if block.startswith('>'):
        for line in lines:
            if not line.startswith('>'):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    if block.startswith('- '):
        for line in lines:
            if not line.startswith('- '):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    
    if block.startswith('1. '):
        n = 1
        for line in lines:
            if not line.startswith(f"{n}. "):
                return BlockType.PARAGRAPH
            n += 1
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH


def markdown_to_blocks(markdown: str):
    cleaned_blocks = []
    md = markdown
    
    blocks = md.split('\n\n')
    
    for block in blocks:
        block = block.strip()
        if block:
            cleaned_blocks.append(block)

    return cleaned_blocks
