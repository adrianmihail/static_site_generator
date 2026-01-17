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


def split_nodes_image(old_nodes):
    new_list = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_list.append(old_node)
        else:
            images = extract_markdown_images(old_node.text)
            remaining_text = old_node.text

            for image in images:
                image_markdown = f"![{image[0]}]({image[1]})"
                before, after = remaining_text.split(image_markdown,1)
                if before != "":
                    new_list.append(TextNode(before, TextType.TEXT))
                
                new_list.append(TextNode(image[0],TextType.IMAGE,image[1]))
                remaining_text = after
            
            if remaining_text != "":
                new_list.append(TextNode(remaining_text,TextType.TEXT))


    return new_list

def split_nodes_link(old_nodes):
    new_list = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_list.append(old_node)
        else:
            links = extract_markdown_links(old_node.text)
            remaining_text = old_node.text

            for link in links:
                image_markdown = f"[{link[0]}]({link[1]})"
                before, after = remaining_text.split(image_markdown,1)
                if before != "":
                    new_list.append(TextNode(before, TextType.TEXT))
                
                new_list.append(TextNode(link[0],TextType.LINK,link[1]))
                remaining_text = after
            
            if remaining_text != "":
                new_list.append(TextNode(remaining_text,TextType.TEXT))


    return new_list


def text_to_textnodes(text):
    new_text = text

    new_text = split_nodes_delimiter(new_text,"`",TextType.CODE)
    new_text = split_nodes_delimiter(new_text,"**",TextType.BOLD)
    new_text = split_nodes_delimiter(new_text,"_",TextType.ITALIC)
    new_text = split_nodes_image(new_text)
    new_text = split_nodes_link(new_text)

    return new_text

def markdown_to_blocks(markdown):
    blocks = []

    split_pieces = markdown.split("\n\n")

    for block in split_pieces:
        stripped = block.strip()
        if stripped != "":
            blocks.append(stripped)
    
    return blocks

md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

print(markdown_to_blocks(md))