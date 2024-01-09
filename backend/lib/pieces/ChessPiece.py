from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, position, color):
        self._position = position
        self._color = color
        self._valid_moves = []

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

    @property
    def valid_moves(self) -> list:
        '''A list of valid moves the piece can make from its current position'''
        return self._valid_moves

    @abstractmethod
    def update_valid_moves(self, board_state: list[list]):
        pass

    @abstractmethod
    def move(self, position: tuple):
        pass


# Testing Only
if __name__ == "__main__":
    pass
