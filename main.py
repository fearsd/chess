from models.basefigure import BaseFigure
from models.gamefield import GameField
from models.rook import Rook
from models.king import King
from models.bishop import Bishop

chess_field = GameField()

chess_field.print_field()

r = Rook('5d', 'rook', 'R')
print(r._available_moves(chess_field))