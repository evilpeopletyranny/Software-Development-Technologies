# Abstract Factory

## Абстрактная фабрика

**Абстрактная фабрика** — это порождающий паттерн проектирования, который позволяет создавать семейства связанных
объектов, не привязываясь к конкретным классам создаваемых объектов.

Зачастую абстрактная фабрика рождается из фабричного метода, когда необходимо добавить новый продукт. В хорошей
программе, каждый класс отвечает только за одну вещь. Если класс имеет слишком много фабричных методов, они способны
затуманить его основную функцию. Поэтому имеет смысл вынести всю логику создания продуктов в отдельную иерархию классов,
применив абстрактную фабрику.

Абстрактная фабрика скрывает от клиентского кода подробности того, как и какие конкретно объекты будут созданы. Но при
этом клиентский код может работать со всеми типами создаваемых продуктов, так как их общий интерфейс был заранее
определён.

#### Основная идея

Основная цель паттерна Абстрактная Фабрика — **изолировать создание объектов от их использования**, обеспечивая таким
образом независимость клиентского кода от конкретных классов продуктов. Это позволяет легко добавлять новые семейства
продуктов без изменения существующего кода.

#### Применение

Паттерн Абстрактная Фабрика рекомендуется использовать в следующих случаях:

- Когда система должна быть независимой от способа создания, композиции и представления её объектов.
- Когда система должна работать с различными семействами взаимосвязанных объектов, не завися от их конкретных классов.
- Когда необходимо обеспечить согласованность создаваемых объектов (например, все элементы интерфейса принадлежат к
  одному стилю).
- Когда нужно добавить новые семейства продуктов без изменения существующего кода.

### Реализация

1. Абстрактные продукты объявляют интерфейсы продуктов, которые связаны друг с другом по смыслу, но выполняют разные
   функции.
2. Конкретные продукты — большой набор классов, которые относятся к различным абстрактным продуктам (кресло/ столик), но
   имеют одни и те же вариации (Барокко/Модерн).
3. Абстрактная фабрика объявляет методы создания различных абстрактных продуктов (кресло/столик).
4. Конкретные фабрики относятся каждая к своей вариации
   продуктов (Барокко/Модерн) и реализуют методы абстрактной фабрики, позволяя создавать все продукты определённой
   вариации.
5. Несмотря на то, что конкретные фабрики порождают конкретные продукты, сигнатуры их методов должны возвращать
   соответствующие абстрактные продукты. Это позволит клиентскому коду, использующему фабрику, не привязываться к
   конкретным классам продуктов. Клиент сможет работать с любыми вариациями продуктов через абстрактные интерфейсы.

### Примеры

#### Пример [main.py](code%2Fmain.py)

Создадим систему, которая может создавать кресла, столы и диваны в разных стилях: Барокко, Готика, Модерн.

##### AbstractProduct: Интерфейсы для продуктов

Определим интерфейсы производимых продуктов.

```python
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

```

##### ConcreteProduct: Конкретные реализации продуктов для разных стилей

**Барокко**

```python
from product import Chair
from product import Sofa
from product import Table


class BaroqueChair(Chair):
    def __str__(self) -> str:
        return "Baroque Chair"


class BaroqueSofa(Sofa):
    def __str__(self) -> str:
        return "Baroque Sofa"


class BaroqueTable(Table):
    def __str__(self) -> str:
        return "Baroque Table"
```

**Готика**

```python
from product import Chair
from product import Sofa
from product import Table


class GoticChair(Chair):
    def __str__(self) -> str:
        return "Gothic Chair"


class GoticSofa(Sofa):
    def __str__(self) -> str:
        return "Gothic Sofa"


class GoticTable(Table):
    def __str__(self) -> str:
        return "Gothic Table"

```

**Модерн**

```python
from product import *


class ModernChair(Chair):
    def __str__(self) -> str:
        return "Modern Chair"


class ModernSofa(Sofa):
    def __str__(self) -> str:
        return "Modern Sofa"


class ModernTable(Table):
    def __str__(self) -> str:
        return "Modern Table"

```

##### AbstractFactory: абстрактный класс Абстрактной Фабрики

```python
class AbstractFurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass
```

##### ConcreteFactory: Конкретные фабрики для разных стилей

**Барокко**

```python
class BaroqueFurnitureFactory(AbstractFurnitureFactory):
    def create_chair(self):
        return BaroqueChair()

    def create_sofa(self):
        return BaroqueSofa()

    def create_table(self):
        return BaroqueTable()
```

**Готика**

```python
class GoticFurnitureFactory(AbstractFurnitureFactory):
    def create_chair(self):
        return GoticChair()

    def create_sofa(self):
        return GoticSofa()

    def create_table(self):
        return GoticTable()
```

**Модерн**

```python
class ModernFurnitureFactory(AbstractFurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()

    def create_table(self):
        return ModernTable()

```

##### Модуль для тестирования

```Python
from factory import *


def main():
    # Мебель в стиле модерн
    factory = ModernFurnitureFactory()
    modern_chair = factory.create_chair()
    modern_sofa = factory.create_sofa()
    modern_table = factory.create_table()
    print("Мебель в стиле модерн:", modern_chair, modern_sofa, modern_table)

    # Мебель в стиле готика
    factory = GoticFurnitureFactory()
    gotic_chair = factory.create_chair()
    gotic_sofa = factory.create_sofa()
    gotic_table = factory.create_table()
    print("Мебель в стиле готика:", gotic_chair, gotic_sofa, gotic_table)

    # Мебель в стиле барокко
    factory = BaroqueFurnitureFactory()
    baroque_chair = factory.create_chair()
    baroque_sofa = factory.create_sofa()
    baroque_table = factory.create_table()
    print("Мебель в стиле барокко:", baroque_chair, baroque_sofa, baroque_table)


if __name__ == "__main__":
    main()
```

### Плюсы данного паттерна

- **Согласованность семейства продуктов**: Паттерн обеспечивает создание совместимых объектов из одного семейства, что
  предотвращает ошибки, связанные с несовместимостью компонентов.
- **Гибкость и расширяемость**: Позволяет легко добавлять новые семейства продуктов без изменения существующего
  клиентского кода.
- **Снижение связанности**: Клиентский код зависит только от абстракций, а не от конкретных реализаций продуктов, что
  упрощает поддержку и модификацию кода.
- **Изоляция от конкретных классов**: Клиентский код не знает о конкретных классах создаваемых объектов, что позволяет
  изменять реализации без влияния на клиента.

### Недостатки данного паттерна

- **Увеличение количества классов**: Для каждого нового семейства продуктов необходимо создавать новую фабрику, что
  может привести к увеличению числа классов в проекте.
- **Сложность понимания**: Для новичков паттерн может показаться сложным из-за использования абстрактных классов и
  интерфейсов.
- **Необходимость знания всех продуктов**: Все продукты, которые могут быть созданы фабрикой, должны быть известны
  заранее, что ограничивает динамическое добавление новых продуктов.