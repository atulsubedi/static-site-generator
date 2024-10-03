from textnode import TextNode
from htmlnode import HTMLNODE
def main():
    node = TextNode("this is a text node", "bold", "https://www.boot.dev")
    n2 = TextNode("this is a text node", "bold", "https://www.boot.dev")
    print(node.__eq__(n2))
    values = node.__repr__()
    print(values)

    p = HTMLNODE("p", "hi I am SWE", None, {
    "href": "https://www.google.com",
    "target": "_blank",
} )
    s = p.props_to_html()
    print(s)
    values = p.__repr__()
    print(values)




main()
