from math import pi

from lab_python_oop.colour import Colour
from lab_python_oop.shape import Shape


class Circle(Shape):
    SHAPE_NAME = "Круг"

    def __init__(self, radius, colour):
        self.radius = radius
        self.colour = Colour(colour)

    def __str__(self):
        return "{}. Цвет: {}. Площадь: {}.".format(self.SHAPE_NAME, self.colour, self.area())

    def area(self):
        return pi * self.radius ** 2
