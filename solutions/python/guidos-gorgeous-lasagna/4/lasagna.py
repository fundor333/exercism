"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_layer: int):
    """Calculate the preparation time.

    :param number_layer: int -number of the layers.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    return PREPARATION_TIME * number_layer


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed timee.

    :param number_layer: int -number of the layers.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes).
    """
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)
