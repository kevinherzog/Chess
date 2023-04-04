from enum import Enum

def main():
    startGame()

def startGame():
    board, dict = generateBoard()
    pass


# Generating the game board 
def generateBoard():
    # Initialize an empty chess board
    chess_board = [['' for _ in range(8)] for _ in range(8)]

    # Map the notation of each square to its corresponding index in the board list
    square_to_index = {}
    for i in range(8):
        for j in range(8):
            square_to_index[chr(j+97)+str(8-i)] = (i,j)

    # Place the pieces based on their notations
    pieces = {
        'R': ['a1', 'h1'], 'N': ['b1', 'g1'], 'B': ['c1', 'f1'], 
        'Q': ['d1'], 'K': ['e1'], 'P': ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'], 
        'r': ['a8', 'h8'], 'n': ['b8', 'g8'], 'b': ['c8', 'f8'], 
        'q': ['d8'], 'k': ['e8'], 'p': ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']
    }

    for piece, squares in pieces.items():
        for square in squares:
            i, j = square_to_index[square]
            chess_board[i][j] = (piece, square)

    return chess_board, square_to_index

def checkAllowedMoves(Piece):
    pass

class Piece:
    def __init__(self, colour, position, pieceType):
        self.Colour = colour
        self.Position = position
        self.PieceType = pieceType

    def getColour(self):
        return self.Colour.name
    def getPosition(self):
        return self.Position
    def getType(self):
        return self.PieceType.name
    def getInfo(self):
        print(str(self.Colour.name) + " " + str(self.PieceType.name) + " has a value of: " + str(self.PieceType.value))


class Colour(Enum):
    WHITE = 0
    BLACK = 1

class PieceType(Enum):
    KING = 100
    QUEEN = 9
    ROOK = 5
    BISHOP = 3
    KNIGHT = 3
    PAWN = 1

if __name__ == "__main__":
    main()
