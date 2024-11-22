from typing import List

def rebase(input_base: int, digits: List[int], output_base: int) -> List[int]:
    """
    Function to translate between bases.
    """
    if not isinstance(input_base, int) or not isinstance(output_base, int):
        raise ValueError("Input_base and output_base must be integers")
    if not isinstance(digits, List):
        raise ValueError("digits must be a list of integers")
    # Validate arguments
    if input_base <= 1:
        raise ValueError("input base must be >= 2")
    if output_base <= 1:
        raise ValueError("output base must be >= 2")
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    # Convert from input base to base 10
    decimal_value = 0
    for digit in digits:
        decimal_value = decimal_value * input_base + digit
    # Convert from base 10 to output base
    if decimal_value == 0:
        return [0]
    output_digits = []
    while decimal_value > 0:
        output_digits.append(decimal_value % output_base)
        decimal_value //= output_base
    # Reverse digits to get the correct order
    return output_digits[::-1]
