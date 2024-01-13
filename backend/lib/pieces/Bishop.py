if __name__ == "__main__":
    from ChessPiece import ChessPiece
else:
    from lib.pieces.ChessPiece import ChessPiece


class Bishop(ChessPiece):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.name = 'bishop'

    def get_valid_moves(self, board: list[list]) -> list[tuple]:
    # Define the possible directions for a bishop (left/up, left/down, right/up, right/down)
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        start_row = self.position[0]
        start_col = self.position[1]
        
        def is_valid_move(row, col):
            # Check if the move is within the bounds of the chessboard
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def explore_moves(row, col):
            valid_moves = []
            for direction in directions:
                new_row, new_col = row + direction[0], col + direction[1]
                while is_valid_move(new_row, new_col) and board[new_row][new_col].piece is None:
                    valid_moves.append((new_row, new_col))
                    new_row, new_col = new_row + direction[0], new_col + direction[1]
                if is_valid_move(new_row, new_col) and board[new_row][new_col].piece is not None:
                    ## Check if last move is a capturable piece of the other color.
                    if board[new_row][new_col].piece.is_capturable and board[new_row][new_col].piece.color != self.color:
                        valid_moves.append((new_row, new_col))
            return valid_moves

        return explore_moves(start_row, start_col)
    
class WhiteBishop(Bishop):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.color = 'white'
        
    def __repr__(self):
        return '-wB-'
    
class BlackBishop(Bishop):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.color = 'black'
        
    def __repr__(self):
        return '-bB-'