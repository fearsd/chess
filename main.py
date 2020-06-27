from models.basefigure import BaseFigure
from models.gamefield import GameField
from models.rook import Rook
from models.king import King
from models.bishop import Bishop

chess_field = GameField()

chess_field.print_field()

b = Bishop('5d', 'bishop', 'B')
print(b._available_moves(chess_field))