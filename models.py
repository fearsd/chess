# TODO: make class for figure

WHITE = (1, 2)
BLACK = (7, 8)

class BaseFigure:

    def __init__(self, coord, name):
        self.coord = coord
        self.team = self._set_team()
        self.name = name

    def _set_team(self):
        if int(self.coord[0]) in WHITE:
            return 'white'
        else:
            return 'black'


class Elephant(BaseFigure):

    def perfome_move(self, field, coords_to):
        available_coords_to_move = 
    
    def _available_moves(self, field):
        pass
        # TODO: продумать логику выявления ходов на основании положения слона

class GameField:

    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.field = self._create_new_field()

    def _create_new_field(self):
        field = {} 

        for n in range(1, 9):
            for l in self.letters:

                # TODO: set appropriate names for figures after googling chess

                # sets elephants for their places
                if (n == 1 and l == 'a') or (n == 1 and l == 'h') or (n == 8 and l == 'a') or (n == 8 and l == 'h'):
                    field[str(n) + l] = 'elephant'

                # sets horses for their places
                elif (n == 1 and l == 'b') or (n == 1 and l == 'g') or (n == 8 and l == 'b') or (n == 8 and l == 'g'):
                    field[str(n) + l] = 'horse'

                # sets soldats for their places
                elif (n == 1 and l == 'c') or (n == 1 and l == 'f') or (n == 8 and l == 'c') or (n == 8 and l == 'f'):
                    field[str(n) + l] = 'soldat'

                # sets queens for their places
                elif (n == 1 and l == 'd') or (n == 8 and l == 'e'):
                    field[str(n) + l] = 'queen'

                # sets kings for their places
                elif (n == 1 and l == 'e') or (n == 8 and l == 'd'):
                    field[str(n) + l] = 'king'

                # sets peshkas for their places
                elif n == 2 or n == 7:
                    field[str(n) + l] = 'peshka'

                else:
                    field[str(n) + l] = ''

        return field

    def print_field(self):
        self.__put_coords_in_list()
        old_row = 1
        print('  ', end='')
        for l in self.letters:
            print(l, end='      ')
        print('\n')
        j = 1
        for i in range(0, 64, 8):
            print(j, end=' ')
            for key in self.keys[i:i+8]:
                print(self.field[key], end=' ')
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