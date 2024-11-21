from typing import List

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rows(letter: str) -> List:
    """
    Function to create a diamond shape according to the given alphabet letter
    """
    if not isinstance(letter, str):
        raise TypeError("Input must be a string")
    if len(letter) > 1 or letter not in ALPHABET:
        raise ValueError("Input must be a single and uppercased letter.")
    max_index = ALPHABET.index(letter)  # Index of the letter in the alphabet
    diamond = []

    # Build the top half of the diamond (including the middle row)
    for i in range(max_index + 1):
        spaces_outside = ' ' * (max_index - i)
        if i == 0:
            row = f"{spaces_outside}{ALPHABET[i]}{spaces_outside}"
        else:
            spaces_inside = ' ' * (2 * i - 1)
            row = f"{spaces_outside}{ALPHABET[i]}{spaces_inside}{ALPHABET[i]}{spaces_outside}"
        diamond.append(row)

    # Mirror the top half (excluding the middle row) to complete the diamond
    diamond.extend(reversed(diamond[:-1]))

    return diamond

# Version with comprehension
# def rows(letter: str) -> List:
#     """
#     Function to create a diamond shape according to the given alphabet letter
#     """
#     if not isinstance(letter, str):
#         raise TypeError("Input must be a string")
#     if len(letter) > 1 or letter not in ALPHABET:
#         raise ValueError("Input must be a single and uppercased letter.")

#     max_index = ALPHABET.index(letter)  # Index of the letter in the alphabet

#     # Build the top half (including the middle row) using a comprehension
#     diamond = [
#         f"{' ' * (max_index - i)}{ALPHABET[i]}{' ' * (2 * i - 1)}{ALPHABET[i] if i > 0 else ''}{' ' * (max_index - i)}"
#         for i in range(max_index + 1)
#     ]

#     # Mirror the top half (excluding the middle row) to complete the diamond
#     diamond.extend(reversed(diamond[:-1]))

#     return diamond
