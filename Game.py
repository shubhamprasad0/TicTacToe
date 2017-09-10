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

        self.board = Board.Board()
        self.player1 = Player.Player(player1, marker1)
        self.player2 = Player.Player(player2, marker2)
        self.player1_turn = True  # False, for player2 turn

    def play(self):
        ''' This method simulates the game play. '''

        print('Enter position to mark: ')
        row, col = input().split()
        print(row, col)


def main():

    print('Enter name of first player (has marker \'x\') : ')
    player1 = input()
    marker1 = 'x'
    print('Enter name of second player (has marker \'o\') : ')
    player2 = input()
    marker2 = 'o'

    # Initialize game
    game = Game(player1, player2, marker1, marker2)
    game.play()


if __name__ == '__main__':
    main()
