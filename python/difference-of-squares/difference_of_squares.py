def square_of_sum(number: int) -> int:
    if not isinstance(number, int):
        raise TypeError('Number must be an integer value')
    result = 0
    for i in range(1, number + 1):
        result += i
    return result**2


def sum_of_squares(number: int) -> int:
    if not isinstance(number, int):
        raise TypeError('Number must be an integer value')
    result = 0
    for i in range(1, number + 1):
        result += i**2
    return result


def difference_of_squares(number: int) -> int:
    if not isinstance(number, int):
        raise TypeError('Number must be an integer value')
    return square_of_sum(number) - sum_of_squares(number)
