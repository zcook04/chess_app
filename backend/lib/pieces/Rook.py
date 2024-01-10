if __name__ == "__main__":
    from ChessPiece import ChessPiece
else:
    from lib.pieces.ChessPiece import ChessPiece


class Rook(ChessPiece):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.name = 'rook'
        
    def get_valid_moves(self, board: list[list]) -> list[tuple]:
    # def get_rook_moves(board, start_row, start_col):
    # Define the possible directions for a rook (up, down, left, right)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        start_row = self.position[0]
        start_col = self.position[1]
        
        def is_valid_move(row, col):
            # Check if the move is within the bounds of the chessboard
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def explore_moves(row, col):
            valid_moves = []
            for direction in directions:
                new_row, new_col = row + direction[0], col + direction[1]
                while is_valid_move(new_row, new_col) and board[new_row][new_col] is None:
                    valid_moves.append((new_row, new_col))
                    new_row, new_col = new_row + direction[0], new_col + direction[1]
                if is_valid_move(new_row, new_col) and board[new_row][new_col] is not None:
                    if board[new_row][new_col].is_capturable and board[new_row][new_col].color != self.color:
                        valid_moves.append((new_row, new_col))
            return valid_moves

        return explore_moves(start_row, start_col)

   
class WhiteRook(Rook):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.color = 'white'
        
    def __repr__(self):
        return '-wR-'
        

    
class BlackRook(Rook):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.color = 'black'
        
    def __repr__(self):
        return '-bR-'