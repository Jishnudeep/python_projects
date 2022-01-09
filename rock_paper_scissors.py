import random


def play():
    user = input("Enter R for Rock, P for Paper and S for Scissors : ").lower();
    computer = random.choice(['r','p','s'])
    if user == computer:
        print("TIE O_o")

    if is_win(user,computer):
        print(f'Computer played {computer}. You Won! :D')

    else:
        print(f'Computer played {computer}. You lost :(')

def is_win(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    else:
        return False




play()