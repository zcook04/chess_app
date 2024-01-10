from __future__ import annotations
from abc import ABC, abstractmethod
import json


class ChessPiece(ABC):
    def __init__(self, position):
        self._position = position
        self.is_capturable = True
        
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
    def color(self):
        '''Color of the chess piece. Either "w" for white, or "b" for black.'''
        if hasattr(self, '_color'):
            return self._color
        return self._color

    @color.setter
    def color(self, value: str) -> str:
        if not isinstance(value, str):
            raise ValueError(
                "Piece color must be a string of either white || black")
        if value[0].lower() != 'w' and value[0].lower() != 'b':
            raise ValueError(
                "Piece color must be a string of either white || black")
        self._color = value[0]

    @abstractmethod
    def get_valid_moves(self, game_board:list[list]) ->list[tuple]:
        '''Returns a list of tuples containing valid moves the piece can make '''
        
    def initialize_coordinates(self) -> dict:
        """Returns a dictionary of each square in chess notation as a
        key with the board coordinates as the value: i.e., a1: (0, 0)

        Returns:
            dict: chess algebraic notation mapped to board coordinates.
        """
        numbers = [x for x in range(1, 9)]
        letters = [chr(i) for i in range(ord('a'), ord('h')+1)]
        
        return {(letter + str(number)): (ord(letter) - ord('a'), number - 1)
                for number in reversed(numbers) for letter in reversed(letters)}
    
    def is_legal_move(self, game_board: list[list[ChessPiece|None]], destination: tuple(int, int)) -> bool:
        """Returns whether the destination square is a legal move.

        Args:
            destination (str): Chess algebreic notation.
            occupying_piece (ChessPiece): ChessPiece at destination square, or None.

        Returns:
            bool: Destination square is a legal move.
        """
        return destination in self.get_valid_moves(game_board)