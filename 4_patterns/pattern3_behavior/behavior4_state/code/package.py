from __future__ import annotations
from state import PackageState, OrderedState


# Контекст (посылка), изменяющий своё состояние
class Package:
    def __init__(self) -> None:
        # Начальное состояние – OrderedState
        self.state: PackageState = OrderedState()

    def set_state(self, state: PackageState) -> None:
        self.state = state

    def previous_state(self) -> None:
        self.state.prev(self)

    def next_state(self) -> None:
        self.state.next(self)

    def print_status(self) -> None:
        self.state.print_status()
