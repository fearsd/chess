from .basefigure import BaseFigure

class Knight(BaseFigure):

    def __init__(self, coord, full_name, short_name):
        super().__init__(coord, full_name, short_name)
        self.mov = {
            '1a': ('2c', '3b'),
            '1b': ('2d', '3a', '3c'),
            '1c': ('2a', '2e', '3b', '3d'),
            '1d': ('2b', '2f', '3c', '3e'),
            '1e': ('2c', '2g', '3d', '3f'),
            '1f': ('2d', '2h', '3e', '3g'),
            '1g': ('2e', '3f', '3h'),
            '1h': ('2f', '3g'),

            '2a': ('1c', '3c', '4b'),
            '2b': ('1d', '3d', '4a', '4c'),
            '2c': ('1a', '1e', '3a', '3e', '4b', '4d'),
            '2d': ('1b', '1f', '3b', '3f', '4c', '4e'),
            '2e': ('1c', '1g', '3c', '3g', '4d', '4f'),
            '2f': ('1d', '1h', '3d', '3h', '4e', '4g'),
            '2g': ('1e', '3e', '4f', '4h'),
            '2h': ('1f', '3f', '4g'),

            '3a': ('1b', '2c', '4c', '5b'),
            '3b': ('1a', '1c', '2d', '4d', '5a', '5c'),
            '3c': ('1b', '1d', '2a', '2e', '4a', '4e', '5b', '5d'),
            '3d': ('1c', '1e', '2b', '2f', '4b', '4f', '5c', '5e'),
            '3e': ('1d', '1f', '2c', '2g', '4c', '4g', '5d', '5f'),
            '3f': ('1e', '1g', '2d', '2h', '4d', '4h', '5e', '5g'),
            '3g': ('1f', '1h', '2e', '4e', '5f', '5h'),
            '3h': ('1g', '2f', '4f', '5g'),

            '4a': ('2b', '3c', '5c', '6b'),
            '4b': ('2a', '2c', '3d', '5d', '6a', '6c'),
            '4c': ('2b', '2d', '3a', '3e', '5a', '5e', '6b', '6d'),
            '4d': ('2c', '2e', '3b', '3f', '5b', '5f', '6c', '6e'),
            '4e': ('2d', '2f', '3c', '3g', '5c', '5g', '6d', '6f'),
            '4f': ('2e', '2g', '3d', '3h', '5d', '5h', '6e', '6g'),
            '4g': ('2f', '2h', '3e', '5e', '6f', '6h'),
            '4h': ('2g', '3f', '5f', '6g'),

            '5a': ('3b', '4c', '6c', '7b'),
            '5b': ('3a', '3c', '4d', '6d', '7a', '7c'),
            '5c': ('3b', '3d', '4a', '4e', '6a', '6e', '7b', '7d'),
            '5d': ('3c', '3e', '4b', '4f', '6b', '6f', '7c', '7e'),
            '5e': ('3d', '3f', '4c', '4g', '6c', '6g', '7d', '7f'),
            '5f': ('3e', '3g', '4d', '4h', '6d', '6h', '7e', '7g'),
            '5g': ('3f', '3h', '4e', '6e', '7f', '7h'),
            '5h': ('3g', '4f', '6f', '7g'),

            '6a': (),
            '6b': (),
            '6c': (),
            '6d': (),
            '6e': (),
            '6f': (),
            '6g': (),
            '6h': (),

            '7a': (),
            '7b': (),
            '7c': (),
            '7d': (),
            '7e': (),
            '7f': (),
            '7g': (),
            '7h': (),

            '8a': (),
            '8b': (),
            '8c': (),
            '8d': (),
            '8e': (),
            '8f': (),
            '8g': (),
            '8h': ()
        }
    
    def _available_moves(self, field):
        pass