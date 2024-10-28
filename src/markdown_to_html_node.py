import re
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from htmlnode import HTMLNode, LeafNode
from textnode import text_node_to_html_node, TextType
from inline_markdown import text_to_text_node

# This function takes markdown text as input and outputs the text as HTMLNodes
def markdown_to_html_node(markdown: str) -> HTMLNode:
    # Separate markdown text into blocks
    blocks = markdown_to_blocks(markdown)
    HTML_node = HTMLNode("div", value=None, children=[])
    # Convert each block into an HTMLNode and append it to the top HTML_node
    for block in blocks:
        block_type: str = block_to_block_type(block)
        # Heading blocks - assume no additional formatting necessasry
        if block_type == 'heading_1':
            stripped_text = block.replace("# ", "")
            block_html_node = LeafNode("h1", stripped_text)
            HTML_node.children.append(block_html_node)
        elif block_type == 'heading_2':
            stripped_text = block.replace("## ", "")
            block_html_node = LeafNode("h2", stripped_text)
            HTML_node.children.append(block_html_node)       
        elif block_type == 'heading_3':
            stripped_text = block.replace("### ", "")
            block_html_node = LeafNode("h3", stripped_text)
            HTML_node.children.append(block_html_node)       
        elif block_type == 'heading_4':
            stripped_text = block.replace("#### ", "")
            block_html_node = LeafNode("h4", stripped_text)
            HTML_node.children.append(block_html_node)       
        elif block_type == 'heading_5':
            stripped_text = block.replace("##### ", "")
            block_html_node = LeafNode("h5", stripped_text)
            HTML_node.children.append(block_html_node)       
        elif block_type == 'heading_6':
            stripped_text = block.replace("###### ", "")
            block_html_node = LeafNode("h6", stripped_text)
            HTML_node.children.append(block_html_node)  
        # Code blocks - no additional formatting needed
        elif block_type == 'code':
            front_stripped_text = block.replace("``` ", "")
            stripped_text = front_stripped_text.replace("```", "")
            pre_node = HTMLNode("pre", children=[])
            pre_node.children.append(LeafNode("code", stripped_text))
            HTML_node.children.append(pre_node) 
        # Quote blocks - check this block for text node formatting
        elif block_type == 'quote':
            stripped_text = block.replace("> ", "")
            #Separate stripped text into text nodes, store are .children items
            block_html_node = LeafNode("blockquote", stripped_text)
            HTML_node.children.append(block_html_node) 
        # Unordered list blocks
        elif block_type == 'unordered_list':
            stripped_text = block.replace("* ", "")
            block_html_node = HTMLNode("ul", stripped_text)
            block_html_node.children = split_nodes_ul_items(stripped_text, "\n")
            block_html_node.value = None
            HTML_node.children.append(block_html_node)  
        # Ordered list blocks
        elif block_type == 'ordered_list':
            stripped_text = block
            block_html_node = HTMLNode("ol", stripped_text)
            block_html_node.children = split_nodes_ol_items(stripped_text, "\n")
            block_html_node.value = None
            HTML_node.children.append(block_html_node)   
        # Paragraph blocks   
        else:
            block_html_node = HTMLNode("p", block)
            child_text_nodes = text_to_text_node(block)
            for node in child_text_nodes:
                block_html_node.children = text_node_to_html_node(node)
            block_html_node.value = ""
            HTML_node.children.append(block_html_node)   
    return HTML_node

# Helper Functions
def list_node_to_leaf_nodes(ordered_list: str) -> list:
    split_ordered_list = ordered_list.split('\n')
    children_nodes = []
    for item in split_ordered_list:
        children_nodes.append(LeafNode("li", item))
    return children_nodes

def split_nodes_ul_items(stripped_text: str, delimiter: str) -> list:
    split_nodes = []
    sections = stripped_text.split(delimiter)
    for section in sections:
        if section == "":
            continue
        split_nodes.append(LeafNode("li", section))
    return split_nodes

def split_nodes_ol_items(stripped_text: str, delimiter: str) -> list:
    split_nodes = []
    sections = stripped_text.split(delimiter)
    for section in sections:
        if section == "":
            continue
        pattern = r"^[0-9]*\.\s"
        clean_section = re.sub(pattern, "", section)
        split_nodes.append(LeafNode("li", clean_section))
    return split_nodes
