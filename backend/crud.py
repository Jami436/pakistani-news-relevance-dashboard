import sqlite3

DB_PATH = "data/raw/processed/database/news.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def insert_article(article):

    conn = get_connection()
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

    finally:
        conn.close()


def get_all_articles():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM articles")

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_article_by_id(article_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM articles WHERE id = ?",
        (article_id,)
    )

    row = cursor.fetchone()

    conn.close()

    return row


def get_stats():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM articles")

    total_articles = cursor.fetchone()[0]

    cursor.execute("""
    SELECT source, COUNT(*)
    FROM articles
    GROUP BY source
    """)

    source_breakdown = cursor.fetchall()

    conn.close()

    return {
        "total_articles": total_articles,
        "source_breakdown": source_breakdown
    }