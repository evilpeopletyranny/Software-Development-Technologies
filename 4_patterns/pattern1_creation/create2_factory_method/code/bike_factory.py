from transport_factory import TransportFactory
from transport import Transport
from bike import Bike


# Конкретный создатель для Bike
class BikeFactory(TransportFactory):
    def create_transport(self) -> Transport:
        return Bike()
