import pytest

from src.Square import Square


@pytest.mark.parametrize(
    'length, area, perimeter, figure, common_area',
    [
        (1, 1, 4, Square(1), 2),
        (1.5, 2.25, 6, Square(1.55), 4.65),
        (1.59, 2.53, 6.36, Square(1.55), 4.93),
    ]
)
def test_base_attrs(
        length: float,
        area: float,
        perimeter: float,
        figure: object,
        common_area: float,
):
    square = Square(length)
    assert square.name == 'Square'
    assert square.length == length
    assert square.width == length
    assert round(square.area, 2) == area
    assert round(square.perimeter, 2) == perimeter
    assert round(square.add_area(figure), 2) == common_area


@pytest.mark.parametrize('length', [0, -1, 'str'])
def test_negative_creation(length: float):
    with pytest.raises(ValueError):
        Square(length)


@pytest.mark.parametrize('non_figure', [0, 1, -1, 'str'])
def test_negative_add_area(non_figure: object):
    square = Square(1)
    with pytest.raises(ValueError):
        square.add_area(non_figure)
