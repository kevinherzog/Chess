from enum import Enum

def main():
    print("Hello World!")
    blackKing = Piece(Colour.BLACK, "h4", PieceType.KING)
    blackKing.getInfo()
    blackKnight = Piece(Colour.BLACK, "h4", PieceType.KNIGHT)
    blackKnight.getInfo()
    blackBishop = Piece(Colour.BLACK, "h4", PieceType.BISHOP)
    blackBishop.getInfo()
    startGame()

def startGame():
    pass

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
    BISHOP = 3 # This may need to be changed in the future because it is not proper use of enumeration
    KNIGHT = 3
    PAWN = 1

if __name__ == "__main__":
    main()
