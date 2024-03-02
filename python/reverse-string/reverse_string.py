"""Function to reverse strings"""


def reverse(text: str) -> str:
    """Function returns the reverse of a given string

    :param test: str - Given string we wish to reverse.
    :return: str - Reversed string
    :raises: TypeError - Function only accepts strings as args.
    """
    if not isinstance(text, str):
        raise TypeError("Function only accepts strings as arguments.")

    return text[::-1]
