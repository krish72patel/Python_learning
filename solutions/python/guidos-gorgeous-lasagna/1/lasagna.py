EXPECTED_BAKE_TIME = 40


def bake_time_remaining(time):
    """Return the remaining baking time in minutes."""
    return EXPECTED_BAKE_TIME - time


def preparation_time_in_minutes(number_of_layers):
    """Return the preparation time based on the number of layers."""
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time.

    Parameters:
        number_of_layers (int): The number of lasagna layers.
        elapsed_bake_time (int): Time the lasagna has been baking.

    Returns:
        int: Total elapsed time for preparation and baking.
    """
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)
