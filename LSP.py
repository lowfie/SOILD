# ------------- LSP ------------- #
# It should be possible to substitute any of its descendant classes instead of the base type

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def __str__(self):
        return f"width {self.width} height: {self.height}"

    @property
    def area(self):
        return self._height * self._width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    # direct violation LSP
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    # direct violation LSP
    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f"Expected an area of {expected}, got {rc.area}")


rc = Rectangle(2, 3)
use_it(rc)

# bad realization
sq = Square(5)
use_it(sq)
