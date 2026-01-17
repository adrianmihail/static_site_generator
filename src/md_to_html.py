from markdown_blocks import *
from convert_markdown import *
from htmlnode import *
from textnode import *


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []

    for tnode in text_nodes:
        html_child = text_node_to_html_node(tnode)
        children.append(html_child)
    
    return children

def markdown_to_html_node(markdown):

    blocks = markdown_to_blocks(markdown)
    block_list = []

    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.PARAGRAPH:
                normalized = " ".join(block.split("\n"))
                new_html_node = HTMLNode("p",None,text_to_children(normalized))
                block_list.append(new_html_node)

            case BlockType.HEADING:
                size = 0
                for char in block:
                    if char == "#":
                        size += 1
                    else:
                        break
                
                heading_text = block[size+1:]
                
                new_html_node = HTMLNode(f"h{size}",None, text_to_children(heading_text))
                block_list.append(new_html_node)

            case BlockType.QUOTE:
                lines = block.split("\n")
                cleaned_lines = []

                for line in lines:
                    line = line.lstrip()
                    if line.startswith("> "):
                        line = line[2:]
                    cleaned_lines.append(line)
                
                cleaned = "\n".join(cleaned_lines)
                new_html_node = HTMLNode("blockquote",None,text_to_children(cleaned))
                block_list.append(new_html_node)

            case BlockType.UNORDERED_LIST:
                lines = block.split("\n")
                li_nodes = []

                for line in lines:
                    cleaned = line.lstrip()[2:]
                    li_nodes.append(HTMLNode("li",None,text_to_children(cleaned)))

                new_html_node = HTMLNode("ul",None, li_nodes)
                block_list.append(new_html_node)

            case BlockType.ORDERED_LIST:
                lines = block.split("\n")
                li_nodes = []

                for line in lines:
                    line = line.lstrip()
                    dot_index = line.find(". ")
                    cleaned = line[dot_index + 2:]
                    li_nodes.append(HTMLNode("li",None,text_to_children(cleaned)))

                new_html_node = HTMLNode("ol",None, li_nodes)
                block_list.append(new_html_node)

            case BlockType.CODE:
                lines = block.split("\n")
                inner_lines = lines[1:-1]
                inner = "\n".join(inner_lines) + "\n"

                code_text_node = TextNode(inner,TextType.CODE)
                code_html_node = text_node_to_html_node(code_text_node)
                new_html_node = HTMLNode("pre",None,[code_html_node])
                block_list.append(new_html_node)


    top_level = HTMLNode("div",None,block_list)
    return top_level