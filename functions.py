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
        for i in enumerate(word):
            if letter == word[i]:
                indexes.append(i)
            else:
                continue
        return indexes
    return -1 #find_index (\n)