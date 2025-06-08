import os

article_dir = "articles"
readme_path = "README.md"

def get_articles():
    entries = []
    for root, dirs, files in os.walk(article_dir):
        for file in files:
            if file == "index.md":
                rel_path = os.path.join(root, file)
                date_folder = root.split("/")[-1]
                with open(rel_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    title_line = next((line for line in lines if line.startswith("# ")), None)
                    title = title_line[2:].strip() if title_line else "Untitled"
                    entries.append((date_folder, title, rel_path))
    return sorted(entries)

def update_readme(entries):
    with open(readme_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    start = next(i for i, line in enumerate(lines) if "## 🗂️ Article Index" in line)
    end = next(i for i in range(start + 1, len(lines)) if lines[i].startswith("---"))

    table = [
        "| Date       | Title | Folder |\n",
        "|------------|-------|--------|\n"
    ]
    for date, title, path in entries:
        folder = os.path.dirname(path)
        table.append(f"| {date} | [{title}](./{path}) | `{folder}/` |\n")

    new_lines = lines[:start+3] + table + lines[end:]
    with open(readme_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    articles = get_articles()
    update_readme(articles)
    print("✅ README.md updated with article index.")

