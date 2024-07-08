
import re
from textnode import TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != "text":
            new_nodes.append(old_node)
            continue
        parts = old_node.text.split(delimiter)
        if len(parts)%2 == 0:
            raise Exception(f"Delimiter {delimiter} not closed in {old_node.text}")
        for i, part in enumerate(parts):
            if i %2 == 0:
                new_nodes.append(TextNode(part, 'text'))
            else:
                new_nodes.append(TextNode(part, text_type))
    return new_nodes
    
def extract_markdown_images(text): 
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)