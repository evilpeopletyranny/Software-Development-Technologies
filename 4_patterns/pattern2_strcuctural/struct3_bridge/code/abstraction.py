from abc import ABC, abstractmethod
from implementation import Color


# Абстракция - Shape, которая управляет раскраской через объект Color
class Shape(ABC):
    def __init__(self, color: Color) -> None:
        self.color = color

    @abstractmethod
    def draw(self) -> None:
        pass


# Уточненная абстракция - прямоугольник
class Rectangle(Shape):
    def __init__(self, color: Color) -> None:
        super().__init__(color)

    def draw(self) -> None:
        print("Drawing rectangle")
        self.color.fill_color()


# Уточненная абстракция - треугольник
class Triangle(Shape):
    def __init__(self, color: Color) -> None:
        super().__init__(color)

    def draw(self) -> None:
        print("Drawing triangle")
        self.color.fill_color()
