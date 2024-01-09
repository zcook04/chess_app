if __name__ == "__main__":
    from ChessPiece import ChessPiece
else:
    from lib.pieces.ChessPiece import ChessPiece


class Bishop(ChessPiece):
    def __init__(self):
        pass

    def move(self, position):
        print(f"Moving to {position}")

    def update_valid_moves(self):
        return []


if __name__ == '__main__':
    bishop = Bishop()
    print(bishop.current_position)
