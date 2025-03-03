from product import *


class ModernChair(Chair):
    def __str__(self) -> str:
        return "Modern Chair"


class ModernSofa(Sofa):
    def __str__(self) -> str:
        return "Modern Sofa"


class ModernTable(Table):
    def __str__(self) -> str:
        return "Modern Table"
