"""Module providing a random number generator function"""
import random

#Reusable Functions
def hide_word(word):
    """Function that changes all characters in a word to "*"."""
    hidden_word = word
    for letter in hidden_word:
        hidden_word = hidden_word.replace(letter, "*")
    return hidden_word



words_list = ["test", "longitude", "karma", "samurai",
              "language", "beginner", "alphabet", "envy", "binocular", "computation"]
secret_word = words_list[random.randint(1, len(words_list) - 1)] 
word_guessed = hide_word(secret_word)
print(secret_word)
print(word_guessed) #run (\n)

#End of file (EOF)