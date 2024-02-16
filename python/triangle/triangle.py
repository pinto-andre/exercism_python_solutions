""" Types of triangles, below we find three functions capable of determining if a given
 triangle is equilateral, isosceles or scalene
"""

from typing import List

def equilateral(sides: List[int | float]) -> bool:
    """ Function to determine if a triangle is equilateral or not.

    :param sides: List[str] - sides of a given triangle
    :return: bool - True or False whether it's an equilateral or not.
    """
    if len(sides) != 3 or sides[0] == 0 or sides[1] == 0 or sides[2] == 0:
        return False

    return sides[0] == sides[1] == sides[2]


def isosceles(sides: List[int | float]) -> bool:
    """ Function to determine if a triangle is isosceles or not.

    :param sides: List[str] - sides of a given triangle
    :return: bool - True or False whether it's an isosceles or not.
    """
    if len(sides) != 3:
        return False

    # Check if any two sides are equal
    if sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]:
        # Check triangle inequality
        if (sides[0] + sides[1] > sides[2] and sides[1] + sides[2] > sides[0] and
            sides[2] + sides[0] > sides[1]):
            return True

    return False



def scalene(sides: List[int | float]) -> bool:
    """ Function to determine if a triangle is scalene or not.

    :param sides: List[str] - sides of a given triangle
    :return: bool - True or False whether it's an scalene or not.
    """
    if len(sides) != 3:
        return False

    a, b, c = sorted(sides)
    if a + b <= c:
        return False

    if sides[0] != sides[1] and sides[1] != sides[2] and sides[2] != sides[0]:
        return True
    return False
