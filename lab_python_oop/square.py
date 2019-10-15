from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    SHAPE_NAME = "Квадрат"

    def __init__(self, side, colour):
        super().__init__(side, side, colour)
