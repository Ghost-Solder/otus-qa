import pytest

from src.Square import Square
from src.Triangle import Triangle


@pytest.mark.parametrize(
    'side1, side2, side3, area, perimeter, figure, common_area',
    [
        (1, 2, 2.5, 0.95, 5.5, Square(1), 1.95),
        (1.5, 1.5, 2, 1.12, 5, Square(1.55), 3.52),
        (1.59, 1.59, 1.59, 1.09, 4.77, Square(1.55), 3.5),
    ]
)
def test_base_attrs(
        side1: float,
        side2: float,
        side3: float,
        area: float,
        perimeter: float,
        figure: object,
        common_area: float,
):
    triangle = Triangle(side1, side2, side3)
    assert triangle.name == 'Triangle'
    assert triangle.side1 == side1
    assert triangle.side2 == side2
    assert triangle.side3 == side3
    assert round(triangle.area, 2) == area
    assert round(triangle.perimeter, 2) == perimeter
    assert round(triangle.add_area(figure), 2) == common_area


@pytest.mark.parametrize(
    'side1, side2, side3',
    [
        (1, 2, 3),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0),
        ('str', 1, 1),
        (1, 'str', 1),
        (1, 1, 'str'),
        (-1, 1, 1),
        (1, -1, 1),
        (1, 1, -1),
    ]
)
def test_negative_creation(side1: float, side2: float, side3: float):
    with pytest.raises(ValueError):
        Triangle(side1, side2, side3)


@pytest.mark.parametrize('non_figure', [0, 1, -1, 'str'])
def test_negative_add_area(non_figure: object):
    triangle = Triangle(1, 1, 1)
    with pytest.raises(ValueError):
        triangle.add_area(non_figure)
