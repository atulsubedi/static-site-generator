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
