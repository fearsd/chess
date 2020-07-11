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
                        moves.append(str(int(self.coord[0]) - 1) + self.coord[1])
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

        i = 0
        while i <= len(moves) - 1:
            if isinstance(field.field[moves[i]], field.figures):
                if field.field[moves[i]].team == self.team:
                    del moves[i]
                else:
                    i += 1
            else:
                i += 1
        
        return moves