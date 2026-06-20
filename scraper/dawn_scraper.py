import requests
from bs4 import BeautifulSoup
from backend.crud import insert_article


def scrape_dawn():

    url = "https://www.dawn.com"

    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch Dawn")
        return []

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

        article_data = {
            "headline": headline,
            "article_url": article_url,
            "image_url": image_url
        }

        articles.append(article_data)

        insert_article(article_data)

    print(f"Dawn: {len(articles)} articles processed")

    return articles


if __name__ == "__main__":
    scrape_dawn()