from textnode import TextNode
from htmlnode import HTMLNode

def main():
    tn = TextNode("This is a text node", "bold", "https://www.google.com")
    print(tn)

    prop_value = HTMLNode("", "", "", {"href": "https://www.google.com", "target": "_blank"})
    print(prop_value)

main()




