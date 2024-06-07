"""Function to create a rotation cypher: aka Caesar cipher"""
from string import ascii_lowercase, ascii_uppercase

def rotate(text: str, key: int) -> str:
    """ Function to create a rotation cypher: aka Caesar cipher.
    
    :param text: str - Given string to turn to cipher
    :param key: int - key deciding how many rotations the letter will have
    :returns: str - cipher
    :raises: TypeError - Only string text and integer keys are allowed.
    :raises: ValueError - Key value must be between 0 and 26."""

    if not isinstance(text, str) or not isinstance(key, int):
        raise TypeError("Only string text and integer keys are allowed.")
    if not 0 <= key <= 26:
        raise ValueError("Key value must be between 0 and 26.")

    rotated = ""

    for char in text:
        if char.islower():
            rotated += ascii_lowercase[(ascii_lowercase.index(char) + key) % 26]
        elif char.isupper():
            rotated += ascii_uppercase[(ascii_uppercase.index(char) + key) % 26]
        else:
            rotated += char

    return rotated
