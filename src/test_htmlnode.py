import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_tag(self):
        node_1 = HTMLNode("b", "This is bold text", props={"this is props key": "this is props value"
        })
        print(node_1.__repr__())

    def test_text(self):
        node_1 = HTMLNode("i", "This is italic text", props={"This is props key": "this is props Value"})
        print(node_1.__repr__())


    def test_children(self):
        pass

    def test_props(self):
        node_1 = HTMLNode("!", props={"alt text for image": "image url"})
        print(node_1.__repr__())

if __name__ == "__main__":
    unittest.main()