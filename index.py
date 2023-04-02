from enum import Enum

def main():
    print("Hello World!")
    blackKing = Piece(Colour.BLACK, "h4", PieceType.KING)
    blackKing.getInfo()

class Piece:
    def __init__(self, Colour, Position, PieceType):
        self.Colour = Colour
        self.Position = Position
        self.PieceType = PieceType
        pass

    def getColour(self):
        return self.Colour.name
    def getPosition(self):
        return self.Position
    def getType(self):
        return self.PieceType.name
    def getInfo(self):
        print(str(self.Colour.name) + " " + str(self.PieceType.name))


class Colour(Enum):
    WHITE = 0
    BLACK = 1

class PieceType(Enum):
    KING = 0
    QUEEN = 1
    ROOK = 2
    BISHOP = 3
    HORSE = 4
    PAWN = 5

if __name__ == "__main__":
    main()
