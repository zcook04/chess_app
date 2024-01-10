from fastapi import APIRouter
from fastapi.responses import JSONResponse

from lib.game.ChessGame import ChessGame

router = APIRouter()

@router.get("/newgame")
async def game_endpoint():
    '''Setups a new game of chess to be played'''
    game = ChessGame()
    return JSONResponse(content={ "game_start": True, "board": game.board, "uuid": game.id })