from .basefigure import BaseFigure

class Bishop(BaseFigure):

    def _available_moves(self, field):
        moves = []
        keys = list(field.field.keys())
        rev = list(field.field.keys())
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


        en = []
        try:
            if field.field[str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) + 1)].team == self.team:
                en.append(str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) + 1))
        except AttributeError as e:
            en.append(str(int(self.coord[0]) - 1) + chr(ord(self.coord[1]) + 1))
        except KeyError as e:
            pass
        
        if not len(en) == 0:
            for c in rev:
                if (int(c[0]) < int(en[-1][0]) and ord(c[1]) > ord(en[-1][1])) and (ord(c[1]) - ord(en[-1][1]) == 1):
                    en.append(c)

        moves += en.copy()

        es = []
        try:
            if field.field[str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]) + 1)].team == self.team:       
                es.append(str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]) + 1))
        except AttributeError as e:
            es.append(str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]) + 1))
        except KeyError as e:
            pass

        if not len(es) == 0:
            for c in keys:
                if (int(c[0]) > int(es[-1][0]) and ord(c[1]) > ord(es[-1][1])):
                    es.append(c)
        
        moves += es.copy()

        ws = []
        try:
            if field.field[str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]) - 1)].team == self.team:
                ws.append(str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]) - 1))
        except AttributeError as e:
            ws.append(str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]) - 1))
        except KeyError as e:
            pass

        if not len(ws) == 0:
            for c in keys:
                if (int(c[0]) > int(ws[-1][0]) and ord(c[1]) < ord(ws[-1][1])) and (ord(c[1]) - ord(ws[-1][1]) == -1):
                    ws.append(c)

        moves += ws.copy()


        return moves
