#!/usr/bin/python3

def no_c(my_string):
    """
    Removes all characters c and C from a string

    Args:
        my_string: string

    Return:
        String
    """
    return "".join([c if c not in "cC" else "" for c in list(my_string)])
