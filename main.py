from models.gamefield import GameField
from models.player import Player, Computer

def game_init():
    chess = GameField()
    modes = (1, 2, 3)
    mode = 9
    while mode not in modes:
        mode = int(input('Choose mode of the game: \n1: human vs human\n2: computer vs human\n3: computer vs computer'))

    if mode == 1:
        white_player = Player('user1', 'white', chess)
        black_player = Player('user2', 'black', chess)
    elif mode == 2:
        white_player = Player('user', 'white', chess)
        black_player = Computer('snapdragon 865', 'black', chess)
    else:
        white_player = Computer('core i5', 'white', chess)
        black_player = Computer('snapdragon 865', 'black', chess)

    return chess, white_player, black_player

def main():
    field, white_player, black_player = game_init()
    white_player.make_move(field, black_player)

if __name__ == "__main__":
    main()