class Board:
    ''' This class represents a standard 3 x 3 Tic Tac Toe board.'''

    def __init__(self):
        ''' The constructor initialises the board with empty positions
        which are represented here by the numeric value of -1. '''

        self.board = [[-1, -1, -1],
                      [-1, -1, -1],
                      [-1, -1, -1]]
