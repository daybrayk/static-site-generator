import shutil
import os
from textnode import TextNode
from inline_markdown import(
    extract_markdown_images,
    extract_markdown_links,
    )
static_file_path = 'static'
public_file_path = 'public'

def main():
    clean_copy(static_file_path, public_file_path)

def clean_copy(source, destination):
    if not os.path.exists(source):
        raise ValueError("Path Error: Source directory does not exist.")
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    print(f"Copying files in {source}...")
    for item in os.listdir(source):
        item_path = os.path.join(source, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, destination)
            print(f"Copying {item_path} to {destination}")
        else:
            clean_copy(item_path, os.path.join(destination, item))

main()