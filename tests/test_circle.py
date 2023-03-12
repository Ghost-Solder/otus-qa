from math import pi

import pytest

from src.Circle import Circle
from src.Square import Square


class TestCircle:
    """Tests for class Rectangle."""
    radius = 1.5
    circle = Circle(radius)

    def test_base_attrs(self):
        assert self.circle.name == 'Circle'
        assert self.circle.radius == self.radius

    def test_area(self):
        assert self.circle.area == pi * self.radius * self.radius

    def test_perimeter(self):
        assert self.circle.perimeter == (2 * pi * self.radius)

    def test_add_area(self):
        side = 1.5
        square = Square(side)
        assert self.circle.add_area(square) == (pi * self.radius * self.radius + side * side)
        with pytest.raises(ValueError):
            self.circle.add_area(side)
