class Player:

    def __init__(self, username, team, field):
        self.username = username
        self.team = team
        self.figures = self._get_figures(field)

    def _get_figures(self, field):
        figures = []
        for k in list(field.field.keys()):
            try:
                if field.field[k].team == self.team:
                    figures.append(k)
            except AttributeError:
                pass

        return figures

    def make_move(self, field, enemy):
        if field.is_game_finished():
            print(field.get_winner(), 'wins')
            return
        field.print_field()
        self.figures = self._get_figures(field)
        print(self.username + "'s move")
        print()
        print('Your figures: ')
        for f in self.figures:
            print(f, '-', field.field[f].full_name)
        c = ''
        while c not in self.figures:
            c = input('Enter coords of figure which you want to move: ')

        print('Available moves: ', end=' ')
        for move in field.field[c]._available_moves(field):
            print(move, end=' ')

        print()
        d = ''
        while d not in field.field[c]._available_moves(field):
            d = input('Enter coord: ')

        field.field[c].perform_move(field, d)

        enemy.make_move(field, self)