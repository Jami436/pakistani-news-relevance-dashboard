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
            image_path,
            article_url
        )
        VALUES (?, ?, ?, ?, ?)
        """, (
            article.get("source", "Unknown"),
            article["headline"],
            article.get("image_url"),
            article.get("image_path"),
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

    cursor.execute("""
    SELECT *
    FROM articles
    """)

    articles = cursor.fetchall()

    conn.close()

    return articles


def get_article_by_id(article_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM articles
    WHERE id = ?
    """, (article_id,))

    article = cursor.fetchone()

    conn.close()

    return article


def get_articles_by_source(source):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM articles
    WHERE source = ?
    """, (source,))

    articles = cursor.fetchall()

    conn.close()

    return articles


def get_stats():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM articles
    """)

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