from transport_factory import TransportFactory
from car_factory import CarFactory
from bike_factory import BikeFactory


def main():
    # Создаем фабрику для автомобиля и создаем объект Car
    factory: TransportFactory = CarFactory()
    car = factory.create_transport()

    # Смена фабрики: создаем фабрику для велосипеда и создаем объект Bike
    factory = BikeFactory()
    bike = factory.create_transport()

    car.drive()
    bike.drive()


if __name__ == '__main__':
    main()
