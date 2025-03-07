from abc import ABC, abstractmethod


# Интерфейс Observer
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float) -> None:
        pass


# Интерфейс Subject
class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass


# Конкретный Subject: датчик температуры
class TemperatureSensor(Subject):
    def __init__(self) -> None:
        self._observers: list[Observer] = []
        self._temperature: float = 0.0

    def add_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature: float) -> None:
        self._temperature = temperature
        self.notify_observers()

    def get_temperature(self) -> float:
        return self._temperature


# Конкретный Observer: Alarm
class Alarm(Observer):
    def update(self, temperature: float) -> None:
        if temperature > 30.0:
            print(f"Сигнал тревоги! Высокая температура: {temperature}°C")


# Конкретный Observer: Display
class Display(Observer):
    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, temperature: float) -> None:
        print(f"Дисплей {self.name} отображает температуру: {temperature}°C")
