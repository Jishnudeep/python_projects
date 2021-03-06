import math
import random


class Player :
    def __init__(self,letter):
        #letter is x or o
        self.letter = letter

    #players get their next game
    def get_move(self,game):
        pass

    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random spot
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        value = None
        while not valid_square:
            square = input(self.letter +"\'s turn. Input move (0-8): ")
            # we are going to check if this is a correct value by trying to cast
            # it to an integer, and if it is not, then we say it is invalid, 
            # if that spot is not available on the board,we also say it is invalid
            try:
                value = int(square)
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True 
            except ValueError:
                print('Invalid square. Try again.')
        
        return value

