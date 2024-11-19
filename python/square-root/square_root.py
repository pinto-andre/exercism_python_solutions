def square_root(number: int) -> int:
    """
    Function to find the square root of any natural number (positive integer)
    without using Pythons built-ins such as 
    the exponentiation operator `**`,
    [`pow()`][pow]
    and [`sum()`][sum]
    """
    for i in range(0, number + 1):
        if i * i == number:
            return i
