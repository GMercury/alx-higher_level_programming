#!/usr/bin/python3
"""
    Module containing the `is_same_class` function.
"""


def is_same_class(obj, a_class):
    """Check if `obj` is an exact instance of `a_class`.
    Args:
        obj: An object.
        a_class: A class.
    Returns: True if `obj` is an exact instance a `a_class`, otherwise False.
    """
    return (type(obj) is a_class)
