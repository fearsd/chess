from models.gamefield import GameField
from models.player import Player

def game_init():
    chess = GameField()
    white_player = Player('user1', 'white', chess)
    black_player = Player('user1', 'black', chess)

    return chess, white_player, black_player

def main():
    field, white_player, black_player = game_init()
    white_player.make_move(field, black_player)
    # print(white_player.figures)


if __name__ == "__main__":
    main()
# chess_field = GameField()
# chess_field.print_field()

# chess_field.field['1b'].perfome_move(chess_field, '3c')
# chess_field.print_field()

# chess_field.field['3c'].perfome_move(chess_field, '5d')
# chess_field.print_field()

# chess_field.field['5d'].perfome_move(chess_field, '7c')
# chess_field.print_field()

# print(chess_field.is_game_finished())

# chess_field.field['7c'].perfome_move(chess_field, '6e')
# chess_field.print_field()

# chess_field.field['6e'].perfome_move(chess_field, '8d')
# chess_field.print_field()

# print(chess_field.is_game_finished())
# # print(chess_field.field['8d'].team, chess_field.field['8d'])
# print(chess_field.get_winner())