"""Function that takes two colour names as input and output a two digit number, even if
the input is more than two colors"""
from typing import List

COLOUR_VALUES = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9,
    }

def value(colors: List[str]) -> int:
    """ Function to return the colour code of two colour combination. """
    colour_value = ""
    for color in colors:
        colour_value += str(COLOUR_VALUES.get(color))
    if len(colour_value) > 2:
        return int(colour_value[0:2])
    return int(colour_value)
