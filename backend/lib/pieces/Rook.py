if __name__ == "__main__":
    from ChessPiece import ChessPiece
else:
    from lib.pieces.ChessPiece import ChessPiece


class Rook(ChessPiece):
    def __init__(self, position: tuple, color: str):
        super().__init__(position, color)
        self.name = 'rook'

    def move(self, position):
        print(f"Moving to {position}")

    def update_valid_moves(self):
        return []
