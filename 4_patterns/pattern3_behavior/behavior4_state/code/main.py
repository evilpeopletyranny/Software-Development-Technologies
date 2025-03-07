from package import Package


def main():
    pkg = Package()
    pkg.print_status()  # Должно вывести состояние OrderedState

    pkg.next_state()  # Переход к DeliveredState
    pkg.print_status()

    pkg.next_state()  # Переход к ReceivedState
    pkg.print_status()

    pkg.next_state()  # Попытка перейти за пределы состояния ReceivedState
    pkg.print_status()


if __name__ == "__main__":
    main()
