from .basefigure import BaseFigure

class King(BaseFigure):

    def perfome_move(self, field, coords_to):
        available_coords_to_move = self._available_moves(field)
        if coords_to not in available_coords_to_move:
            return 'Not available move'
        else:
            self.coord = coords_to
            return 'Moved!'

    def _available_moves(self, field):

        moves = []
        try:
            if not field.field[str(int(self.coord[0]) - 1) + self.coord[1]].team == self.team and not int(self.coord[0]) - 1 == 0:
                moves.append(str(int(self.coord[0]) - 1) + self.coord[1])
        except AttributeError:
            moves.append(str(int(self.coord[0]) - 1) + self.coord[1])

        try:
            if not field.field[str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) + 1)].team == self.team and not int(self.coord[0]) - 1 == 0:
                moves.append(str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) + 1))
        except AttributeError:
            moves.append(str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) + 1))

