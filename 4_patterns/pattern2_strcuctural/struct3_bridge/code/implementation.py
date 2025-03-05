from abc import ABC, abstractmethod


# Интерфейс реализации цвета ("Реализация")
class Color(ABC):
    @abstractmethod
    def fill_color(self) -> None:
        pass


# Конкретные реализации цвета
class BlackColor(Color):
    def fill_color(self) -> None:
        print("Filling in black color")


class GreenColor(Color):
    def fill_color(self) -> None:
        print("Filling in green color")


class RedColor(Color):
    def fill_color(self) -> None:
        print("Filling in red color")
