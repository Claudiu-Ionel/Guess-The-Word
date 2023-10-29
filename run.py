"""Modules imported:
   - datetime - current date methods
   - random - function that provides a random number
"""
from datetime import datetime
import random

#Reusable Functions
def hide_word(word):
    """Function that changes all characters in a word to "*"."""
    hidden_word = word
    for letter in hidden_word:
        hidden_word = hidden_word.replace(letter, "*")
    return hidden_word

def greet_player():
    """ function that takes in the time and prints out a greeting to the player"""
    if hour_now in range(13):
        print("Good day player (^_^)")
    if hour_now in range(13, 19):
        print("Good afternoon player (^_^)")
    if hour_now in range(19, 24):
        print("Good evening player (^_^)")


words_list = ["test", "longitude", "karma", "samurai",
              "language", "beginner", "alphabet", "envy", "binocular", "computation"]
secret_word = words_list[random.randint(1, len(words_list) - 1)] 
word_guessed = hide_word(secret_word)
hour_now = datetime.now().hour

print(secret_word)
print(word_guessed) #run (\n)

greet_player()


#Ask for username
username = input("What is your name? : ")
print(f"username: {username}")

# game logic functions
startGame = input("Want to start the game? (y/n): ")
if (startGame == ("y" or "Y")):
    print("Game started")
else:
    print("Game ended")



#End of file (EOF)