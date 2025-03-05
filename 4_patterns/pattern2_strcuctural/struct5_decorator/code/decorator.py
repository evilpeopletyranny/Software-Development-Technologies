from abc import ABC, abstractmethod
from datetime import datetime


# Интерфейс Message
class Message(ABC):
    @abstractmethod
    def get_content(self) -> str:
        pass


# Конкретная реализация сообщения
class SimpleMessage(Message):
    def __init__(self, content: str) -> None:
        self.content = content

    def get_content(self) -> str:
        return self.content


# Базовый декоратор, реализующий интерфейс Message
class MessageDecorator(Message):
    def __init__(self, message: Message) -> None:
        self.message = message

    def get_content(self) -> str:
        return self.message.get_content()


# Декоратор, добавляющий шифрование (в данном случае – разворот строки)
class EncryptedMessageDecorator(MessageDecorator):
    def __init__(self, message: Message) -> None:
        super().__init__(message)

    def get_content(self) -> str:
        return self.encrypt(self.message.get_content())

    def encrypt(self, content: str) -> str:
        # Простая симуляция шифрования: разворот строки
        return content[::-1]


# Декоратор, добавляющий временную метку
class TimestampedMessageDecorator(MessageDecorator):
    def __init__(self, message: Message) -> None:
        super().__init__(message)

    def get_content(self) -> str:
        return self.add_timestamp(self.message.get_content())

    def add_timestamp(self, content: str) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{timestamp}] {content}"
