from transport import Transport


# Конкретный продукт - Bike
class Bike(Transport):
    def drive(self):
        print("Вождение велосипеда.")
