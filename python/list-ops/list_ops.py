"""Functions to return severall list methods"""
from typing import Any, Callable, List

def append(list1: List, list2: List) -> List:
    """
    Function to add all items in the second list 
    to the end of the first list
    """
    # First approach
    # full_list = list1.copy()
    # for item in list2:
    #     full_list.append(item)
    # return full_list

    return list1 + list2


def concat(lists: List[List]) -> List:
    """
    Function to combine all items in all lists 
    into one flattened list
    """
    flat_list = [item for sublist in lists for item in sublist]
    return flat_list


def filter(function: Callable, list: List) -> List:
    """
    Function to return the list of all items 
    for which `predicate(item)` is True
    """
    return [item for item in list if function(item)]


def length(list: List) -> int:
    """
    Function to return the total number of items within a list
    """
    return len(list)


def map(function: Callable, list: List) -> List:
    """
    Function to return the list of the results
    of applying `function(item)` on all items
    """
    return [function(item) for item in list]


def foldl(function: Callable, list: List, initial: Any) -> Any:
    """
    It's a function that 
    Given a function, a list, and initial accumulator, 
    fold (reduce) each item into the accumulator 
    from the left
    """
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function: Callable, list: List, initial: Any) -> Any:
    """
    It's a function that 
    Given a function, a list, and an initial accumulator,
    Fold (reduce) each item into the accumulator
    from the right
    """
    accumulator = initial
    for item in reversed(list):
        accumulator = function(accumulator, item)
    return accumulator


def reverse(list: List) -> List:
    """
    Function to return a list with all the original items,
    but in reversed order
    """
    return [item for item in reversed(list)]
