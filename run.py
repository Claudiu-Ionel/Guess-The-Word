"""
Modules imported:
   - datetime - current date methods
   - prepare_game from functions.py
   - play_game from functions.py
"""
import sys
from datetime import datetime
from functions import prepare_game
from functions import play_game

# Reusable Functions


def greet_player():
    """function that prints out the time and greets the player"""
    print("-----------------")
    if hour_now in range(13):
        print("Good day player (^_^)")
    if hour_now in range(13, 19):
        print("Good afternoon player (^_^)")
    if hour_now in range(19, 24):
        print("Good evening player (^_^)")
    print("-----------------")


secret_word_list = {
    "easy": [
        {"word": "dog", "hint": "Four-legged friend with a tail"},
        {"word": "cat", "hint": "Independent feline companion"},
        {"word": "ball", "hint": "Round and used in games"},
        {"word": "nose", "hint": "Found on your face, helps you smell"},
        {"word": "phone", "hint": "Portable communication device"},
        {"word": "gold", "hint": "Precious metal, symbol of wealth"},
    ],
    "medium": [
        {"word": "bathroom", "hint": "Where you go to freshen up"},
        {"word": "deadline", "hint": "Time limit for a task"},
        {"word": "favorite", "hint": "What you like the most"},
        {"word": "birthday", "hint": "The day you celebrate your birth"},
        {"word": "accurate", "hint": "Correct and precise"},
        {"word": "aircraft", "hint": "Flies in the sky"},
        {"word": "champion", "hint": "The best in a competition"},
        {"word": "charming", "hint": "Attractive and pleasant"},
        {"word": "creature", "hint": "A living being"},
        {"word": "samurai", "hint": "Skilled warrior from Japan"},
        {"word": "alphabet", "hint": "Letters used to write words"},
        {"word": "delivery", "hint": "Bringing something to you"},
    ],
    "hard": [
        {"word": "aggressivity", "hint": "Intensity of confrontation"},
        {"word": "battleground", "hint": "Place of conflict"},
        {"word": "biodiversity", "hint": "Variety of life"},
        {
            "word": "biophysicist",
            "hint": "Scientist studying life's physical aspects"
        },
        {"word": "calligrapher", "hint": "Skilled in elegant writing"},
        {"word": "candleholder", "hint": "Holds a source of light"},
        {"word": "creativity", "hint": "Source of innovative ideas"},
        {"word": "contemporary", "hint": "In the present time"},
        {"word": "continuation", "hint": "Going forward with something"},
        {"word": "eavesdropper", "hint": "Secret listener"},
        {"word": "entrepreneur", "hint": "Business innovator"},
        {"word": "exacerbation", "hint": "Intensification of a problem"},
        {"word": "fearsom", "hint": "Quality of being intimidating"},
    ]
}
hour_now = datetime.now().hour

greet_player()

# Ask for username
username = input("What is your name? : ")
print(f"username: {username}")

# game logic functions

while True:
    startGame = input("Want to start the game? (y/n): ")
    if startGame.lower() == "y":
        print("Game started")
        game_data = prepare_game(secret_word_list)
        secret_word = game_data["secret_word"]
        word_guessed = game_data["word_guessed"]
        num_of_guesses = game_data["num_of_guesses"]
        play_game(secret_word,
                  word_guessed,
                  num_of_guesses,
                  secret_word_list,
                  letter_guess_set={""}
                  )
        break
    if startGame.lower() == "n":
        print("Game ended")
        sys.exit()
    else:
        print("Please type in the correct letter")
        continue

# End of file (EOF)
