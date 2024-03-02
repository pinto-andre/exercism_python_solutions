""" Function that determines if a given sentence is a pangram"""

import string


def is_pangram(sentence: str) -> bool:
    """Function that determines if a given sentence is a pangram

    :param sentence: str - Given sentence to determine if it is a pangram or not
    :return: bool - True if pangram and false otherwise
    :raises: TypeError - Sentence must be a string
    """
    if not isinstance(sentence, str):
        raise TypeError("Sentence must be a string")

    alphab = string.ascii_lowercase
    unique_characters = set()
    for letter in sentence:
        if letter.isalpha():
            unique_characters.add(letter.lower())
    return set(alphab) == unique_characters
