import unittest

from models.bishop import Bishop
from models.gamefield import GameField

class TestBishop(unittest.TestCase):

    def test_moves_on_1a(self):
        b = Bishop('1a', 'bishop', 'b')
        b.team = 'black'
        self.assertEqual(b._available_moves(GameField()), ['2b'])
        g = GameField()
        g.field['2b'].perform_move(g, '3b')
        self.assertEqual(b._available_moves(g), ['2b', '3c', '4d', '5e', '6f'])
        g.field['7g'].perform_move(g, '6g')
        g.field['7h'].perform_move(g, '6h')
        g.field['8h'].perform_move(g, '7h')
        self.assertEqual(b._available_moves(g), ['2b', '3c', '4d', '5e', '6f', '7g', '8h'])


if __name__ == "__main__":
    unittest.main()