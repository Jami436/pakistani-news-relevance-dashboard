import pandas as pd
import requests
from bs4 import BeautifulSoup
from backend.crud import insert_article
from scraper.utils import download_image

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

    image_path = None

    if image_url:
        image_path = download_image(
            image_url,
            f"article_{len(articles)+1}.webp"
        )

    articles.append({
        "source": "Dawn",
        "headline": headline,
        "article_url": article_url,
        "image_url": image_url,
        "image_path": image_path
    })

article_id = article_url.split("/")[-1]

image_path = download_image(
    image_url,
    f"{article_id}.webp"
)

for article in articles[:10]:
    print(article)

for article in articles:
    insert_article(article)

df = pd.DataFrame(articles)

df.to_csv(
    "data/raw/dawn_articles.csv",
    index=False,
    encoding="utf-8"
)

print("CSV file created successfully.")

print(f"\nTotal Articles Found: {len(articles)}")

print(f"\nTotal Articles Found: {len(articles)}")

