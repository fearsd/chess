WHITE = (1, 2)
BLACK = (7, 8)

class BaseFigure:

    def __init__(self, coord, full_name, short_name):
        self.coord = coord
        self.team = self._set_team()
        self.full_name = full_name
        self.short_name = short_name

    def _set_team(self):
        if int(self.coord[0]) in WHITE:
            return 'white'
        elif int(self.coord[0]) in BLACK:
            return 'black'
        else:
            return 'white'

    def perfome_move(self, field, coords_to):
        available_coords_to_move = self._available_moves(field)
        if coords_to not in available_coords_to_move:
            return 'Not available move'
        else:
            self.coord = coords_to
            return 'Moved!'

    def __str__(self):
        return self.full_name + ' ' + self.coord