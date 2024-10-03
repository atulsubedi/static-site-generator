import unittest

from htmlnode import HTMLNODE

class TESTHTMLNODE(unittest.TestCase):

    def test_to_html_prop(self):
        node = HTMLNODE("p", "hi I am a programmer", None, {
            "href": "www.test.link.com",
            "alt": "test_case",
        })

        self.assertEqual(node.props_to_html(), " href=www.test.link.com alt=test_case",)

if __name__ == "__main__":
    unittest.main()
