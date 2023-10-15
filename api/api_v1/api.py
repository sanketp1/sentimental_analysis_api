from fastapi import APIRouter
# from endpoints import health

from .endpoints import health
from .endpoints import sentiment_analysis
api_router = APIRouter()

api_router.include_router(health.router, tags=["Health"])
api_router.include_router(sentiment_analysis.router, tags=["Sentiment Analysis"])