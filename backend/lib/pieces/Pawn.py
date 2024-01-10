if __name__ == "__main__":
    from ChessPiece import ChessPiece
else:
    from lib.pieces.ChessPiece import ChessPiece


class Pawn(ChessPiece):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.name = 'pawn'
        self.has_moved = False
        
class WhitePawn(Pawn):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.color = 'white'
        
    def __repr__(self):
        return '-wP-'

    def get_valid_moves(self, game_board: list[list[ChessPiece]]) -> list[tuple]:
        valid_moves = set()
        x, y = self.position
        if not self.has_moved:
            valid_moves.add((x+2, y))
            valid_moves.add((x+1, y))
        # Can Move Forward One Square
        if x+1 <= 7:
            if game_board[x+1][y] is None:
                valid_moves.add(( x+1, y ))
        # Can Capture Diag Left One Square
        if x+1 <=7 and y-1 >= 0:
            occupying_piece = game_board[ x+1 ][ y-1 ]
            if occupying_piece is not None:
                if occupying_piece.is_capturable:
                    valid_moves.add(( x+1, y-1 ))
        # Can Capture Diag Right One Square
        if x+1 <= 7 and y+1 <= 7:
            occupying_piece = game_board[x+1][y+1]
            if occupying_piece is not None:
                if occupying_piece.is_capturable:
                    valid_moves.add(( x+1, y+1 ))
        return valid_moves

    
class BlackPawn(Pawn):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.color = 'black'
        
    def __repr__(self):
        return '-bP-'
        
    def get_valid_moves(self, game_board: list[list]) -> list[tuple]:
        valid_moves = set()
        x, y = self.position
        if not self.has_moved:
            valid_moves.add((x-2, y))
            valid_moves.add((x-2, y))
        if x-1 >= 0:
            if game_board[x-1][y] is None:
                valid_moves.add(( x-1, y ))
        if x-1 >= 0 and y-1 >= 0:
            occupying_piece = game_board[ x-1 ][ y-1 ]
            if occupying_piece is not None:
                if occupying_piece.is_capturable:
                    valid_moves.add(( x-1, y-1 ))
        if x-1 >= 0 and y+1 <= 7:
            occupying_piece = game_board[x-1][y+1]
            if occupying_piece is not None:
                if occupying_piece.is_capturable:
                    valid_moves.add(( x-1, y+1 ))
        return valid_moves