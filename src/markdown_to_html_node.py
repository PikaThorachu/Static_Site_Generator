from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from htmlnode import HTMLNode
from textnode import TextNode, TextType
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
            block_html_node = HTMLNode("h1", stripped_text)
            HTML_node.children.append(block_html_node)
        elif block_type == 'heading_2':
            stripped_text = block.replace("## ", "")
            block_html_node = HTMLNode("h2", stripped_text)
            HTML_node.children.append(block_html_node)       
        elif block_type == 'heading_3':
            stripped_text = block.replace("### ", "")
            block_html_node = HTMLNode("h3", stripped_text)
            HTML_node.children.append(block_html_node)       
        elif block_type == 'heading_4':
            stripped_text = block.replace("#### ", "")
            block_html_node = HTMLNode("h4", stripped_text)
            HTML_node.children.append(block_html_node)       
        elif block_type == 'heading_5':
            stripped_text = block.replace("##### ", "")
            block_html_node = HTMLNode("h5", stripped_text)
            HTML_node.children.append(block_html_node)       
        elif block_type == 'heading_6':
            stripped_text = block.replace("###### ", "")
            block_html_node = HTMLNode("h6", stripped_text)
            HTML_node.children.append(block_html_node)  
        # Code blocks - no additional formatting needed
        elif block_type == 'code':
            front_stripped_text = block.replace("``` ", "")
            stripped_text = front_stripped_text.replace("```", "")
            block_html_node = HTMLNode("code", stripped_text)
            HTML_node.children.append(block_html_node) 
        # Quote blocks - check this block for text node formatting
        elif block_type == 'quote':
            stripped_text = block.replace("> ", "")
            #Separate stripped text into text nodes, store are .children items
            block_html_node = HTMLNode("quote", stripped_text)
            HTML_node.children.append(block_html_node) 
        # Unordered list blocks
        elif block_type == 'unordered_list':
            stripped_text = block.replace("* ", "")
            block_html_node = HTMLNode("unordered_list", stripped_text)
            block_html_node.children = list_node_to_text_nodes(stripped_text)
            block_html_node.value = ""
            HTML_node.children.append(block_html_node)  
        # Ordered list blocks
        elif block_type == 'ordered_list':
            stripped_text = block
            block_html_node = HTMLNode("ordered_list", stripped_text)
            block_html_node.children = list_node_to_text_nodes(stripped_text)
            block_html_node.value = ""
            HTML_node.children.append(block_html_node)   
        # Paragraph blocks   
        else:
            block_html_node = HTMLNode("paragraph", block)
            block_html_node.children = text_to_text_node(block)
            block_html_node.value = ""
            HTML_node.children.append(block_html_node)   
    return HTML_node

# Helper Functions
def list_node_to_text_nodes(ordered_list: str) -> list:
    split_ordered_list = ordered_list.split('\n')
    children_nodes = []
    for item in split_ordered_list:
        children_nodes.append(TextNode(item, TextType.LIST_ITEM))
    return children_nodes