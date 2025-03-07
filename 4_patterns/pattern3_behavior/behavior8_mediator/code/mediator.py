from abc import ABC, abstractmethod


# Интерфейс медиатора
class Mediator(ABC):
    @abstractmethod
    def register(self, user: "User") -> None:
        pass

    @abstractmethod
    def send_message(self, message: str, sender: "User") -> None:
        pass


# Конкретный медиатор - чат-комната
class ChatRoom(Mediator):
    def __init__(self) -> None:
        self.users = []

    def register(self, user: "User") -> None:
        if user not in self.users:
            self.users.append(user)
            user.set_mediator(self)
            print(f"{user.get_name()} присоединился к чат-комнате.")

    def send_message(self, message: str, sender: "User") -> None:
        for user in self.users:
            if user != sender:
                user.receive(message)


# Класс пользователя
class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self.mediator = None

    def set_mediator(self, mediator: Mediator) -> None:
        self.mediator = mediator

    def get_name(self) -> str:
        return self.name

    def send(self, message: str) -> None:
        print(f"{self.name} отправил сообщение: {message}")
        if self.mediator:
            self.mediator.send_message(message, self)

    def receive(self, message: str) -> None:
        print(f"{self.name} получил сообщение: {message}")
