""" Calculating the number of grains of wheat on a chessboard given that the number on
each square doubles.
"""

def square(number: int) -> int:
    """ Function that determines how many grains of wheat exist in a given square of a
    chessboard.

    :param number: int - indicates the chessboard square number
    :return: int - returns the total number of grains in that given square
    :raises: ValueError - Square must be between 1 and 64
    """
    if not 1 <= number < 65:
        raise ValueError("square must be between 1 and 64")
    return 2 **(number - 1)


def total():
    """ Function that determines how many grains of wheat exist in a chessboard.
    """
    grains_in_board = 0
    for item in range(1 ,65):
        grains_in_board += square(item)
    return grains_in_board
