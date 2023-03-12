from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, length: float, width: float):
        super().__init__('Rectangle')
        self.length = length
        self.width = width

    @property
    def area(self) -> float:
        return self.length * self.width

    @property
    def perimeter(self) -> float:
        return 2 * self.length + 2 * self.width
