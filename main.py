from models import *

chess_field = GameField()

chess_field.print_field()

r = Rook('2d', 'rook', 'R')

r.team = 'black'

print(r._available_moves(chess_field))