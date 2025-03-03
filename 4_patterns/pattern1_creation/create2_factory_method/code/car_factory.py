from transport_factory import TransportFactory
from transport import Transport
from car import Car


# Конкретный создатель для Car

class CarFactory(TransportFactory):
    def create_transport(self) -> Transport:
        return Car()
