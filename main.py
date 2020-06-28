from models.basefigure import BaseFigure
from models.gamefield import GameField
from models.rook import Rook
from models.king import King
from models.bishop import Bishop
from models.queen import Queen

chess_field = GameField()

chess_field.print_field()

q = Queen('5d', 'queen', 'Q')
print(q._available_moves(chess_field))