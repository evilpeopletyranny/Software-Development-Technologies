from product import Chair
from product import Sofa
from product import Table


class GoticChair(Chair):
    def __str__(self) -> str:
        return "Gothic Chair"


class GoticSofa(Sofa):
    def __str__(self) -> str:
        return "Gothic Sofa"


class GoticTable(Table):
    def __str__(self) -> str:
        return "Gothic Table"
