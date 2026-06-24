from fastapi import FastAPI

from backend.routers.articles import router as articles_router
from backend.routers.stats import router as status_router
from backend.routers.live import router as live_router

app  = FastAPI(
    title="Pakistani News Relevance Dashboard",
    version="1.0"
)

app.include_router(articles_router)
app.include_router(status_router)
app.include_router(live_router)

@app.get("/")
def root():

    return {
        "message":
        "Pakistani News Relevance Dashboard API"
    }