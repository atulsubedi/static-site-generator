import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        n1 = TextNode("hi how are you doing", "not bold", "https://testurl.com")
        n2 = TextNode("hellow how are you doing", " bold", "https://testurl.com" )
        self.assertNotEqual(n1,n2)

    



if __name__ == "__main__":
    unittest.main()
