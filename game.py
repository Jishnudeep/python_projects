from player import HumanPlayer, RandomComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single list to rep 3x3 board
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' | ')


    @staticmethod
    def print_board_nums():
        #0 | 1 | 2
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print(' | ' + ' | '.join(row) + ' | ')

    def available_moves(self):
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
            
        
        return moves

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        #if valid move, then make the move. Assign square to letter.
        # then return true. If invalid, then return false.
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self,square, letter):
        # winner if three in a row anywhere
        #first lets check row.
        row_ind = square // 3 
        row = self.board[row_ind * 3 : ( row_ind + 1 ) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        #check columns
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check diagonals
        #but only if the square is an even number 
        #these are the only numbers possible to win a diagonal
        if square % 2 == 0:
            diag1 = [self.board[i] for i in [0,4,8]]
            diag2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diag1]):
                return True
            if all([spot == letter for spot in diag2]):
                return True
        
        return False


    
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X' #starting letter

    #iterate while game has empty squares
    while game.empty_squares():
        #get the move from appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #lets define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                    return letter


            letter = 'O' if letter == 'X' else 'X'
    
    time.sleep(1)
    if print_game:
        print("It\'s a tie.")


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game= True)
