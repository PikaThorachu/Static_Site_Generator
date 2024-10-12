from textnode import TextNode


def main():
    nodes = [
        TextNode('This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)', "text"),
        TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", "text")
    ]
    results = TextNode.text_to_textnodes(nodes)
    print('\n'.join(str(i) for i in results))
    
main()
