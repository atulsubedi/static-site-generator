import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "hello, world",
            None,
            {"class": "welcome", "href":"https://google.com"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="welcome" href="https://google.com"',
        )

if __name__ == "__main__":
    unittest.main()
