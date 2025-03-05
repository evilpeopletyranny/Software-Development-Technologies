from abc import ABC, abstractmethod


# Абстрактный базовый класс для всех узлов дерева
class Node(ABC):
    @abstractmethod
    def calc_cost(self) -> int:
        """Вычисляет стоимость узла (или дерева)"""
        pass

    @abstractmethod
    def get_parent(self):
        """Возвращает родительский узел"""
        pass

    @abstractmethod
    def set_parent(self, parent):
        """Устанавливает родительский узел"""
        pass


# Интерфейс конечного элемента (лист)
# В данном примере Leaf не добавляет новых методов,
# поэтому можно просто использовать класс Node для листьев.
class Leaf(Node):
    pass


# Интерфейс контейнера, который может содержать дочерние узлы
class Container(Node, ABC):
    @abstractmethod
    def add(self, node: Node):
        """Добавляет узел в контейнер"""
        pass

    @abstractmethod
    def remove(self, node: Node):
        """Удаляет узел из контейнера"""
        pass

    @abstractmethod
    def get_children(self) -> list:
        """Возвращает список дочерних узлов"""
        pass
