from math import pi

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius: float):
        self._check_radius(radius)
        super().__init__('Circle')
        self.radius = radius

    @property
    def area(self) -> float:
        return pi * self.radius * self.radius

    @property
    def perimeter(self) -> float:
        return 2 * pi * self.radius

    @staticmethod
    def _check_radius(radius: float) -> bool:
        if isinstance(radius, (int, float)) and radius > 0:
            return True
        raise ValueError('The circle cannot be created, please try other radius.')
