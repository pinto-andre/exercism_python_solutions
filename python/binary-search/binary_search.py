from typing import List

def find(search_list: List, value: int) -> int:
    """
    Function that finds an item in a list by repeatedly splitting it in half,
    only keeping the half which contains the item we're looking for.
    """
    left, right = 0, len(search_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if search_list[mid] == value:
            return mid
        if search_list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    raise ValueError("value not in array")
