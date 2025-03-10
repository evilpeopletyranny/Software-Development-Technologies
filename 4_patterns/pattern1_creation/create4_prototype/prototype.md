# Prototype

## Прототип

**Прототип** — это порождающий паттерн проектирования, который позволяет копировать объекты, не вдаваясь в подробности
их реализации.

Прототип особенно полезен при создании сложных или ресурсоемкий объектов. Чтобы не создавать идентичный/схожий сложный
объект с нуля, мы просто копируем объект, а затем меняем нужные параметры.

#### Основная идея

Основная идея паттерна Прототип заключается в том, чтобы определить виды объектов, которые могут быть клонированы, и
создать копии этих объектов без привязки к их конкретным классам.

#### Применение

Паттерн Прототип рекомендуется использовать в следующих случаях:

- **Когда создание объекта напрямую является ресурсоёмким**: Если создание объекта требует значительных затрат времени
  или ресурсов, клонирование существующего объекта может быть более эффективным.
- **Когда требуется создать объект, соответствующий определённому состоянию**: Если требуется создать объект с
  определённым состоянием, который уже существует, прототип может служить шаблоном.
- **Когда системы должны быть независимыми от классов создаваемых объектов**: Паттерн Прототип позволяет системе
  создавать объекты без знания о конкретных классах.
- **Когда необходимо динамически добавлять новые виды объектов**: Паттерн позволяет легко расширять систему новыми
  типами объектов путем добавления новых прототипов.

### Реализация

1. Интерфейс прототипов описывает операции клонирования. В большинстве случаев — это единственный метод ```clone```.
2. Конкретный прототип реализует операцию клонирования самого себя. Помимо банального копирования значений всех полей,
   здесь могут быть спрятаны различные сложности, о которых не нужно знать клиенту. Например, клонирование связанных
   объектов, распутывание рекурсивных зависимостей и прочее.
3. Клиент создаёт копию объекта, обращаясь к нему через общий интерфейс прототипов.

### Примеры

#### Проблема с примером из книги Швеца

В книге *Александра Швеца* рассказывается про прототип с общим хранилищем:

1. Это уже частная реализация. Сам паттерн ограничивается только клонированием на самом деле.
2. Это сложно и запутывает для начала.
3. Такую вещь мы рассмотрим в ЛР2, где в Spring такой механизм используется по умолчанию.

#### Пример 

##### Абстрактный класс ```Prototype``` с единственным методом копирования

```python
import copy

class Prototype:
    def clone(self):
        """Создаёт глубокую копию объекта."""
        return copy.deepcopy(self)
```

##### Некий класс, который реализуй паттерн Прототип

```python
class ConcretePrototype(Prototype):
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes  # Например, список или словарь

    def __str__(self):
        return f"ConcretePrototype(name={self.name}, attributes={self.attributes})"

```

##### Модуль для проверки

```python
def main():
    # Создаем исходный объект
    original = ConcretePrototype("Original", {"color": "red", "size": [1, 2, 3]})
    print("Исходный объект:", original)
    
    # Клонируем объект с помощью метода clone()
    clone = original.clone()
    print("Клон:", clone)
    
    # Изменим клон, чтобы убедиться, что копия действительно независима
    clone.name = "Clone"
    clone.attributes["color"] = "blue"
    clone.attributes["size"].append(4)
    
    print("\nПосле изменения клона:")
    print("Исходный объект:", original)
    print("Клон:", clone)


if __name__ == "__main__":
    main()
```


### Недостатки данного паттерна

- **Сложность реализации**: Необходимо правильно реализовать метод ```clone()```, особенно для глубокого клонирования.
- **Проблемы с наследованием**: Клонирование может стать сложным, если классы имеют сложную иерархию наследования.
- **Проблемы с безопасностью**: Некорректное клонирование может привести к нарушению инвариантов объекта или к утечкам
  данных.
