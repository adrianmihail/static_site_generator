class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        if self.tag is None:
            return self.value

        attrs = ""
        if self.props:
            attrs = "".join(f' {k}="{v}"' for k, v in self.props.items())

        if self.children:
            inner = "".join(child.to_html() for child in self.children)
        else:
            inner = self.value or ""

        return f"<{self.tag}{attrs}>{inner}</{self.tag}>"

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
        # plain text node: no tag, just value
        if self.tag is None:
            return self.value or ""

        if self.value is None:
            raise ValueError("LeafNode with tag must have value")

        # props should be a dict or None; reuse props_to_html
        attrs = ""
        if self.props:
            if isinstance(self.props, dict):
                attrs = "".join(f' {k}="{v}"' for k, v in self.props.items())
            else:
                # if older code passed a prebuilt string, just prepend a space
                attrs = " " + str(self.props)

        return f"<{self.tag}{attrs}>{self.value}</{self.tag}>"


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