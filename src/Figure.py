from abc import ABC, abstractmethod


class Figure(ABC):
    """Parent class for all geometric figures."""

    def __init__(self, name: str):
        self.name = name

    @property
    @abstractmethod
    def area(self) -> float:
        pass

    @property
    @abstractmethod
    def perimeter(self) -> float:
        pass

    def add_area(self, figure: object) -> float:
        if isinstance(figure, Figure):
            return self.area + figure.area
        raise ValueError(f'The received object {type(figure)} is not a figure!')
