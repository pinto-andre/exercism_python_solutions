""" Function to determine if the given isbn is valid."""


def is_valid(isbn: str) -> bool:
    """Function to determine if the given isbn is valid.

    :param isbn: str - Given string to test
    :return: bool - True if valid, False otherwise
    :raise: TypeError - Please input argument as a string data type.
    """
    # Extra self validation
    if not isinstance(isbn, str):
        raise TypeError("Please input argument as a string data type.")

    # Actual exercise
    split_isbn = isbn.replace("-", "")

    # Validation the only acceptable length
    if len(split_isbn) != 10:
        return False

    isbn_validation = 0
    multiplier = 10
    # Since "X" is valid as a check character if it is at the end, we need to validate
    # that as well
    for i, char in enumerate(split_isbn):
        if char == "X" and i == 9:
            numeric_char = 10
        elif char.isdigit():
            numeric_char = int(char)
        else:
            return False

        isbn_validation += numeric_char * multiplier
        # At the end of each iteration the multiplier decreases by one
        multiplier -= 1

    return isbn_validation % 11 == 0
