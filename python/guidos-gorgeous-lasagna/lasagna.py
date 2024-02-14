"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# EXPECTED_BAKE_TIME constant defines the number of minutes the lasagna should be in the
# oven
EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the lasagna layering time.

    :param number_of_layers: int - number of layers Guido wants in the lasagna
    :return: int - total time passed (in minutes) preparing the lasagna

    This function takes one integer representing the number of layers the lasagna and
    calculates the total time spent layering."""

    preparation_time = number_of_layers * 2
    return preparation_time


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the lasagna layering time.

    :param number of layers: int - number of layers Guido wants in the lasagna
    :param elapsed_bake_time: int - elapsed cooking time
    :return: int - total time passed (in minutes) making the lasagna

    This function takes two integers representing the number of layers the lasagna has
    and the elapsed baking time, calculates the total time spent making the lasagna"""

    preparation_time = preparation_time_in_minutes(number_of_layers)
    return elapsed_bake_time + preparation_time
