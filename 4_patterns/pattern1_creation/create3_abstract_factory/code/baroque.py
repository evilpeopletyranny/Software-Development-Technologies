from product import Chair
from product import Sofa
from product import Table


class BaroqueChair(Chair):
    def __str__(self) -> str:
        return "Baroque Chair"


class BaroqueSofa(Sofa):
    def __str__(self) -> str:
        return "Baroque Sofa"


class BaroqueTable(Table):
    def __str__(self) -> str:
        return "Baroque Table"
