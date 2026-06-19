import os
import sqlite3

# 1. Get the directory where test_scraper.py lives (E:\...\docs\tests)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Go up two levels to reach your main project root (E:\pakistani-news-relevance-dashboard)
project_root = os.path.dirname(os.path.dirname(current_dir))

# 3. Define the exact path to your database file
db_path = os.path.join(project_root, "data", "raw", "processed", "database", "news.db")

# 4. Crucial: Automatically create the folders if they don't exist yet
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# 5. Connect safely
conn = sqlite3.connect(db_path)

print("Successful")