from htmlnode import HTMLNode


block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ordered_list = "ordered_list"
block_type_unordered_list = "unordered_list"

def markdown_to_blocks(markdown):
    markdown_blocks = []
    for block in markdown.split("\n\n"):
        if block != "":
            block.strip()
            markdown_blocks.append(block)
    return markdown_blocks

def block_to_block_type(block: str):
    if block.count("#", 0, 5) <= 6 and block.count("#", 0, 5) > 0 and block.endswith(" ", 0, block.count("#")+1):
        return block_type_heading
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    if block != '':
        if block.count(">") == len(block.splitlines()):
            return block_type_quote
        
        if block.count("- ") == len(block.splitlines()) or block.count("* ") == len(block.splitlines()):
            return block_type_unordered_list
        
        if block.count(". ") == len(block.splitlines()):
            is_valid_ordered_list = True
            block_lines = block.splitlines()
            for i in range(0, len(block_lines)):
                if not block_lines[i][0].isdigit() and not block_lines[i-1][0] + 1 == block_lines[i][0]:
                    is_valid_ordered_list = False
                    break
            if is_valid_ordered_list:
                return block_type_ordered_list
    return block_type_paragraph

#TODO check if those 2 methods work properly
def paragraph_block_to_html(block: str):
    return HTMLNode('p', block)

def heading_block_to_html(block: str):
    heading_number = block.count("#")
    return HTMLNode(f"h{heading_number}", block[heading_number+1:])