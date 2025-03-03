from factory import *


def main():
    # Мебель в стиле модерн
    factory = ModernFurnitureFactory()
    modern_chair = factory.create_chair()
    modern_sofa = factory.create_sofa()
    modern_table = factory.create_table()
    print("Мебель в стиле модерн:", modern_chair, modern_sofa, modern_table)

    # Мебель в стиле готика
    factory = GoticFurnitureFactory()
    gotic_chair = factory.create_chair()
    gotic_sofa = factory.create_sofa()
    gotic_table = factory.create_table()
    print("Мебель в стиле готика:", gotic_chair, gotic_sofa, gotic_table)

    # Мебель в стиле барокко
    factory = BaroqueFurnitureFactory()
    baroque_chair = factory.create_chair()
    baroque_sofa = factory.create_sofa()
    baroque_table = factory.create_table()
    print("Мебель в стиле барокко:", baroque_chair, baroque_sofa, baroque_table)


if __name__ == "__main__":
    main()
