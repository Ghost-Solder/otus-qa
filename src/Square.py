from src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, length: float):
        super().__init__(length, length)
        super(Rectangle, self).__init__('Square')

    @property
    def area(self) -> float:
        return self.length * self.length

    @property
    def perimeter(self) -> float:
        return 4 * self.length
