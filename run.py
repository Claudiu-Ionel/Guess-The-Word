"""Modules imported:
   - datetime - current date methods
   - random - function that provides a random number
   hide_word from functions file
   start_game from functions file
"""
import sys
from datetime import datetime
import random
from functions import hide_word
from functions import start_game

#Reusable Functions
def greet_player():
    print("-----------------")
    """ function that takes in the time and prints out a greeting to the player"""
    if hour_now in range(13):
        print("Good day player (^_^)")
    if hour_now in range(13, 19):
        print("Good afternoon player (^_^)")
    if hour_now in range(19, 24):
        print("Good evening player (^_^)")
    print("-----------------")


words_list = ["test", "longitude", "karma", "samurai",
              "language", "beginner", "alphabet", "envy", "binocular", "computation"]
secret_word = words_list[random.randint(1, len(words_list) - 1)] 
word_guessed = hide_word(secret_word)
hour_now = datetime.now().hour
num_of_guesses = round(len(secret_word) / 2)

greet_player()

#Ask for username
username = input("What is your name? : ")
print(f"username: {username}")

# game logic functions
startGame = input("Want to start the game? (y/n): ")
if (startGame == ("y" or "Y")):
    print("Game started")
    start_game(secret_word, word_guessed, num_of_guesses, username)
else:
    print("Game ended")
    sys.exit()

# End of file (EOF)