text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


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