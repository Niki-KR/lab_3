import unittest

from math import pi

from lab_python_oop import shape, circle, colour


class CircleTests(unittest.TestCase):
    def setUp(self):
        self.radius = 2
        self.circle = circle.Circle(self.radius, "Синий")

    def test_circle_subclass_of_shape(self):
        self.assertIsInstance(self.circle, shape.Shape)

    def test_circle_colour_property_is_instance_of_colour_class(self):
        self.assertIsInstance(self.circle.colour, colour.Colour)

    def test_circle_shape_name(self):
        self.assertEqual(self.circle.SHAPE_NAME, "Круг")

    def test_circle_area(self):
        self.assertEqual(self.circle.area(), pi * self.radius ** 2)