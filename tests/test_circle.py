import pytest

from src.Circle import Circle
from src.Square import Square


@pytest.mark.parametrize(
    'radius, area, perimeter, figure, common_area',
    [
        (1, 3.14, 6.28, Square(1), 4.14),
        (1.5, 7.07, 9.42, Square(1.55), 9.47),
    ]
)
def test_base_attrs(
        radius: float,
        area: float,
        perimeter: float,
        figure: object,
        common_area: float,
):
    circle = Circle(radius)
    assert circle.name == 'Circle'
    assert circle.radius == radius
    assert round(circle.area, 2) == area
    assert round(circle.perimeter, 2) == perimeter
    assert round(circle.add_area(figure), 2) == common_area


@pytest.mark.parametrize('radius', [0, -1, 'str'])
def test_negative_creation(radius: float):
    with pytest.raises(ValueError):
        Circle(radius)


@pytest.mark.parametrize('non_figure', [0, 1, -1, 'str'])
def test_negative_add_area(non_figure: object):
    circle = Circle(1)
    with pytest.raises(ValueError):
        circle.add_area(non_figure)
