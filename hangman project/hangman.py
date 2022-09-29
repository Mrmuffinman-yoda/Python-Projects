import random
from words import words as wordCollection
import string
from os import system as sys
def get_valid_word(words):
    word = random.choice(words) # pick a random word
    while " " in word or "-" in word: # if there is " " Empty space or hypen , we ignore the word
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(wordCollection)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # once a letter has been used , put in here
    guesses = 10 
    while len(word_letters) > 0 and guesses > 0:
        sys("cls")
        # Lets tell the user what letters they have 
        # Already used 
        print("Guessed letters : ", ",".join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("[Current word: ", " ".join(word_list) +"]")
        print(f"You have : {guesses} guesses left")
        user_letter = input("Guess a letter : ").upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            guesses -= 1
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print(f"You have already used the character {user_letter}")

    if guesses == 0:
        print("You have run out of guesses :(")
    else:
        print("You have guessed the word!")
    print(f"Your word was {word[0] + word[1:].lower()}")
if __name__ == "__main__":
    hangman()




