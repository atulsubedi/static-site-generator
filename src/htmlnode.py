class HTMLNODE:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("no value")

    def props_to_html(self):
        if self.props is None:
            return ''
        string = ''
        for k in self.props:
            string += f" {k}={self.props[k]}"
        return string

    def __repr__(self):
        return f"tag: {self.tag} value: {self.value} props:{self.props} children: {self.children}"

class LEAFNODE(HTMLNODE):
    def __init__(self, tag=None, value='' ,props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("all leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
