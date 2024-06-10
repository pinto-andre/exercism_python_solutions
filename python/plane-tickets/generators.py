"""Functions to automate Conda airlines ticketing system."""
from typing import Generator, List, Dict

def generate_seat_letters(number: int) -> Generator:
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    SEAT_LETTERS = ['A', 'B', 'C', 'D']
    for index in range(number):
        yield SEAT_LETTERS[index % len(SEAT_LETTERS)]


def generate_seats(number: int) -> Generator:
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    SEAT_LETTERS = ['A', 'B', 'C', 'D']
    row = 1
    for index in range(number):
        if row == 13:
            row += 1
        yield f'{row}{SEAT_LETTERS[index % 4]}'

        if (index + 1) % 4 == 0:
            row += 1

def assign_seats(passengers: List[str]) -> Dict[str, str]:
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    passenger_seats = list(generate_seats(len(passengers)))
    assigned_seats = dict(zip(passengers, passenger_seats))
    return assigned_seats

def generate_codes(seat_numbers: List[str], flight_id: str) -> Generator:
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    seat_number_with_flight_id = ""
    for seat in seat_numbers:
        seat_number_with_flight_id = seat + flight_id
        while len(seat_number_with_flight_id) < 12:
            seat_number_with_flight_id += "0"
        yield seat_number_with_flight_id
