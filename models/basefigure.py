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

    def __str__(self):
        return self.full_name + ' ' + self.coord