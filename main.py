from models.basefigure import BaseFigure
from models.gamefield import GameField
from models.rook import Rook
from models.king import King
from models.bishop import Bishop
from models.queen import Queen
from models.pawn import Pawn

chess_field = GameField()

chess_field.print_field()

p = Pawn('6d', 'pawn', 'p')
print(p._available_moves(chess_field))