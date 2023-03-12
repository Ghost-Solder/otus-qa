import pytest

from src.Square import Square


class TestSquare:
    """Tests for class Square."""

    side = 1.5
    square = Square(side)

    def test_base_attrs(self):
        assert self.square.name == 'Square'
        assert self.square.length == self.side
        assert self.square.width == self.side

    def test_area(self):
        assert self.square.area == (self.side * self.side)

    def test_perimeter(self):
        assert self.square.perimeter == (4 * self.side)

    def test_add_area(self):
        side = 2.5
        square = Square(side)
        assert self.square.add_area(square) == (self.side * self.side + side * side)
        with pytest.raises(ValueError):
            self.square.add_area(side)
