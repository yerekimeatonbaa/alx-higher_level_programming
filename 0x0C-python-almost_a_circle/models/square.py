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

"""The overloading __str__ method should return [Square] (<id>) <x>/<y> - <size> - in our case, width or height"""

    def __str__(self):
    return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Width must be a positive integer")
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
