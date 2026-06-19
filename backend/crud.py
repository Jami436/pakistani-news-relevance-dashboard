import sqlite3

def insert_article(article):

    conn = sqlite3.connect("data/raw/processed/database/news.db")
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO articles(
            source,
            headline,
            image_url,
            article_url
        )
        VALUES (?, ?, ?, ?)
        """, (
            "Dawn",
            article["headline"],
            article["image_url"],
            article["article_url"]
        ))

        conn.commit()

    except sqlite3.IntegrityError:
        pass

    conn.close()