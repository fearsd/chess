from .basefigure import BaseFigure

class Rook(BaseFigure):

    def _available_moves(self, field):

        moves = []
        keys = list(field.field.keys())
        rev = list(field.field.keys())
        rev.reverse()


        top = []
        try:
            if field.field[str(int(self.coord[0]) - 1) + self.coord[1]].team == self.team:
                top.append(str(int(self.coord[0]) - 1) + self.coord[1])
        except AttributeError as e:
            top.append(str(int(self.coord[0]) - 1) + self.coord[1])
        except KeyError as e:
            pass
        
        if not len(top) == 0:
            for c in rev:
                if (int(c[0]) < int(top[-1][0]) and c[1] == top[-1][1]):
                    top.append(c)

        i = 0
        while i <= len(top) - 1:
            if isinstance(field.field[top[i]], BaseFigure):
                try:
                    del top[i + 1]
                except IndexError:
                    break
            else:
                i += 1


        down = []
        try:
            if field.field[str(int(self.coord[0]) + 1) + chr(ord(self.coord[1]))].team == self.team:
                down.append(str(int(self.coord[0]) + 1) + chr(ord(self.coord[1])))
        except AttributeError as e:
            down.append(str(int(self.coord[0]) + 1) + chr(ord(self.coord[1])))
        except KeyError as e:
            pass

        if not len(down) == 0:
            for c in keys:
                if (int(c[0]) > int(down[-1][0]) and c[1] == down[-1][1]):
                    down.append(c)

        i = 0
        while i <= len(down) - 1:
            if isinstance(field.field[down[i]], BaseFigure):
                try:
                    del down[i + 1]
                except IndexError:
                    break
            else:
                i += 1
        

        left = []
        try:
            if field.field[str(int(self.coord[0])) + chr(ord(self.coord[1]) - 1)].team == self.team:
                left.append(str(int(self.coord[0])) + chr(ord(self.coord[1]) - 1))
        except AttributeError as e:
            left.append(str(int(self.coord[0])) + chr(ord(self.coord[1]) - 1))
        except KeyError as e:
            pass

        if not len(left) == 0:
            for c in rev:
                if (int(c[0]) == int(left[-1][0]) and ord(c[1]) < ord(left[-1][1])):
                    left.append(c)

        i = 0
        while i <= len(left) - 1:
            if isinstance(field.field[left[i]], BaseFigure):
                try:
                    del left[i + 1]
                except IndexError:
                    break
            else:
                i += 1


        right = []
        try:
            if field.field[str(int(self.coord[0])) + chr(ord(self.coord[1]) + 1)].team == self.team:
                right.append(str(int(self.coord[0])) + chr(ord(self.coord[1]) + 1))
        except AttributeError as e:
            right.append(str(int(self.coord[0])) + chr(ord(self.coord[1]) + 1))
        except KeyError as e:
            pass

        if not len(right) == 0:
            for c in keys:
                if (int(c[0]) == int(right[-1][0]) and ord(c[1]) > ord(right[-1][1])):
                    right.append(c)

        i = 0
        while i <= len(right) - 1:
            if isinstance(field.field[right[i]], BaseFigure):
                try:
                    del right[i + 1]
                except IndexError:
                    break
            else:
                i += 1


        moves += top.copy()
        moves += down.copy()
        moves += left.copy()
        moves += right.copy()

        i = 0
        while i <= len(moves) - 1:
            if isinstance(field.field[moves[i]], BaseFigure):
                if field.field[moves[i]].team == self.team:
                    del moves[i]
                else:
                    i += 1
            else:
                i += 1

        return moves
