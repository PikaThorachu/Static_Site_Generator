import re

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

text_delimiter_bold = "**"
text_delimiter_italic = "*"
text_delimiter_code = "`"
text_delimiter_link = "[link]"
text_delimiter_image = "!"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(text_node):
        if text_node.text_type == "text":
            return f'LeafNode("{text_node.text}")'
        elif text_node.text_type == "bold":
            return f'LeafNode("b", "{text_node.text}")'
        elif text_node.text_type == "italic":
            return f'LeafNode("i", "{text_node.text}")'
        elif text_node.text_type == "code":
            return f'LeafNode("code", "{text_node.text}")'
        elif text_node.text_type == "link":
            prop = '{"href", ' + f'"{text_node.url}"' + "}"
            return f'LeafNode("a", "{text_node.text}", {prop})'
        elif text_node.text_type == "img":
            prop = '{"src":' + f'"{text_node.url}"' + ', "alt", ' + f'"{text_node.text}"' + "}"
            return f'LeafNode("img", "None", {prop})'
    
    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []
        for node in old_nodes:
            if node.text_type != "text":
                new_nodes.append(node)
            elif node.text.count(delimiter) == 0:
                new_nodes.append(node)
            elif node.text.count(delimiter) % 2 != 0:
                raise ValueError("Invalid Markdown syntax")
            else:
                parts = node.text.split(delimiter)
                for i, part in enumerate(parts):
                    if i % 2 == 0:
                        # This is text outside delimiters
                        new_nodes.append(TextNode(part, "text"))
                    else:
                        # This is text that was between delimiters
                        if part == "":
                            pass
                        else:
                            new_nodes.append(TextNode(part, text_type))
        return new_nodes
    
    def extract_markdown_images(text):
        pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
        matches = re.findall(pattern, text)
        if not matches:
            return []
        return matches
    
    def extract_markdown_links(text):
        pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
        matches = re.findall(pattern, text)
        if not matches:
            return {}
        return matches
        
    
    def split_nodes_image(old_nodes):
        new_nodes = []
        if not old_nodes:
            raise Exception("No nodes detected")
        for node in old_nodes:
            img_tuples = TextNode.extract_markdown_images(node.text)
            if not img_tuples:
                new_nodes.append(node)
            else:
                temp = node.text
                for img, url in img_tuples:
                    sequence = temp.split(f"![{img}]({url})", 1)
                    if sequence[0] == "":
                        pass
                    else:
                        new_nodes.append(TextNode(sequence[0], "text"))
                    new_nodes.append(TextNode(img, text_type="img", url=url))
                    if sequence[1]:
                        temp = sequence[1]
        return new_nodes

    def split_nodes_link(old_nodes):
        new_nodes = []
        if not old_nodes:
            raise Exception("No nodes detected")
        for node in old_nodes:
            link_tuples = TextNode.extract_markdown_links(node.text)
            if not link_tuples:
                new_nodes.append(node)
            else:
                temp = node.text
                for link, url in link_tuples:
                    sequence = temp.split(f"[{link}]({url})", 1)
                    if sequence[0] == "":
                        pass
                    else:
                        new_nodes.append(TextNode(sequence[0], "text"))
                    new_nodes.append(TextNode(link, text_type="link", url=url))
                    if sequence[1]:
                        temp = sequence[1]
                new_nodes.append(TextNode(temp, "text"))
        return new_nodes







# Start with a string
# new_nodes = [] to hold new nods as they are split and formatted
# extract markdown images
# results in a list of tuples (alt_text, img_url)
# sequences = [] outside the loop so it doesn't get reset each iteration
# for each tuple:
    # split the string using the img markdown as delimiter
    # if sequence[0] is ""
        # pass
    # else format as text textnode and append to new nodes
    # format delimiter as img node and append to new nodes
    # if sequence[1]:
    # update sequence[] to sequence[1]