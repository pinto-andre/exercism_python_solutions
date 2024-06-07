"""Functions to keep track and alter inventory."""
from typing import List, Tuple, Dict

def create_inventory(items: List[str]) -> Dict[str, int]:
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    :raises: TypeError - Argument has to be a list data type.
    """
    if not isinstance(items, List):
        raise TypeError("Argument has to be a list data type.")
    return {item: items.count(item) for item in items}


def add_items(inventory: Dict[str, int], items: List[str]) -> Dict[str, int]:
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    :raises: TypeError - Inventory must be a dictionary and items must be a list.
    """
    if not isinstance(inventory, Dict) or not isinstance(items, List):
        raise TypeError("Inventory must be a dictionary and items must be a list.")

    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def decrement_items(inventory: Dict[str, int], items: List[str]) -> Dict[str, int]:
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    :raises: TypeError - Inventory must be a dictionary and items must be a list.
    """
    if not isinstance(inventory, Dict) or not isinstance(items, List):
        raise TypeError("Inventory must be a dictionary and items must be a list.")

    for item in items:
        if item not in inventory:
            continue
        inventory[item] -= 1
        # max() defines bottom between two values (floor, ceil)
        # min() defines ceiling between two values (floor, ceil)
        inventory[item] = max(0, inventory[item])
    return inventory


def remove_item(inventory: Dict[str, int], item: str) -> Dict[str, int]:
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    :raises: TypeError - Inventory must be a dictionary and items must be a list.
    """
    if not isinstance(inventory, Dict) or not isinstance(item, str):
        raise TypeError("Inventory must be a dictionary and items must be a list.")

    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory: Dict[str, int]) -> List[Tuple[str, int]]:
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    :raises: TypeError - Inventory must be a dictionary data type.
    """
    if not isinstance(inventory, Dict):
        raise TypeError("Inventory must be a dictionary data type.")

    return [(key, value) for key, value in inventory.items() if value != 0]
