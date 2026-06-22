import sqlite3
import os

DB_PATH = "data/raw/processed/database/news.db"

os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS articles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT,
    headline TEXT,
    image_url TEXT,
    image_path TEXT,
    article_url TEXT UNIQUE,
    published_at TEXT,
    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    score REAL,
    label TEXT
)
""")

conn.commit()
conn.close()

print("Database initialized successfully.")