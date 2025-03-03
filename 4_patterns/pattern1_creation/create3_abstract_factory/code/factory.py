from abc import ABC, abstractmethod

from baroque import *
from gotic import *
from modern import *


class AbstractFurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass


class BaroqueFurnitureFactory(AbstractFurnitureFactory):
    def create_chair(self):
        return BaroqueChair()

    def create_sofa(self):
        return BaroqueSofa()

    def create_table(self):
        return BaroqueTable()


class GoticFurnitureFactory(AbstractFurnitureFactory):
    def create_chair(self):
        return GoticChair()

    def create_sofa(self):
        return GoticSofa()

    def create_table(self):
        return GoticTable()


class ModernFurnitureFactory(AbstractFurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()

    def create_table(self):
        return ModernTable()
