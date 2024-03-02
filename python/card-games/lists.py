"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number: int) -> list[int]:
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    :raises: ValueError - Only positive integers are allowed.
    """
    if number < 0 or isinstance(number, float):
        raise ValueError("Only positive integers are allowed")
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int] :
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds: list[int], number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand: list[int]) -> float:
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand: list[int]) -> bool:
    """Return if an average is using (first + last index values ) OR ('middle' card) == 
    calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    min_max_method = (hand[0] + hand[len(hand) - 1]) / 2
    median_method = hand[len(hand) // 2]
    return min_max_method == card_average(hand) or median_method == card_average(hand)


def average_even_is_average_odd(hand: list[int]) -> bool:
    """Return if the (average of even indexed card values) == (average of odd indexed
    card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    :raises: ValueError - Hand must have more than one element
    """
    if len(hand) <= 1:
        raise ValueError("Hand must have more than one element")
    even_hand = hand[0::2]
    odd_hand = hand[1::2]
    return card_average(even_hand) == card_average(odd_hand)


def maybe_double_last(hand: list[int]) -> list[int]:
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[len(hand) - 1] == 11:
        hand[len(hand) - 1] = hand[len(hand) - 1] * 2
    return hand
