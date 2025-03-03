from abc import ABC, abstractmethod


class Chair(ABC):
    @abstractmethod
    def __str__(self) -> str:
        """Возвращает строковое представление кресла"""
        pass


class Sofa(ABC):
    @abstractmethod
    def __str__(self) -> str:
        """Возвращает строковое представление дивана"""
        pass


class Table(ABC):
    @abstractmethod
    def __str__(self) -> str:
        """Возвращает строковое представление стола"""
        pass
