import re

from inline_markdown import(
    split_nodes_delimiter,
    )

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    splits = markdown.split("\n\n")
    blocks = []

    for split in splits:
        if split == "":
            continue

        blocks.append(split.strip())

    return blocks

def block_to_block_type(block):
    #Heading
    if block[0] == '#':
        return block_type_heading
    
    #Code
    if block[:3] == "```":
        if block[-3:] == "```": 
            return block_type_code
        else:
            raise ValueError("Invalid Markdown, code block is never closed!")

    splits = block.split('\n')

    #Quotes
    is_quote_block = True
    for split in splits:
        if split[0] != '>':
            is_quote_block = False 
            break
    if is_quote_block:
        return block_type_quote

    #Unordered List
    is_unordered_list = True
    for split in splits:
        if split[:2] != "* " and split[:2] != "- ":
            is_unordered_list = False
            break
    if is_unordered_list:
        return block_type_unordered_list

    #Ordered List
    is_ordered_list = True
    for i in range(0, len(splits)):
        split = splits[i]
        if split[:3] != f"{i+1}. ":
            is_ordered_list = False
            break
    if is_ordered_list:
        return block_type_ordered_list

    return block_type_paragraph