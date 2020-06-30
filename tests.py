import unittest

from models.bishop import Bishop
from models.gamefield import GameField

class TestBishop(unittest.TestCase):

    def test_moves_on_1a_when_figure_is_white_and_no_one_is_moved(self):
        # creating Bishop instance
        b = Bishop('1a', 'bishop', 'b')

        # creating GameField instance
        g = GameField()

        self.assertEqual(b._available_moves(g), [])


    def test_moves_on_1a_when_figure_is_white_and_white_pawn_on_2b_is_moved_to_3b(self):
        # creating Bishop instance
        b = Bishop('1a', 'bishop', 'b')

        # creating GameField instance
        g = GameField()

        # moving teammate pawn
        g.field['2b'].perform_move(g, '3b')
        self.assertEqual(b._available_moves(g), ['2b', '3c', '4d', '5e', '6f', '7g'])


    def test_moves_on_1a_when_figure_is_white_and_black_pawn_on_7g_is_moved_to_6g(self):
        # creating Bishop instance
        b = Bishop('1a', 'bishop', 'b')

        # creating GameField instance
        g = GameField()

        # moving enemy pawn
        g.field['7g'].perform_move(g, '6g')
        self.assertEqual(b._available_moves(g), [])


    def test_moves_on_1a_when_figure_is_white_and_black_pawn_on_7g_is_moved_to_6g_and_white_pawn_on_2b_is_moved_to_3b(self):
        # creating Bishop instance
        b = Bishop('1a', 'bishop', 'b')

        # creating GameField instance
        g = GameField()

        # moving teammate pawn
        g.field['2b'].perform_move(g, '3b')
        # moving enemy pawn
        g.field['7g'].perform_move(g, '6g')
        self.assertEqual(b._available_moves(g), ['2b', '3c', '4d', '5e', '6f', '7g', '8h'])


    def test_moves_on_1a_when_figure_is_black_and_no_one_is_moved(self):
        # creating Bishop instance
        b = Bishop('1a', 'bishop', 'b')
        b.team = 'black'
        # creating GameField instance
        g = GameField()
        self.assertEqual(b._available_moves(g), ['2b'])


    def test_moves_on_1a_when_figure_is_black_and_white_pawn_on_2b_is_moved_to_3b(self):
        b = Bishop('1a', 'bishop', 'b')
        b.team = 'black'
        # creating GameField instance
        g = GameField()
        g.field['2b'].perform_move(g, '3b')
        self.assertEqual(b._available_moves(g), ['2b', '3c', '4d', '5e', '6f'])

    
    def test_moves_on_1b_when_figure_is_white_and_no_one_is_moved(self):
        b = Bishop('1b', 'bishop', 'b')
        # creating GameField instance
        g = GameField()
        self.assertEqual(b._available_moves(g), [])


    def test_moves_on_1b_when_figure_is_white_and_white_pawn_on_2c_is_moved_to_3c(self):
        b = Bishop('1b', 'bishop', 'b')
        g = GameField()
        g.field['2c'].perform_move(g, '3c')
        self.assertEqual(b._available_moves(g), ['2c', '3d', '4e', '5f', '6g', '7h'])
    

    def test_moves_on_1b_when_figure_is_white_and_white_pawn_on_2c_is_moved_to_3c_and_white_pawn_on_2a_is_moved_to_3a(self):
        b = Bishop('1b', 'bishop', 'b')
        g = GameField()
        g.field['2c'].perform_move(g, '3c')
        g.field['2a'].perform_move(g, '3a')
        self.assertEqual(b._available_moves(g), ['2c', '3d', '4e', '5f', '6g', '7h', '2a'])


    def test_moves_on_1b_when_figure_is_black_and_no_one_is_moved(self):
        b = Bishop('1b', 'bishop', 'b')
        b.team = 'black'
        g = GameField()
        self.assertEqual(b._available_moves(g), ['2c', '2a'])

    
    def test_moves_on_1b_when_figure_is_black_and_white_pawn_on_2c_is_moved_to_3c(self):
        b = Bishop('1b', 'bishop', 'b')
        b.team = 'black'
        g = GameField()
        g.field['2c'].perform_move(g, '3c')
        self.assertEqual(b._available_moves(g), ['2c', '3d', '4e', '5f', '6g', '2a'])


if __name__ == "__main__":
    unittest.main()