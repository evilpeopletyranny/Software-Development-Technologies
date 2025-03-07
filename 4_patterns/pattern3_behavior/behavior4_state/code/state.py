from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from package import Package  # Импортируется только для аннотаций, чтобы избежать циклического импорта


# Общий интерфейс (абстрактный класс) состояния посылки
class PackageState(ABC):
    @abstractmethod
    def next(self, pkg: Package) -> None:
        """Переход в следующее состояние."""
        pass

    @abstractmethod
    def prev(self, pkg: Package) -> None:
        """Переход в предыдущее состояние."""
        pass

    @abstractmethod
    def print_status(self) -> None:
        """Вывод статуса посылки."""
        pass


class OrderedState(PackageState):
    def next(self, pkg: Package) -> None:
        pkg.set_state(DeliveredState())

    def prev(self, pkg: Package) -> None:
        print("The package is in its root state.")

    def print_status(self) -> None:
        print("Package ordered, not delivered to the office yet.")


class DeliveredState(PackageState):
    def next(self, pkg: Package) -> None:
        pkg.set_state(ReceivedState())

    def prev(self, pkg: Package) -> None:
        pkg.set_state(OrderedState())

    def print_status(self) -> None:
        print("Package delivered to post office, not received yet.")


class ReceivedState(PackageState):
    def next(self, pkg: Package) -> None:
        print("This package is already received by a client.")

    def prev(self, pkg: Package) -> None:
        pkg.set_state(DeliveredState())

    def print_status(self) -> None:
        print("Package received.")
