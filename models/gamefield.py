from .bishop import Bishop
from .king import King
from .knight import Knight
from .pawn import Pawn
from .queen import Queen
from .rook import Rook

class GameField:

    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.field = self._create_new_field()
        self.figures = (Bishop, King, Knight, Pawn, Queen, Rook)

    def _create_new_field(self):
        field = {} 

        for n in range(1, 9):
            for l in self.letters:

                # sets rooks for their places
                if (n == 1 and l == 'a') or (n == 1 and l == 'h') or (n == 8 and l == 'a') or (n == 8 and l == 'h'):
                    field[str(n) + l] = Rook(str(n) + l, 'rook', 'R')

                # sets knights for their places
                elif (n == 1 and l == 'b') or (n == 1 and l == 'g') or (n == 8 and l == 'b') or (n == 8 and l == 'g'):
                    field[str(n) + l] = Knight(str(n) + l, 'knight', 'k')

                # sets bishops for their places
                elif (n == 1 and l == 'c') or (n == 1 and l == 'f') or (n == 8 and l == 'c') or (n == 8 and l == 'f'):
                    field[str(n) + l] = Bishop(str(n) + l, 'bishop', 'B')

                # sets queens for their places
                elif (n == 1 and l == 'd') or (n == 8 and l == 'e'):
                    field[str(n) + l] = Queen(str(n) + l, 'queen', 'Q')

                # sets kings for their places
                elif (n == 1 and l == 'e') or (n == 8 and l == 'd'):
                    field[str(n) + l] = King(str(n) + l, 'king', 'K')

                # sets pawns for their places
                elif n == 2 or n == 7:
                    field[str(n) + l] = Pawn(str(n) + l, 'pawn', 'p')

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
                if isinstance(self.field[key], self.figures):
                    print(self.field[key].short_name, end='    ')
                else:
                    print(self.field[key], end='    ')
            print('\n')
            j += 1

    def is_game_finished(self):
        kings = []
        for f in list(self.field.keys()):
            try:
                if self.field[f].short_name == 'K':
                    kings.append(f)
            except AttributeError:
                pass

        if len(kings) == 1:
            return True
        else:
            return False

    def get_winner(self):
        winner = ''
        for f in list(self.field.keys()):
            try:
                if self.field[f].short_name == 'K':
                    winner = f
            except AttributeError:
                pass
        
        return self.field[winner].team

    def __put_coords_in_list(self):
        keys = []

        for key in self.field.keys():
            keys.append(key)
        
        self.keys = keys
