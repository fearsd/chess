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


    # def test_moves_on_1a_when_figure_is_black(self):
    #     # creating Bishop instance
    #     b = Bishop('1a', 'bishop', 'b')
    #     # creating GameField instance
    #     g = GameField()
    #     # creating Bishop instance
    #     b = Bishop('1a', 'bishop', 'b')
    #     b.team = 'black'
    #     # creating GameField instance
    #     g = GameField()
    #     self.assertEqual(b._available_moves(g), ['2b'])


if __name__ == "__main__":
    unittest.main()