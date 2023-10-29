"""Module providing a random number generator function"""
import random

words_list = ["test", "longitude", "karma", "samurai",
              "language", "beginner", "alphabet", "envy", "binocular", "computation"]

secret_word = words_list[random.randint(1, len(words_list) - 1)] #run (\n)
print(secret_word)