import feedparser
import datetime

feed = feedparser.parse('https://ronaldjbotelho.substack.com/feed')

header = '''<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1.0'>
  <title>Ron Botelho – Substack Archive</title>
  <style>
    body { font-family: Georgia, serif; background-color: #0e0e0e; color: #f0f0f0; max-width: 960px; margin: 0 auto; padding: 2em; line-height: 1.6; }
    h1, h2 { text-align: center; color: #ffffff; }
    .article-list { margin-top: 2em; }
    .article-item { margin-bottom: 1.5em; }
    .article-item a { color: #3fa9f5; font-size: 1.1em; text-decoration: none; }
    .article-item a:hover { text-decoration: underline; }
    .date { display: block; color: #aaa; font-size: 0.9em; margin-top: 0.3em; }
    .footer { text-align: center; margin-top: 3em; font-size: 0.85em; color: #666; }
  </style>
</head>
<body>
  <h1>Ronald J. Botelho</h1>
  <h2>Substack Article Archive</h2>
  <p style='text-align:center; font-size: 1em; color: #ccc;'>
    <strong>Ronald J. Botelho</strong> is a Ph.D. student in Complex Sciences at Binghamton University.  
    His research draws from intelligence analysis, systems science, and information theory to expose 
    systemic threats to democracy and trace the anatomy of disinformation in modern governance.
  </p>
  <div class='article-list'>
'''

footer = '''  </div>
  <div class='footer'>
    <p>All content &copy; Ronald J. Botelho | <a href='https://ronaldjbotelho.substack.com'>Back to Substack</a></p>
  </div>
</body>
</html>'''

items = ''
for entry in feed.entries:
    title = entry.title
    link = entry.link
    date = datetime.datetime(*entry.published_parsed[:6]).strftime('%B %d, %Y')
    items += f"<div class='article-item'><a href='{link}'>{title}</a><span class='date'>{date}</span></div>\n"

with open("index.html", "w") as f:
    f.write(header + items + footer)

