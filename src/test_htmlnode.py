import unittest

from htmlnode import HTMLNODE
from htmlnode import LEAFNODE
from htmlnode import PARENTNODE

class TESTHTMLNODE(unittest.TestCase):

    def test_to_html_prop(self):
        node = HTMLNODE("p", "hi I am a programmer", None, {
            "href": "www.test.link.com",
            "alt": "test_case",
        })

        self.assertEqual(node.props_to_html(), " href=www.test.link.com alt=test_case",)

    def test_to_html_no_children(self):
        node = LEAFNODE("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LEAFNODE(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

        
    def test_to_html_many_children(self):
        node = PARENTNODE(
            "p",
            [
                LEAFNODE("b", "Bold text"),
                LEAFNODE(None, "Normal text"),
                LEAFNODE("i", "italic text"),
                LEAFNODE(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

if __name__ == "__main__":
    unittest.main()
