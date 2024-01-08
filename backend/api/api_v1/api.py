from fastapi import APIRouter
from api.api_v1.endpoints import game

router = APIRouter()
router.include_router(game.router, prefix="/game", tags=["game"])