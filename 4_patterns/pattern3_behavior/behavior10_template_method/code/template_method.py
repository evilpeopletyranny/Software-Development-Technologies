from abc import ABC, abstractmethod


class Beverage(ABC):
    def prepare_recipe(self) -> None:
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self) -> None:
        print("Кипячение воды")

    def pour_in_cup(self) -> None:
        print("Наливание в чашку")

    @abstractmethod
    def brew(self) -> None:
        pass

    @abstractmethod
    def add_condiments(self) -> None:
        pass


class Coffee(Beverage):
    def brew(self) -> None:
        print("Заваривание кофе")

    def add_condiments(self) -> None:
        print("Добавление сахара и молока")


class Tea(Beverage):
    def brew(self) -> None:
        print("Заваривание чая")

    def add_condiments(self) -> None:
        print("Добавление лимона")
