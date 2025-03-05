from abc import ABC, abstractmethod


# Вспомогательный класс для хранения внешнего состояния
class CharacterContext:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


# Интерфейс Flyweight
class CharacterFlyweight(ABC):
    @abstractmethod
    def display(self, context: CharacterContext) -> None:
        pass


# Конкретная реализация Flyweight
class ConcreteCharacterFlyweight(CharacterFlyweight):
    def __init__(self, character: str, font: str, size: int) -> None:
        self.character = character
        self.font = font
        self.size = size

    def display(self, context: CharacterContext) -> None:
        print(f"Character: {self.character}, Font: {self.font}, Size: {self.size}, "
              f"Position: ({context.x}, {context.y})")


# Фабрика Flyweight, которая хранит созданные объекты в словаре
class CharacterFlyweightFactory:
    _flyweights = {}

    @classmethod
    def get_character(cls, character: str, font: str, size: int) -> CharacterFlyweight:
        key = f"{character}-{font}-{size}"
        if key not in cls._flyweights:
            cls._flyweights[key] = ConcreteCharacterFlyweight(character, font, size)
            print(f"Creating new Flyweight for: {key}")
        return cls._flyweights[key]

    @classmethod
    def get_flyweight_count(cls) -> int:
        return len(cls._flyweights)
