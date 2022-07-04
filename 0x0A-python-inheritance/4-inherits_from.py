#!/usr/bin/python3
"""
    Module containing the `inherits_from` function.
"""


def inherits_from(obj, a_class):
    """Check if `obj` is an instance of a class that has `a_class` as a
    superclass but not an instance of `a_class` itself.
    Args:
        obj: An object.
        a_class: A class.
    Returns: True if `obj` is an instance of a subclass of `a_class`,
    otherwise False.
    """
    return (isinstance(obj, a_class) and (type(obj) is not a_class))
