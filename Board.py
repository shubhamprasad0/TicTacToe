class Board:
    ''' This class represents a standard 3 x 3 Tic Tac Toe board.'''

    def __init__(self):
        ''' The constructor initialises the board with empty positions
        which are represented here by the character '_' (underscore). '''

        self.board = [['_', '_', '_'],
                      ['_', '_', '_'],
                      ['_', '_', '_']]
