"""Function to determine if a given year is a leap year or not.
"""

def leap_year(year: int) -> bool:
    """Function that determines if a given year is a leap year or not
    
    :param year: int - given year to determine if is leap
    :return: bool - True if it's a leap year, and False otherwise
    """
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
