from abc import ABC, abstractmethod
import json


class ChessPiece(ABC):
    def __init__(self, position):
        self._position = position
        self.is_capturable = True
        self.name = ""
        
    def __repr__(self):
        return json.dumps({
            'position': self.position,
            'is_capturable': self.is_capturable,
            'name': self.name,
            'color': self.color,
        })
        
    @property
    def position(self):
        '''Position of the piece on the chessboard represented by a coordinate tuple (int, int)'''
        if hasattr(self, '_position'):
            return self._position

    @position.setter
    def position(self, value: tuple) -> tuple:
        if not self.valid_position():
            return tuple()
        self.update_valid_moves()
        self._position = value

    @position.deleter
    def position(self):
        del self._x

    @property
    def piece_color(self):
        '''Color of the chess piece. Either "w" for white, or "b" for black.'''
        if hasattr(self, '_color'):
            return self._color
        return self._color

    @piece_color.setter
    def piece_color(self, value: str) -> str:
        if not isinstance(value, str):
            raise ValueError(
                "Piece color must be a string of either white || black")
        if value[0].lower() != 'w' or value[0].lower() != 'b':
            raise ValueError(
                "Piece color must be a string of either white || black")
        self._piece_color = value[0]

    @abstractmethod
    def get_valid_moves(self, game_board:list[list]) ->list[tuple]:
        '''Returns a list of tuples containing valid moves the piece can make '''
        pass