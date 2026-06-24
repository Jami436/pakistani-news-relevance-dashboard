from pydantic import BaseModel
from typing import Optional

class Article(BaseModel):
    id: int
    source: str
    headline: str
    image_url: Optional[str]
    image_path: Optional[str]
    article_url: str
    published_at: Optional[str]
    scraped_at: Optional[str]
    score: Optional[str]
    label: Optional[str]

class Stats(BaseModel):
    total_articles: int
    source_breakdown: list