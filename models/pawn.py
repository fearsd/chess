from .basefigure import BaseFigure

class Pawn(BaseFigure):

    def _available_moves(self, field):

        moves = []

        if self.team == 'white':
            if int(self.coord[0]) == 2:
                try:
                    if not isinstance(field.field[str(int(self.coord[0]) + 1) + self.coord[1]], field.figures):
                        moves.append(str(int(self.coord[0]) + 1) + self.coord[1])
                        if not isinstance(field.field[str(int(self.coord[0]) + 2) + self.coord[1]], field.figures):
                            moves.append(str(int(self.coord[0]) + 2) + self.coord[1])
                except KeyError:
                    pass

                try:    
                    if isinstance(field.field[str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]) + 1)], field.figures):
                        moves.append(str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]) + 1))
                except KeyError:
                    pass

                try:    
                    if isinstance(field.field[str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]) - 1)], field.figures):
                        moves.append(str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]) - 1))
                except KeyError:
                    pass
            else:
                try:
                    if not isinstance(field.field[str(int(self.coord[0]) + 1) + self.coord[1]], field.figures):
                        moves.append(str(int(self.coord[0]) + 1) + self.coord[1])
                except KeyError:
                    pass

                try:    
                    if isinstance(field.field[str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]) + 1)], field.figures):
                        moves.append(str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]) + 1))
                except KeyError:
                    pass

                try:    
                    if isinstance(field.field[str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]) - 1)], field.figures):
                        moves.append(str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]) - 1))
                except KeyError:
                    pass
        else:
            if int(self.coord[0]) == 7:
                try:
                    if not isinstance(field.field[str(int(self.coord[0]) - 1) + self.coord[1]], field.figures):
                        moves.append(str(int(self.coord[0]) + 1) + self.coord[1])
                        if not isinstance(field.field[str(int(self.coord[0]) - 2) + self.coord[1]], field.figures):
                            moves.append(str(int(self.coord[0]) - 2) + self.coord[1])
                except KeyError:
                    pass

                try:    
                    if isinstance(field.field[str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) + 1)], field.figures):
                        moves.append(str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) + 1))
                except KeyError:
                    pass

                try:    
                    if isinstance(field.field[str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) - 1)], field.figures):
                        moves.append(str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) - 1))
                except KeyError:
                    pass
            else:
                try:
                    if not isinstance(field.field[str(int(self.coord[0]) - 1) + self.coord[1]], field.figures):
                        moves.append(str(int(self.coord[0]) - 1) + self.coord[1])
                except KeyError:
                    pass

                try:    
                    if isinstance(field.field[str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) + 1)], field.figures):
                        moves.append(str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) + 1))
                except KeyError:
                    pass

                try:    
                    if isinstance(field.field[str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) - 1)], field.figures):
                        moves.append(str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) - 1))
                except KeyError:
                    pass
        
        return moves