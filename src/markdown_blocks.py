from enum import Enum
import re

def markdown_to_blocks(markdown):
    blocks = []

    split_pieces = markdown.split("\n\n")

    for block in split_pieces:
        stripped = block.strip()
        if stripped != "":
            blocks.append(stripped)
    
    return blocks


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    
    #header check
    if bool(re.search(r"^#{1,6}\s.*",block)):
        return BlockType.HEADING
    #code check
    elif bool(re.search(r"^(`{3}\n).*(`{3})$",block,re.DOTALL)):
        return BlockType.CODE
    #quote check
    elif bool(re.search(r"^>\s", block)):
        return BlockType.QUOTE
    #unordered_list_check
    elif bool(re.search(r"-\s",block)):
        return BlockType.UNORDERED_LIST
    #ordered_list check
    elif bool(re.search(r"\d.\s",block)):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
