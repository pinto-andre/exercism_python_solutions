""" Function to determine if a sentence or word is an isogram."""


def is_isogram(string: str) -> bool:
    """Function to determine if a given string is an isogram.

    :param string: str - Given word or sentence to test.
    :return: bool - True if it is an isogram, False otherwise.
    :raise: ValueError - Argument must be a string.
    """
    # Extra self validation
    if not isinstance(string, str):
        raise ValueError("Argument must be a string.")

    # Actual exercise
    lowered_string = string.lower()
    for letter in lowered_string:
        if letter.isalpha() and lowered_string.count(letter) > 1:
            return False
    return True
