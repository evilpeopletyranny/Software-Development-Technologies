# Composite

## Компоновщик

**Компоновщик** — это структурный паттерн проектирования, который позволяет сгруппировать объекты в древовидную
структуру, а затем работать с ними так, если бы это был единичный объект.

В разработке программного обеспечения часто необходимо представлять иерархические структуры объектов, где отдельные
элементы и их композиции должны обрабатываться единообразно. Паттерн проектирования Компоновщик (Composite)
предоставляет решение этой задачи, позволяя клиентам работать с отдельными объектами и их композициями одинаково. Это
повышает гибкость и упрощает управление сложными структурами.

Паттерн Компоновщик имеет смысл только тогда, когда основная модель вашей программы может быть структурирована в виде
дерева.

#### Основная идея

Основная идея паттерна Компоновщик заключается в том, чтобы создать единый интерфейс для работы как с простыми, так и с
составными объектами. Это достигается путем определения общего интерфейса или абстрактного класса для всех элементов
иерархии, включая как "листья" (простые объекты), так и "композиты" (составные объекты, содержащие другие элементы).

#### Применение

Паттерн Компоновщик рекомендуется использовать в следующих случаях:

- Необходимо представить иерархическую структуру объектов.
- Хочется, чтобы клиенты могли одинаково обращаться к отдельным объектам и их композициям.
- Необходимо добавить новые виды объектов, не изменяя существующий код.
- Структура иерархии должна быть гибкой и расширяемой.

### Реализация

1. Убедитесь, что вашу бизнес-логику можно представить как древовидную структуру. Попытайтесь разбить её на простые
   элементы и контейнеры. Помните, что контейнеры могут содержать как простые элементы, так и другие контейнеры.
2. Создайте общий интерфейс компонентов, который объединит операции контейнеров и простых элементов дерева. Интерфейс
   будет удачным, если вы сможете взаимозаменять простые и составные компоненты без потери смысла.
3. Создайте класс компонентов-листьев, не имеющих дальнейших ответвлений. Имейте в виду, что программа может содержать
   несколько видов таких классов.
4. Создайте класс компонентов-контейнеров, и добавьте в него массив для хранения ссылок на вложенные компоненты. Этот
   массив должен быть способен содержать как простые, так и составные компоненты, поэтому убедитесь, что он объявлен с
   типом интерфейса компонентов. Реализуйте в контейнере методы интерфейса компонентов, помня о том, что контейнеры
   должны делегировать основную работу своим дочерним компонентам.
5. Добавьте операции добавления и удаления дочерних элементов в класс контейнеров. Имейте в виду, что методы
   добавления/удаления дочерних элементов можно поместить и в интерфейс компонентов. Да, это нарушит принцип разделения
   интерфейса, так как реализации методов будут пустыми в компонентах-листьях. Но зато все компоненты дерева станут
   действительно одинаковыми для клиента.

### Примеры

#### Фреймворки для разработки десктоп приложений

Почти в любой фреймворке для разработки десктопных приложений, например **Qt C++**, **PyQt**, **Java Swing** и тд Все
графические элементы представлены в виде иерархической структуры, реализующей паттерн Компоновщик - всё есть элемент
граф. интерфейса и эти элементы вкладываются друг в друга.

#### [Пример](code/main.py) иерархии упаковок товаров

Предположим нам необходимо создать систему для обсчета стоимости товаров. Товары могут храниться как в штучном виде, так
и несколько разных товаров в коробке. Ценой коробки считается сумма всех товаров внутри коробки.

##### Общие интерфейсы компоновщика

```python
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
```

##### Конкретные реализации

```python
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
```

##### Класс для тестирования

```python
from composite import *


def main():
    # Корневая коробка без родителя
    root = Box()
    # Вложенная коробка с родителем root
    second_box = Box(root)
    root.add(second_box)

    # Добавляем товары во вторую коробку
    second_box.add(Item(50))
    second_box.add(Item(100))
    second_box.add(Item(150))

    # Добавляем товары непосредственно в корневую коробку
    root.add(Item(3))
    root.add(Item(7))

    # Выводим общую стоимость товаров в корневой коробке
    print("Общая стоимость товаров:", root.calc_cost())


if __name__ == "__main__":
    main()
```

### Плюсы данного паттерна

- **Простота использования:** Клиенты могут взаимодействовать с отдельными объектами и их композициями одинаково,
  упрощая код.
- **Гибкость структуры:** Легко добавлять новые виды компонентов и композитов без изменения существующего кода.
- **Повторное использование кода:** Общие операции могут быть реализованы в базовом компоненте, уменьшая дублирование.
- **Упрощение кода клиента:** Клиенты не нуждаются в проверке типа объекта; они работают через общий интерфейс.

### Недостатки данного паттерна

- **Сложность реализации:** Для небольших систем использование паттерна Компоновщик может быть избыточным.
- **Производительность:** Рекурсивные вызовы могут влиять на производительность при работе с большими иерархиями.
- **Ограниченная функциональность:** Некоторые специфические операции могут требовать дополнительной обработки или
  обхода иерархии.

### Заключение

Паттерн проектирования **Компоновщик** предоставляет мощный механизм для организации иерархических структур объектов,
обеспечивая единообразное взаимодействие с ними. Он широко применяется в различных областях разработки, включая
графические интерфейсы, файловые системы и коллекции.

Понимание и правильное применение паттерна Компоновщик способствует созданию гибких, расширяемых и легко поддерживаемых
систем. Однако, как и любой паттерн, его следует применять осознанно, учитывая требования и особенности конкретного
проекта.
