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

    def get_valid_moves(self, game_board: list[list]) -> list[tuple]:
        valid_moves = []
        row, col = self.position
        if row > 0: ## Move One Square Down
            if game_board[row-1][col] is None:
                valid_moves.append((row-1, col))
            if col < 7: ## Capture Diagnally Down/Right
                if game_board[row-1][col+1] is not None:
                    valid_moves.append((row-1, col+1))
            if col > 0: ## Capture Diagnally Down/Left
                if game_board[row-1][col-1] is not None:
                    valid_moves.append((col-1, row-1))
        ## Start of game, option to move two squares.
        if game_board[row-2][col] is None and not self.has_moved:
            valid_moves.append((row-2, col))
        return valid_moves

    
class BlackPawn(Pawn):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.color = 'black'
        
    def get_valid_moves(self, game_board: list[list]) -> list[tuple]:
        valid_moves = []
        row, col = self.position
        if row < 7: ## Move One Square Up
            if game_board[row+1][col] is None:
                valid_moves.append((row+1, col))
            if col < 7: ## Capture Diagnally Up/Right
                if game_board[row+1][col+1] is not None:
                    valid_moves.append((row+1, col+1))
            if col > 0: ## Capture Diagnally Up/Lef
                if game_board[row-1][col+1] is not None:
                    valid_moves.append((row+1, col-1))
        ## Start of game option to move two squares.
        if game_board[row+2][col] is None and self.has_moved == False:
            valid_moves.append((row+2, col)) 
        return valid_moves