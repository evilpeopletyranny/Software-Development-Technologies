import copy


class Prototype:
    def clone(self):
        """Создаёт глубокую копию объекта."""
        return copy.deepcopy(self)


class ConcretePrototype(Prototype):
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes  # Например, список или словарь

    def __str__(self):
        return f"ConcretePrototype(name={self.name}, attributes={self.attributes})"


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
