from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/newgame")
async def game_endpoint():
    '''Setups a new game of chess to be played'''
    return JSONResponse(content={"game_start": True})