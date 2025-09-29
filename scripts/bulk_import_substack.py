#!/usr/bin/env python3
"""
Bulk import Substack posts from CSV or JSON
Usage: python scripts/bulk_import_substack.py posts.csv
"""

import csv
import json
import sys
import os
from import_substack import create_hugo_post

def import_from_csv(filename):
    """Import posts from CSV file"""
    """
    Expected CSV format:
    title,summary,date,url,tags,categories,content
    """
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tags = row.get('tags', '').split(',') if row.get('tags') else ['Substack']
            categories = row.get('categories', '').split(',') if row.get('categories') else ['Blog']

            # Clean up lists
            tags = [tag.strip() for tag in tags if tag.strip()]
            categories = [cat.strip() for cat in categories if cat.strip()]

            create_hugo_post(
                title=row['title'],
                content=row['content'],
                date_str=row['date'],
                url=row['url'],
                tags=tags,
                categories=categories,
                summary=row.get('summary', '')
            )

def import_from_json(filename):
    """Import posts from JSON file"""
    """
    Expected JSON format:
    [
        {
            "title": "Post Title",
            "summary": "Post summary",
            "date": "2024-01-15",
            "url": "https://substack.com/...",
            "tags": ["tag1", "tag2"],
            "categories": ["category1"],
            "content": "Post content..."
        }
    ]
    """
    with open(filename, 'r', encoding='utf-8') as f:
        posts = json.load(f)
        for post in posts:
            create_hugo_post(
                title=post['title'],
                content=post['content'],
                date_str=post['date'],
                url=post['url'],
                tags=post.get('tags', ['Substack']),
                categories=post.get('categories', ['Blog']),
                summary=post.get('summary', '')
            )

def create_sample_files():
    """Create sample CSV and JSON files for reference"""

    # Sample CSV
    csv_content = '''title,summary,date,url,tags,categories,content
"My First Substack Post","An introduction to my newsletter","2024-01-15","https://mystack.substack.com/p/first-post","Substack,Introduction","Blog","This is my first post content..."
"Deep Learning Insights","Exploring neural networks","2024-01-20","https://mystack.substack.com/p/deep-learning","AI,Deep Learning,Research","Research,Technology","Content about deep learning..."'''

    with open('sample_posts.csv', 'w') as f:
        f.write(csv_content)

    # Sample JSON
    json_content = [
        {
            "title": "My First Substack Post",
            "summary": "An introduction to my newsletter",
            "date": "2024-01-15",
            "url": "https://mystack.substack.com/p/first-post",
            "tags": ["Substack", "Introduction"],
            "categories": ["Blog"],
            "content": "This is my first post content..."
        },
        {
            "title": "Deep Learning Insights",
            "summary": "Exploring neural networks",
            "date": "2024-01-20",
            "url": "https://mystack.substack.com/p/deep-learning",
            "tags": ["AI", "Deep Learning", "Research"],
            "categories": ["Research", "Technology"],
            "content": "Content about deep learning..."
        }
    ]

    with open('sample_posts.json', 'w') as f:
        json.dump(json_content, f, indent=2)

    print("📄 Created sample_posts.csv and sample_posts.json")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python scripts/bulk_import_substack.py posts.csv")
        print("  python scripts/bulk_import_substack.py posts.json")
        print("  python scripts/bulk_import_substack.py --samples")
        sys.exit(1)

    filename = sys.argv[1]

    if filename == "--samples":
        create_sample_files()
        return

    if not os.path.exists(filename):
        print(f"❌ File not found: {filename}")
        sys.exit(1)

    if filename.endswith('.csv'):
        print(f"📊 Importing from CSV: {filename}")
        import_from_csv(filename)
    elif filename.endswith('.json'):
        print(f"📊 Importing from JSON: {filename}")
        import_from_json(filename)
    else:
        print("❌ Unsupported file format. Use .csv or .json")
        sys.exit(1)

    print("🎉 Import completed!")

if __name__ == "__main__":
    main()