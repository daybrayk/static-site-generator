import re
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import(
    TextNode,
    text_node_to_html_node,
    )
from inline_markdown import(
    text_to_textnodes,
    )
from block_markdown import(
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,)

def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    html = ""
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_paragraph:
            html = f"{html}{paragraph_to_html_node(block).to_html()}"
        elif block_type == block_type_heading:
            html = f"{html}{heading_to_html_node(block).to_html()}"
        elif block_type == block_type_code:
            html = f"{html}{code_to_html_node(block).to_html()}"
        elif block_type == block_type_quote:
            html = f"{html}{quote_to_html_node(block).to_html()}"
        elif block_type == block_type_unordered_list:
            html = f"{html}{ulist_to_html_node(block).to_html()}"
        elif block_type == block_type_ordered_list:
            html = f"{html}{olist_to_html_node(block).to_html()}"
    return html

def paragraph_to_html_node(paragraph):
    return LeafNode("p", paragraph) 

def heading_to_html_node(heading):
    count = 0
    while heading[count] == '#':
        count += 1
    splits = re.split("#+ ", heading)
    return ParentNode(f"h{count}", text_to_children(splits[1]))

def code_to_html_node(code):
    text = re.findall(r"```(.*?)```", code)
    child_nodes = text_to_children(text)
    return ParentNode("code", child_nodes)

def quote_to_html_node(quote):
    child_nodes = []
    body = ""
    splits = quote.split('\n')
    for split in splits:
        if split == ">":
            child_nodes.append(ParentNode("p", text_to_children(body)))
            body = ""
            continue
        split = split.replace("> ", "")
        body = f"{body}{split}"

    child_nodes.append(ParentNode("p", text_to_children(body)))

    return ParentNode("blockquote", child_nodes)

def ulist_to_html_node(ulist):
    child_nodes = []
    splits = ulist.split('\n')
    for split in splits:
        split = split.replace("* ", "")
        split = split.replace("- ", "")
        child_nodes.append(ParentNode("li", text_to_children(split)))
    return ParentNode("ul", child_nodes)

def olist_to_html_node(olist):
    child_nodes = []
    splits = olist.split('\n')
    for split in splits:
        split = re.replace(r"[0-9][0-9]\*. ", "")
        child_nodes.append(ParentNode("li"), text_to_children(split))
    return ParentNode("ol", child_nodes)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    child_nodes = []
    for node in text_nodes:
        child_nodes.append(text_node_to_html_node(node))
    return child_nodes