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
            




guess(10)