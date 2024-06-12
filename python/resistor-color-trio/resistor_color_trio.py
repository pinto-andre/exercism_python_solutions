"""Function that takes 3 colors as input, and outputs the correct value, in ohms. """
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

def label(colors: List[str]) -> int:
    if len(colors) > 3:
        colors = colors[0:3]

    first_digit = COLOUR_VALUES[colors[0]]
    second_digit = COLOUR_VALUES[colors[1]]
    multiplier = COLOUR_VALUES[colors[2]]

    resistance_value = (first_digit * 10 + second_digit) * (10 ** multiplier)
    if resistance_value >= 1000000000:
        return f"{int(resistance_value / 1000000000)} gigaohms"
    elif resistance_value >= 1000000:
        return f"{int(resistance_value / 1000000)} megaohms"
    elif resistance_value >= 1000:
        return f"{int(resistance_value / 1000)} kiloohms"
    else:
        return f"{resistance_value} ohms"
