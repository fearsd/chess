from models import Player, Computer, GameField

def game_init():
    chess = GameField()
    modes = (1, 2, 3)
    mode = 9
    while mode not in modes:
        mode = int(input('Choose mode of the game: \n1: human vs human\n2: computer vs human\n3: computer vs computer \n: '))

    if mode == 1:
        name1 = input('Input name of first (white) player: ')
        name2 = input('Input name of second (black) player: ')
        white_player = Player(name1, 'white', chess)
        black_player = Player(name2, 'black', chess)
    elif mode == 2:
        name1 = input('Input name of first (white) player: ')
        name2 = input('Input name of second (black) player (computer): ')
        white_player = Player(name1, 'white', chess)
        black_player = Computer(name2, 'black', chess)
    else:
        name1 = input('Input name of first (white) player (computer): ')
        name2 = input('Input name of second (black) player (computer): ')
        white_player = Computer(name1, 'white', chess)
        black_player = Computer(name2, 'black', chess)

    return chess, white_player, black_player

def main():
    field, white_player, black_player = game_init()
    white_player.make_move(field, black_player)

if __name__ == "__main__":
    main()