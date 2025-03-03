# Абстрактный создатель (фабрика)
from abc import ABC, abstractmethod
from transport import Transport


class TransportFactory(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass
