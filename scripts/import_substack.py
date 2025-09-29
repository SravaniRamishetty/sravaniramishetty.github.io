#!/usr/bin/env python3
"""
Script to help import Substack posts to Hugo
Usage: python scripts/import_substack.py
"""

import os
import re
from datetime import datetime
from urllib.parse import urlparse

def slugify(text):
    """Convert title to URL-friendly slug"""
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'[-\s]+', '-', text)

def create_hugo_post(title, content, date_str, url, tags=None, categories=None, summary=""):
    """Create a Hugo post from Substack content"""

    # Create slug for directory name
    slug = slugify(title)
    post_dir = f"content/post/{slug}"

    # Create directory if it doesn't exist
    os.makedirs(post_dir, exist_ok=True)

    # Format date
    try:
        post_date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%dT00:00:00Z")
    except:
        post_date = datetime.now().strftime("%Y-%m-%dT00:00:00Z")

    # Default tags and categories
    if tags is None:
        tags = ["Substack", "Blog"]
    if categories is None:
        categories = ["Blog"]

    # Create frontmatter
    frontmatter = f"""---
title: "{title}"
subtitle: ""

# Summary for listings and search engines
summary: "{summary}"

# Link this post with a project
projects: []

# Date published
date: '{post_date}'

# Date updated
lastmod: '{post_date}'

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false

# Featured image
image:
  caption: ''
  focal_point: ''
  placement: 2
  preview_only: false

authors:
  - admin

tags:
{chr(10).join(f'  - {tag}' for tag in tags)}

categories:
{chr(10).join(f'  - {cat}' for cat in categories)}

# Original Substack post
external_link: "{url}"
---

> **Note**: This post was originally published on [Substack]({url}).

{content}
"""

    # Write to file
    with open(f"{post_dir}/index.md", "w", encoding="utf-8") as f:
        f.write(frontmatter)

    print(f"✅ Created post: {post_dir}/index.md")
    return post_dir

def main():
    """Interactive script to create Substack import"""
    print("🚀 Substack to Hugo Import Helper")
    print("=" * 40)

    title = input("Post Title: ")
    summary = input("Post Summary (optional): ")
    date_str = input("Publication Date (YYYY-MM-DD): ")
    url = input("Substack URL: ")

    # Tags
    tags_input = input("Tags (comma-separated, optional): ")
    tags = [tag.strip() for tag in tags_input.split(",")] if tags_input else ["Substack"]

    # Categories
    categories_input = input("Categories (comma-separated, optional): ")
    categories = [cat.strip() for cat in categories_input.split(",")] if categories_input else ["Blog"]

    print("\n📝 Now paste your Substack post content (Ctrl+D when done):")
    content_lines = []
    try:
        while True:
            line = input()
            content_lines.append(line)
    except EOFError:
        pass

    content = "\n".join(content_lines)

    # Create the post
    post_dir = create_hugo_post(title, content, date_str, url, tags, categories, summary)

    print(f"\n🎉 Post created successfully!")
    print(f"📁 Location: {post_dir}")
    print(f"✏️  Edit the file to refine formatting")
    print(f"🚀 Run 'hugo server' to preview")

if __name__ == "__main__":
    main()