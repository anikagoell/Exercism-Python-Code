EXPECTED_BAKE_TIME=40
PREPARATION_TIME=70

def bake_time_remaining(elapsed_time):
    """ Checking for the time"""
    return EXPECTED_BAKE_TIME - elapsed_time
    

def preparation_time_in_minutes(number_of_layers):
    """Calc prep time"""
    return 2 * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Runing func"""
    return preparation_time_in_minutes(number_of_layers)+elapsed_bake_time



