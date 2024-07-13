import re
from textnode import(
        TextNode,
        text_type_text,
        text_type_bold,
        text_type_italic,
        text_type_code,
        text_type_link,
        text_type_image,
)

def text_to_textnodes(text):
    #Image
    nodes = split_nodes_image([TextNode(text, text_type_text)]) 
    #Links
    nodes = split_nodes_link(nodes)
    #Bold
    nodes = split_nodes_delimiter(nodes, '**', text_type_bold)
    #Italics
    nodes = split_nodes_delimiter(nodes, '*', text_type_italic)
    #Code
    nodes = split_nodes_delimiter(nodes, '`', text_type_code)
    return nodes

def  split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if not isinstance(node, TextNode) or node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        texts = node.text.split(delimiter)
        if len(texts) % 2 == 0:
            raise ValueError(f"Missing closing {delimiter}")

        for i in range(0, len(texts)):
            if texts[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(texts[i], text_type_text))
            else:
                new_nodes.append(TextNode(texts[i], text_type))

    return new_nodes

def extract_markdown_images(text):
    images = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return images

def split_nodes_image(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if not isinstance(node, TextNode) or node.text_type != text_type_text:
            new_nodes.append(node)
            continue
    
        text = node.text
        images = extract_markdown_images(node.text)
        
        if len(images) == 0:
            new_nodes.append(node)
            continue
        
        for i in range(0, len(images)):
            image = images[i]
            splits = text.split(f"![{image[0]}]({image[1]})", 1)
            if len(splits) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if splits[0] != "":
                new_nodes.append(TextNode(splits[0], text_type_text))
            new_nodes.append(TextNode(image[0], text_type_image, image[1]))                
            text = splits[1]
        if text != "":
            new_nodes.append(TextNode(text, text_type_text))
    
    return new_nodes

def extract_markdown_links(text):
    links = re.findall(r"[^!]\[(.*?)\]\((.*?)\)", text)
    return links

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
    
        text = node.text
        links = extract_markdown_links(node.text)
    
        if len(links) == 0:
            new_nodes.append(node)
            continue
    
        for i in range(0, len(links)):
            link = links[i]
            splits = text.split(f"[{link[0]}]({link[1]})", 1)
            if len(splits) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if splits[0] != "":
                new_nodes.append(TextNode(splits[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            text = splits[1]
        if text != "":
            new_nodes.append(TextNode(text, text_type_text))
    
    return new_nodes