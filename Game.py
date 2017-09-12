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

    def is_valid(self, row, col):
        ''' This method checks whether a move is valid or not.

        Arguments:
        row -- The row index of specified move
        col -- The col index of specified move
        '''

        if row < 0 or row > 2 or col < 0 or col > 2:
            return False

        if self.board.board[row][col] != '_':
            return False

        return True

    def play(self):
        ''' This method simulates the game play. '''

        while self.board.is_full() is False:
            print('_'*40)
            self.board.show_board()

            if self.player1_turn is True:
                # player1's turn
                print('{}\'s Turn (marker = {})'.format(self.player1.name,
                                                        self.player1.marker))
                row, col = self.best_move(self.board)
                self.player1.moves.append((row, col))
                self.board.board[row][col] = 'x'
                self.player1_turn = False
            else:
                # player2's turn
                print('{}\'s Turn (marker = {})'.format(self.player2.name,
                                                        self.player2.marker))
                print('Enter position to mark (0 based indexing)')
                row, col = [int(i) for i in input().split()]
                if self.is_valid(row, col) is False:
                    print('Invalid move, try again!')
                    continue
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

    def minimax(self, board, depth, player1_turn):
        ''' This method implements the minimax algorithm for ranking each
        possible move from the current board setup, and returns the best score
        which can be obtained from this setup.

        Arguments:
        board -- The board setup which needs to be evaluated.  It is
                 actually a Board type object.
        depth -- The depth in the game tree.  It is an integer value.
        player1_turn -- A boolean indicating whether it is player1's turn
                        or not. True, if it is player1's turn and False,
                        otherwise.
        '''

        score = board.score()

        # If the game has been won by player1
        if score == 10:
            return 10 - depth

        # If the game has been won by player2
        if score == -10:
            return -10 + depth

        # If the game ended in a draw
        if board.is_full() is True:
            return 0

        if player1_turn is True:
            ''' This block tries to maximize the score relative to player1. '''

            best = -1000
            for i, row in enumerate(board.board):
                for j, char in enumerate(row):
                    if char == '_':
                        board.set_mark(i, j, self.player1.marker)
                        best = max(best, self.minimax(board, depth + 1, False))
                        board.remove_mark(i, j)

            return best
        else:
            ''' This block tries to minimize the score relative to player1. '''

            best = 1000
            for i, row in enumerate(board.board):
                for j, char in enumerate(row):
                    if char == '_':
                        board.set_mark(i, j, self.player2.marker)
                        best = min(best, self.minimax(board, depth + 1, True))
                        board.remove_mark(i, j)
            return best

    def best_move(self, board):
        ''' This method returns the best move for player1 at the board position
        depicted by board.

        Arguments:
        board -- The board setup at which player1's move has to be predicted.
        '''

        best_move = [-1, -1]
        best_score = -1000

        for i, row in enumerate(board.board):
            for j, char in enumerate(row):
                if char == '_':

                    board.set_mark(i, j, self.player1.marker)

                    # player1 made it's move, so next move should be player2's.
                    move_score = self.minimax(board, 0, False)
                    board.remove_mark(i, j)

                    if move_score > best_score:
                        best_score = move_score
                        best_move = [i, j]

        return best_move


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
