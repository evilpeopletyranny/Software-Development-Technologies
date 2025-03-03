from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self) -> None:
        """Рисует фигуру."""
        pass


class Circle(Shape):
    def __init__(self, name: str):
        self.name = name

    def draw(self) -> None:
        print(f"Рисование круга: {self.name}")


class Rectangle(Shape):
    def __init__(self, name: str):
        self.name = name

    def draw(self) -> None:
        print(f"Рисование прямоугольника: {self.name}")


class Triangle(Shape):
    def __init__(self, name: str):
        self.name = name

    def draw(self) -> None:
        print(f"Рисование треугольника: {self.name}")
