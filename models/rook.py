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

        moves += top.copy()


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
        
        moves += down.copy()


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

        moves += left.copy()


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

        print(right)
        moves += right.copy()

        # # finding all coords whose rook can move to if these coord would be empty
        # moves = []
        # for n in range(1, 9):
        #     for l in field.letters:
        #         if n == int(self.coord[0]) and not str(n) + l == self.coord:
        #             moves.append(str(n) + l)

        # for n in range(1, 9):
        #     for l in field.letters:
        #         if l == self.coord[1] and not str(n) + l == self.coord and str(n) + l not in moves:
        #             moves.append(str(n) + l)

        # # finding coords that under rook
        # down = []
        # for move in moves:
        #     if int(move[0]) > int(self.coord[0]):
        #         down.append(move)

        # # deleting not available moves on downside
        # i = 0
        # while i <= len(down) - 1:
        #     if isinstance(field.field[down[i]], BaseFigure):
        #         try:
        #             del down[i + 1]
        #         except IndexError:
        #             break
        #     else:
        #         i += 1

        # i = 0
        # while i <= len(moves) - 1:
        #     if moves[i] not in down and int(moves[i][0]) > int(self.coord[0]):
        #         del moves[i]
        #     else:
        #         i += 1


        # # finding coords that over rook
        # top = []
        # for move in moves:
        #     if int(move[0]) < int(self.coord[0]):
        #         top.append(move)
        
        # # deleting not available moves on topside
        # i = len(top) - 1
        # while i >= 0:
        #     if isinstance(field.field[top[i]], BaseFigure):
        #         if not i == 0:
        #             del top[i - 1]
        #         else:
        #             break
        #     else:
        #         i -= 1
        
        # i = 0
        # while i <= len(moves) - 1:
        #     if moves[i] not in top and int(moves[i][0]) < int(self.coord[0]):
        #         del moves[i]
        #     else:
        #         i += 1

        # horizontal = []
        # for move in moves:
        #     if int(move[0]) == int(self.coord[0]):
        #         horizontal.append(move)

        # left = []
        # for move in horizontal:
        #     if ord(move[1]) < ord(self.coord[1]):
        #         left.append(move)

        # i = ord(self.coord[1]) - 1
        # while i >= 97:
        #     if isinstance(field.field[str(self.coord[0]) + chr(i)], BaseFigure):
        #         if not i == 97:
        #             try:
        #                 del left[i - 98]
        #                 i -= 1
        #             except IndexError:
        #                 break
        #         else:
        #             i -= 1
        #     else:
        #         i -= 1
        
        # i = 0
        # while i <= len(moves) - 1:
        #     if moves[i] not in left and ord(moves[i][1]) < ord(self.coord[1]) and int(moves[i][0]) == int(self.coord[0]):
        #         del moves[i]
        #     else:
        #         i += 1

        # right = []
        # for move in horizontal:
        #     if ord(move[1]) > ord(self.coord[1]):
        #         right.append(move)
        

        # i = ord(self.coord[1]) + 1
        # while i <= 104:
        #     if isinstance(field.field[str(self.coord[0]) + chr(i)], BaseFigure):
        #         if not i == 104:
        #             try:
        #                 del right[i - 100]
        #             except IndexError:
        #                 break
        #         else:
        #             i += 1
        #     else:
        #         i += 1
        
        # i = 0
        # while i <= len(moves) - 1:
        #     if moves[i] not in right and ord(moves[i][1]) > ord(self.coord[1]) and int(moves[i][0]) == int(self.coord[0]):
        #         del moves[i]
        #     else:
        #         i += 1

        # # deleting coords that contains teammates
        # i = 0
        # while i <= len(moves) - 1:
        #     if isinstance(field.field[moves[i]], BaseFigure):
        #         if field.field[moves[i]].team == self.team:
        #             del moves[i]
        #         else:
        #             i += 1
        #     else:
        #         i += 1

        return moves
