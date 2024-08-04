""" Function to get Collatz Conjecture working"""
def steps(number: int) -> int:
    """ Function to get Collatz Conjecture working
    :param number: int - number on which to apply the collatz conjecture
    :returns count: int - number of steps until the number gets to 1."""
    if number <= 0 or not isinstance(number, int):
        raise ValueError("Only positive integers are allowed")

    new_number = number
    count = 1
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    new_number = number
    count = 0  # Start the count at 0

    while new_number != 1: # Endless loop since we don't know how many steps Collatz will create
        if new_number % 2 == 0:
            new_number = new_number // 2  # Use integer division
        else:
            new_number = new_number * 3 + 1
        count += 1

    return count
