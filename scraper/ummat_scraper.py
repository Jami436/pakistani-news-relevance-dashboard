import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

from backend.crud import insert_article
from scraper.utils import download_image

translator = GoogleTranslator(source="urdu", target="en")


def scrape_ummat():

    url = "https://ummat.net"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Map article URL -> image URL
    image_by_url = {}

    for a in soup.find_all("a", href=True):

        img = a.find("img")

        if img:
            image_url = img.get("src") or img.get("data-src")

            if image_url:
                image_by_url.setdefault(a["href"], image_url)

    articles = []
    seen_urls = set()

    for heading in soup.find_all(["h1", "h2", "h3", "h4"]):

        link = heading.find("a", href=True)

        if not link:
            continue

        headline = (
            link.get("title")
            or link.get("alt")
            or link.get_text(strip=True)
        )

        article_url = link.get("href")

        if not headline or not article_url:
            continue

        if article_url in seen_urls:
            continue

        seen_urls.add(article_url)

        try:
            english = translator.translate(headline)
            time.sleep(0.3)

        except Exception:
            english = headline

        image_url = image_by_url.get(article_url)

        image_path = None

        if image_url:
            image_path = download_image(
                image_url,
                f"ummat_article_{len(articles)+1}.webp"
            )

        articles.append({
            "source": "Ummat",
            "headline": english,
            "article_url": article_url,
            "image_url": image_url,
            "image_path": image_path
        })

    for article in articles[:10]:
        print(article)

    # Save to database
    for article in articles:
        insert_article(article)

    # Save CSV
    df = pd.DataFrame(articles)

    df.to_csv(
        "data/raw/ummat_articles.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print("CSV file created successfully.")
    print(f"\nTotal Articles Found: {len(articles)}")


if __name__ == "__main__":
    scrape_ummat()