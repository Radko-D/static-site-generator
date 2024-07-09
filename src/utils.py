
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

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        current_text = old_node.text
        
        while True:
            images = extract_markdown_images(current_text)
            if not images:
                if current_text:
                    new_nodes.append(TextNode(current_text, 'text'))
                break
            
            image_tup = images[0]
            parts = current_text.split(f"![{image_tup[0]}]({image_tup[1]})", 1)
            
            pre_image_text = parts[0]
            post_image_text = parts[1] if len(parts) > 1 else ""
            
            if pre_image_text:
                new_nodes.append(TextNode(pre_image_text, 'text'))
            
            new_nodes.append(TextNode(image_tup[0], 'image', image_tup[1]))
            
            current_text = post_image_text
    
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        current_text = old_node.text
        
        while True:
            images = extract_markdown_links(current_text)
            if not images:
                if current_text:
                    new_nodes.append(TextNode(current_text, 'text'))
                break
            
            link_tup = images[0]
            parts = current_text.split(f"[{link_tup[0]}]({link_tup[1]})", 1)
            
            pre_image_text = parts[0]
            post_image_text = parts[1] if len(parts) > 1 else ""
            
            if pre_image_text:
                new_nodes.append(TextNode(pre_image_text, 'text'))
            
            new_nodes.append(TextNode(link_tup[0], 'link', link_tup[1]))
            
            current_text = post_image_text
    
    return new_nodes      

def extract_markdown_images(text): 
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)