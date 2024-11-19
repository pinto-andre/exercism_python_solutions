from typing import Iterable, List


def flatten(iterable: Iterable) -> List:
    """
    Function that accepts an arbitrarily-deep nested list-like structure
    and returns a flattened structure without any nil/null values
    """
    flatten_list = []
    for item in iterable:
        if isinstance(item, (list, tuple, set)):
            flatten_list.extend(flatten(item))
        elif item is not None:
            flatten_list.append(item)
    return flatten_list
