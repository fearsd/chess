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
        return self.full_name


class Rook(BaseFigure):

    def perfome_move(self, field, coords_to):
        available_coords_to_move = self._available_moves(field)
    
    def _available_moves(self, field):

        # finding all coords whose rook can move to if these coord would be empty
        moves = []
        for n in range(1, 9):
            for l in field.letters:
                if n == int(self.coord[0]) and not str(n) + l == self.coord:
                    moves.append(str(n) + l)

        for n in range(1, 9):
            for l in field.letters:
                if l == self.coord[1] and not str(n) + l == self.coord and str(n) + l not in moves:
                    moves.append(str(n) + l)

        # deleting coords that contains teammates
        i = 0
        while i <= len(moves) - 1:
            if isinstance(field.field[moves[i]], BaseFigure):
                if field.field[moves[i]].team == self.team:
                    del moves[i]
                else:
                    i += 1
            else:
                i += 1

        # finding coords that under rook
        down = []
        for move in moves:
            if int(move[0]) > int(self.coord[0]):
                down.append(move)

        # deleting not available moves on downside
        i = 0
        while i <= len(down) - 1:
            if isinstance(field.field[down[i]], BaseFigure):
                try:
                    del down[i + 1]
                except IndexError:
                    break
            else:
                i += 1

        i = 0
        while i <= len(moves) - 1:
            if moves[i] not in down and int(moves[i][0]) > int(self.coord[0]):
                del moves[i]
            else:
                i += 1


        # finding coords that over rook
        top = []
        for move in moves:
            if int(move[0]) < int(self.coord[0]):
                top.append(move)
        
        # deleting not available moves on topside
        i = len(top) - 1
        while i >= 0:
            if isinstance(field.field[top[i]], BaseFigure):
                if not i == 0:
                    del top[i - 1]
                else:
                    break
            else:
                i -= 1
        
        i = 0
        while i <= len(moves) - 1:
            if moves[i] not in top and int(moves[i][0]) < int(self.coord[0]):
                del moves[i]
            else:
                i += 1

        horizontal = []
        for move in moves:
            if int(move[0]) == int(self.coord[0]):
                horizontal.append(move)

        left = []
        for move in horizontal:
            if ord(move[1]) < ord(self.coord[1]):
                left.append(move)

        i = ord(self.coord[1]) - 1
        while i >= 97:
            if isinstance(field.field[str(self.coord[0]) + chr(i)], BaseFigure):
                if not i == 97:
                    try:
                        del left[i - 98]
                        i -= 1
                    except IndexError:
                        break
                else:
                    i -= 1
            else:
                i -= 1
        
        i = 0
        while i <= len(moves) - 1:
            if moves[i] not in left and ord(moves[i][1]) < ord(self.coord[1]) and int(moves[i][0]) == int(self.coord[0]):
                del moves[i]
            else:
                i += 1

        right = []
        for move in horizontal:
            if ord(move[1]) > ord(self.coord[1]):
                right.append(move)
        

        i = ord(self.coord[1]) + 1
        while i <= 104:
            if isinstance(field.field[str(self.coord[0]) + chr(i)], BaseFigure):
                if not i == 104:
                    try:
                        del right[i - 100]
                    except IndexError:
                        break
                else:
                    i += 1
            else:
                i += 1
        
        i = 0
        while i <= len(moves) - 1:
            if moves[i] not in right and ord(moves[i][1]) > ord(self.coord[1]) and int(moves[i][0]) == int(self.coord[0]):
                del moves[i]
            else:
                i += 1

        return moves


class GameField:

    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.field = self._create_new_field()

    def _create_new_field(self):
        field = {} 

        for n in range(1, 9):
            for l in self.letters:

                # sets rooks for their places
                if (n == 1 and l == 'a') or (n == 1 and l == 'h') or (n == 8 and l == 'a') or (n == 8 and l == 'h'):
                    field[str(n) + l] = BaseFigure(str(n) + l, 'rook', 'R')

                # sets knights for their places
                elif (n == 1 and l == 'b') or (n == 1 and l == 'g') or (n == 8 and l == 'b') or (n == 8 and l == 'g'):
                    field[str(n) + l] = BaseFigure(str(n) + l, 'knight', 'k')

                # sets bishops for their places
                elif (n == 1 and l == 'c') or (n == 1 and l == 'f') or (n == 8 and l == 'c') or (n == 8 and l == 'f'):
                    field[str(n) + l] = BaseFigure(str(n) + l, 'bishop', 'B')

                # sets queens for their places
                elif (n == 1 and l == 'd') or (n == 8 and l == 'e'):
                    field[str(n) + l] = BaseFigure(str(n) + l, 'queen', 'Q')

                # sets kings for their places
                elif (n == 1 and l == 'e') or (n == 8 and l == 'd'):
                    field[str(n) + l] = BaseFigure(str(n) + l, 'king', 'K')

                # sets pawns for their places
                elif n == 2 or n == 7:
                    field[str(n) + l] = BaseFigure(str(n) + l, 'pawn', 'p')

                else:
                    field[str(n) + l] = '.'

        return field

    def print_field(self):
        self.__put_coords_in_list()
        old_row = 1
        print('      ', end='')
        for l in self.letters:
            print(l, end='    ')
        print('\n\n')
        j = 1
        for i in range(0, 64, 8):
            print(j, end='     ')
            for key in self.keys[i:i+8]:
                if isinstance(self.field[key], BaseFigure):
                    print(self.field[key].short_name, end='    ')
                else:
                    print(self.field[key], end='    ')
            print('\n')
            j += 1


    def __put_coords_in_list(self):
        keys = []

        for key in self.field.keys():
            keys.append(key)
        
        self.keys = keys

    # this methhod will be deleted after making classes for figures
    def perfom_move(self, x, y):
        self.field[x], self.field[y] = self.field[y], self.field[x]