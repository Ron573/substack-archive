import feedparser

rss_url = "https://ronaldjbotelho.substack.com/feed"
feed = feedparser.parse(rss_url)

for entry in feed.entries:
    print(f"Title: {entry.title}")
    print(f"Published: {entry.published}")
    print(f"Link: {entry.link}\n")

