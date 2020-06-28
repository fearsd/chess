from models.gamefield import GameField

chess_field = GameField()
chess_field.print_field()

chess_field.field['1b'].perfome_move(chess_field, '3c')
chess_field.print_field()

chess_field.field['3c'].perfome_move(chess_field, '5d')
chess_field.print_field()

chess_field.field['5d'].perfome_move(chess_field, '7c')
chess_field.print_field()