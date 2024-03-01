"""Function to convert raindrops into sounds"""


def convert(number: int) -> str:
    """Function to convert the number of raindrops into speific sounds according to
    their divisibility.

    :param number: int - Given number of raindrops
    :return: str - Sound of raindrops or if there's no possible divisibility returns the
    stringified number.
    :raises: ValueError - Number value must be a positive integer"""
    # Validation for integers (Code self-improvement out of exercism)
    if not isinstance(number, int) or number < 0:
        raise ValueError("Number value must be a positive integer")

    # Actual exercise
    stringified_number = ""
    if number % 3 == 0:
        stringified_number += "Pling"
    if number % 5 == 0:
        stringified_number += "Plang"
    if number % 7 == 0:
        stringified_number += "Plong"
    if stringified_number == "":
        stringified_number += str(number)
    return stringified_number
