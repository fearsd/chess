from .basefigure import BaseFigure

class Bishop(BaseFigure):

    def _available_moves(self, field):
        moves = []
        keys = rev = list(field.field.keys())
        rev.reverse()


        wn = []
        try:
            if field.field[str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) - 1)].team == self.team:
                wn.append(str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) - 1))
        except AttributeError as e:
            wn.append(str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) - 1))
        except KeyError as e:
            pass

        if not len(wn) == 0:
            for c in rev:
                if (int(c[0]) < int(wn[-1][0]) and ord(c[1]) < ord(wn[-1][1])):
                    wn.append(c)

        moves += wn.copy()

        return moves
