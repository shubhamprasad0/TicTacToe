import Board
import Player


class Game:

    ''' This class defines a tic-tac-toe game. '''
    def __init__(self, player1, player2, marker1, marker2):
        ''' The constructor initializes a tic-tac-toe game.

        Arguments:
        player1 -- name of first player
        player2 -- name of second player
        marker1 -- marker of first player
        marker2 -- marker of second player
        '''

        self.board = Board()
        self.player1 = Player(player1, marker1)
        self.player2 = Player(player2, marker2)
