import string


def hide_word(word):
    """Function that changes all characters in a word to "*"."""
    hidden_word = word
    for letter in hidden_word:
        hidden_word = hidden_word.replace(letter, "*")
    return hidden_word


def replace_hidden_character(word, indexes, letter):
    '''
    Function that replaces "*" with letter
    - creates a list out of a word
    - loops through list of indexes
    - changes "*" according to index
    - returns string
    '''
    new_word = list(word)
    for index in indexes:
        new_word[index] = letter

    print(new_word)
    print(f"player letter guess {letter}")
    return "".join(new_word)


def find_index(letter, word):
    '''
    Function that finds occurances of a letter in a word
    - loops through a word
    - when the letter is found at an index it stores into list
    - when letter does not exist in word returns "-1"
    - list of indexes
    '''
    indexes = []
    if letter in word:
        for i in range(len(word)):
            if letter == word[i]:
                indexes.append(i)
            else:
                continue
        return indexes
    return -1

def start_game(secret_word, word_guessed, num_of_guesses):
    player_word_guess = word_guessed
    print("-------------")
    print(f"You have {num_of_guesses} attempts to guess the word")
    print(f"Your guess: {player_word_guess}")
    player_letter_guess = ""
    # users can only input one character and it has to be a letter
    while True:
        user_input = input('Enter a single letter: ')
        # if users entered a single character and it is a letter:
        # break while loop
        if len(user_input) == 1 and user_input.isalpha():
            player_letter_guess = user_input
            break
        # if users have not entered a single letter:
        # repeat while loop
        print('Enter a single letter to continue.')
        continue

    letter_indexes = find_index(player_letter_guess, secret_word)
    print(letter_indexes)
    # If player guess is found in the secret word:
    # Replace the * with the letter at the corresponding index
    if letter_indexes != -1:
        player_word_guess = replace_hidden_character(
            word_guessed, letter_indexes, player_letter_guess)
        print(f"The letter \"{player_letter_guess}\" is in the word! Good Job!")
    else:
        # if the letter is not in the secret word:
        # Decrease the number of guesses the player has
        num_of_guesses -= 1
        print(f"The letter \"{player_letter_guess}\" is not in the word")
    # If the player has no remaining number of guesses:
    # Display message and the secret word the player did not guess
    if num_of_guesses == 0:
        print("Sorry you did not guess the word")
        print(f"The word was \"{secret_word}\"")
        print("Better luck next time! ^_^")
        exit()
    # if the player has not guessed the full secret word:
    # Recursion!
    # Use the start_game function with the new values
    if secret_word != player_word_guess:
        start_game(secret_word, player_word_guess, num_of_guesses)
    # if the player guessed the word:
    # End the program
    else:
        print(f"Congratulations! The word was \"{secret_word}\" and you guessed it!")