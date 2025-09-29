# 📝 Substack to Hugo Import Guide

This directory contains tools to help you import your Substack posts into your Hugo website.

## 🚀 Quick Start

### Method 1: Single Post Import (Interactive)

```bash
cd /path/to/your/hugo/site
python scripts/import_substack.py
```

Follow the prompts to import one post at a time.

### Method 2: Bulk Import

1. **Create a data file** (CSV or JSON format)
2. **Run the bulk importer**

```bash
# Create sample files to see the format
python scripts/bulk_import_substack.py --samples

# Import from your data file
python scripts/bulk_import_substack.py my_posts.csv
# or
python scripts/bulk_import_substack.py my_posts.json
```

## 📋 Data Formats

### CSV Format
```csv
title,summary,date,url,tags,categories,content
"Post Title","Brief summary","2024-01-15","https://substack.com/...","tag1,tag2","Blog,Research","Post content here..."
```

### JSON Format
```json
[
  {
    "title": "Post Title",
    "summary": "Brief summary",
    "date": "2024-01-15",
    "url": "https://substack.com/...",
    "tags": ["tag1", "tag2"],
    "categories": ["Blog", "Research"],
    "content": "Post content here..."
  }
]
```

## 🔄 Workflow Options

### Option A: Manual Copy-Paste
1. Open your Substack post
2. Copy the content
3. Run `python scripts/import_substack.py`
4. Paste content when prompted

### Option B: Substack Export
1. Export your Substack posts (if available)
2. Convert to CSV/JSON format
3. Use bulk import script

### Option C: Web Scraping (Advanced)
For bulk importing, you could extend the scripts to scrape Substack directly (respecting rate limits and terms of service).

## 🎨 Post Customization

After importing, you can customize each post by editing the `index.md` file:

- **Add featured images**: Place `featured.jpg` in the post folder
- **Adjust categories and tags**: Edit the frontmatter
- **Modify content**: Clean up formatting, add Hugo shortcodes
- **Set featured posts**: Change `featured: true`

## 📂 File Structure

After import, each post will have this structure:
```
content/post/my-post-title/
├── index.md          # Main post file
└── featured.jpg      # Optional featured image
```

## 🔧 Advanced Features

### Custom Templates
Modify the `create_hugo_post()` function in `import_substack.py` to customize:
- Frontmatter fields
- Content formatting
- File organization

### Automated Workflow
Set up a GitHub Action or cron job to:
1. Check for new Substack posts
2. Import them automatically
3. Commit to your Hugo repository

### Content Processing
Add markdown processing to:
- Convert HTML to markdown
- Optimize images
- Add internal links
- Apply consistent formatting

## 🎯 Tips for Best Results

1. **Review imported content**: Always check formatting after import
2. **Optimize images**: Compress and resize images for web
3. **Update internal links**: Link to other posts on your Hugo site
4. **Add Hugo features**: Use shortcodes, math rendering, etc.
5. **SEO optimization**: Ensure good titles, descriptions, and tags

## 🐛 Troubleshooting

- **Import fails**: Check file format and encoding (use UTF-8)
- **Broken formatting**: Review markdown conversion
- **Missing images**: Download and add images manually
- **Date issues**: Ensure dates are in YYYY-MM-DD format

## 📚 Resources

- [Hugo Documentation](https://gohugo.io/documentation/)
- [HugoBlox Docs](https://hugoblox.com/docs/)
- [Markdown Guide](https://www.markdownguide.org/)