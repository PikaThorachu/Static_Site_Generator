import re
def block_to_block_type(block: str) -> str:
    pattern_1 = r'^"[0-9]\.\s'
    pattern_2 = r"(?<=\n)[0-9]?\.\s"
    # Heading blocks
    if block.startswith('# '):
        return 'heading_1'
    elif block.startswith('## '):
        return 'heading_2'
    elif block.startswith('### '):
        return 'heading_3'
    elif block.startswith('#### '):
        return 'heading_4'
    elif block.startswith('##### '):
        return 'heading_5'
    elif block.startswith('###### '):
        return 'heading_6'    
    # code block
    elif block.startswith("```") and block.endswith("```"):
        return "code"
    # quote block
    elif block.startswith(">"):
        return "quote"
    # unordered list block
    elif block.startswith("*") or block.startswith("-"):
        return "unordered_list"
    # ordered list block
    elif re.findall(pattern_1, block) or re.findall(pattern_2, block):
        return "ordered_list"
    else:
        return "paragraph"

