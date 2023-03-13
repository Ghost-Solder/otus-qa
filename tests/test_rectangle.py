import pytest

from src.Rectangle import Rectangle
from src.Square import Square


@pytest.mark.parametrize(
    'length, width, area, perimeter, figure, common_area',
    [
        (1, 1, 1, 4, Square(1), 2),
        (1.5, 2, 3, 7, Square(1.55), 5.4),
        (1.59, 2.65, 4.21, 8.48, Square(1.55), 6.62),
    ]
)
def test_base_attrs(
        length: float,
        width: float,
        area: float,
        perimeter: float,
        figure: object,
        common_area: float,
):
    rectangle = Rectangle(length, width)
    assert rectangle.name == 'Rectangle'
    assert rectangle.length == length
    assert rectangle.width == width
    assert round(rectangle.area, 2) == area
    assert round(rectangle.perimeter, 2) == perimeter
    assert round(rectangle.add_area(figure), 2) == common_area


@pytest.mark.parametrize(
    'length, width',
    [
        (0, 1),
        (1, 0),
        (-1, 1),
        (1, -1),
        ('str', 1),
        (1, 'str'),
    ]
)
def test_negative_creation(length: float, width: float):
    with pytest.raises(ValueError):
        Rectangle(length, width)


@pytest.mark.parametrize('non_figure', [0, 1, -1, 'str'])
def test_negative_add_area(non_figure: object):
    rectangle = Rectangle(1, 1)
    with pytest.raises(ValueError):
        rectangle.add_area(non_figure)
