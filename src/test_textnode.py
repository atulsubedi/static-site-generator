import unittest

from textnode import (
    TEXTNODE,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_node_to_html_node,
)



class TestTEXTNODE(unittest.TestCase):
    def test_eq(self):
        node = TEXTNODE("This is a text node", text_type_text)
        node2 = TEXTNODE("This is a text node", text_type_text)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TEXTNODE("This is a text node", text_type_text)
        node2 = TEXTNODE("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TEXTNODE("This is a text node", text_type_text)
        node2 = TEXTNODE("This is a text node2", text_type_text)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TEXTNODE("This is a text node", text_type_text, "https://www.boot.dev")
        node2 = TEXTNODE("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TEXTNODE("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TEXTNODE(This is a text node, text, https://www.boot.dev)", repr(node)
        )


class TestTEXTNODEToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TEXTNODE("This is a text node", text_type_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TEXTNODE("This is an image", text_type_image, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TEXTNODE("This is bold", text_type_bold)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()
