#!/usr/bin/python3
"""
this module includes a function that adds
two integers and returns the sum
"""


def add_integer(a, b=98):
    """
        adds and returns the sum of two integers.

    Args:
        a (int): The first number.
        b (int, optional): The second number.
        If a float is passed, it is typecasted to an int

    Returns:
        int: The sum of the two integers.
    """

    if (not isinstance(a, int)) and (not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int)) and (not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
