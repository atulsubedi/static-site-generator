from textnode import TextNode
def main():
    node = TextNode("this is a text node", "bold", "https://www.boot.dev")
    n2 = TextNode("this is a text node", "bold", "https://www.boot.dev")
    print(node.__eq__(n2))
    values = node.__repr__()
    print(values)



main()
