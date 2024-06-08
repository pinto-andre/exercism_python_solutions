"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*number_of_wagons):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(number_of_wagons)


def fix_list_of_wagons(each_wagons_id: list, missing_wagons: list) -> list:
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    list_transformer = each_wagons_id[2:]
    list_transformer.insert(1, missing_wagons)
    list_transformer.extend(each_wagons_id[:2])

    final_list = []
    for item in list_transformer:
        if isinstance(item, list):
            for arg in item:
                final_list.append(arg)
            continue
        final_list.append(item)
    return final_list


def add_missing_stops(route, **number_stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    updated_route = route.copy()
    updated_route["stops"] = list(number_stops.values())
    return updated_route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    route.update(more_route_information)
    return route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    fixed_rows = [list(row) for row in zip(*wagons_rows)]
    return fixed_rows
