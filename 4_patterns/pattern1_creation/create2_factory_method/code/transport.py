from abc import ABC, abstractmethod


# Общий интерфейс "продукта" - транспорт
class Transport(ABC):
    @abstractmethod
    def drive(self):
        pass
