from abc import ABC, abstractmethod


# Абстрактная стратегия
class TextStrategy(ABC):
    @abstractmethod
    def format_text(self, text: str) -> str:
        pass


# Конкретная стратегия: перевод в верхний регистр
class UpperCaseStrategy(TextStrategy):
    def format_text(self, text: str) -> str:
        return text.upper()


# Конкретная стратегия: перевод в нижний регистр
class LowerCaseStrategy(TextStrategy):
    def format_text(self, text: str) -> str:
        return text.lower()


# Конкретная стратегия: каждое слово с заглавной буквы
class TitleCaseStrategy(TextStrategy):
    def format_text(self, text: str) -> str:
        return text.title()

