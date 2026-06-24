from fastapi import APIRouter
from backend.crud import get_stats

router = APIRouter()

@router.get("/stats")
def stats():

    return get_stats()