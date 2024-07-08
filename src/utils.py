
import re
from textnode import TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != "text":
            new_nodes.append(old_node)
            continue
        parts = old_node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise Exception(f"Delimiter {delimiter} not closed in {old_node.text}")
        for i, part in enumerate(parts):
            if i % 2 == 0:
                new_nodes.append(TextNode(part, 'text'))
            else:
                new_nodes.append(TextNode(part, text_type))
    return new_nodes


#TODO fix for multiple images
def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        images = extract_markdown_images(old_node.text)
        if old_node.text_type != "text" or images == []:
            new_nodes.append(old_node)
            continue
        for image_tup in images:
            parts = old_node.text.split(f"![{image_tup[0]}]({image_tup[1]})")
            for i, part in enumerate(parts):
                new_nodes.append(TextNode(part, 'text'))
                if i == 0:
                    new_nodes.append(TextNode(image_tup[0], 'image', image_tup[1]))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        images = extract_markdown_links(old_node.text)
        if old_node.text_type != "text" or images == []:
            new_nodes.append(old_node)
            continue
        for link_tup in images:
            parts = old_node.text.split(f"![{link_tup[0]}]({link_tup[1]})")
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, 'text'))
                    if i == 0:
                        new_nodes.append(TextNode(link_tup[0], 'link', link_tup[1]))
    return new_nodes        

def extract_markdown_images(text): 
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)