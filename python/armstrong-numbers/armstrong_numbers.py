""" Single function to determine whether a given number is an Armstrong number or not.
"""
def is_armstrong_number(number):
    """Function to determine if a given number is an Armstrong number or not.
    """
    if not isinstance(number, int):
        raise ValueError("Function only accepts integer numbers.")
    
    number_array = str(number)
    power_for_armstrong_calculus = len(number_array)
    sum_of_powers = 0

    for num in number_array:
        sum_of_powers += int(num)**power_for_armstrong_calculus

    return sum_of_powers == number
