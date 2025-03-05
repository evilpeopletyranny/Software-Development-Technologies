from abc import ABC, abstractmethod


class Target(ABC):
    """
    Целевой интерфейс, который необходимо реализовать
    """
    @abstractmethod
    def request(self) -> str:
        return "Target: The default target's behavior."


class ConcreteTarget(Target):
    """
    Одна из конкретных реализаций необходимого интерфейса
    """

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    """
    Адаптируемый класс содержит некоторое полезное поведение, но его интерфейс
    несовместим с существующим клиентским кодом. Адаптируемый класс нуждается в
    некоторой доработке, прежде чем клиентский код сможет его использовать.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):
    """
    Адаптер делает интерфейс Адаптируемого класса совместимым с целевым
    интерфейсом благодаря агрегации.
    """

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


def main():
    # Работа с объектом, реализующим Target
    target = ConcreteTarget()
    print("Клиент: Работаю с объектом Target:")
    print(target.request())

    # Работа с объектом Adaptee напрямую (интерфейс не подходит для клиента)
    adaptee = Adaptee()
    print("\nКлиент: У объекта Adaptee странный интерфейс:")
    print(adaptee.specific_request())

    # Использование адаптера для приведения интерфейса Adaptee к Target
    adapter = Adapter(adaptee)
    print("\nКлиент: Но через адаптер я могу работать с ним:")
    print(adapter.request())


if __name__ == "__main__":
    main()
