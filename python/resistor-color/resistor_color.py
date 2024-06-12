"""Functions to return the numerical value associated with a particular color band"""
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
def color_code(color: str) -> int:
    """Function to return the numeric value for a respective colour"""
    if not color in COLOUR_VALUES:
        raise ValueError("The inserted value has no correspondence")
    return COLOUR_VALUES.get(color)


def colors() -> List[str]:
    """Function to return the list of possible colours"""
    return [
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'grey',
    'white',
    ]
