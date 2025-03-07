from template_method import Tea, Coffee


def main():
    print("Приготовление чая:")
    tea = Tea()
    tea.prepare_recipe()

    print("\nПриготовление кофе:")
    coffee = Coffee()
    coffee.prepare_recipe()


if __name__ == "__main__":
    main()
