from models.basefigure import BaseFigure
from models.gamefield import GameField
from models.rook import Rook

chess_field = GameField()

chess_field.print_field()

r = Rook('2d', 'rook', 'R')

r.team = 'white'

print(r._available_moves(chess_field))
print(r.perfome_move(chess_field, '6d'))
print(r.coord)
print(r._available_moves(chess_field))