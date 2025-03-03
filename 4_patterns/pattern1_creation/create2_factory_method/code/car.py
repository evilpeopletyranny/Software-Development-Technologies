from transport import Transport


# Конкретный продукт - Car
class Car(Transport):
    def drive(self):
        print("Вождение автомобиля.")
