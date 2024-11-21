"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it's memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

from typing import List, Literal

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(list_one: List, list_two: List) -> Literal["SUBLIST", "SUPERLIST", "EQUAL", "UNEQUAL"]:
    # Taking care of both lists being inexistent / empty
    if not list_one and not list_two:
        return EQUAL
    # An empty list is always a sublist of any list
    if not list_one and list_two:
        return SUBLIST
    # Any list is a superlist of an empty list
    if not list_two and list_one:
        return SUPERLIST

    # Taking care of equality which also considers order
    if list_one == list_two:
        return EQUAL

    # Given two different lists, checking if list_one contains list_two
    list_two_len = len(list_two)
    if any(
        list_one[i:i + list_two_len] == list_two for i in range(len(list_one) - list_two_len + 1)
    ):
        return SUPERLIST

    # Given two different lists, checking if list_one is contained by list_two
    list_one_len = len(list_one)
    if any(
        list_two[i:i + list_one_len] == list_one for i in range(len(list_two) - list_one_len + 1)
    ):
        return SUBLIST

    # The provided lists are neither equal, sublists, nor superlists
    return UNEQUAL
