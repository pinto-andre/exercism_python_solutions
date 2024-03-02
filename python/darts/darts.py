""" Function that given a point in the target (defined by its Cartesian Coordinates 'x'
and 'y', where 'x' and 'y' are real-numbers, returns the correct amount earned by a dart
landing at that point).
"""

import math


def score(x: float | int, y: float | int) -> int:
    """Function that returns the correct amount earned by a dart landing at the given
    coordinates point.

    :param x: float | int - Given number for axis-X
    :param y: float | int - Given number for axis-Y
    :return: int - Returns the score for the given coordinates
    :raises: ValueError - Imaginary numbers are not accepted.
    :raises: ValueError - Given input must be a real number.
    """
    # Extra self-validation
    if isinstance(x, complex) or isinstance(y, complex):
        raise ValueError("Imaginary numbers are not accepted.")
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Given input must be a real number.")

    # Actual exercise
    if 5 < math.sqrt((x * x) + (y * y)) <= 10:
        return 1
    if 1 < math.sqrt((x * x) + (y * y)) <= 5:
        return 5
    if math.sqrt((x * x) + (y * y)) <= 1:
        return 10
    return 0
