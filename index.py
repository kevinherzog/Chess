# Imports
from aenum import Enum, NoAlias

# Functions 
def startGame():
    board = gameBoard()
    current_player = Colour.WHITE
    finished = False
    while not finished:
        print_board(board.chess_board)
        makeTurn(current_player, board)
    pass


def makeTurn(player, board):    
    move = input("What is your move? ")

    checkAllowedMoves(player, board, move)

    print(move)
    pass


def print_board(board):
    print("  " + " ".join(["{}".format(chr(i+97)) for i in range(8)]))
    for i in range(8):
        print("{} {}".format(8-i, " ".join([str(board[i][j]) if not board[i][j] else board[i][j].Symbol for j in range(8)])))
    print("  " + " ".join(["{}".format(chr(i+97)) for i in range(8)]))


def add_piece(self, piece):
    i, j = self.square_to_index[piece.Position]
    self.chess_board[i][j] = piece


def checkAllowedMoves(player, board, move):

    pass

def generatePieces():
    pieces = [
        Piece(Colour.WHITE, "e1", PieceType.KING),
        Piece(Colour.WHITE, "d1", PieceType.QUEEN),
        Piece(Colour.WHITE, "a1", PieceType.ROOK),
        Piece(Colour.WHITE, "h1", PieceType.ROOK),
        Piece(Colour.WHITE, "b1", PieceType.KNIGHT),
        Piece(Colour.WHITE, "g1", PieceType.KNIGHT),
        Piece(Colour.WHITE, "c1", PieceType.BISHOP),
        Piece(Colour.WHITE, "f1", PieceType.BISHOP),
        Piece(Colour.WHITE, "a2", PieceType.PAWN),
        Piece(Colour.WHITE, "b2", PieceType.PAWN),
        Piece(Colour.WHITE, "c2", PieceType.PAWN),
        Piece(Colour.WHITE, "d2", PieceType.PAWN),
        Piece(Colour.WHITE, "e2", PieceType.PAWN),
        Piece(Colour.WHITE, "f2", PieceType.PAWN),
        Piece(Colour.WHITE, "g2", PieceType.PAWN),
        Piece(Colour.WHITE, "h2", PieceType.PAWN),
        Piece(Colour.BLACK, "e8", PieceType.KING),
        Piece(Colour.BLACK, "d8", PieceType.QUEEN),
        Piece(Colour.BLACK, "a8", PieceType.ROOK),
        Piece(Colour.BLACK, "h8", PieceType.ROOK),
        Piece(Colour.BLACK, "b8", PieceType.KNIGHT),
        Piece(Colour.BLACK, "g8", PieceType.KNIGHT),
        Piece(Colour.BLACK, "c8", PieceType.BISHOP),
        Piece(Colour.BLACK, "f8", PieceType.BISHOP),
        Piece(Colour.BLACK, "a7", PieceType.PAWN),
        Piece(Colour.BLACK, "b7", PieceType.PAWN),
        Piece(Colour.BLACK, "c7", PieceType.PAWN),
        Piece(Colour.BLACK, "d7", PieceType.PAWN),
        Piece(Colour.BLACK, "e7", PieceType.PAWN),
        Piece(Colour.BLACK, "f7", PieceType.PAWN),
        Piece(Colour.BLACK, "g7", PieceType.PAWN),
        Piece(Colour.BLACK, "h7", PieceType.PAWN)
    ]
    return pieces

# Classes

class gameBoard():
    def __init__(self):
         # Initialize an empty chess board
        self.chess_board = [['' for _ in range(8)] for _ in range(8)]

        # Map the notation of each square to its corresponding index in the board list
        self.square_to_index = {}
        for i in range(8):
            for j in range(8):
                self.square_to_index[chr(j+97)+str(8-i)] = (i,j)

        pieces = generatePieces()

        for piece in pieces:
            add_piece(self, piece)

        pass

    pass

class MoveList:
    # TODO
    def __init__(self):

        pass
class Piece:
    def __init__(self, colour, position, pieceType):
        self.Colour = colour
        self.Position = position
        self.PieceType = pieceType
        match pieceType:
            case PieceType.PAWN if colour == Colour.WHITE:
                self.Symbol = "\u2659"
                pass
            case PieceType.BISHOP if colour == Colour.WHITE:
                self.Symbol = "\u2657"
                pass
            case PieceType.KNIGHT if colour == Colour.WHITE:
                self.Symbol = "\u2658"
                pass
            case PieceType.QUEEN if colour == Colour.WHITE:
                self.Symbol = "\u2655"
                pass
            case PieceType.KING if colour == Colour.WHITE:
                self.Symbol = "\u2654"
                pass
            case PieceType.ROOK if colour == Colour.WHITE:
                self.Symbol = "\u2656"
                pass
            case PieceType.ROOK if colour == Colour.BLACK:
                self.Symbol = "\u265C"
                pass
            case PieceType.PAWN if colour == Colour.BLACK:
                self.Symbol = "\u265F"
                pass
            case PieceType.BISHOP if colour == Colour.BLACK:
                self.Symbol = "\u265D"
                pass
            case PieceType.KNIGHT if colour == Colour.BLACK:
                self.Symbol = "\u265E"
                pass
            case PieceType.QUEEN if colour == Colour.BLACK:
                self.Symbol = "\u265B"
                pass
            case PieceType.KING if colour == Colour.BLACK:
                self.Symbol = "\u265A"
                pass

    def getColour(self):
        return self.Colour.name
    def getPosition(self):
        return self.Position
    def getType(self):
        return self.PieceType.name
    def getSymbol(self):
        return self.Symbol
    def getInfo(self):
        print(str(self.Colour.name) + " " + str(self.PieceType.name) + " has a value of: " + str(self.PieceType.value) + " and is on: " + str(self.Position))

class Colour(Enum):
    WHITE = 0
    BLACK = 1

class PieceType(Enum):

    _settings_ = NoAlias

    KING = 100
    QUEEN = 9
    ROOK = 5
    BISHOP = 3
    KNIGHT = 3
    PAWN = 1

# Main

def main():
    startGame()

if __name__ == "__main__":
    main()