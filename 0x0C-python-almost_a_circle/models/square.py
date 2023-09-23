#!/usr/bin/python3

"""Defines a Square class."""

from models.rectangle import Rectangle

"""The Square class inherits from Rectangle class"""

class Square(Rectangle):

    """class constructor"""

    def __init__(self, size, x=0, y=0, id=None):

        """assigns it the attribute of the Rectangle class
        a square is a rectangle with the same width and size so you must not assign new attributes ti the square class"""

        super().__init__(size, size, x, y, id)
    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):

        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

"""The overloading __str__ method should return [Square] (<id>) <x>/<y> - <size> - in our case, width or height"""
    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)


