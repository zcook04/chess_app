import sys
import os
import uuid
import json

## Temp for testing.
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..')))

from lib.pieces.ChessPiece import ChessPiece
from lib.pieces.Bishop import WhiteBishop
from lib.pieces.Bishop import BlackBishop
from lib.pieces.King import WhiteKing
from lib.pieces.King import BlackKing
from lib.pieces.Knight import WhiteKnight
from lib.pieces.Knight import BlackKnight
from lib.pieces.Pawn import WhitePawn
from lib.pieces.Pawn import BlackPawn
from lib.pieces.Queen import WhiteQueen
from lib.pieces.Queen import BlackQueen
from lib.pieces.Rook import WhiteRook
from lib.pieces.Rook import BlackRook

class Coordinates:
    def __init__(self):
        self.coordinates = self.initialize_coordinates()
        
    def initialize_coordinates(self) -> dict:
        """Returns a dictionary of each square in chess notation as a
        key with the board coordinates as the value: i.e., a1: (0, 0)

        Returns:
            dict: chess algebraic notation mapped to board coordinates.
        """
        numbers = [x for x in range(1, 9)]
        letters = [chr(i) for i in range(ord('a'), ord('h')+1)]

        return {(letter + str(number)): (number-1, ord(letter) - ord('a'))
                for number in numbers for letter in letters}


class ChessSquare(Coordinates):
    def __init__(self, location: tuple, piece: ChessPiece|None):
        super().__init__()
        self.location = location
        self.name = ''.join([k for k,v in self.coordinates.items() if v == location])
        self.piece = piece
        
    def __repr__(self):
        return self.name


class ChessGame(Coordinates):
    def __init__(self):
        super().__init__()
        self.id = uuid.uuid4()
        self.game_moves = []
        self.board = self.initialize_board()
        self.initialize_pieces()

        
    def __repr__(self):
        return json.dumps({
            'uuid': self.id,
            'game_moves': self.moves,
            'board': self.board,
        })



    def initialize_board(self) -> list[list[ChessSquare]]:
        """Returns a chessboard represented by a list of lists with
        None as placeholders for pieces.

        Returns:
            list[list]: A list of lists (8x8) containing either None or a ChessPiece
        """
        board = []
        for i in range(8):
            board.append([ChessSquare((i,j),  None) for j in range(8)])
            
        return board

    def place_piece(self, chess_piece: ChessPiece, chess_square: str) -> None:
        """Places a ChessPiece on the chess_square.

        Args:
            chess_piece (ChessPiece): A class inheriting from ChessPiece.
            chess_square (str): chess algebraic notation ie. "a1"
        """
        self.board[self.coordinates[chess_square][0]][self.coordinates[chess_square][1]].piece = chess_piece

    def initialize_pieces(self) -> None:
        """Place chess pieces on their starting squares."""
        white_pawn_squares = ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']
        black_pawn_squares = ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']
        for square in white_pawn_squares:
            self.place_piece(WhitePawn(self.coordinates[square]), square)
        for square in black_pawn_squares:
            self.place_piece(BlackPawn(self.coordinates[square]), square)
        self.place_piece(WhiteRook(self.coordinates['a1']), 'a1')
        self.place_piece(WhiteRook(self.coordinates['h1']), 'h1')
        self.place_piece(BlackRook(self.coordinates['a8']), 'a8')
        self.place_piece(BlackRook(self.coordinates['h8']), 'h8')
        self.place_piece(WhiteKnight(self.coordinates['b1']), 'b1')
        self.place_piece(WhiteKnight(self.coordinates['g1']), 'g1')
        self.place_piece(BlackKnight(self.coordinates['b8']), 'b8')
        self.place_piece(BlackKnight(self.coordinates['g8']), 'g8')
        self.place_piece(WhiteBishop(self.coordinates['c1']), 'c1')
        self.place_piece(WhiteBishop(self.coordinates['f1']), 'f1')
        self.place_piece(BlackBishop(self.coordinates['c8']), 'c8')
        self.place_piece(BlackBishop(self.coordinates['f8']), 'f8')
        self.place_piece(WhiteKing(self.coordinates['e1']), 'e1')
        self.place_piece(BlackKing(self.coordinates['e8']), 'e8')
        self.place_piece(WhiteQueen(self.coordinates['d1']), 'd1')
        self.place_piece(BlackQueen(self.coordinates['d8']), 'd8')

    def remove_piece(self, chess_square: str) -> None:
        """Removes a piece from the chessboard.

        Args:
            chess_square (str): chess algebreic notation ie. "a1"
        """
        row, column = self.coordinates[chess_square.lower()]
        self.board[row][column] = None

    def square(self, chess_square: str) -> ChessPiece | None:
        """Returns a ChessPiece if coordinates is occupied otherwise returns None

        Args:
            chess_square (str): chess algebreic notation ie. "a1"

        Returns:
            ChessPiece | None: returns class inheriting from ChessPiece | None.
        """
        row, column = self.coordinates[chess_square.lower()]
        if self.board[row][column]:
            return self.board[row][column]

    def move_piece(self, starting_square: str, ending_square: str) -> None:
        """Moves a piece from a starting square to ending square if
        piece exists at the starting square and is a legal move.

        Args:
            starting_square (str): chess algebreic notation ie. 'a1'
            ending_square (str): chess algebreic notation ie. 'a1'
        """
        piece_to_move = self.square(starting_square).piece
        if not piece_to_move:
            return
        if piece_to_move.is_legal_move(self.board, self.coordinates[ending_square]):            
            self.remove_piece(ending_square)
            self.remove_piece(starting_square)
            self.place_piece(piece_to_move, ending_square)
            

        
if __name__ == '__main__':
    from pprint import pprint
    game = ChessGame()
    pprint(game.board)