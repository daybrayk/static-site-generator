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

def extract_title(markdown):
    title = re.search(r"#(.+)\n?", markdown)
    if title:
        return title.group(1).strip()
    else:
        raise ValueError("Missing Title: Could not find a title in the markdown document")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        nodes.append(block_to_html_node(block))     
    return ParentNode("div", nodes)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    elif block_type == block_type_heading:
        return heading_to_html_node(block)
    elif block_type == block_type_code:
        return code_to_html_node(block)
    elif block_type == block_type_quote:
        return quote_to_html_node(block)
    elif block_type == block_type_unordered_list:
        return ulist_to_html_node(block)
    elif block_type == block_type_ordered_list:
        return olist_to_html_node(block)

def paragraph_to_html_node(paragraph):
    splits = paragraph.split('\n')
    paragraph = " ".join(splits)
    return ParentNode("p", text_to_children(paragraph))

def heading_to_html_node(heading):
    count = 0
    while heading[count] == '#':
        count += 1
    splits = re.split("#+ ", heading)
    return ParentNode(f"h{count}", text_to_children(splits[1]))

def code_to_html_node(code):
    text = code[4:-3]
    child_nodes = text_to_children(text)
    return ParentNode("pre", [ParentNode("code", child_nodes)])

def quote_to_html_node(quote):
    child_nodes = []
    lines = []
    splits = quote.split('\n')
    for split in splits:
    #     lines.append(split.strip('>').strip())
    # content = " ".join(lines)
    # return ParentNode("blockquote", text_to_children(content))
        split = split.rstrip(" ")
        if split == ">":
            if len(lines) == 0:
                continue
            child_nodes.append(ParentNode("p", text_to_children(" ".join(lines))))
            lines.clear()
            continue
        lines.append(split.lstrip(">").strip())

    child_nodes.append(ParentNode("p", text_to_children(" ".join(lines))))

    return ParentNode("blockquote", child_nodes)


def ulist_to_html_node(ulist):
    child_nodes = []
    splits = ulist.split('\n')
    for split in splits:
        split = re.sub("^\* ", "", split)
        split = re.sub("^- ", "", split)
        child_nodes.append(ParentNode("li", text_to_children(split)))
    return ParentNode("ul", child_nodes)

def olist_to_html_node(olist):
    child_nodes = []
    splits = olist.split('\n')
    for split in splits:
        split = re.sub(r"[0-9][0-9]*. ", "", split)
        child_nodes.append(ParentNode("li", text_to_children(split)))
    return ParentNode("ol", child_nodes)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    child_nodes = []
    for node in text_nodes:
        # node.text = node.text.replace("\n", " ")
        child_nodes.append(text_node_to_html_node(node))
    return child_nodes