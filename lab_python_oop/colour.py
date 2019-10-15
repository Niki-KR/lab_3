class Colour:
    def __init__(self, colour=None):
        self._colour = colour

    def get_colour(self):
        return self._colour

    def set_colour(self, colour):
        self._colour = colour

    def del_colour(self):
        del self._colour

    def __str__(self):
        return str(self._colour)

    c = property(get_colour, set_colour, del_colour, "This is the colour property.")
