from models.basefigure import BaseFigure
from models.gamefield import GameField
from models.rook import Rook
from models.king import King

chess_field = GameField()

chess_field.print_field()

k = King('4h', 'king', 'K')
print(k.team)
print(k._available_moves(chess_field))