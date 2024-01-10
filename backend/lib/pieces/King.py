if __name__ == "__main__":
    from ChessPiece import ChessPiece
else:
    from lib.pieces.ChessPiece import ChessPiece


class King(ChessPiece):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.name = 'king'
        self.is_capturable = False
        self.in_check = False

    def get_valid_moves(self, board: list[list]) -> list[tuple]:
        # Define the possible directions for a king (including diagonals)
        start_row, start_col = self.position
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0),  # Horizontal and vertical
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Diagonals
        ]

        def is_valid_move(row, col):
            # Check if the move is within the bounds of the chessboard
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        valid_moves = []
        for direction in directions:
            new_row, new_col = start_row + direction[0], start_col + direction[1]
            if is_valid_move(new_row, new_col) and (board[new_row][new_col] is None or
                                                    (board[new_row][new_col].is_capturable and board[new_row][new_col].color != self.color)):
                valid_moves.append((new_row, new_col))

        return valid_moves
    
class WhiteKing(King):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.color = 'white'
        
    def __repr__(self):
        return '-wK-'
    
    
class BlackKing(King):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.color = 'black'
        
    def __repr__(self):
        return '-bK-'