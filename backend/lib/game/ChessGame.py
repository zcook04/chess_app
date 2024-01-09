import sys
import os

## Temp for testing.
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..')))

from lib.pieces.ChessPiece import ChessPiece
from lib.pieces.Bishop import Bishop
from lib.pieces.King import King
from lib.pieces.Knight import Knight
from lib.pieces.Pawn import Pawn
from lib.pieces.Queen import Queen
from lib.pieces.Rook import Rook



class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.coordinates = self.initialize_coordinates()
        self.initialize_pieces()

    def initialize_board(self) -> list[list]:
        '''Returns a chessboard represented by a list of lists with
        None as placeholders for pieces.'''
        board = []
        for _ in range(8):
            board.append([None for _ in range(8)])
        return board

    def initialize_coordinates(self) -> dict:
        '''Returns a dictionary of each square in chess notation as a
        key with the board coordinates as the value: i.e., a1: (0, 0)'''
        numbers = [x for x in range(1, 9)]
        letters = [chr(i) for i in range(ord('a'), ord('h')+1)]
        return {(letter + str(number)): (ord(letter) - ord('a'), 8 - number)
                for number in numbers for letter in letters}

    def initialize_pieces(self) -> None:
        '''Place chess pieces on their starting squares.'''
        white_pawn_squares = ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']
        black_pawn_squares = ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']
        for square in white_pawn_squares:
            self.place_piece(Pawn(self.coordinates[square], 'w'), square)
        for square in black_pawn_squares:
            self.place_piece(Pawn(self.coordinates[square], 'b'), square)
        self.place_piece(Rook('a1', 'w'), 'a1')
        self.place_piece(Rook('h1', 'w'), 'h1')
        self.place_piece(Rook('a8', 'b'), 'a8')
        self.place_piece(Rook('h8', 'b'), 'h8')
        self.place_piece(Knight('b1', 'w'), 'b1')
        self.place_piece(Knight('g1', 'w'), 'g1')
        self.place_piece(Knight('b8', 'b'), 'b8')
        self.place_piece(Knight('g8', 'b'), 'g8')
        self.place_piece(Bishop('c1', 'w'), 'c1')
        self.place_piece(Bishop('f1', 'w'), 'f1')
        self.place_piece(Bishop('c8', 'b'), 'c8')
        self.place_piece(Bishop('f8', 'b'), 'f8')
        self.place_piece(King('e1', 'w'), 'e1')
        self.place_piece(King('e8', 'b'), 'e8')
        self.place_piece(Queen('d1', 'w'), 'd1')
        self.place_piece(Queen('d8', 'b'), 'd8')

    def place_piece(self, chess_piece: ChessPiece, chess_square: str) -> None:
        '''Places a ChessPiece on the square.  chess_square should be entered as
        a chess notation, ie a1, or d4.'''
        column, row = self.coordinates[chess_square.lower()]
        self.board[row][column] = chess_piece

    def remove_piece(self, chess_square: str) -> None:
        column, row = self.coordinates[chess_square.lower()]
        self.board[row][column] = None

    def occupying_piece(self, chess_square: str) -> ChessPiece | None:
        '''Returns a ChessPiece if coordinates is occupied otherwise returns None'''
        column, row = self.coordinates[chess_square.lower()]
        if self.board[row][column]:
            return self.board[row][column]

    def move_piece(self, starting_square, ending_square):
        '''Moves a piece from a starting square to ending square if
        piece exists at the starting square and is a legal move.'''
        piece_to_move = self.occupying_piece(starting_square)
        if not piece_to_move:
            return
        self.remove_piece(starting_square)
        self.place_piece(piece_to_move, ending_square)


game = ChessGame()
game.move_piece('a2', 'a4')
print(game.occupying_piece('a5').name)
