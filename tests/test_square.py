import unittest

from lab_python_oop import shape, colour, square, rectangle


class SquareTests(unittest.TestCase):
    def setUp(self):
        self.square = square.Square(2, "Красный")

    def test_square_subclass_of_shape(self):
        self.assertIsInstance(self.square, shape.Shape)

    def test_square_subclass_of_rectangle(self):
        self.assertIsInstance(self.square, rectangle.Rectangle)

    def test_square_colour_property_is_instance_of_colour_class(self):
        self.assertIsInstance(self.square.colour, colour.Colour)

    def test_square_shape_name(self):
        self.assertEqual(self.square.SHAPE_NAME, "Квадрат")

    def test_square_area(self):
        self.assertEqual(self.square.area(), 4)
