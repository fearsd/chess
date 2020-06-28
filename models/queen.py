from .basefigure import BaseFigure

from .bishop import Bishop
from .rook import Rook

class Queen(BaseFigure):
    
    def _available_moves(self, field):

        moves = []

        diagonales = Bishop(self.coord, 'bishop', 'B')._available_moves(field)
        top_down_left_right = Rook(self.coord, 'rook', 'R')._available_moves(field)

        moves += diagonales.copy()
        moves += top_down_left_right.copy()

        return moves