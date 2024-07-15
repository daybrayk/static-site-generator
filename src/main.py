import shutil
import os
from textnode import TextNode
from inline_markdown import(
    extract_markdown_images,
    extract_markdown_links,
    )
from markdown_to_html import (
    extract_title,
    markdown_to_html_node,
    )

static_file_path = 'static'
public_file_path = 'public'
# src_path = "content/index.md"
content_path = "content"
template_path = "template.html"
dest_path = "public"
# dest_path = "public/index.html"

def main():
    clean_copy(static_file_path, public_file_path)
    # generate_page(src_path, template_path, dest_path)
    generate_pages_recursive(content_path, template_path, dest_path)

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

def generate_page(src, tmpl, dest):
    print(f"Generating page at {src} using {tmpl} to {dest}")
    file = open(src, "r")
    md = file.read()
    file.close()

    file = open(tmpl, "r")
    template = file.read()
    file.close()

    html = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    
    file = open(dest.replace(".md", ".html"), "w")
    file.write(template)
    file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        if os.path.isfile(item_path):
            if ".md" in item:
                generate_page(item_path, template_path, os.path.join(dest_dir_path, item))
        else:
            path = os.path.join(dest_dir_path, item)
            if not os.path.exists(path):
                os.mkdir(path)
            generate_pages_recursive(item_path, template_path, path)

main()