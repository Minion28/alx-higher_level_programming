#!/usr/bin/python3
"""Integer validator"""


class BaseGeometry:
    """A Base Geometry class"""

    def area(self):
        #Raises an exception
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the inputs: name and values
        """
        if type(value) not in [int]:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation of width and height"""
        self.integer_validator(width, height)
        self.__width = width
        self.__height = height
