class ChessPiece:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"{self.color} {self.name}"


class PieceFactory:
    _pieces = {}

    @classmethod
    def get_piece(cls, name, color):
        key = (name, color)
        if key not in cls._pieces:
            cls._pieces[key] = ChessPiece(name, color)
        return cls._pieces[key]



class ChessPieceOnBoard:
    def __init__(self, piece, position):
        self.piece = piece
        self.position = position

    def display(self):
        print(f"{self.piece} на позиції {self.position}")


if __name__ == "__main__":
    factory = PieceFactory()

    # створюємо фігури
    white_pawn1 = ChessPieceOnBoard(factory.get_piece("пішак", "білий"), "A2")
    white_pawn2 = ChessPieceOnBoard(factory.get_piece("пішак", "білий"), "B2")
    black_queen = ChessPieceOnBoard(factory.get_piece("ферзь", "чорний"), "D8")

    white_pawn1.display()
    white_pawn2.display()
    black_queen.display()


    print("Той самий об'єкт у пам'яті:", white_pawn1.piece is white_pawn2.piece)
