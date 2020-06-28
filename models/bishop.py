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

        i = 0
        while i <= len(wn) - 1:
            if isinstance(field.field[wn[i]], field.figures):
                try:
                    del wn[i + 1]
                except IndexError:
                    break
            else:
                i += 1


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

        i = 0
        while i <= len(en) - 1:
            if isinstance(field.field[en[i]], field.figures):
                try:
                    del en[i + 1]
                except IndexError:
                    break
            else:
                i += 1

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

        i = 0
        while i <= len(es) - 1:
            if isinstance(field.field[es[i]], field.figures):
                try:
                    del es[i + 1]
                except IndexError:
                    break
            else:
                i += 1
        

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

        i = 0
        while i <= len(ws) - 1:
            if isinstance(field.field[ws[i]], field.figures):
                try:
                    del ws[i + 1]
                except IndexError:
                    break
            else:
                i += 1
        

        moves += wn.copy()
        moves += en.copy()
        moves += es.copy()
        moves += ws.copy()

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
