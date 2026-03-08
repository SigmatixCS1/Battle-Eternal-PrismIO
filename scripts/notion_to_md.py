"""
Notion HTML → Clean Markdown Converter
Converts SingleFile browser-saved Notion pages to machine-readable Markdown.
Output: knowledge_base/notion/
"""

import os
import re
import sys
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# Paths
NOTION_DIR = Path(r"C:\Users\Sigma\Battle Eternal Notion")
OUTPUT_DIR = Path(r"C:\Users\Sigma\Battle Eternal PrismIO\knowledge_base\notion")


def clean_filename(html_filename: str) -> str:
    """Strip timestamps and Notion suffix from filename, produce clean .md name."""
    name = html_filename
    # Remove .html extension
    name = re.sub(r'\.html$', '', name, flags=re.IGNORECASE)
    # Remove the timestamp pattern: (M_D_YYYY HH：MM：SS AM/PM)
    name = re.sub(r'\s*\(\d+_\d+_\d+\s+\d+[：:]\d+[：:]\d+\s+[AP]M\)', '', name)
    # Remove " ｜ Notion" or " | Notion" suffix
    name = re.sub(r'\s*[｜|]\s*Notion', '', name)
    # Replace fullwidth colons and other problematic chars
    name = name.replace('：', '-').replace(':', '-').replace('"', '').replace('"', '')
    name = name.replace('/', '-').replace('\\', '-').replace('?', '').replace('*', '')
    name = name.replace('<', '').replace('>', '').replace('|', '-')
    # Collapse multiple spaces/dashes
    name = re.sub(r'\s+', ' ', name).strip()
    name = re.sub(r'-{2,}', '-', name)
    return name + '.md'


def extract_content(soup: BeautifulSoup) -> str:
    """Extract the main page content from a Notion HTML page."""
    # Remove non-content elements
    for tag in soup.find_all(['script', 'style', 'svg', 'img', 'link', 'meta']):
        tag.decompose()

    # Remove Notion UI elements
    selectors_to_remove = [
        'notion-sidebar', 'notion-print-ignore', 'sf-hidden',
        'sticky-portal', 'notion-record-icon', 'notion-sidebar-switcher',
        'notion-close-sidebar',
    ]
    for tag in soup.find_all('div', class_=lambda c: c and any(
        x in c for x in selectors_to_remove
    )):
        tag.decompose()

    # Remove buttons
    for tag in soup.find_all('button'):
        tag.decompose()

    # Primary: notion-page-content div
    page_content = soup.find('div', class_='notion-page-content')
    if page_content:
        return page_content

    # Fallback: layout-content inside main
    main = soup.find('main')
    if main:
        layout = main.find('div', class_='layout-content')
        if layout:
            return layout
        return main

    # Last resort
    return soup.body or soup


def convert_to_markdown(content_element, title: str) -> str:
    """Convert extracted HTML content to clean Markdown."""
    raw = md(
        str(content_element),
        heading_style='ATX',
        strip=['img', 'svg', 'button'],
    )

    # Clean up
    # Remove excessive blank lines
    raw = re.sub(r'\n{3,}', '\n\n', raw)
    # Remove leading/trailing whitespace per line while preserving structure
    lines = raw.split('\n')
    cleaned_lines = []
    for line in lines:
        # Don't strip indentation from list items or code blocks
        if line.startswith('    ') or line.startswith('\t'):
            cleaned_lines.append(line)
        else:
            cleaned_lines.append(line.rstrip())
    raw = '\n'.join(cleaned_lines).strip()

    # Remove any leftover "Add icon/cover/comment" noise
    raw = re.sub(r'^Add icon\s*\n?', '', raw)
    raw = re.sub(r'^Add cover\s*\n?', '', raw)
    raw = re.sub(r'^Add comment\s*\n?', '', raw)

    # Prepend title as H1
    return f"# {title}\n\n{raw}"


def get_title(soup: BeautifulSoup, filename: str) -> str:
    """Extract page title from the HTML."""
    title_tag = soup.find('title')
    if title_tag:
        title = title_tag.get_text().split('|')[0].strip()
        # Remove " Notion" if it slipped through
        title = re.sub(r'\s*Notion\s*$', '', title).strip()
        if title:
            return title

    # Fallback: derive from filename
    return clean_filename(filename).replace('.md', '')


def process_file(filepath: Path) -> tuple[str, str, int]:
    """Process a single Notion HTML file. Returns (output_name, title, char_count)."""
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        soup = BeautifulSoup(f, 'html.parser')

    title = get_title(soup, filepath.name)
    content_el = extract_content(soup)
    markdown = convert_to_markdown(content_el, title)

    output_name = clean_filename(filepath.name)
    output_path = OUTPUT_DIR / output_name

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown)

    return output_name, title, len(markdown)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    html_files = sorted(NOTION_DIR.glob('*.html'))
    if not html_files:
        print(f"No HTML files found in {NOTION_DIR}")
        sys.exit(1)

    print(f"Converting {len(html_files)} Notion HTML files → Markdown\n")
    total_chars = 0
    results = []

    for filepath in html_files:
        try:
            output_name, title, char_count = process_file(filepath)
            total_chars += char_count
            results.append((output_name, title, char_count))
            print(f"  ✓ {output_name} ({char_count:,} chars)")
        except Exception as e:
            print(f"  ✗ {filepath.name}: {e}")

    print(f"\n{'='*60}")
    print(f"Converted: {len(results)}/{len(html_files)} files")
    print(f"Total output: {total_chars:,} chars ({total_chars/1024:.1f} KB)")
    print(f"Output dir: {OUTPUT_DIR}")


if __name__ == '__main__':
    main()
