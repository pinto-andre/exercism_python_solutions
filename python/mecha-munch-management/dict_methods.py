"""Functions to manage a users shopping cart items."""
from typing import Dict, Iterable
from collections import defaultdict

def add_item(current_cart: Dict[str, int], items_to_add: Iterable[str]) -> Dict[str, int]:
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    # Make a copy to not mess with the original, this way the original is always intact
    updated_cart = current_cart.copy()

    for item in items_to_add:
        if item in updated_cart:
            updated_cart[item] += 1
        else:
            updated_cart[item] = 1

    return updated_cart



def read_notes(notes: Iterable) -> Dict[str, int]:
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    shopping_cart = defaultdict(int)
    for item in notes:
        shopping_cart[item] += 1
    return shopping_cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    updated_ideas = ideas.copy()
    for plate, recipe in recipe_updates:
        updated_ideas[plate] = recipe

    return updated_ideas


def sort_entries(cart: Dict[str, int]) -> Dict[str, int]:
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return {item: cart[item] for item in sorted(cart)}


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment_cart = {}
    
    for item, quantity in cart.items():
        if item in aisle_mapping:
            aisle, refrigeration = aisle_mapping[item]
            fulfillment_cart[item] = [quantity, aisle, refrigeration]
    
    # Sort the items in reverse alphabetical order
    sorted_fulfillment_cart = {
        item: fulfillment_cart[item] for item in sorted(fulfillment_cart, reverse=True)
    }
    
    return sorted_fulfillment_cart


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    updated_store_inventory = store_inventory.copy()

    for item, specs in store_inventory.items():
        if item not in fulfillment_cart:
            updated_store_inventory[item] = specs
        else:
            new_quantity = specs[0] - fulfillment_cart[item][0]
            updated_store_inventory[item][0] = max(new_quantity, 0)
            if updated_store_inventory[item][0] == 0:
                updated_store_inventory[item][0] = "Out of Stock"
    return updated_store_inventory
