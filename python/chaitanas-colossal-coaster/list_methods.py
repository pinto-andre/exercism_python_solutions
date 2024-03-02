"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(
    express_queue: list[str],
    normal_queue: list[str],
    ticket_type: int,
    person_name: str,
) -> list[str]:
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue: list - names in the normal queue.
    :param ticket_type: int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    :raises: ValueError - Invalid ticket type, only 0 and 1 are accepted
    :raises: TypeError - Person name must be a string
    """
    # Self improved validation
    if ticket_type not in (0, 1):
        raise ValueError("Invalid ticket type, only 0 and 1 are accepted")
    if not isinstance(person_name, str):
        raise TypeError("Person name must be a string")
    # Actual exercise
    updated_queue = []
    if ticket_type == 0:
        updated_queue.extend(normal_queue)
        updated_queue.append(person_name)
    if ticket_type == 1:
        updated_queue.extend(express_queue)
        updated_queue.append(person_name)
    return updated_queue


def find_my_friend(queue: list[str], friend_name: str) -> int:
    """Search the queue for a name and return their queue position (index).

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    :raises: TypeError - Invalid friend_name, please make sure its type is a string
    """
    if not isinstance(friend_name, str):
        raise TypeError("Invalid friend_name, please make sure its type is a string")
    return queue.index(friend_name)


def add_me_with_my_friends(queue: list[str], index: int, person_name: str) -> list[str]:
    """Insert the late arrival's name at a specific index of the queue.

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    :raises: TypeError - Please make sure to input the correct data
    """
    if not isinstance(index, int) or not isinstance(person_name, str):
        raise TypeError("Please make sure to input the correct data")
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue: list[str], person_name: str) -> list[str]:
    """Remove the mean person from the queue by the provided name.

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return: list - queue update with the mean persons name removed.
    """
    queue.remove(person_name)
    return queue


def how_many_namefellows(queue: list[str], person_name: str) -> int:
    """Count how many times the provided name appears in the queue.

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return: int - the number of times the name appears in the queue.
    """
    number_of_occurrences = queue.count(person_name)
    return number_of_occurrences


def remove_the_last_person(queue: list[str]) -> str:
    """Remove the person in the last index from the queue and return their name.

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """
    return queue.pop()


def sorted_names(queue: list[str]) -> list[str]:
    """Sort the names in the queue in alphabetical order and return the result.

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """
    sorted_queue = sorted(queue)
    return sorted_queue
