"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*n):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return list(n)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    f, s, locomotive, *rest = each_wagons_id
    return [locomotive, *missing_wagons, *rest, f,s]


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    Returns:
        dict: The updated route dictionary.
    """
    if "stops" not in route:
        route["stops"] = []
        
    for stop_name in kwargs.values():
        route["stops"].append(stop_name)
            
    return route



    


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    for i in more_route_information:
        if i not in route.keys():
            route[i]=more_route_information[i]
    return route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    return list(map(list, zip(*wagons_rows)))
    
