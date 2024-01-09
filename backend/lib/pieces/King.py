if __name__ == "__main__":
    from ChessPiece import ChessPiece
else:
    from lib.pieces.ChessPiece import ChessPiece


class King(ChessPiece):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.name = 'king'

    
class WhiteKing(King):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.color = 'white'
        
    def get_valid_moves(self, game_board: list[list]) -> list[tuple]:
        row, col = self.position
        return []
    
class BlackKing(King):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.color = 'black'
        
    def get_valid_moves(self, game_board: list[list]) -> list[tuple]:
        row, col = self.position
        return []
