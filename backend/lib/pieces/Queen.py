if __name__ == "__main__":
    from ChessPiece import ChessPiece
else:
    from lib.pieces.ChessPiece import ChessPiece


class Queen(ChessPiece):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.name = 'queen'
    
    def get_valid_moves(self, board: list[list]) -> list[tuple]:
        # Define the possible directions for a queen (up, down, left, right, and diagonals)
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
            for i in range(1, max(len(board), len(board[0]))):  # Max possible distance on the board
                new_row, new_col = start_row + i * direction[0], start_col + i * direction[1]
                if is_valid_move(new_row, new_col):
                    if board[new_row][new_col].piece is None:
                        valid_moves.append((new_row, new_col))
                    elif board[new_row][new_col].piece.is_capturable and board[new_row][new_col].piece.color != self.color:
                        valid_moves.append((new_row, new_col))
                        break  # Stop exploring in this direction after capturing an opponent's piece
                    else:
                        break  # Stop exploring in this direction if the path is blocked by own piece
                else:
                    break  # Stop exploring if the move is out of bounds

        return valid_moves

   
class WhiteQueen(Queen):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.color = 'white'
        
    def __repr__(self):
        return '-wQ-'
    
class BlackQueen(Queen):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.color = 'black'
        
    def __repr__(self):
        return '-bQ-'
