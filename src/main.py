import os
import shutil
from textnode import TextNode


def main():
    obj = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(obj)


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


copy_from_static()
# main()
