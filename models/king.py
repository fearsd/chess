from .basefigure import BaseFigure

class King(BaseFigure):

    def _available_moves(self, field):

        moves = []
        try:
            if field.field[str(int(self.coord[0]) - 1) + self.coord[1]].team == self.team:
                pass
            else:
                moves.append(str(int(self.coord[0]) - 1) + self.coord[1])
        except AttributeError as e:
            moves.append(str(int(self.coord[0]) - 1) + self.coord[1])
        except KeyError as e:
            pass

        try:
            if field.field[str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) + 1)].team == self.team:
                pass
            else:
                moves.append(str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) + 1))
        except AttributeError as e:
            moves.append(str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) + 1))
        except KeyError as e:
            pass

        try:
            if field.field[str(int(self.coord[0])) + chr(ord(self.coord[1]) + 1)].team == self.team:
                pass
            else:
                moves.append(str(int(self.coord[0])) + chr(ord(self.coord[1]) + 1))
        except AttributeError as e:
            moves.append(str(int(self.coord[0])) + chr(ord(self.coord[1]) + 1))
        except KeyError as e:
            pass

        try:
            if field.field[str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]) + 1)].team == self.team:       
                pass
            else:
                moves.append(str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]) + 1))
        except AttributeError as e:
            moves.append(str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]) + 1))
        except KeyError as e:
            pass

        try:
            if field.field[str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]))].team == self.team:
                pass
            else:
                moves.append(str(int(self.coord[0]) + 1) + chr(ord(self.coord[1])))
        except AttributeError as e:
            moves.append(str(int(self.coord[0]) + 1) + chr(ord(self.coord[1])))
        except KeyError as e:
            pass

        try:
            if field.field[str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]) - 1)].team == self.team:
                pass
            else:
                moves.append(str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]) - 1))
        except AttributeError as e:
            moves.append(str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]) - 1))
        except KeyError as e:
            pass

        try:
            if field.field[str(int(self.coord[0])) + chr(ord(self.coord[1]) - 1)].team == self.team:
                pass
            else:
                moves.append(str(int(self.coord[0])) + chr(ord(self.coord[1]) - 1))
        except AttributeError as e:
            moves.append(str(int(self.coord[0])) + chr(ord(self.coord[1]) - 1))
        except KeyError as e:
            pass

        try:
            if field.field[str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) - 1)].team == self.team:
                pass
            else:
                moves.append(str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) - 1))
        except AttributeError as e:
            moves.append(str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) - 1))
        except KeyError as e:
            pass

        return moves
