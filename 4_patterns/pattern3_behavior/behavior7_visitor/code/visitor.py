from abc import ABC, abstractmethod


# Интерфейс элемента (Element)
class Element(ABC):
    @abstractmethod
    def accept(self, visitor: "Visitor") -> None:
        pass


# Интерфейс посетителя (Visitor)
class Visitor(ABC):
    @abstractmethod
    def visit_circle(self, circle: "Circle") -> None:
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle: "Rectangle") -> None:
        pass


# Конкретный элемент - Circle
class Circle(Element):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def get_radius(self) -> float:
        return self.radius

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_circle(self)


# Конкретный элемент - Rectangle
class Rectangle(Element):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def get_width(self) -> float:
        return self.width

    def get_height(self) -> float:
        return self.height

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_rectangle(self)


# Конкретный посетитель - PrintVisitor
class PrintVisitor(Visitor):
    def visit_circle(self, circle: Circle) -> None:
        print(f"Circle with radius: {circle.get_radius()}")

    def visit_rectangle(self, rectangle: Rectangle) -> None:
        print(f"Rectangle with width: {rectangle.get_width()} and height: {rectangle.get_height()}")
