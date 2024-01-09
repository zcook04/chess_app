if __name__ == "__main__":
    from ChessPiece import ChessPiece
else:
    from lib.pieces.ChessPiece import ChessPiece


class Pawn(ChessPiece):
    def __init__(self, position: tuple, color: str):
        super().__init__(position, color)
        self.name = 'pawn'
        self.has_moved = False

    def move(self, position):
        '''Move the chess piece to target position if legal.'''
        pass

    def update_valid_moves(self):
        '''Return all available moves as a list'''
        valid_moves = []
        row, column = self.position
        if not self.has_moved:
            valid_moves.append((row, column+1), (row, column+2))

        return valid_moves
