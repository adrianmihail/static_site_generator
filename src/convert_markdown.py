from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    new_list = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_list.append(old_node)
        else:
            split_node = old_node.text.split(delimiter)

            for i in range(0,len(split_node)):
                if i % 2 == 0:
                    new_node = TextNode(split_node[i],TextType.TEXT)
                    new_list.append(new_node)
                else:
                    new_node = TextNode(split_node[i],text_type)
                    new_list.append(new_node)

    return new_list

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
print(extract_markdown_links(text))
# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]