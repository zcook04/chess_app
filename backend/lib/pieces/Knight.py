if __name__ == "__main__":
    from ChessPiece import ChessPiece
else:
    from lib.pieces.ChessPiece import ChessPiece


class Knight(ChessPiece):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.name = 'knight'
        
    def get_valid_moves(self, board: list[list]) -> list[tuple]:
        # Define the possible knight moves as offsets from the current position
        start_row = self.position[0]
        start_col = self.position[1]
        knight_moves = [
            (1, 2), (1, -2), (-1, 2), (-1, -2),
            (2, 1), (2, -1), (-2, 1), (-2, -1)
        ]
        

        def is_valid_move(row, col):
            # Check if the move is within the bounds of the chessboard
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        valid_moves = []
        for move in knight_moves:
            new_row, new_col = start_row + move[0], start_col + move[1]
            if is_valid_move(new_row, new_col) and board[new_row][new_col].piece is None:
                valid_moves.append((new_row, new_col))
            elif is_valid_move(new_row, new_col) and board[new_row][new_col].piece is not None:
                if board[new_row][new_col].piece.is_capturable and board[new_row][new_col].piece.color != self.color:
                    valid_moves.append((new_row, new_col))

        return valid_moves
        
    
class WhiteKnight(Knight):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.color = 'white'

    def __repr__(self):
        return '-wN-'
    
    
class BlackKnight(Knight):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.color = 'black'
        
    def __repr__(self):
        return '-bN-'
