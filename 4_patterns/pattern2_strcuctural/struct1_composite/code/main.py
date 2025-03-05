from composite import *


def main():
    # Корневая коробка без родителя
    root = Box()
    # Вложенная коробка с родителем root
    second_box = Box(root)
    root.add(second_box)

    # Добавляем товары во вторую коробку
    second_box.add(Item(50))
    second_box.add(Item(100))
    second_box.add(Item(150))

    # Добавляем товары непосредственно в корневую коробку
    root.add(Item(3))
    root.add(Item(7))

    # Выводим общую стоимость товаров в корневой коробке
    print("Общая стоимость товаров:", root.calc_cost())


if __name__ == "__main__":
    main()
