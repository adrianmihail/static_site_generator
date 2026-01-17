class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == "" or self.props is None:
            return ""
        else:
            props_keys = list(self.props.keys())
            string = ""
            for key in props_keys:
                string += f' {key}="{self.props[key]}"'
            return string

    def __repr__(self):
        return f"HTMLNode: {self.tag},{self.value},{self.children},{self.props}"

class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
          super().__init__()
          self.tag = tag
          self.value = value
          self.props = props
    
    def to_html(self):
        if self.value is None:
            raise ValueError
        elif self.value is None or self.value == "":
            return self.value
        elif self.props != None:
            props_keys = list(self.props.keys())
            string = f"<{self.tag}"
            for key in props_keys:
                string += f' {key}="{self.props[key]}"'
            string += f'>{self.value}</{self.tag}>'
            return string
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"


    def __repr__(self):
           return f"LeafNode: {self.tag},{self.value},{self.props}"


class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__()
        self.tag = tag
        self.children = children
        self.props = props
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("tag is empty")
        
        if self.children is None:
            raise ValueError("children is empty")
        
        string = f'<{self.tag}>'

        for child in self.children:
            string += child.to_html()
        
        string += f'</{self.tag}>'

        return string