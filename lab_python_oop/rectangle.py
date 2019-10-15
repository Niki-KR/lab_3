from lab_python_oop.colour import Colour
from lab_python_oop.shape import Shape


class Rectangle(Shape):
    SHAPE_NAME = "Прямоугольник"

    def __init__(self, width, height, colour):
        self.width = width
        self.height = height
        self.colour = Colour(colour)

    def __str__(self):
        return "{}. Цвет: {}. Площадь: {}.".format(self.SHAPE_NAME, self.colour, self.area())

    def area(self):
        return self.width * self.height
