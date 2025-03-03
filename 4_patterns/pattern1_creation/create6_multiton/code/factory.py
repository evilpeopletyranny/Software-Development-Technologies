from abc import ABC, abstractmethod
from shape import *


class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self, name: str) -> Shape:
        """Создаёт фигуру с заданным именем."""
        pass


class CircleFactory(ShapeFactory):
    def create_shape(self, name: str) -> Shape:
        return Circle(name)


class RectangleFactory(ShapeFactory):
    def create_shape(self, name: str) -> Shape:
        return Rectangle(name)


class TriangleFactory(ShapeFactory):
    def create_shape(self, name: str) -> Shape:
        return Triangle(name)
