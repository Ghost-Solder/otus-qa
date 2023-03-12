from math import sqrt

import pytest

from src.Square import Square
from src.Triangle import Triangle


class TestTriangle:
    """Tests for class Triangle."""

    side1 = 1
    side2 = 2
    side3 = 2.5
    perimeter = side1 + side2 + side3
    p_half = perimeter / 2
    area = sqrt(p_half * (p_half - side1) * (p_half - side2) * (p_half - side3))
    triangle = Triangle(side1, side2, side3)

    def test_base_attrs(self):
        assert self.triangle.name == 'Triangle'
        assert self.triangle.side1 == self.side1
        assert self.triangle.side2 == self.side2
        assert self.triangle.side3 == self.side3

    def test_area(self):
        assert self.triangle.area == self.area

    def test_perimeter(self):
        assert self.triangle.perimeter == self.perimeter

    def test_add_area(self):
        side = 1.5
        square = Square(side)
        assert self.triangle.add_area(square) == (self.area + side * side)
        with pytest.raises(ValueError):
            self.triangle.add_area(side)

    def test_creation(self):
        with pytest.raises(ValueError):
            Triangle(1, 2, 3)
