from models.gamefield import GameField
from models.player import Player

def game_init():
    chess = GameField()
    white_player = Player('user1', 'white', chess)
    black_player = Player('user2', 'black', chess)

    return chess, white_player, black_player

def main():
    field, white_player, black_player = game_init()
    white_player.make_move(field, black_player)

if __name__ == "__main__":
    main()