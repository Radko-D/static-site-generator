import os
import re
import shutil

from block_markdown import markdown_to_html_node
from textnode import TextNode


def main():
    copy_from_static()
    generate_page_recursive()


def copy_from_static(current_path="./static", should_recreate_public=True):
    if should_recreate_public:
        shutil.rmtree("./public", ignore_errors=True)
        os.mkdir("./public")
        should_recreate_public = False
    for entry in os.listdir(current_path):
        public_path = current_path.replace("static", "public")
        if os.path.isfile(f"{current_path}/{entry}"):
            if not os.path.exists(public_path):
                os.makedirs(public_path)
            shutil.copy(
                f"{current_path}/{entry}",
                f"{public_path}/{entry}",
            )
        else:
            copy_from_static(f"{current_path}/{entry}", should_recreate_public)


def extract_title(markdown: str):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[1:].strip()
    raise ValueError("No title found")


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = re.sub(r"\{\{ Title \}\}", title, template)
    template = re.sub(r"\{\{ Content \}\}", html, template)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def generate_page_recursive(template_path="./template.html", from_path="./content"):
    if os.path.isdir(from_path):
        for entry in os.listdir(from_path):
            generate_page_recursive(template_path, f"{from_path}/{entry}")
    else:
        generate_page(
            from_path,
            template_path,
            from_path.replace("content", "public").replace(".md", ".html"),
        )


main()
