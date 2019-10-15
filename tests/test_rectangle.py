import unittest

from lab_python_oop import shape, colour, rectangle


class RectangleTests(unittest.TestCase):
    def setUp(self):
        self.rectangle = rectangle.Rectangle(2, 2, "Красный")

    def test_rectangle_subclass_of_shape(self):
        self.assertIsInstance(self.rectangle, shape.Shape)

    def test_rectangle_colour_property_is_instance_of_colour_class(self):
        self.assertIsInstance(self.rectangle.colour, colour.Colour)

    def test_rectangle_shape_name(self):
        self.assertEqual(self.rectangle.SHAPE_NAME, "Прямоугольник")

    def test_rectangle_area(self):
        self.assertEqual(self.rectangle.area(), 4)
