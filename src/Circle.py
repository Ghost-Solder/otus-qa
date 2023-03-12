from math import pi

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius: float):
        super().__init__('Circle')
        self.radius = radius

    @property
    def area(self) -> float:
        return pi * self.radius * self.radius

    @property
    def perimeter(self) -> float:
        return 2 * pi * self.radius
