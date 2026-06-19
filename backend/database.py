import sqlite3
import os

conn = sqlite3.connect("data/raw/processed/database/news.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS articles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT,
    headline TEXT,
    subheadline TEXT,
    image_url TEXT,
    article_url TEXT UNIQUE,
    published_at TEXT,
    scraped_at TEXT,
    score REAL,
    label TEXT
)
""")

conn.commit()
conn.close()

print("Database Initialized")

