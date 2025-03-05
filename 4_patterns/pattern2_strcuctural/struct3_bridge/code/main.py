from implementation import *
from abstraction import *


# Клиентский код (аналог Main.java)
def main():
    rect = Rectangle(RedColor())
    rect.draw()

    print("---------------")

    triangle = Triangle(GreenColor())
    triangle.draw()


if __name__ == "__main__":
    main()
