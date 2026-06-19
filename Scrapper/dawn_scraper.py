import requests
from bs4 import BeautifulSoup
from backend.crud import insert_article

url = "https://www.dawn.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

articles = []

for article in soup.find_all("article", class_="story"):

    link = article.find("a", href=True)

    if not link:
        continue

    headline = (
    link.get("title")
    or link.get("alt")
    or link.get_text(strip=True)
)
    article_url = link.get("href")

    image = article.find("img")
    image_url = image.get("src") if image else None

    if not headline:
        continue

    articles.append({
        "headline": headline,
        "article_url": article_url,
        "image_url": image_url
    })

for article in articles[:10]:
    print(article)

for article in articles:
    insert_article(article)

print(f"\nTotal Articles Found: {len(articles)}")

