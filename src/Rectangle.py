from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, length: float, width: float):
        self._check_sides(length, width)
        super().__init__('Rectangle')
        self.length = length
        self.width = width

    @property
    def area(self) -> float:
        return self.length * self.width

    @property
    def perimeter(self) -> float:
        return 2 * self.length + 2 * self.width

    @staticmethod
    def _check_sides(length: float, width: float) -> bool:
        if isinstance(length, (int, float)) and isinstance(width, (int, float)):
            if length > 0 and width > 0:
                return True
        raise ValueError('The figure cannot be created, please try other sides.')
