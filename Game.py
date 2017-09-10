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
        self.winner = None

    def play(self):
        ''' This method simulates the game play. '''

        while self.board.is_full() is False:
            print('_'*40)
            self.board.show_board()
            print('{}\'s Turn'.format(self.player1.name)
                  if self.player1_turn is True else
                  '{}\'s Turn'.format(self.player2.name))
            print('Enter position to mark (0 based indexing): ')
            row, col = [int(i) for i in input().split()]

            # Check if the entered row and col are valid or not
            if row < 0 or row > 2 or col < 0 or col > 2:
                print('Entered position is invalid')
                continue

            # Check if the position entered is vacant or not
            if self.board.board[row][col] != '_':
                print('Entered position is already occupied, try again!')
                continue

            if self.player1_turn is True:
                # player1's turn
                self.player1.moves.append((row, col))
                self.board.board[row][col] = 'x'
                self.player1_turn = False
            else:
                # player2's turn
                self.player2.moves.append((row, col))
                self.board.board[row][col] = 'o'
                self.player1_turn = True

            verdict = self.board.winning_position()

            if verdict is not None:
                self.winner = self.player1 if verdict == 'x' else self.player2
                break

        # Show board at the end of the game
        print('Game Over')
        print('_' * 40)
        self.board.show_board()

        # Declare result of the game
        if self.winner is not None:
            print('Winner is {}'.format(self.winner.name))
        else:
            print('This is a draw')


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
