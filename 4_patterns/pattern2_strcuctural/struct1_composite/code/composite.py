from tree import *


# Конкретный класс для товара (лист)
class Item(Leaf):
    def __init__(self, cost: int, parent: Node = None):
        self.cost = cost
        self.parent = parent

    def calc_cost(self) -> int:
        return self.cost

    def get_parent(self):
        return self.parent

    def set_parent(self, parent: Node):
        self.parent = parent

    def __str__(self):
        return f"Item(cost={self.cost})"

    def __repr__(self):
        return self.__str__()


# Конкретная реализация контейнера - коробка
class Box(Container):
    def __init__(self, parent: Node = None):
        self.parent = parent
        self.children = []

    def add(self, node: Node):
        self.children.append(node)
        node.set_parent(self)

    def remove(self, node: Node):
        if node in self.children:
            self.children.remove(node)
            node.set_parent(None)

    def get_children(self) -> list:
        return self.children

    def calc_cost(self) -> int:
        # Стоимость коробки равна сумме стоимостей всех её детей
        total = 0
        for child in self.children:
            total += child.calc_cost()
        return total

    def get_parent(self):
        return self.parent

    def set_parent(self, parent: Node):
        self.parent = parent

    def __str__(self):
        return f"Box(cost={self.calc_cost()}, children={self.children})"

    def __repr__(self):
        return self.__str__()
