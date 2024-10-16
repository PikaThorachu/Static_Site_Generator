import re

block_type_heading = ['# ', '## ', '### ', '#### ', '##### ', '###### ']
block_type_code = "```"
block_type_quote = ">"
block_type_unordered_list = ["* ", "- "]

def block_to_block_type(blocks):
    block_types = []
    pattern_1 = r'^"[0-9]'
    pattern_2 = r"(?<=\n)[0-9]?\.\s"
    for block in blocks:
        # heading block
        if block.startswith("#") or block.startswith("##") or block.startswith("###") or block.startswith("####") or block.startswith("#####") or block.startswith("######"):
            block_types.append("heading")
        # code block
        elif block.startswith("```") and block.endswith("```"):
            block_types.append("code")
        # quote block
        elif block.startswith(">"):
            block_types.append("quote")
        # unordered list block
        elif block.startswith("*") or block.startswith("-"):
            block_types.append("unordered_list")
        # ordered list block
        elif re.findall(pattern_1, block) or re.findall(pattern_2, block):
            block_types.append("ordered_list")
    return block_types
