#!/usr/bin/python3
"""
    Module containing the `Rectangle` class that inherits the `BaseGeometry`
    class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from the `BaseGeometry` class.
    """

    def __init__(self, width, height):
        """Initializes the Rectangle instance.
        Args:
            width (int): `width` of the `Rectangle` instance.
            heigth (int): `height` of the `Rectangle` instance.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
