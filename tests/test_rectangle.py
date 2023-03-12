import pytest

from src.Rectangle import Rectangle
from src.Square import Square


class TestRectangle:
    """Tests for class Rectangle."""

    length = 1.5
    width = 2.5
    rect = Rectangle(length, width)

    def test_base_attrs(self):
        assert self.rect.name == 'Rectangle'
        assert self.rect.length == self.length
        assert self.rect.width == self.width

    def test_area(self):
        assert self.rect.area == (self.length * self.width)

    def test_perimeter(self):
        assert self.rect.perimeter == (2 * self.length + 2 * self.width)

    def test_add_area(self):
        side = 1.5
        square = Square(side)
        assert self.rect.add_area(square) == (self.length * self.width + side * side)
        with pytest.raises(ValueError):
            self.rect.add_area(side)
