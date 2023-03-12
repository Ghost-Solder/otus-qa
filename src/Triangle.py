from math import sqrt

from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, side1: float, side2: float, side3: float):
        self._check_sides(side1, side2, side3)
        super().__init__('Triangle')
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @property
    def area(self) -> float:
        p_half = self.perimeter / 2
        return sqrt(
            p_half * (p_half - self.side1) * (p_half - self.side2) * (p_half - self.side3)
        )

    @property
    def perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3

    @staticmethod
    def _check_sides(side1: float, side2: float, side3: float) -> bool:
        if side1 + side2 > side3:
            if side1 + side3 > side2:
                if side2 + side3 > side1:
                    return True
        raise ValueError('The triangle cannot be created, please try other sides.')
