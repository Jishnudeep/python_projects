import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # wat the user has guessed

    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #we need to tell user what letters they have used
        print(f'You have used these letters. \n You have {lives} lives left \n ',' '.join(used_letters))

        #what current word is 
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word : ",' '.join(word_list))


        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in word.")

        elif user_letter in used_letters:
            print("You have already guess that character. Please try again.")

        else:
            print("Invalid character. ")

    if lives == 0:
        print(f"Sorry, you are out of lives. The word was {word}")
    else:
        print(f"You guessed the word, {word}!!")


hangman()