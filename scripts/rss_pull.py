import feedparser
import os
import re
from datetime import datetime
from pathlib import Path

# === CONFIGURATION ===
FEED_URL = "https://ronaldjbotelho.substack.com/feed"
ARTICLES_DIR = "articles"
POST_FILENAME = "index.md"
MAX_ARTICLES = 100  # for full archive sync

# === UTILS ===
def sanitize_title(title):
    return re.sub(r'[^a-zA-Z0-9\-]', '', re.sub(r'\s+', '-', title.strip().lower()))

def fetch_and_parse():
    return feedparser.parse(FEED_URL)

def article_exists(slug):
    return Path(f"{ARTICLES_DIR}/{slug}/{POST_FILENAME}").exists()

def write_article(entry):
    published = datetime(*entry.published_parsed[:6]).strftime('%Y-%m-%d')
    title = entry.title.strip()
    slug = f"{published}-{sanitize_title(title)}"
    folder = Path(f"{ARTICLES_DIR}/{slug}")
    folder.mkdir(parents=True, exist_ok=True)
    content_path = folder / POST_FILENAME

    with open(content_path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"*Published: {published}*\n\n")
        f.write(entry.summary.replace('<p>', '').replace('</p>', '').strip())

    print(f"✓ Added: {title}")
    return slug

def main():
    feed = fetch_and_parse()
    if not feed.entries:
        print("⚠️ No entries found.")
        return

    new_articles = 0
    for entry in feed.entries[:MAX_ARTICLES]:
        title = entry.title
        published = datetime(*entry.published_parsed[:6]).strftime('%Y-%m-%d')
        slug = f"{published}-{sanitize_title(title)}"
        if not article_exists(slug):
            write_article(entry)
            new_articles += 1

    if new_articles == 0:
        print("✅ No new articles.")
    else:
        os.system("python3 generate_index.py")
        os.system("git add articles README.md")
        os.system("git commit -m 'Auto-import new Substack articles via RSS'")
        os.system("git push origin main")

if __name__ == "__main__":
    main()