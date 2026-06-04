

def markdown_to_blocks(markdown: str):
    cleaned_blocks = []
    md = markdown
    
    blocks = md.split('\n\n')
    
    for block in blocks:
        block = block.strip()
        if block:
            cleaned_blocks.append(block)

    return cleaned_blocks
