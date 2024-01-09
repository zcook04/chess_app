from pprint import pprint


class ChessBoard:
    def __init__(self):
        self.board = self.initialize_board()
        self.coordinates = self.initialize_coordinates()

    def initialize_board(self) -> list[list]:
        board = []
        for _ in range(8):
            board.append([None for _ in range(8)])
        return board

    def initialize_coordinates(self) -> dict:
        '''Returns a dictionary of each square in chess notation as a
        key with the board coordinates as the value: ie G1: (7,0)'''
        numbers = [x for x in range(1, 9)]
        letters = [chr(i) for i in range(ord('a'), ord('h')+1)]
        coord_map = {
            letter: number-1 for letter in letters for number in numbers}
        return {letter+str(number): (
            coord_map[letter], number-1
        ) for letter in letters for number in numbers}


chess_board = ChessBoard()
pprint(chess_board.board)
pprint(chess_board.coordinates)
