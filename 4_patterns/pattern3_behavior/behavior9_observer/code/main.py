from observer import TemperatureSensor, Display, Alarm


# Клиентский код
def main():
    sensor = TemperatureSensor()

    # Создаем наблюдателей
    display1 = Display("1")
    display2 = Display("2")
    alarm = Alarm()

    # Подписываем наблюдателей на датчик
    sensor.add_observer(display1)
    sensor.add_observer(display2)
    sensor.add_observer(alarm)

    # Изменяем состояние датчика
    sensor.set_temperature(25.0)
    sensor.set_temperature(28.5)
    sensor.set_temperature(32.0)


if __name__ == "__main__":
    main()
