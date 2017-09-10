class Board:
    ''' This class represents a standard 3 x 3 Tic Tac Toe board.'''

    def __init__(self):
        ''' The constructor initialises the board with empty positions
        which are represented here by the character '_' (underscore). '''

        self.board = [['_', '_', '_'],
                      ['_', '_', '_'],
                      ['_', '_', '_']]

    def show_board(self):
        for row in self.board:
            print(row[0], row[1], row[2])

    def is_full(self):
        ''' This method checks if there is any vacant position left on the
        board or not.  If there is any vacant position left, it returns True,
        else it returns False.
        '''

        full = True
        for row in self.board:
            for position in row:
                if position == '_':
                    full = False
                    break
            if full is False:
                break

        return full

    def winning_position(self):
        ''' This method checks if the board is in winning position.
        If the board is in winning position , it returns the marker of
        the player who has won.  If the board is not in a winning position,
        it returns None.
        '''

        # Check each row
        for row in self.board:
            if (row[0] != '_' and row[0] == row[1] and row[0] == row[2]):
                return row[0]

        # Check each column
        board_transpose = list(zip(*self.board))
        for col in board_transpose:
            if (col[0] != '_' and col[0] == col[1] and col[0] == col[2]):
                return col[0]

        # Check main diagonal (top-left to bottom-right)
        if (self.board[0][0] != '_' and
                self.board[0][0] == self.board[1][1] and
                self.board[0][0] == self.board[2][2]):
            return self.board[0][0]

        # Check other diagonal (top-right to bottom-left)
        if (self.board[0][2] != '_' and
                self.board[0][2] == self.board[1][1] and
                self.board[0][2] == self.board[2][0]):
            return self.board[0][2]

        # The board is not in a winning position, so return None
        return None
