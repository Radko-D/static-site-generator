from htmlnode import HTMLNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node


block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ordered_list = "ordered_list"
block_type_unordered_list = "unordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block: str) -> str:
    lines = block.split("\n")
    if (
        block.count("#", 0, 5) <= 6
        and block.count("#", 0, 5) > 0
        and block.endswith(" ", 0, block.count("#") + 1)
    ):
        return block_type_heading
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    if block != "":
        if block.count(">") == len(block.splitlines()):
            return block_type_quote

        if block.startswith("* "):
            for line in lines:
                if not line.startswith("* "):
                    return block_type_paragraph
            return block_type_unordered_list
        if block.startswith("- "):
            for line in lines:
                if not line.startswith("- "):
                    return block_type_paragraph
            return block_type_unordered_list

        if block.startswith("1. "):
            i = 1
            for line in lines:
                if not line.startswith(f"{i}. "):
                    return block_type_paragraph
                i += 1
            return block_type_ordered_list
    return block_type_paragraph


def markdown_to_html_node(markdown) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    children_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_paragraph:
            children_nodes.append(paragraph_block_to_html(block))
        elif block_type == block_type_heading:
            children_nodes.append(heading_block_to_html(block))
        elif block_type == block_type_code:
            children_nodes.append(code_block_to_html(block))
        elif block_type == block_type_quote:
            children_nodes.append(quote_block_to_html(block))
        elif block_type == block_type_ordered_list:
            children_nodes.append(ol_block_to_html(block))
        elif block_type == block_type_unordered_list:
            children_nodes.append(ul_block_to_html(block))
    return ParentNode("div", children_nodes)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_block_to_html(block: str):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    return ParentNode("p", text_to_children(paragraph))


def heading_block_to_html(block: str):
    heading_number = block.count("#")
    return ParentNode(
        f"h{heading_number}", text_to_children(block[heading_number + 1 :])
    )


def code_block_to_html(block: str):
    return ParentNode("pre", [ParentNode("code", text_to_children(block[4:-3]))])


def ol_block_to_html(block: str):
    children = []
    for line in block.splitlines():
        text = line[3:]
        children.append(ParentNode("li", text_to_children(text)))
    return ParentNode("ol", children)


def ul_block_to_html(block: str):
    children = []
    for line in block.splitlines():
        text = line[2:]
        children.append(ParentNode("li", text_to_children(text)))
    return ParentNode("ul", children)


def quote_block_to_html(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)
