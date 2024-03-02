"""Function to classify a number if perfect or not"""


def classify(number: int) -> str | None:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    :raises: ValueError - Classification is only possible for positive integers.
    :raises: ValueError - Classification is only possible for positive integers.
    """
    # Self improved validation
    if not isinstance(number, int) or isinstance(number, bool):
        raise ValueError("Classification is only possible for positive integers.")
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    # Actual exercise
    perfect_list = []
    for item in range(1, number):
        if number % item == 0:
            perfect_list.append(item)

    if sum(perfect_list) == number:
        return "perfect"
    if sum(perfect_list) < number:
        return "deficient"
    if sum(perfect_list) > number:
        return "abundant"
    return None
