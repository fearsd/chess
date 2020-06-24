from models import *

chess_field = GameField()

chess_field.print_field()

r = Rook('5d', 'rook', 'R')

print(r._available_moves(chess_field))