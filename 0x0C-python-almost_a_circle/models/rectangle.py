#!/usr/bin/python3
"""Rectangle 1"""
from models.base import Base


class Rectangle(Base):
    """A rectangle class that inherits from the base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructs the rectange's attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the Width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the Width (private) of the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height (private) of the rectangle"""
        return self.__height

    @width.setter
    def height(self, value):
        """Sets the height(private) of the rectangle"""
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x value"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the x value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y value"""
        if type(value) not in [int]:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Draw area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """print in stdout the Rectangle instance with the character #"""
        print("\n" * self.y,  end="")
        print((" " * self.x + "#" * self.__width + '\n') * self.__height, end="")

    def __str__(self):
        """String representation of rectangle class"""
        str_res = "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.__width, self.__height)
        return str_res

    def update(self, *args, **kwargs):
        """Updates rectangle class and assigns an argument to each attribute"""
        if not args and not kwargs:
            return
        if args is not None:
            attributes = ["id", "width", "height", "x", "y"]
            for i, j in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], j)
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """Return the dictionary representation of a rectangle"""
        _map = {}
        for key, value in self.__dict__.items():
            if key.startswith("_"):
                _map[key.split("__")[-1]] = value
            else:
                _map[key] = value
        return _map
