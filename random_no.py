import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Please guess a number between 1 and {x}: "))
        if guess > random_number :
            print("Sorry not right. Too High. Try again.")
        elif guess < random_number :
            print("Sorry not right. Too low. Try again.")
    
    print(f"You got it! The number is {random_number}")
            
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low != high :
        if low != high :
            guess = random.randint(low, high)
        else : 
            guess = low
        feedback = input(f"is {guess} too high(H) or too low(L) or Correct (C)?").lower();
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f"The computer guessed your number {guess}")



# guess(10)
computer_guess(1000)