from htmlnode import LEAFNODE

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TEXTNODE:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, OtherNode):
        return (self.text == OtherNode.text
                and self.text_type == OtherNode.text_type
                and self.url == OtherNode.url)

    def __repr__(self):
        return f"TEXTNODE({self.text}, {self.text_type}, {self.url})"



def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LEAFNODE(None, text_node.text)
    if text_node.text_type == text_type_bold:
        return LEAFNODE("b", text_node.text)
    if text_node.text_type == text_type_italic:
        return LEAFNODE("i", text_node.text)
    if text_node.text_type == text_type_code:
        return LEAFNODE("code", text_node.text)
    if text_node.text_type == text_type_link:
        return LEAFNODE("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == text_type_image:
        return LEAFNODE("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text_type}")
